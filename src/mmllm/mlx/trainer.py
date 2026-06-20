"""MLX bird-round trainer — the train-long body in MLX.

Architecture (reuses the proven torch-boundary, MLX for the hot loop):
  basilisp build-model -> extract weights by ROLE into an MLX trainable pytree
  (all dense arrays incl. gate/bank-dense params) + static config (dims, eps,
  rope, bank hyperparams) -> MLX training loop (mx.value_and_grad: dense AdamW +
  per-bank SparseAdam on V_local/V_net) -> write trained MLX weights BACK into
  the torch model by role -> torch dense.pt (+ bank .bin) via the bridge, which
  is harvest-compatible by construction.

The per-bank V gradient uses the dense-V-grad path (MLX autograd through mx.take
yields a [N,c] grad whose nonzero rows are the touched rows); Stage 6 swaps to
the two-pass grad-on-gathered-slice to avoid that allocation. Aux losses
(distill/z) and LR schedules layer on top (task #26).

Imports mlx.core at module top — only reached via mmllm.mlx.run_round when
active() (Apple Silicon).
"""
from __future__ import annotations

import os
import math
import numpy as np
import mlx.core as mx
from mlx.utils import tree_map, tree_flatten

from mmllm.mlx import model as _model
from mmllm.mlx import blocks as _blocks
from mmllm.mlx.sparse_adam import SparseAdam


# ───────────────────────── torch <-> mlx helpers ─────────────────────────
def _np(t):
    return t.detach().cpu().numpy()


def _mxa(t):
    return mx.array(_np(t))


def _eps(mod):
    e = getattr(mod, "eps", None)
    return e if e is not None else 1e-6


# ───────────────────────── extract / reassemble ─────────────────────────
# Trainable = arrays we differentiate (dense + gate + bank-dense + V tables).
# Static    = dims/eps/hyperparams/rope. V_local/V_net are tagged for SparseAdam.

def _extract(m, K, trunk_ids_mx):
    """torch model dict -> (trainable pytree, static, meta). meta records, per
    block, which gate kind + whether banks are present, so reassemble and
    write-back can mirror the structure."""
    blocks = m.get(K("blocks"))
    static = {
        "norm_final_eps": _eps(m.get(K("norm-final"))),
        "rope_cos": _mxa(m.get(K("rope-cos"))),
        "rope_sin": _mxa(m.get(K("rope-sin"))),
        "blocks": [],
    }
    trainable = {
        "tok_emb": _mxa(m.get(K("tok-emb")).weight),
        "norm_final_w": _mxa(m.get(K("norm-final")).weight),
        "blocks": [],
    }
    meta = {"blocks": []}
    for blk in blocks:
        g = lambda n: blk.get(K(n))
        tb = {
            "norm1_w": _mxa(g("norm1").weight), "norm2_w": _mxa(g("norm2").weight),
            "q_proj": _mxa(g("q-proj").weight),
            "k_proj_s": _mxa(g("k-proj-s").weight), "v_proj_s": _mxa(g("v-proj-s").weight),
            "k_proj_l": _mxa(g("k-proj-l").weight), "v_proj_l": _mxa(g("v-proj-l").weight),
            "o_proj": _mxa(g("o-proj").weight),
            "gate_proj": _mxa(g("gate-proj").weight), "up_proj": _mxa(g("up-proj").weight),
            "down_proj": _mxa(g("down-proj").weight),
        }
        sb = {
            "n_heads": g("n-heads"), "n_short_heads": g("n-short-heads"),
            "n_long_heads": g("n-long-heads"), "n_short_kv": g("n-short-kv-heads"),
            "n_long_kv": g("n-long-kv-heads"), "head_dim": g("head-dim"),
            "norm1_eps": _eps(g("norm1")), "norm2_eps": _eps(g("norm2")),
        }
        bmeta = {"gate_kind": type(g("long-gate")).__name__, "memory": False, "netbank": False}

        gate = g("long-gate")
        if bmeta["gate_kind"] == "SwitchGate":
            # sw_ prefix avoids colliding with the SwiGLU FFN gate_proj weight.
            tb["sw_gate_proj"] = _mxa(gate.gate_proj)        # 2-way head
            tb["sw_gate_proj_3"] = _mxa(gate.gate_proj_3)
            if getattr(gate, "alpha_net", None) is not None:
                tb["sw_alpha_net"] = _mxa(gate.alpha_net)
            if getattr(gate, "local_active_proj", None) is not None:
                tb["sw_local_active_proj"] = _mxa(gate.local_active_proj)
                tb["sw_local_active_bias"] = _mxa(gate.local_active_bias)

        # ctx-add bank query: CtxAddBankQuery has a .proj Linear (W_ctx); PlainBankQuery
        # does not. W_ctx makes the bank query content-discriminative (bank_q += W_ctx·x)
        # — the missing ingredient that de-collapses retrieval. Trained as a dense param.
        bq = g("bank-query")
        if bq is not None and getattr(bq, "proj", None) is not None:
            tb["bank_query_w"] = _mxa(bq.proj.weight)        # [q_dim, d_model]

        mem = g("memory")
        if mem is not None:
            bmeta["memory"] = True
            tb["mem_q_norm_w"] = _mxa(mem.q_norm.weight)
            tb["mem_K_a"] = _mxa(mem.K_a); tb["mem_K_b"] = _mxa(mem.K_b)
            tb["V_local"] = _mxa(mem.V.weight)
            sb["mem"] = {"eps": _eps(mem.q_norm), "sub_dim": mem.sub_dim,
                         "sqrt_n": mem.sqrt_n, "sub_top_k": mem.sub_top_k,
                         "top_k": mem.top_k, "n_trunks": getattr(mem, "n_trunks", 1)}
        nb = g("netbank")
        if nb is not None:
            bmeta["netbank"] = True
            # MMLLM_NET_WIDEN=C: widen netbank code dim c_net -> C (8->16=q_dim),
            # removing the expander-rank bottleneck. V_net new cols=0; expander
            # new cols=small random (zero-on-both deadlocks the gradient).
            _widen = int(os.environ.get("MMLLM_NET_WIDEN", "0"))
            def _emit_net(bank):
                d = {"net_q_norm_w": _mxa(bank.q_norm.weight),
                     "net_K_a": _mxa(bank.K_a), "net_K_b": _mxa(bank.K_b),
                     "net_expander_w": _mxa(bank.expander.weight),
                     "V_net": _mxa(bank.V.weight)}
                if _widen > d["V_net"].shape[1]:
                    _pad = _widen - d["V_net"].shape[1]; _N = d["V_net"].shape[0]
                    d["V_net"] = mx.concatenate(
                        [d["V_net"], mx.zeros((_N, _pad), dtype=d["V_net"].dtype)], axis=1)
                    _ew = d["net_expander_w"]
                    d["net_expander_w"] = mx.concatenate(
                        [_ew, (0.02 * mx.random.normal((_ew.shape[0], _pad))).astype(_ew.dtype)], axis=1)
                return d
            if hasattr(nb, "banks"):                 # ModularNetBank (skill-module partition)
                bmeta["net_modular"] = True
                bmeta["net_modules"] = list(nb.module_names)
                tb["netbanks"] = {name: _emit_net(nb.banks[name]) for name in nb.module_names}
                ref = nb.banks[nb.module_names[0]]
                sb["net"] = {"eps": _eps(ref.q_norm), "sub_dim": ref.sub_dim,
                             "sqrt_n": ref.sqrt_n, "sub_top_k": ref.sub_top_k, "top_k": ref.top_k}
            else:                                    # legacy single NetBank (keys unchanged)
                d = _emit_net(nb)
                tb["net_q_norm_w"] = d["net_q_norm_w"]
                tb["net_K_a"] = d["net_K_a"]; tb["net_K_b"] = d["net_K_b"]
                tb["net_expander_w"] = d["net_expander_w"]; tb["V_net"] = d["V_net"]
                sb["net"] = {"eps": _eps(nb.q_norm), "sub_dim": nb.sub_dim,
                             "sqrt_n": nb.sqrt_n, "sub_top_k": nb.sub_top_k, "top_k": nb.top_k}

        trainable["blocks"].append(tb)
        static["blocks"].append(sb)
        meta["blocks"].append(bmeta)
    static["trunk_ids"] = trunk_ids_mx
    return trainable, static, meta


def _reassemble(trainable, static, meta, student=False, drop_net=False):
    """trainable + static -> the param dict model.forward consumes. Gate params
    come from `trainable` (via closures) so gradients flow to them.

    student names the OUTPUT-KD student forward's freeze level (all LOCAL banks
    off in every case — the future state when locals reset):
      "off"   -> not a student forward (locals ON, nothing frozen): the teacher/CE path.
      "none"  -> locals off, nothing frozen (gate+net+trunk all adapt to locals-off).
      "trunk" -> locals off, freeze the DENSE TRUNK + embeddings; gate + netbank
                 adapt. Honours "the trunk freezes over time" while letting routing
                 and consolidation (where learning belongs) adapt. [default]
      "all"   -> locals off, freeze everything except V_net (over-froze: V_net through
                 frozen keys can't absorb the gap → distorts. kept for ablation)."""
    sg = mx.stop_gradient
    lvl = student if isinstance(student, str) else ("all" if student else "off")
    Ft = (lambda t: sg(t)) if lvl in ("trunk", "all") else (lambda t: t)   # dense trunk + emb
    Fa = (lambda t: sg(t)) if lvl == "all" else (lambda t: t)              # gate + net keys
    Fo = (lambda t: None if t is None else Fa(t))                          # optional gate tensor
    locals_off = (lvl != "off")
    P = {
        "tok_emb": Ft(trainable["tok_emb"]),
        "norm_final_w": Ft(trainable["norm_final_w"]),
        "norm_final_eps": static["norm_final_eps"],
        "rope_cos": static["rope_cos"], "rope_sin": static["rope_sin"],
        "blocks": [],
    }
    for tb, sb, bm in zip(trainable["blocks"], static["blocks"], meta["blocks"]):
        b = {k: Ft(tb[k]) for k in ("norm1_w", "norm2_w", "q_proj", "k_proj_s",
                                    "v_proj_s", "k_proj_l", "v_proj_l", "o_proj",
                                    "gate_proj", "up_proj", "down_proj")}
        b.update(n_heads=sb["n_heads"], n_short_heads=sb["n_short_heads"],
                 n_long_heads=sb["n_long_heads"], n_short_kv=sb["n_short_kv"],
                 n_long_kv=sb["n_long_kv"], head_dim=sb["head_dim"],
                 norm1_eps=sb["norm1_eps"], norm2_eps=sb["norm2_eps"],
                 trunk_ids=static["trunk_ids"], memory=None, netbank=None)
        b["bank_query_w"] = Ft(tb["bank_query_w"]) if "bank_query_w" in tb else None
        if bm["gate_kind"] == "SumGate":
            b["gate"] = _blocks.sum_gate
        else:  # SwitchGate — close over this block's gate params (frozen in student)
            gp = {"gate_proj": Fa(tb["sw_gate_proj"]), "gate_proj_3": Fa(tb["sw_gate_proj_3"]),
                  "alpha_net": Fo(tb.get("sw_alpha_net")),
                  "local_active_proj": Fo(tb.get("sw_local_active_proj")),
                  "local_active_bias": Fo(tb.get("sw_local_active_bias"))}
            b["gate"] = (lambda gp: (lambda ql, s, mo, no=None, collect_distill=False:
                                     _blocks.switch_gate_eval(gp, ql, s, mo, no, collect_distill)))(gp)
        if bm["memory"] and not locals_off:                     # locals OFF in student
            mm = sb["mem"]
            b["memory"] = {"q_norm_w": tb["mem_q_norm_w"], "eps": mm["eps"],
                           "K_a": tb["mem_K_a"], "K_b": tb["mem_K_b"], "V": tb["V_local"],
                           "sub_dim": mm["sub_dim"], "sqrt_n": mm["sqrt_n"],
                           "sub_top_k": mm["sub_top_k"], "top_k": mm["top_k"],
                           "n_trunks": mm["n_trunks"]}
        if bm.get("net_modular") and not drop_net:     # ModularNetBank (skill-module partition)
            nn_ = sb["net"]
            b["netbanks"] = {name: {"q_norm_w": Fa(d["net_q_norm_w"]), "eps": nn_["eps"],
                                    "K_a": Fa(d["net_K_a"]), "K_b": Fa(d["net_K_b"]),
                                    "V": d["V_net"],                    # V_net stays LIVE
                                    "expander_w": Fa(d["net_expander_w"]),
                                    "sub_dim": nn_["sub_dim"], "sqrt_n": nn_["sqrt_n"],
                                    "sub_top_k": nn_["sub_top_k"], "top_k": nn_["top_k"]}
                             for name, d in tb["netbanks"].items()}
            # per-batch skill routing: active module(s) set on `static` by the
            # train loop from the batch's corpus (None = all → composition).
            b["net_active"] = static.get("_net_active")
        elif bm["netbank"] and not drop_net:            # drop_net=True -> LOCAL-only teacher
            nn_ = sb["net"]
            b["netbank"] = {"q_norm_w": Fa(tb["net_q_norm_w"]), "eps": nn_["eps"],
                            "K_a": Fa(tb["net_K_a"]), "K_b": Fa(tb["net_K_b"]),
                            "V": tb["V_net"],                    # V_net stays LIVE
                            "expander_w": Fa(tb["net_expander_w"]), "sub_dim": nn_["sub_dim"],
                            "sqrt_n": nn_["sqrt_n"], "sub_top_k": nn_["sub_top_k"],
                            "top_k": nn_["top_k"]}
        P["blocks"].append(b)
    return P


def _write_back(trainable, m, K):
    """Copy trained MLX arrays back into the torch model params, by role."""
    import torch
    def cp(param, arr):
        param.data.copy_(torch.from_numpy(np.array(arr)).to(param.dtype))
    cp(m.get(K("tok-emb")).weight, trainable["tok_emb"])
    cp(m.get(K("norm-final")).weight, trainable["norm_final_w"])
    for tb, blk in zip(trainable["blocks"], m.get(K("blocks"))):
        g = lambda n: blk.get(K(n))
        for role, key in (("norm1_w", "norm1"), ("norm2_w", "norm2"), ("q_proj", "q-proj"),
                          ("k_proj_s", "k-proj-s"), ("v_proj_s", "v-proj-s"),
                          ("k_proj_l", "k-proj-l"), ("v_proj_l", "v-proj-l"),
                          ("o_proj", "o-proj"), ("gate_proj", "gate-proj"),
                          ("up_proj", "up-proj"), ("down_proj", "down-proj")):
            cp(g(key).weight, tb[role])
        gate = g("long-gate")
        if type(gate).__name__ == "SwitchGate":
            cp(gate.gate_proj, tb["sw_gate_proj"]); cp(gate.gate_proj_3, tb["sw_gate_proj_3"])
            if "sw_alpha_net" in tb: cp(gate.alpha_net, tb["sw_alpha_net"])
            if "sw_local_active_proj" in tb:
                cp(gate.local_active_proj, tb["sw_local_active_proj"])
                cp(gate.local_active_bias, tb["sw_local_active_bias"])
        mem = g("memory")
        if mem is not None:
            cp(mem.q_norm.weight, tb["mem_q_norm_w"]); cp(mem.K_a, tb["mem_K_a"])
            cp(mem.K_b, tb["mem_K_b"]); cp(mem.V.weight, tb["V_local"])
        nb = g("netbank")
        if nb is not None:
            if hasattr(nb, "banks"):                  # ModularNetBank: per-module write-back
                for name, d in tb["netbanks"].items():
                    bank = nb.banks[name]
                    cp(bank.q_norm.weight, d["net_q_norm_w"]); cp(bank.K_a, d["net_K_a"])
                    cp(bank.K_b, d["net_K_b"]); cp(bank.expander.weight, d["net_expander_w"])
                    cp(bank.V.weight, d["V_net"])
            else:
                cp(nb.q_norm.weight, tb["net_q_norm_w"]); cp(nb.K_a, tb["net_K_a"])
                cp(nb.K_b, tb["net_K_b"]); cp(nb.expander.weight, tb["net_expander_w"])
                cp(nb.V.weight, tb["V_net"])


# ───────────────────────── optimizers ─────────────────────────
def _blk_get(block, path):
    """Navigate a per-block trainable subtree by a path tuple. Sparse-V keys are
    ('V_local',)/('V_net',) (legacy) or ('netbanks', <module>, 'V_net') (modular)."""
    node = block
    for p in path:
        node = node[p]
    return node


def _blk_set(block, path, val):
    node = block
    for p in path[:-1]:
        node = node[p]
    node[path[-1]] = val


class _DenseAdam:
    """Adam over the dense subtree (everything except the V tables). Operates on
    a flat name->array view so SparseAdam can own V_local/V_net separately."""
    def __init__(self, lr=1e-3, betas=(0.9, 0.999), eps=1e-8, wd=0.0):
        self.lr, (self.b1, self.b2), self.eps, self.wd = lr, betas, eps, wd
        self.m, self.v, self.t = {}, {}, 0

    def step(self, params, grads, skip_keys):
        self.t += 1
        bc1 = 1.0 - self.b1 ** self.t
        bc2 = 1.0 - self.b2 ** self.t
        def upd(path, p, g):
            if path in skip_keys or g is None:
                return p
            self.m[path] = self.b1 * self.m.get(path, mx.zeros(p.shape)) + (1 - self.b1) * g
            self.v[path] = self.b2 * self.v.get(path, mx.zeros(p.shape)) + (1 - self.b2) * g * g
            step = self.lr * (self.m[path] / bc1) / (mx.sqrt(self.v[path] / bc2) + self.eps)
            if self.wd:
                step = step + self.lr * self.wd * p
            return p - step
        return _map_with_path(params, grads, upd)


def _map_with_path(params, grads, fn, prefix=""):
    """Walk two matching pytrees (dict/list of arrays), applying fn(path,p,g)."""
    if isinstance(params, dict):
        return {k: _map_with_path(params[k], grads.get(k), fn, f"{prefix}.{k}")
                for k in params}
    if isinstance(params, list):
        return [_map_with_path(params[i], grads[i], fn, f"{prefix}.{i}")
                for i in range(len(params))]
    return fn(prefix, params, grads)


# ───────────────────────── the round ─────────────────────────
def _run_pkm_diag(P, load_corpus, T):
    """PKM key-collapse diagnostic. For each MMLLM_PKM_DIAG corpus, capture which
    V_net rows the NETBANK retrieves (per layer), then report per-corpus row spread
    and PAIRWISE overlap (averaged over layers). HIGH Jaccard = corpora share rows
    -> each round overwrites the last -> no retention (collapse IS the blocker).
    LOW Jaccard = distinct allocation -> collapse is NOT the blocker (look elsewhere)."""
    import mmllm.mlx.banks as _bk
    DIAG_B = 8
    paths = [p.strip() for p in os.environ["MMLLM_PKM_DIAG"].split(",") if p.strip()]
    cap = {}
    cur = [None]
    orig = _bk.netbank_forward
    def cap_nb(p, q, want_z=False):                     # capture this layer's top rows
        qn = _bk._rms_norm(q, p["q_norm_w"], p["eps"])
        qa = qn[..., : p["sub_dim"]]; qb = qn[..., p["sub_dim"]:]
        _, tg = _bk._pkm_select(qa, qb, p["K_a"], p["K_b"], p["sqrt_n"], p["sub_top_k"], p["top_k"])
        cap[cur[0]].append(np.asarray(tg).reshape(-1))
        return orig(p, q, want_z=want_z)
    _bk.netbank_forward = cap_nb
    _rng = np.random.default_rng(0)
    try:
        for path in paths:
            name = os.path.basename(path); cap[name] = []; cur[0] = name
            data = np.asarray(load_corpus(path, use_mmap=True)).reshape(-1)
            xb = np.empty((DIAG_B, T), dtype=np.int64)
            for j in range(DIAG_B):
                o = int(_rng.integers(0, max(1, data.size - T - 1)))
                xb[j] = data[o:o + T]
            mx.eval(_model.forward(P, mx.array(xb)))
    finally:
        _bk.netbank_forward = orig
    names = [os.path.basename(p) for p in paths]
    Vn = next((b["netbank"]["V"].shape[0] for b in P["blocks"] if b.get("netbank") is not None), None)
    nL = len(cap[names[0]])
    setsL = {n: [set(np.unique(cap[n][L]).tolist()) for L in range(nL)] for n in names}
    print("\n===== PKM KEY-COLLAPSE DIAGNOSTIC =====")
    print(f"  V_net rows={Vn}, netbank layers={nL}, tokens/corpus={DIAG_B*T}")
    for n in names:
        ur = np.mean([len(setsL[n][L]) for L in range(nL)])
        pd = np.mean([len(setsL[n][L]) / max(1, cap[n][L].size) for L in range(nL)])
        print(f"   {n}: avg {ur:.0f} unique rows/layer ({100*pd:.1f}% distinct of hits)")
    print("  pairwise Jaccard of retrieved-row sets, mean over layers (1.0=identical, 0=disjoint):")
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            jac = np.mean([len(setsL[names[i]][L] & setsL[names[j]][L]) /
                           max(1, len(setsL[names[i]][L] | setsL[names[j]][L])) for L in range(nL)])
            print(f"   {names[i]} vs {names[j]}: meanJaccard={jac:.3f}")
    print("  READ: high Jaccard = KEY COLLAPSE (corpora overwrite each other). low = distinct alloc.")
    print("=======================================\n")


def train_round(cfg, train_path, val_path, ckpt_dir, log_path,
                total, eval_every, ckpt_every):
    """Run one bird round in MLX. Builds via basilisp, trains in MLX, writes
    back to the torch model, saves dense.pt + bank bins (harvest-compatible)."""
    import basilisp.lang.runtime as rt
    from basilisp.lang import keyword as kw, symbol as sym
    import torch
    K = kw.keyword
    def bvar(n):
        return rt.Var.find(sym.symbol(n, ns="mmllm.core")).value

    build_model = bvar("build-model")
    from mmllm.corpus import load_as_tensor as load_corpus  # plain Python module

    B = int(os.environ.get("MMLLM_BATCH", str(bvar("pick-batch")())))  # match torch's pick-batch
    T = int(cfg.get(K("seq-len")) or 256)
    cap = int(os.environ.get("MMLLM_MLX_MAX_STEPS", str(total)))
    n_steps = min(total, cap)
    # LRs are NOT fixed here — they're computed per step by the recipe schedule
    # (lr-at-step × pick-lr-{bank,net,dense}-mult; see `schedule` below). The bank
    # SparseAdam / dense AdamW are seeded with the recipe base and overwritten each
    # step, so there are no standalone lr_dense/lr_bank/lr_net knobs to drift.
    lr_base = float(bvar("pick-lr")())

    print(f"  [mlx] train_round: B={B} T={T} steps={n_steps} "
          f"lr_base={lr_base} (per-step schedule: pick-lr × {{bank,net,dense}}-mult)")

    m = build_model(cfg)
    # REWARM: one-shot realign the NetBank K_a/K_b from the (healthy, content-aligned)
    # Local Bank keys — the purpose-built lever (core.lpy rewarm-netbank-keys-only!)
    # for breaking the collapsed-keys / gate-suppresses-Net feedback loop. train-long
    # calls this on the torch path; the MLX path bypasses train-long, so do it here.
    if os.environ.get("MMLLM_REWARM_NETBANK_KEYS", "").lower() == "true":
        bvar("rewarm-netbank-keys-only!")(m)
        print("  [mlx] REWARM_NETBANK_KEYS: realigned net K_a/K_b from Local (V untouched)")
    params_fn = bvar("parameters")
    vocab = m.get(K("tok-emb")).weight.shape[0]

    # Chain resume: load the LATEST ckpt_dir/step-<N>/dense.pt — the layout
    # extend_chain.sh uses (it seeds the chain head at step-1/dense.pt and reads
    # the bird's output from the highest step-N dir). Loading from ckpt_dir
    # directly would MISS the head and train from scratch, regressing the chain.
    # V_net carries across rounds via its stable mmap path (bank_on_gpu=false);
    # V_local resets to build-time init — standard chain semantics.
    import glob as _glob, re as _re
    resume_step = 0
    _cands = []
    for _p in _glob.glob(os.path.join(ckpt_dir, "step-*")):
        _mo = _re.match(r".*step-(\d+)$", _p)
        if _mo and os.path.exists(os.path.join(_p, "dense.pt")):
            _cands.append((int(_mo.group(1)), _p))
    _cands.sort()
    if (os.environ.get("MMLLM_MLX_RESUME", "true").lower() in ("1", "true")
            and _cands):
        resume_step, resume_dir = _cands[-1]
        resume = os.path.join(resume_dir, "dense.pt")
        saved = list(torch.load(resume, map_location="cpu", weights_only=False))
        ps = list(params_fn(m))
        nload = 0
        for p, s in zip(ps, saved):
            if tuple(p.shape) == tuple(s.shape):
                p.data.copy_(s.to(p.dtype)); nload += 1
        print(f"  [mlx] resumed {nload}/{len(ps)} dense params from {resume} (step {resume_step})")
        # chain semantics: V_local zero-inits each round (V_net carries via mmap).
        if os.environ.get("MMLLM_MLX_RESET_LOCAL", "true").lower() in ("1", "true"):
            for blk in m.get(K("blocks")):
                mem = blk.get(K("memory"))
                if mem is not None:
                    mem.V.weight.data.zero_()

    # steps this round = train from the resumed step toward `total` (extend_chain
    # passes total=STEPS+1 and seeds step-1, i.e. STEPS training steps).
    n_steps = min(max(1, total - resume_step), cap)

    # PER-STEP MIX: each batch draws its windows from corpora sampled per-window
    # (weighted), so EVERY step trains on the diverse mix and the NetBank
    # consolidates GENERAL memory. The prior per-ROUND single-corpus draw (#64)
    # broke consolidation: each round baked one corpus into V_net, then the
    # diverse mix-val eval scored that corpus-specific content as harmful → Δ_net
    # went corpus-dependent (positive on centered corpora, negative on off-center
    # like aesop), and 1-way harvests had no averaging to wash it out. Smoke:
    # per-round-single gave Δ_net −0.11/−0.19 on aesop rounds; per-step mix keeps
    # the netbank general. MMLLM_MIX="path:w,path:w,..."; mmap'd uint8 so memory is
    # bounded regardless of mix size (windows cast to int64 at batch time).
    _rng = np.random.default_rng()
    # RETENTION test phase switch: train MMLLM_MIX_P1 (the probe corpus) for the
    # first MMLLM_PHASE1_STEPS cumulative steps, then MMLLM_MIX_P2 (other corpora)
    # — locals reset each round, V_net carries. With MMLLM_PROBE fixed on the probe
    # corpus, Δ_net over the P2 rounds measures how much of P1 the net RETAINS.
    _p1_rounds = int(os.environ.get("MMLLM_PHASE1_ROUNDS", "0"))
    if _p1_rounds:
        # Phase by a per-arm FILE COUNTER (neither resume_step nor log_path carry a
        # usable round index — resume_step is pinned at 1, log_path is a generic
        # name). train_round runs once per round, so increment-per-call IS the round
        # count: train MMLLM_MIX_P1 (the probe) for the first _p1_rounds rounds, then
        # MMLLM_MIX_P2 (others). The driver clears the marker before each run.
        _marker = os.environ.get("MMLLM_PHASE_MARKER", "/tmp/ret-phase-start")
        _n = int(open(_marker).read().strip()) if os.path.exists(_marker) else 0
        with open(_marker, "w") as _f:
            _f.write(str(_n + 1))
        _mix = os.environ.get("MMLLM_MIX_P1" if _n < _p1_rounds else "MMLLM_MIX_P2", "").strip()
        print(f"  [mlx] retention phase: {'P1(probe)' if _n < _p1_rounds else 'P2(other)'} "
              f"round_count={_n} (P1 rounds={_p1_rounds})")
    else:
        _mix = os.environ.get("MMLLM_MIX", "").strip()
    if _mix:
        ents = []
        for e in _mix.split(","):
            e = e.strip()
            if not e:
                continue
            c = e.rfind(":")
            ents.append((e[:c].strip(), float(e[c + 1:].strip())))
        corpora = [np.asarray(load_corpus(p, use_mmap=True)).reshape(-1) for p, _ in ents]
        ws = np.array([w for _, w in ents], dtype=float); ws = ws / ws.sum()
        corpus_path = ents[0][0]                          # for the "round" eval-mode fallback
        _mix_paths = [p for p, _ in ents]
        print(f"  [mlx] per-step mix: {len(corpora)} corpora (weighted), windows drawn per-sample")
    else:
        corpora = [np.asarray(load_corpus(train_path, use_mmap=True)).reshape(-1)]
        ws = np.array([1.0]); corpus_path = train_path; _mix_paths = [train_path]

    # Skill-module routing: per-corpus module name (None unless MMLLM_NET_MODULES).
    # When modular, sample ONE corpus per batch (not per-window) so the batch maps
    # to a single module — partitioning obviates the per-window-mix consolidation
    # fix (that was for the SHARED net; modules don't cross-contaminate).
    from mmllm.skill_modules import parse_modules as _pm, module_for_corpus as _m4c
    _net_modules = _pm()
    def _corp_base(p):
        b = os.path.basename(p)
        for suf in (".train.bin", ".bin"):
            if b.endswith(suf):
                b = b[:-len(suf)]
        return b
    corpus_modules = ([_m4c(_corp_base(p), _net_modules) for p in _mix_paths]
                      if _net_modules else None)
    if corpus_modules is not None:
        print(f"  [mlx] skill-module routing: corpus→module {dict(zip([_corp_base(p) for p in _mix_paths], corpus_modules))}")

    def batch():
        if corpus_modules is not None:
            # MODULAR: one corpus for the whole batch → route all windows to its module.
            ci = int(_rng.choice(len(corpora), p=ws))
            static["_net_active"] = corpus_modules[ci]
            c = corpora[ci]
            xb = np.empty((B, T), dtype=np.int64); yb = np.empty((B, T), dtype=np.int64)
            for j in range(B):
                o = int(_rng.integers(0, c.size - T - 1))
                xb[j] = c[o:o + T]; yb[j] = c[o + 1:o + 1 + T]
            return mx.array(xb), mx.array(yb)
        # per-window mix (monolithic net): each of B samples its own corpus + window
        cis = _rng.choice(len(corpora), size=B, p=ws)
        xb = np.empty((B, T), dtype=np.int64); yb = np.empty((B, T), dtype=np.int64)
        for j in range(B):
            c = corpora[int(cis[j])]; o = int(_rng.integers(0, c.size - T - 1))
            xb[j] = c[o:o + T]; yb[j] = c[o + 1:o + 1 + T]
        return mx.array(xb), mx.array(yb)

    n_trunks = 1
    for blk in m.get(K("blocks")):
        mem = blk.get(K("memory"))
        if mem is not None:
            n_trunks = max(n_trunks, getattr(mem, "n_trunks", 1))
    trunk_ids = mx.array((np.arange(B) % n_trunks).astype(np.int64))

    # MMLLM_NET_WIDEN=C: widen the torch NetBank code dim c_net -> C (8->16=q_dim),
    # AFTER the head is loaded, so the FULL pipeline (extract/train/eval/write-back)
    # runs at C — the expander rank (c_net) is the netbank's functional bottleneck.
    # V new cols=0 (empty memory); expander new cols=small random (zero-on-both
    # deadlocks the gradient). Output unchanged at start; distill can then populate
    # the new capacity. Smoke-only (the chain V_net.bin stays c_net=8).
    _wide = int(os.environ.get("MMLLM_NET_WIDEN", "0"))
    if _wide:
        import torch
        import torch.nn as nn
        _did = 0
        for blk in m.get(K("blocks")):
            nb = blk.get(K("netbank"))
            if nb is None or not hasattr(getattr(nb, "V", None), "weight"):
                continue
            if getattr(nb, "c_net", _wide) >= _wide:
                continue
            with torch.no_grad():
                Vw = nb.V.weight; dev, dt = Vw.device, Vw.dtype; pad = _wide - Vw.shape[1]
                newV = torch.cat([Vw, torch.zeros(Vw.shape[0], pad, device=dev, dtype=dt)], dim=1)
                nb.V = nn.Embedding(newV.shape[0], _wide, _weight=newV).to(dev)
                Ew = nb.expander.weight
                newE = torch.cat([Ew, 0.02 * torch.randn(Ew.shape[0], pad, device=dev, dtype=dt)], dim=1)
                exp = nn.Linear(_wide, Ew.shape[0], bias=False).to(dev); exp.weight = nn.Parameter(newE)
                nb.expander = exp; nb.c_net = _wide
                _did += 1
        print(f"  [mlx] NET_WIDEN: widened {_did} netbanks to c_net={_wide} (torch model)")

    trainable, static, meta = _extract(m, K, trunk_ids)

    # CTXADD inject: add a zero W_ctx (ctx-add bank query) at the MLX-trainable level
    # AFTER the (positional) resume, so resume stays clean. W_ctx trains as a dense
    # param toward content-discriminative queries → de-collapses retrieval. Single-run
    # test (not persisted — for genesis/chain it must live in the torch model).
    if os.environ.get("MMLLM_CTXADD_INJECT") == "true":
        _dm = trainable["tok_emb"].shape[1]; _n = 0; _loaded = 0
        for _bi, (tb, sb) in enumerate(zip(trainable["blocks"], static["blocks"])):
            if "bank_query_w" not in tb:
                _wp = os.path.join(os.environ.get("MMLLM_SCRATCH") or ckpt_dir, f"wctx.{_bi}.npy")
                if os.path.exists(_wp):
                    tb["bank_query_w"] = mx.array(np.load(_wp)); _loaded += 1
                else:
                    _qd = sb["n_long_heads"] * sb["head_dim"]
                    tb["bank_query_w"] = mx.zeros((_qd, _dm))
                _n += 1
        print(f"  [mlx] CTXADD_INJECT: W_ctx on {_n} blocks ({_loaded} loaded from persisted, rest zero)")

    if os.environ.get("MMLLM_PKM_DIAG") and not os.environ.get("MMLLM_POST_DIAG"):
        _run_pkm_diag(_reassemble(trainable, static, meta), load_corpus, T)
        return {"pkm_diag": True}

    # sparse optimizers per bank (keyed by block index + which table)
    sparse = {}   # (bi, path_tuple) -> SparseAdam; path navigates trainable["blocks"][bi]
    for bi, tb in enumerate(trainable["blocks"]):
        if "V_local" in tb:
            sparse[(bi, ("V_local",))] = SparseAdam(tb["V_local"].shape[0],
                                                    tb["V_local"].shape[1], lr=lr_base)
        if "netbanks" in tb:                          # ModularNetBank: one SparseAdam per module
            for name, d in tb["netbanks"].items():
                sparse[(bi, ("netbanks", name, "V_net"))] = SparseAdam(
                    d["V_net"].shape[0], d["V_net"].shape[1], lr=lr_base)
        elif "V_net" in tb:
            sparse[(bi, ("V_net",))] = SparseAdam(tb["V_net"].shape[0],
                                                  tb["V_net"].shape[1], lr=lr_base)
    dense_opt = _DenseAdam(lr=lr_base)  # overwritten per-step by the schedule
    sparse_keys = {f".blocks.{bi}." + ".".join(path) for (bi, path) in sparse}
    # snapshot V tables at init for the consolidation/moved% check (CLAUDE.md
    # false-positive guard: real training -> moved% >> 1% AND cos(V,init) < 1).
    v_init = {(bi, path): np.array(_blk_get(trainable["blocks"][bi], path))
              for (bi, path) in sparse}

    z_coef = float(bvar("pick-z-loss-coef")())
    # OUTPUT-KD: real Hinton distillation instead of feature-MSE. The model WITH
    # the local banks (just trained on this round's data) is the teacher; the
    # model with all locals OFF (net banks only — the FUTURE state, when locals
    # reset) is the student. The net learns to reproduce the local-augmented
    # model's SOFT LOGITS on its own → it absorbs the locals' learned function.
    _kd_obj = os.environ.get("MMLLM_DISTILL_OBJECTIVE", "mse") == "logitkd"
    _kd_temp = float(os.environ.get("MMLLM_KD_TEMP", "2.0"))
    _kd_coef = float(os.environ.get("MMLLM_KD_COEF", "1.0"))
    _kd_freeze = os.environ.get("MMLLM_KD_FREEZE", "trunk")     # off/none/trunk/all
    # NetBank anti-collapse: its own router-entropy z-loss coef (the local bank's is
    # pick-z-loss-coef). The netbank historically had NO such term -> keys collapsed
    # (corpora share ~1% hot rows). Crank this to de-collapse: spread net routing so
    # corpora get distinct V_net rows. Default 0 = old (collapsed) behaviour.
    _net_z_coef = float(os.environ.get("MMLLM_NET_Z_COEF", "0"))

    def loss_fn(tr):
        xb, yb = static["_xb"], static["_yb"]
        P = _reassemble(tr, static, meta)
        logits, distill_total, z_total, net_z_total, n_distill = _model.forward(
            P, xb, collect_aux=True)
        lg = logits.reshape(-1, vocab)
        logp = lg - mx.logsumexp(lg, axis=-1, keepdims=True)
        ce = -mx.take_along_axis(logp, yb.reshape(-1)[:, None], axis=-1).mean()
        loss = ce
        if z_coef:
            loss = loss + z_coef * z_total
        if _net_z_coef:
            loss = loss + _net_z_coef * net_z_total
        if _kd_obj:
            # REAL LB->NB output distillation (Hinton soft-target KD):
            #   TEACHER = Local-only forward (sdpa+local, net OFF), the good/stable
            #     teacher (local just trained this round's data). Detached (stop_grad).
            #   STUDENT = net-only forward (sdpa+net, local OFF) — the future state.
            #   loss = KL(teacher_softT || student_softT) * T^2  (dark knowledge).
            # The net LEARNS to reproduce the local's OUTPUT DISTRIBUTION. Success is
            # this KL FALLING (net matches local) — not Δ_net.
            Ploc = _reassemble(tr, static, meta, drop_net=True)        # local-only teacher
            t_lg = _model.forward(Ploc, xb).reshape(-1, vocab) / _kd_temp
            t_logp = mx.stop_gradient(t_lg - mx.logsumexp(t_lg, axis=-1, keepdims=True))
            t_p = mx.exp(t_logp)
            Pnet = _reassemble(tr, static, meta, student=_kd_freeze)   # net-only student (locals off)
            s_lg = _model.forward(Pnet, xb).reshape(-1, vocab) / _kd_temp
            s_logp = s_lg - mx.logsumexp(s_lg, axis=-1, keepdims=True)
            kd = (t_p * (t_logp - s_logp)).sum(-1).mean() * (_kd_temp * _kd_temp)
            loss = loss + _kd_coef * kd
        else:
            dc = static["_distill_coef"]
            if dc and n_distill:
                loss = loss + dc * (distill_total / max(1, n_distill))
        return loss

    # Per-step LR + distill schedule — call the SAME basilisp functions train-long
    # uses (core.lpy:4783-4789) so the recipe is byte-identical: cur_lr =
    # lr-at-step(cosine from pick-lr to LR_MIN); lr_bank/lr_net/lr_dense = cur_lr ×
    # the per-tier mult ramps (lr_net ramps to pick-lr × LR_NET_MULT_END — the
    # wake/sleep consolidation the prod recipe needs; my old hardcoded lr_net=1e-4
    # was the bug that left V_net frozen). The round trains the [resume_step+1,
    # total] slice of the global schedule.
    _lr_at_step = bvar("lr-at-step"); _pick_lr = bvar("pick-lr")
    _pick_lr_min = bvar("pick-lr-min"); _warmup = bvar("pick-lr-warmup")()
    _bank_mult = bvar("pick-lr-bank-mult"); _net_mult = bvar("pick-lr-net-mult")
    _dense_mult = bvar("pick-lr-dense-mult"); _distill = bvar("pick-distill-coef")

    def schedule(local_step):
        g = resume_step + local_step                       # global step in schedule
        cur = float(_lr_at_step(g, total, _pick_lr(), _warmup, _pick_lr_min()))
        return (cur * float(_bank_mult(g, total)),         # lr_bank (V_local)
                cur * float(_net_mult(g, total)),          # lr_net  (V_net)
                cur * float(_dense_mult(g, total)),        # lr_dense
                float(_distill(g, total)))                 # distill coef

    losses = []
    for step in range(1, n_steps + 1):
        lb, ln, ld, dc = schedule(step)
        static["_distill_coef"] = dc
        dense_opt.lr = ld
        for (bi, path), opt in sparse.items():
            opt.lr = lb if path[-1] == "V_local" else ln
        xb, yb = batch()
        static["_xb"], static["_yb"] = xb, yb
        loss, grads = mx.value_and_grad(loss_fn)(trainable)
        mx.eval(loss)
        # sparse banks first (read grads before dense update rewrites the tree)
        for (bi, path), opt in sparse.items():
            gV = np.array(_blk_get(grads["blocks"][bi], path))
            rows = np.nonzero(np.abs(gV).sum(1) > 0)[0]
            if len(rows):
                _blk_set(trainable["blocks"][bi], path,
                         opt.step(_blk_get(trainable["blocks"][bi], path),
                                  mx.array(rows), mx.array(gV[rows])))
        trainable = dense_opt.step(trainable, grads, sparse_keys)
        mx.eval(tree_map(lambda a: a, trainable))
        losses.append(float(loss))
        if step % max(1, eval_every) == 0 or step == n_steps:
            # DISTILL DIAGNOSTIC (smoke): separate forward outside the grad trace —
            # is distill firing? raw magnitude, layer coverage (24 vs 8 = topology
            # regression), per-layer, coef×contribution vs CE (over/under-firing).
            try:
                _lg, _dt, _zt, _nzt, _nd = _model.forward(_reassemble(trainable, static, meta), xb, collect_aux=True)
                _dtv = float(_dt); _ndv = int(_nd)
                _lr2 = _lg.reshape(-1, vocab); _lp2 = _lr2 - mx.logsumexp(_lr2, axis=-1, keepdims=True)
                _ce = float(-mx.take_along_axis(_lp2, yb.reshape(-1)[:, None], axis=-1).mean())
                _dbg = (f"  [DISTILL] raw_total={_dtv:.4f} n_layers={_ndv} "
                        f"per_layer={_dtv/max(1,_ndv):.4f} coef×contrib={dc*_dtv/max(1,_ndv):.4f} vs CE={_ce:.4f}"
                        f" | net_z={float(_nzt):.3f} (collapse proxy: falling=spreading)")
                if _kd_obj:
                    # THE distillation success metric: KL(local-only teacher || net-only
                    # student). FALLING = the net is learning to reproduce the local
                    # (distillation actually working) — independent of Δ_net.
                    _Pl = _reassemble(trainable, static, meta, drop_net=True)
                    _tl = _model.forward(_Pl, xb).reshape(-1, vocab) / _kd_temp
                    _tlp = _tl - mx.logsumexp(_tl, axis=-1, keepdims=True); _tp = mx.exp(_tlp)
                    _Pn = _reassemble(trainable, static, meta, student=_kd_freeze)
                    _sl = _model.forward(_Pn, xb).reshape(-1, vocab) / _kd_temp
                    _slp = _sl - mx.logsumexp(_sl, axis=-1, keepdims=True)
                    _kdv = float((_tp * (_tlp - _slp)).sum(-1).mean())
                    # teacher (local-only) and student (net-only) standalone bpc on this batch
                    _tbpc = float(-mx.take_along_axis(_tl * _kd_temp - mx.logsumexp(_tl * _kd_temp, axis=-1, keepdims=True),
                                  yb.reshape(-1)[:, None], axis=-1).mean()) / math.log(2)
                    _sbpc = float(-mx.take_along_axis(_sl * _kd_temp - mx.logsumexp(_sl * _kd_temp, axis=-1, keepdims=True),
                                  yb.reshape(-1)[:, None], axis=-1).mean()) / math.log(2)
                    _dbg += (f" | KD(local→net)={_kdv:.4f} (FALLING=net learning local) "
                             f"teacher_bpc={_tbpc:.3f} student_bpc={_sbpc:.3f}")
            except Exception as _e:
                _dbg = f"  [DISTILL] diag-failed: {_e}"
            print(f"  [mlx] step {step}/{n_steps}  loss={losses[-1]:.4f}  "
                  f"lr_b={lb:.2e} lr_n={ln:.2e} lr_d={ld:.2e} distill_c={dc:.2f}{_dbg}")

    # POST-TRAINING diag: run the key-collapse diagnostic on the TRAINED trainable
    # (with the now-trained W_ctx if ctx-add was injected). Tests whether learned
    # content-discriminative queries de-collapsed retrieval, in-process (no resume).
    if os.environ.get("MMLLM_POST_DIAG"):
        _run_pkm_diag(_reassemble(trainable, static, meta), load_corpus, T)

    # write trained weights back into the torch model + save (harvest-compatible)
    _write_back(trainable, m, K)
    # Save dense.pt into a step-<total> dir (the layout extend_chain.sh reads:
    # it copies the highest step-N/dense.pt out for delta-encode + push). Bank
    # bins stay at ckpt_dir level (matches save-checkpoint!).
    target_step = total
    step_dir = os.path.join(ckpt_dir, f"step-{target_step}")
    os.makedirs(step_dir, exist_ok=True)
    dense_path = os.path.join(step_dir, "dense.pt")
    torch.save([p.detach().clone() for p in params_fn(m)], dense_path)
    with open(os.path.join(step_dir, "step.txt"), "w") as _sf:
        _sf.write(str(target_step))
    # bank V -> per-layer bins (the harvest reads these; same path as
    # save-checkpoint!'s mem.save_to_mmap). NetBank V is mmap-backed and the
    # write-back .copy_ writes through; Local needs an explicit save_to_mmap.
    from mmllm.mlx import bridge as _bridge
    for i, blk in enumerate(m.get(K("blocks"))):
        mem = blk.get(K("memory"))
        if mem is not None and hasattr(mem, "save_to_mmap"):
            try:
                mem.save_to_mmap(os.path.join(ckpt_dir, f"bank-latest.{i}.bin"))
            except Exception as e:
                print(f"  [mlx] WARN local V save layer {i}: {e}")
        nb = blk.get(K("netbank"))
        if nb is not None:
            # When mmap-backed (bank_on_gpu=false) the write-back .copy_ already
            # wrote through to nb.mmap_path. On GPU-resident V (MPS birds) persist
            # it explicitly so the harvest can read V_net.
            mp = getattr(nb, "mmap_path", None)
            if mp and not nb.V.weight.is_cpu:
                try:
                    _np(nb.V.weight).astype(np.float32).tofile(mp)
                except Exception as e:
                    print(f"  [mlx] WARN netbank V save layer {i}: {e}")
    # persist W_ctx (ctx-add bank query) across rounds — separate from dense.pt so the
    # positional harvest format is untouched. Loaded by the CTXADD_INJECT block.
    if os.environ.get("MMLLM_CTXADD_INJECT") == "true":
        _have = [_bi for _bi, tb in enumerate(trainable["blocks"]) if "bank_query_w" in tb]
        _norm = (float(np.linalg.norm(np.array(trainable["blocks"][_have[0]]["bank_query_w"])))
                 if _have else -1.0)
        print(f"  [mlx] wctx-save: {len(_have)} blocks have W_ctx; ||W_ctx[0]||={_norm:.4f}; ckpt_dir={ckpt_dir}")
        _wdir = os.environ.get("MMLLM_SCRATCH") or ckpt_dir
        for _bi in _have:
            np.save(os.path.join(_wdir, f"wctx.{_bi}.npy"), np.array(trainable["blocks"][_bi]["bank_query_w"]))
    print(f"  [mlx] wrote {dense_path} ({len(losses)} steps, "
          f"loss {losses[0]:.4f}->{losses[-1]:.4f})")

    # consolidation check: how far did each V table move from init?
    result = {"steps": len(losses), "loss_start": losses[0], "loss_end": losses[-1]}
    for (bi, path), opt in sparse.items():
        cur = np.array(_blk_get(trainable["blocks"][bi], path)); init = v_init[(bi, path)]
        # label: "V_local" / "V_net" (legacy) or "V_net.<module>" (modular)
        label = "V_net." + path[1] if path[0] == "netbanks" else path[-1]
        if path[-1] == "V_local":
            # V_local zero-inits each round — moved%-from-zero is undefined; report
            # the filled norm (how much Local accumulated this round) instead.
            print(f"  [mlx] V_local block{bi}: ||V||={np.linalg.norm(cur):.3f} (filled from 0)")
            continue
        moved = float(np.linalg.norm(cur - init) / (np.linalg.norm(init) + 1e-9))
        cos = float((cur.ravel() @ init.ravel()) /
                    (np.linalg.norm(cur) * np.linalg.norm(init) + 1e-9))
        result[f"{label}_b{bi}_moved%"] = round(moved * 100, 3)
        print(f"  [mlx] {label} block{bi}: moved%={moved*100:.3f}  cos(V,init)={cos:.4f}")

    # eval ctrl_bpc (torch forward of the MLX-trained, written-back model — also
    # cross-validates the write-back). Best-effort.
    #
    # Eval corpus must REFLECT the training distribution, not a fixed single corpus
    # — otherwise ctrl_bpc measures drift away from that corpus rather than quality
    # (the chain-wide default evals val_path=fim-json even while training the diverse
    # MMLLM_MIX). MMLLM_MLX_EVAL_MODE:
    #   mix   (default when MMLLM_MIX set) — held-out tail of EACH mix corpus,
    #          concatenated: mix-representative AND identical across birds (so the
    #          harvest's cross-bird ctrl_bpc comparison stays valid).
    #   round — this round's trained corpus (reflects the round; not cross-comparable)
    #   val   — legacy fixed val_path (fim-json)
    # Eval cap + B mirror the torch path (pick-ablation-eval-cap, B=16).
    try:
        eval_bpc = bvar("eval-bpc")
        ev = int(bvar("pick-ablation-eval-cap")(25000))          # = torch's cap (recipe-driven)
        eval_b = int(os.environ.get("MMLLM_EVAL_BATCH", "16"))   # torch evals at 16
        eval_mode = os.environ.get("MMLLM_MLX_EVAL_MODE", "mix" if _mix else "val")
        _probe = os.environ.get("MMLLM_PROBE", "").strip()
        if _probe:
            # RETENTION test: eval on a FIXED probe corpus, DECOUPLED from the train
            # mix. Train the net on the probe early, then train on OTHER corpora
            # (locals reset, net carries); Δ_net on the probe each round = how much
            # of the probe the net still retains (true cross-round consolidation).
            vdata = load_corpus(_probe)
            print(f"  [mlx] eval corpus: PROBE {os.path.basename(_probe)} (retention test)")
        elif eval_mode == "mix" and _mix:
            # Same builder the torch train-long calls (core.lpy:pick-mix-val):
            # held-out tail of EACH MMLLM_MIX corpus, in MMLLM_MIX order, sized by
            # MMLLM_MIX_VAL_PER_CORPUS. Calling it (rather than rebuilding inline)
            # is what guarantees MLX and fork birds eval byte-identical tokens, so
            # the harvest's cross-bird ctrl_bpc comparison stays valid.
            vdata = bvar("pick-mix-val")()
            per = int(os.environ.get("MMLLM_MIX_VAL_PER_CORPUS", "4096"))
            print(f"  [mlx] eval corpus: mix held-out ({len(ents)} corpora × {per} tok)")
        elif eval_mode == "round":
            vdata = load_corpus(corpus_path)
            print(f"  [mlx] eval corpus: {os.path.basename(corpus_path)} (this round's)")
        else:
            vdata = load_corpus(val_path)
            print(f"  [mlx] eval corpus: {os.path.basename(val_path)} (fixed val)")
        r = eval_bpc(m, vdata, T, eval_b, ev)
        bpc = float(r.get(kw.keyword("bpc")))
        result["ctrl_bpc"] = bpc
        print(f"  [mlx] eval ctrl_bpc={bpc:.4f}")
        # ablations: Δ_local, Δ_net, Δ_both (zero the bank V -> re-eval -> restore).
        # Then write the {"event":"ablation",...} JSON line extend_chain.sh parses
        # for FINAL_CTRL + the round summary (control_bpc/delta_* keys; without it
        # the bird reported FINAL_CTRL=unknown).
        dl = dn = db = None
        try:
            # Δ_net only per round (the headline consolidation signal). Δ_local /
            # Δ_both are extra eval-bpc passes — expensive on the 24-layer CPU
            # eval — so we skip them per round (extend_chain tolerates null).
            _n = bvar("ablation-step-net!")(m, vdata, T, eval_b, ev)
            dn = (float(_n) - bpc) if _n is not None else None
            if dn is not None:
                result["delta_net"] = dn
            print(f"  [mlx] Δ_net={dn}  (ablated_bpc={_n})")
        except Exception as e:
            print(f"  [mlx] ablation skipped: {e}")
        # CONSOLIDATION metric: locals-off bpc (zero LOCAL V -> model on net+trunk
        # only = the future state when locals reset). LOWER = the net carries more.
        # This is the signal same-round Δ_net can't see (locals present mask the
        # net). env-gated — it's an extra eval pass, skip in production.
        if os.environ.get("MMLLM_ABLATE_LOCAL"):
            try:
                _l = bvar("ablation-step!")(m, vdata, T, eval_b, ev)
                dl = (float(_l) - bpc) if _l is not None else None
                if dl is not None:
                    result["delta_local"] = dl
                print(f"  [mlx] locals_off_bpc={_l} (Δ_local={dl}) "
                      f"← consolidation: lower locals_off = net carries more")
            except Exception as e:
                print(f"  [mlx] local-ablation skipped: {e}")
        # emit the harvest/summary event (extend_chain reads control_bpc/delta_*).
        try:
            import json as _json
            with open(log_path, "a") as _lf:
                _lf.write(_json.dumps({
                    "event": "ablation", "control_bpc": bpc,
                    "delta_local": dl, "delta_net": dn, "delta_both": db,
                }) + "\n")
        except Exception as e:
            print(f"  [mlx] log-event write skipped: {e}")
    except Exception as e:
        print(f"  [mlx] eval skipped: {e}")
    return result
