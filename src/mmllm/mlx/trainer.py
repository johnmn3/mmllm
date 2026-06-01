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
            tb["net_q_norm_w"] = _mxa(nb.q_norm.weight)
            tb["net_K_a"] = _mxa(nb.K_a); tb["net_K_b"] = _mxa(nb.K_b)
            tb["net_expander_w"] = _mxa(nb.expander.weight)
            tb["V_net"] = _mxa(nb.V.weight)
            sb["net"] = {"eps": _eps(nb.q_norm), "sub_dim": nb.sub_dim,
                         "sqrt_n": nb.sqrt_n, "sub_top_k": nb.sub_top_k, "top_k": nb.top_k}

        trainable["blocks"].append(tb)
        static["blocks"].append(sb)
        meta["blocks"].append(bmeta)
    static["trunk_ids"] = trunk_ids_mx
    return trainable, static, meta


def _reassemble(trainable, static, meta):
    """trainable + static -> the param dict model.forward consumes. Gate params
    come from `trainable` (via closures) so gradients flow to them."""
    P = {
        "tok_emb": trainable["tok_emb"],
        "norm_final_w": trainable["norm_final_w"],
        "norm_final_eps": static["norm_final_eps"],
        "rope_cos": static["rope_cos"], "rope_sin": static["rope_sin"],
        "blocks": [],
    }
    for tb, sb, bm in zip(trainable["blocks"], static["blocks"], meta["blocks"]):
        b = {k: tb[k] for k in ("norm1_w", "norm2_w", "q_proj", "k_proj_s",
                                "v_proj_s", "k_proj_l", "v_proj_l", "o_proj",
                                "gate_proj", "up_proj", "down_proj")}
        b.update(n_heads=sb["n_heads"], n_short_heads=sb["n_short_heads"],
                 n_long_heads=sb["n_long_heads"], n_short_kv=sb["n_short_kv"],
                 n_long_kv=sb["n_long_kv"], head_dim=sb["head_dim"],
                 norm1_eps=sb["norm1_eps"], norm2_eps=sb["norm2_eps"],
                 trunk_ids=static["trunk_ids"], memory=None, netbank=None)
        if bm["gate_kind"] == "SumGate":
            b["gate"] = _blocks.sum_gate
        else:  # SwitchGate — close over this block's (trainable) gate params
            gp = {"gate_proj": tb["sw_gate_proj"], "gate_proj_3": tb["sw_gate_proj_3"],
                  "alpha_net": tb.get("sw_alpha_net"),
                  "local_active_proj": tb.get("sw_local_active_proj"),
                  "local_active_bias": tb.get("sw_local_active_bias")}
            b["gate"] = (lambda gp: (lambda ql, s, mo, no=None, collect_distill=False:
                                     _blocks.switch_gate_eval(gp, ql, s, mo, no, collect_distill)))(gp)
        if bm["memory"]:
            mm = sb["mem"]
            b["memory"] = {"q_norm_w": tb["mem_q_norm_w"], "eps": mm["eps"],
                           "K_a": tb["mem_K_a"], "K_b": tb["mem_K_b"], "V": tb["V_local"],
                           "sub_dim": mm["sub_dim"], "sqrt_n": mm["sqrt_n"],
                           "sub_top_k": mm["sub_top_k"], "top_k": mm["top_k"],
                           "n_trunks": mm["n_trunks"]}
        if bm["netbank"]:
            nn_ = sb["net"]
            b["netbank"] = {"q_norm_w": tb["net_q_norm_w"], "eps": nn_["eps"],
                            "K_a": tb["net_K_a"], "K_b": tb["net_K_b"], "V": tb["V_net"],
                            "expander_w": tb["net_expander_w"], "sub_dim": nn_["sub_dim"],
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
            cp(nb.q_norm.weight, tb["net_q_norm_w"]); cp(nb.K_a, tb["net_K_a"])
            cp(nb.K_b, tb["net_K_b"]); cp(nb.expander.weight, tb["net_expander_w"])
            cp(nb.V.weight, tb["V_net"])


# ───────────────────────── optimizers ─────────────────────────
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

    B = int(os.environ.get("MMLLM_BATCH", "4"))
    T = int(cfg.get(K("seq-len")) or 256)
    lr_dense = float(os.environ.get("MMLLM_LR_DENSE", "1e-3"))
    lr_bank = float(os.environ.get("MMLLM_LR", "3e-2"))
    lr_net = float(os.environ.get("MMLLM_LR_NET", "1e-4"))
    cap = int(os.environ.get("MMLLM_MLX_MAX_STEPS", str(total)))
    n_steps = min(total, cap)

    print(f"  [mlx] train_round: B={B} T={T} steps={n_steps} "
          f"lr_dense={lr_dense} lr_bank={lr_bank} lr_net={lr_net}")

    m = build_model(cfg)
    params_fn = bvar("parameters")
    vocab = m.get(K("tok-emb")).weight.shape[0]

    # Chain resume: load the prior round's dense.pt positionally. V_net carries
    # across rounds via its stable mmap path (bank_on_gpu=false); V_local resets
    # to build-time init — standard chain semantics (dense+V_net forward, V_local
    # zero each round).
    resume = os.path.join(ckpt_dir, "dense.pt")
    if (os.environ.get("MMLLM_MLX_RESUME", "true").lower() in ("1", "true")
            and os.path.exists(resume)):
        saved = list(torch.load(resume, map_location="cpu", weights_only=False))
        ps = list(params_fn(m))
        nload = 0
        for p, s in zip(ps, saved):
            if tuple(p.shape) == tuple(s.shape):
                p.data.copy_(s.to(p.dtype)); nload += 1
        print(f"  [mlx] resumed {nload}/{len(ps)} dense params from {resume}")
        # chain semantics: V_local zero-inits each round (V_net carries via mmap).
        if os.environ.get("MMLLM_MLX_RESET_LOCAL", "true").lower() in ("1", "true"):
            for blk in m.get(K("blocks")):
                mem = blk.get(K("memory"))
                if mem is not None:
                    mem.V.weight.data.zero_()

    # corpus -> flat int token array (host)
    data = load_corpus(train_path)
    toks_np = np.asarray(data).astype(np.int64).reshape(-1)
    n_tok = toks_np.size
    rng = np.random.RandomState(0)

    def batch():
        # random-window LM batching: xb=[off:off+T], yb=[off+1:off+T+1]
        offs = rng.randint(0, n_tok - T - 1, size=B)
        xb = np.stack([toks_np[o:o + T] for o in offs])
        yb = np.stack([toks_np[o + 1:o + 1 + T] for o in offs])
        return mx.array(xb), mx.array(yb)

    n_trunks = 1
    for blk in m.get(K("blocks")):
        mem = blk.get(K("memory"))
        if mem is not None:
            n_trunks = max(n_trunks, getattr(mem, "n_trunks", 1))
    trunk_ids = mx.array((np.arange(B) % n_trunks).astype(np.int64))

    trainable, static, meta = _extract(m, K, trunk_ids)

    # sparse optimizers per bank (keyed by block index + which table)
    sparse = {}
    for bi, tb in enumerate(trainable["blocks"]):
        if "V_local" in tb:
            sparse[(bi, "V_local")] = SparseAdam(tb["V_local"].shape[0],
                                                 tb["V_local"].shape[1], lr=lr_bank)
        if "V_net" in tb:
            sparse[(bi, "V_net")] = SparseAdam(tb["V_net"].shape[0],
                                               tb["V_net"].shape[1], lr=lr_net)
    dense_opt = _DenseAdam(lr=lr_dense)
    sparse_keys = {f".blocks.{bi}.{name}" for (bi, name) in sparse}
    # snapshot V tables at init for the consolidation/moved% check (CLAUDE.md
    # false-positive guard: real training -> moved% >> 1% AND cos(V,init) < 1).
    v_init = {k: np.array(trainable["blocks"][bi][name])
              for k in sparse for (bi, name) in [k]}

    z_coef = float(os.environ.get("MMLLM_Z_LOSS_COEF", "1e-5"))
    distill_end = float(os.environ.get("MMLLM_DISTILL_COEF_END", "1.0"))

    def loss_fn(tr):
        xb, yb = static["_xb"], static["_yb"]
        logits, distill_total, z_total, n_distill = _model.forward(
            _reassemble(tr, static, meta), xb, collect_aux=True)
        lg = logits.reshape(-1, vocab)
        logp = lg - mx.logsumexp(lg, axis=-1, keepdims=True)
        ce = -mx.take_along_axis(logp, yb.reshape(-1)[:, None], axis=-1).mean()
        loss = ce
        if z_coef:
            loss = loss + z_coef * z_total
        dc = static["_distill_coef"]
        if dc and n_distill:
            loss = loss + dc * (distill_total / max(1, n_distill))
        return loss

    def schedule(step):
        """Wake/sleep: Local phase (0-50%) fills V_local (bank hot, net~0, no
        distill); Net phase (50-100%) cosines bank down, ramps net up + distill
        in — Local's content flows to Net via the distill MSE (CLAUDE.md)."""
        frac = step / max(1, n_steps)
        if frac < 0.5:
            return lr_bank, lr_net * 0.01, 0.0
        p = (frac - 0.5) / 0.5
        lb = lr_bank * 0.5 * (1.0 + math.cos(math.pi * p))   # cosine 1->0
        return lb, lr_net * p, distill_end * p

    losses = []
    for step in range(1, n_steps + 1):
        lb, ln, dc = schedule(step)
        static["_distill_coef"] = dc
        for (bi, name), opt in sparse.items():
            opt.lr = lb if name == "V_local" else ln
        xb, yb = batch()
        static["_xb"], static["_yb"] = xb, yb
        loss, grads = mx.value_and_grad(loss_fn)(trainable)
        mx.eval(loss)
        # sparse banks first (read grads before dense update rewrites the tree)
        for (bi, name), opt in sparse.items():
            gV = np.array(grads["blocks"][bi][name])
            rows = np.nonzero(np.abs(gV).sum(1) > 0)[0]
            if len(rows):
                trainable["blocks"][bi][name] = opt.step(
                    trainable["blocks"][bi][name], mx.array(rows), mx.array(gV[rows]))
        trainable = dense_opt.step(trainable, grads, sparse_keys)
        mx.eval(tree_map(lambda a: a, trainable))
        losses.append(float(loss))
        if step % max(1, eval_every) == 0 or step == n_steps:
            print(f"  [mlx] step {step}/{n_steps}  loss={losses[-1]:.4f}  "
                  f"lr_b={lb:.2e} lr_n={ln:.2e} distill_c={dc:.2f}")

    # write trained weights back into the torch model + save (harvest-compatible)
    _write_back(trainable, m, K)
    os.makedirs(ckpt_dir, exist_ok=True)
    dense_path = os.path.join(ckpt_dir, "dense.pt")
    params_fn = bvar("parameters")
    torch.save([p.detach().clone() for p in params_fn(m)], dense_path)
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
    print(f"  [mlx] wrote {dense_path} ({len(losses)} steps, "
          f"loss {losses[0]:.4f}->{losses[-1]:.4f})")

    # consolidation check: how far did each V table move from init?
    result = {"steps": len(losses), "loss_start": losses[0], "loss_end": losses[-1]}
    for (bi, name), opt in sparse.items():
        cur = np.array(trainable["blocks"][bi][name]); init = v_init[(bi, name)]
        moved = float(np.linalg.norm(cur - init) / (np.linalg.norm(init) + 1e-9))
        cos = float((cur.ravel() @ init.ravel()) /
                    (np.linalg.norm(cur) * np.linalg.norm(init) + 1e-9))
        result[f"{name}_b{bi}_moved%"] = round(moved * 100, 3)
        print(f"  [mlx] {name} block{bi}: moved%={moved*100:.2f}  cos(V,init)={cos:.4f}")

    # eval ctrl_bpc on val (torch forward of the MLX-trained, written-back model
    # — also cross-validates the write-back). Best-effort.
    try:
        eval_bpc = bvar("eval-bpc")
        vdata = load_corpus(val_path)
        ev = int(os.environ.get("MMLLM_EVAL_MAX_TOKENS", "20000"))
        r = eval_bpc(m, vdata, T, B, ev)
        bpc = float(r.get(kw.keyword("bpc")))
        result["ctrl_bpc"] = bpc
        print(f"  [mlx] eval ctrl_bpc={bpc:.4f}")
        # ablation Δ_net: zero V_net -> re-eval -> restore. The headline
        # consolidation metric a bird reports (Δ_net = ablated - ctrl).
        try:
            abl = bvar("ablation-step-net!")
            ablated = abl(m, vdata, T, B, ev)
            if ablated is not None:
                dnet = float(ablated) - bpc
                result["delta_net"] = dnet
                print(f"  [mlx] Δ_net={dnet:+.5f}  (ablated_bpc={float(ablated):.4f})")
        except Exception as e:
            print(f"  [mlx] ablation skipped: {e}")
    except Exception as e:
        print(f"  [mlx] eval skipped: {e}")
    return result
