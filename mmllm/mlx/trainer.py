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


# ───────────────────────── VQ dead-code revive (shared) ─────────────────────────
# Standard VQ dead-code split, factored out so the flat block_codebook revive and
# the Phase-A per-level trie revive (trie_C/trie_A) share ONE implementation.
def _vq_dead_live(_h, _dead_thresh):
    """Split a usage histogram into (dead, live-busiest-first) code-index arrays."""
    _dead = np.nonzero(_h <= _dead_thresh)[0]
    _live = np.argsort(-_h)
    _live = _live[_h[_live] > _dead_thresh]               # donors = codes with usage
    return _dead, _live


def _vq_apply_split(_Ck, _dead, _live, _eps):
    """Reset _Ck[dead] to a perturbed copy of a busy donor (cycled busiest-first),
    perturbation scaled to the codebook's own std. Mutates and returns _Ck."""
    _std = float(_Ck.std()) or 1.0
    for _j, _d in enumerate(_dead):
        _donor = int(_live[_j % len(_live)])              # cycle over busy codes → split
        _Ck[_d] = _Ck[_donor] + (np.random.standard_normal(_Ck.shape[1])
                                 * (_eps * _std)).astype(_Ck.dtype)
    return _Ck


def _zero_adam_moments(_opt, _pth, _rows):
    """Zero the dense-Adam m/v moments for the given rows of a param (post-revive)
    so stale momentum doesn't drag the freshly-split centroids back."""
    for _state in (_opt.m, _opt.v):
        if _pth in _state:
            _mm = np.array(_state[_pth]); _mm[_rows] = 0.0; _state[_pth] = mx.array(_mm)


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
    # Phase C: MTP byte heads (one Linear(d, n*vocab)). Present only when
    # MMLLM_MTP_COEF>0. Lives at END of the param order (positional ckpt compat).
    _mtp = m.get(K("mtp-head"))
    if _mtp is not None:
        trainable["mtp_head_w"] = _mxa(_mtp.weight)              # (n*vocab, d_model)
        static["mtp_heads"] = int(_mtp.weight.shape[0]) // int(m.get(K("tok-emb")).weight.shape[0])
    # Phase C: n-gram hash tables. Present only when MMLLM_NGRAM_HASH set.
    _ng = m.get(K("ngram-emb"))
    if _ng is not None:
        trainable["ngram_tables"] = [_mxa(t.weight) for t in _ng.tables]
        static["ngram_specs"] = [(int(g), int(h)) for (g, h) in _ng.specs]
    # Phase B: H-Net spine (Mamba enc/dec + cosine chunker). Present only when
    # MMLLM_HNET set. Arrays -> trainable (dense Adam), scalar config -> static.
    _hn = m.get(K("hnet"))
    if _hn is not None:
        def _emit_mamba(blk):
            return {"in_proj_w": _mxa(blk.in_proj_w), "conv_w": _mxa(blk.conv_w),
                    "conv_b": _mxa(blk.conv_b), "x_proj_w": _mxa(blk.x_proj_w),
                    "dt_proj_w": _mxa(blk.dt_proj_w), "dt_proj_b": _mxa(blk.dt_proj_b),
                    "A_log": _mxa(blk.A_log), "D": _mxa(blk.D),
                    "out_proj_w": _mxa(blk.out_proj_w), "norm_w": _mxa(blk.norm_w)}
        trainable["hnet"] = {
            "enc": [_emit_mamba(b) for b in _hn.enc],
            "dec": [_emit_mamba(b) for b in _hn.dec],
            "W_q": _mxa(_hn.W_q.weight), "W_k": _mxa(_hn.W_k.weight)}
        static["hnet"] = {
            "enc_eps": [float(b.norm_eps) for b in _hn.enc],
            "dec_eps": [float(b.norm_eps) for b in _hn.dec],
            "target_n": float(_hn.target_n), "conf_gate": bool(_hn.conf_gate),
            "smooth": bool(_hn.smooth)}
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
            _vstream = os.environ.get("MMLLM_NET_VSTREAM", "").lower() in ("1", "true", "yes")
            def _emit_net(bank):
                d = {"net_q_norm_w": _mxa(bank.q_norm.weight),
                     "net_K_a": _mxa(bank.K_a), "net_K_b": _mxa(bank.K_b),
                     "net_expander_w": _mxa(bank.expander.weight)}
                if not _vstream:                          # disk-stream: V stays on disk (StreamV), not resident
                    d["V_net"] = _mxa(bank.V.weight)
                if getattr(bank, "trie_depth", 0) > 0:                    # PHASE A: depth-D trie codebooks/ancestors (trainable, dense Adam)
                    d["net_trie_C"] = _mxa(bank.trie_C); d["net_trie_A"] = _mxa(bank.trie_A)
                if getattr(bank, "block_codebook", None) is not None:
                    d["net_block_codebook"] = _mxa(bank.block_codebook)   # learned VQ centroids (trainable)
                for _nm in ("coarse_codebook", "coarse_value", "coarse2_codebook", "coarse2_value", "fine_codebook"):   # Stage 2 path-sum
                    if getattr(bank, _nm, None) is not None:
                        d["net_" + _nm] = _mxa(getattr(bank, _nm))
                if (not _vstream) and _widen > d["V_net"].shape[1]:
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
                             "sqrt_n": ref.sqrt_n, "sub_top_k": ref.sub_top_k, "top_k": ref.top_k,
                             "n_blocks": getattr(ref, "n_blocks", 1),
                             "net_trie_depth": getattr(ref, "trie_depth", 0),
                             "net_trie_branch": getattr(ref, "trie_branch", 32),
                             "net_trie_stop_tau": getattr(ref, "trie_stop_tau", 0.0)}
                if _vstream:                              # disk-stream: V on disk via StreamV handles (per module)
                    from mmllm.mlx.stream_v import StreamV
                    _slr = float(os.environ.get("MMLLM_NET_STREAM_LR", "0.003"))
                    # COLD-SHARE: cold (cooled) modules open the shared round-bank
                    # inode read-only (MAP_SHARED, page-cache shared across births);
                    # the hot module keeps the writable F_NOCACHE slab. Off → every
                    # module is the writable slab (byte-identical to pre-cold-share).
                    _cold_share = os.environ.get("MMLLM_NET_COLD_SHARE", "").lower() in ("1", "true", "yes")
                    _hotmod = os.environ.get("MMLLM_NET_HOT_MODULE", "")
                    sb["net"]["stream"] = {
                        name: StreamV(nb.banks[name].mmap_path,
                                      nb.banks[name].n, nb.banks[name].c_net, lr=_slr,
                                      readonly=(_cold_share and bool(_hotmod) and name != _hotmod))
                        for name in nb.module_names}
                    if getattr(ref, "trie_stream", False):    # STREAMED-NODE trie: C/A handles per module (cold-share like V)
                        _qd = ref.q_dim; _nn = ref.n_trie_nodes
                        sb["net"]["trie_stream"] = {
                            name: {"C": StreamV(nb.banks[name].trie_C_path, _nn, _qd, lr=_slr,
                                                readonly=(_cold_share and bool(_hotmod) and name != _hotmod)),
                                   "A": StreamV(nb.banks[name].trie_A_path, _nn, _qd, lr=_slr,
                                                readonly=(_cold_share and bool(_hotmod) and name != _hotmod))}
                            for name in nb.module_names}
                if getattr(ref, "n_blocks", 1) > 1 and hasattr(ref, "block_proj"):
                    # fixed LSH [q_dim, n_blocks] — CONSTANT, lives in static (not
                    # trainable, so no spurious grad / optimizer corruption). Same R
                    # across modules (shared seed), so one copy suffices.
                    sb["net"]["block_proj"] = _mxa(ref.block_proj)
                if getattr(nb, "router", None) is not None:   # learned skill router
                    tb["router_keys"] = _mxa(nb.router.module_keys)   # dense param [N, q_dim]
                    sb["net"]["router"] = {"names": list(nb.module_names),
                                           "k_load": nb.router.k_load,
                                           "k_tok": nb.router.k_tok,
                                           "drive": bool(nb.router_drive)}
            else:                                    # legacy single NetBank (keys unchanged)
                d = _emit_net(nb)
                tb["net_q_norm_w"] = d["net_q_norm_w"]
                tb["net_K_a"] = d["net_K_a"]; tb["net_K_b"] = d["net_K_b"]
                tb["net_expander_w"] = d["net_expander_w"]; tb["V_net"] = d["V_net"]
                sb["net"] = {"eps": _eps(nb.q_norm), "sub_dim": nb.sub_dim,
                             "sqrt_n": nb.sqrt_n, "sub_top_k": nb.sub_top_k, "top_k": nb.top_k,
                             "net_trie_depth": getattr(nb, "trie_depth", 0),
                             "net_trie_branch": getattr(nb, "trie_branch", 32),
                             "net_trie_stop_tau": getattr(nb, "trie_stop_tau", 0.0)}

        trainable["blocks"].append(tb)
        static["blocks"].append(sb)
        meta["blocks"].append(bmeta)
    static["trunk_ids"] = trunk_ids_mx
    return trainable, static, meta


def _mlx_eval_bpc(trainable, static, meta, vdata, T, B, cap, net_active, vocab, drop_net=False):
    """MLX bits-per-char over vdata, full-model forward — used in the disk-stream
    path (MMLLM_NET_VSTREAM) instead of eval_bpc's torch forward, which would index
    the 1-row dummy torch V. Routes V through StreamV (bounded LRU, hard eviction
    authority), exactly like training. net_active: None=all modules, or [names].
    drop_net=True → netbank OFF (for the Δ_net consolidation ablation)."""
    import numpy as _np, mlx.core as _mx, mmllm.mlx.model as _MD
    data = _np.asarray(vdata).reshape(-1).astype(_np.int64)
    n_win = max(1, min((len(data) - 1) // T, cap // T))
    static = dict(static); static["_net_active"] = net_active     # control eval composition
    P = _reassemble(trainable, static, meta, drop_net=drop_net)   # full model (or net OFF), V via StreamV
    tot_nats = 0.0; tot_tok = 0
    for s in range(0, n_win, B):
        nb = min(B, n_win - s)
        xb = _np.empty((nb, T), _np.int64); yb = _np.empty((nb, T), _np.int64)
        for j in range(nb):
            o = (s + j) * T
            xb[j] = data[o:o + T]; yb[j] = data[o + 1:o + 1 + T]
        lg = _MD.forward(P, _mx.array(xb))
        lg = (lg[0] if isinstance(lg, tuple) else lg).reshape(-1, vocab)
        logp = lg - _mx.logsumexp(lg, axis=-1, keepdims=True)
        ce = -_mx.take_along_axis(logp, _mx.array(yb).reshape(-1)[:, None], axis=-1)
        _mx.eval(ce)
        tot_nats += float(_mx.sum(ce)); tot_tok += ce.size
    return (tot_nats / max(1, tot_tok)) / 0.6931471805599453   # nats→bits


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
    # VQ dead-code revive capture slots (per (bi,name) list). Present only when the
    # trainer enabled MMLLM_NET_VQ_REVIVE → static carries "_vq_usage". None = OFF →
    # no "vq_usage" key is attached to any bank dict → netbank_forward is unchanged.
    _vq_usage = static.get("_vq_usage")
    # PHASE A trie leaf-fill capture (per (bi,name) list of leaf ids). Present only
    # when the trainer enabled MMLLM_NET_TRIE_DEPTH logging → static["_trie_usage"].
    _trie_usage = static.get("_trie_usage")
    P = {
        "tok_emb": Ft(trainable["tok_emb"]),
        "norm_final_w": Ft(trainable["norm_final_w"]),
        "norm_final_eps": static["norm_final_eps"],
        "rope_cos": static["rope_cos"], "rope_sin": static["rope_sin"],
        "blocks": [],
    }
    # Phase C: MTP head + n-gram tables are dense trunk params (frozen with the
    # trunk in a KD student via Ft). Absent keys -> absent in P -> inert forward.
    if "mtp_head_w" in trainable:
        P["mtp_head_w"] = Ft(trainable["mtp_head_w"])
    if "ngram_tables" in trainable:
        P["ngram"] = {"tables": [Ft(t) for t in trainable["ngram_tables"]],
                      "specs": static["ngram_specs"]}
    # Phase B: H-Net spine. enc/dec/W_q/W_k are dense trunk params (Ft-frozen with
    # the trunk in a KD student). norm_eps comes from static; the rest are arrays.
    # Absent key -> no "hnet" in P -> model.forward bypass (byte-identical).
    if "hnet" in trainable:
        _hs = static["hnet"]; _ht = trainable["hnet"]
        def _mamba_p(d, eps):
            q = {k: Ft(v) for k, v in d.items()}; q["norm_eps"] = eps; return q
        P["hnet"] = {
            "enc": [_mamba_p(d, e) for d, e in zip(_ht["enc"], _hs["enc_eps"])],
            "dec": [_mamba_p(d, e) for d, e in zip(_ht["dec"], _hs["dec_eps"])],
            "W_q": Ft(_ht["W_q"]), "W_k": Ft(_ht["W_k"]),
            "target_n": _hs["target_n"], "conf_gate": _hs["conf_gate"],
            "smooth": _hs["smooth"]}
    for bi, (tb, sb, bm) in enumerate(zip(trainable["blocks"], static["blocks"], meta["blocks"])):
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
            # COMPOSED depth-push: when MMLLM_NET_HOT_MODULE names one module, only THAT
            # module's V flows gradient; the cold modules' V are stop_gradient'd so MLX
            # doesn't retain their backward activations → a composed (all-modules+router)
            # bird costs ≈ a single-module bird → PAR=N composed fits. Unset = all live
            # (byte-identical to before).
            _hot = os.environ.get("MMLLM_NET_HOT_MODULE", "")
            _stream = nn_.get("stream")               # disk-stream StreamV handles (per module) or None
            b["netbanks"] = {name: {"q_norm_w": Fa(d["net_q_norm_w"]), "eps": nn_["eps"],
                                    "K_a": Fa(d["net_K_a"]), "K_b": Fa(d["net_K_b"]),
                                    **({"V_stream": _stream[name]} if _stream else
                                       {"V": (d["V_net"] if (not _hot or name == _hot) else sg(d["V_net"]))}),
                                    "expander_w": Fa(d["net_expander_w"]),
                                    "sub_dim": nn_["sub_dim"], "sqrt_n": nn_["sqrt_n"],
                                    "sub_top_k": nn_["sub_top_k"], "top_k": nn_["top_k"],
                                    "n_blocks": nn_.get("n_blocks", 1),
                                    **({"block_proj": nn_["block_proj"]}
                                       if "block_proj" in nn_ else {}),
                                    **({"block_codebook": Fa(d["net_block_codebook"])}
                                       if "net_block_codebook" in d else {}),
                                    **{k: Fa(d["net_" + k]) for k in
                                       ("coarse_codebook", "coarse_value", "coarse2_codebook", "coarse2_value", "fine_codebook")
                                       if "net_" + k in d},
                                    **(({"net_trie_depth": nn_["net_trie_depth"],
                                         "net_trie_branch": nn_["net_trie_branch"],
                                         "net_trie_stop_tau": nn_.get("net_trie_stop_tau", 0.0),
                                         # STREAMED-NODE trie → disk handles (grad scatters via stream_node_read);
                                         # else the dense C/A params.
                                         **({"net_trie_C_stream": nn_["trie_stream"][name]["C"],
                                             "net_trie_A_stream": nn_["trie_stream"][name]["A"]}
                                            if nn_.get("trie_stream") else
                                            {"net_trie_C": Fa(d["net_trie_C"]),
                                             "net_trie_A": Fa(d["net_trie_A"])})}
                                        if "net_trie_C" in d else {})),
                                    **({"trie_usage": _trie_usage.setdefault((bi, name), [])}
                                       if (_trie_usage is not None and lvl == "off"
                                           and not drop_net and "net_trie_C" in d) else {}),
                                    **({"vq_usage": _vq_usage.setdefault((bi, name), [])}
                                       if (_vq_usage is not None and lvl == "off"
                                           and not drop_net and "net_block_codebook" in d) else {})}
                             for name, d in tb["netbanks"].items()}
            # per-batch skill routing: active module(s) set on `static` by the
            # train loop from the batch's corpus (None = all → composition).
            b["net_active"] = static.get("_net_active")
            if "router_keys" in tb:                 # learned skill router (keys Fa-frozen in KD student)
                _r = nn_["router"]
                # drive is read at REASSEMBLE time (runtime env) so genesis can train
                # the router with drive OFF and eval can toggle it per pass.
                _drive = os.environ.get("MMLLM_NET_ROUTER_DRIVE", "false").lower() in ("1", "true", "yes")
                b["net_router"] = {"keys": Fa(tb["router_keys"]), "names": _r["names"],
                                   "k_load": _r["k_load"], "k_tok": _r["k_tok"],
                                   "drive": _drive,
                                   "gate": os.environ.get("MMLLM_NET_ROUTER_GATE", "softmax").lower(),
                                   # AUX-LOSS-FREE bias on SELECTION logits (None when off → inert).
                                   "sel_bias": (static.get("_router_sel_bias") or {}).get(bi),
                                   # grad-free qbar capture slot (only present when bias enabled).
                                   "cap": (static.get("_router_cap") or {}).get(bi)}
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
    # Phase C: persist trained MTP head + n-gram tables back to torch.
    if "mtp_head_w" in trainable:
        cp(m.get(K("mtp-head")).weight, trainable["mtp_head_w"])
    if "ngram_tables" in trainable:
        for t, arr in zip(m.get(K("ngram-emb")).tables, trainable["ngram_tables"]):
            cp(t.weight, arr)
    # Phase B: persist trained H-Net spine (Mamba enc/dec + chunker) back to torch.
    if "hnet" in trainable:
        _hn = m.get(K("hnet")); _ht = trainable["hnet"]
        def _cp_mamba(blk, d):
            for nm in ("in_proj_w", "conv_w", "conv_b", "x_proj_w", "dt_proj_w",
                       "dt_proj_b", "A_log", "D", "out_proj_w", "norm_w"):
                cp(getattr(blk, nm), d[nm])
        for blk, d in zip(_hn.enc, _ht["enc"]): _cp_mamba(blk, d)
        for blk, d in zip(_hn.dec, _ht["dec"]): _cp_mamba(blk, d)
        cp(_hn.W_q.weight, _ht["W_q"]); cp(_hn.W_k.weight, _ht["W_k"])
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
                    if "V_net" in d:                      # streaming: V already updated on disk by StreamV
                        cp(bank.V.weight, d["V_net"])
                    if "net_trie_C" in d and getattr(bank, "trie_depth", 0) > 0:
                        cp(bank.trie_C, d["net_trie_C"]); cp(bank.trie_A, d["net_trie_A"])   # Phase A trie (ckpt/harvest parity)
                    if "net_block_codebook" in d and getattr(bank, "block_codebook", None) is not None:
                        cp(bank.block_codebook, d["net_block_codebook"])   # learned VQ centroids (Stage 1)
                    for _nm in ("coarse_codebook", "coarse_value", "coarse2_codebook", "coarse2_value", "fine_codebook"):   # Stage 2 path-sum
                        if "net_" + _nm in d and getattr(bank, _nm, None) is not None:
                            cp(getattr(bank, _nm), d["net_" + _nm])
                if getattr(nb, "router", None) is not None and "router_keys" in tb:
                    cp(nb.router.module_keys, tb["router_keys"])   # learned router keys
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
        # Router keys are dense but must keep learning when the trunk is FROZEN
        # (extension regime). router_lr (when set) overrides self.lr for any
        # *.router_keys leaf so MMLLM_LR_DENSE_MULT=0 doesn't freeze routing.
        self.router_lr = None
        self.m, self.v, self.t = {}, {}, 0

    def step(self, params, grads, skip_keys):
        self.t += 1
        bc1 = 1.0 - self.b1 ** self.t
        bc2 = 1.0 - self.b2 ** self.t
        def upd(path, p, g):
            if path in skip_keys or g is None:
                return p
            lr = (self.router_lr if (self.router_lr is not None and path.endswith("router_keys"))
                  else self.lr)
            self.m[path] = self.b1 * self.m.get(path, mx.zeros(p.shape)) + (1 - self.b1) * g
            self.v[path] = self.b2 * self.v.get(path, mx.zeros(p.shape)) + (1 - self.b2) * g * g
            step = lr * (self.m[path] / bc1) / (mx.sqrt(self.v[path] / bc2) + self.eps)
            if self.wd and not path.endswith("router_keys"):
                step = step + lr * self.wd * p
            return p - step
        return _map_with_path(params, grads, upd)


def _named_params(m, K):
    """Stable {name: torch.Parameter} over the basilisp model map (which has NO
    .named_parameters — only its leaf components are torch Modules). Names are
    structural (b<i>.<component>.<param>) so they're invariant to module-count
    changes: a cold-added module's params get NEW names → resume leaves them at
    init while existing params load by name. Used by the module-growth-safe
    name-keyed dense_named.pt save/resume."""
    out = {}
    for tk in ("tok-emb", "norm-final", "mtp-head", "ngram-emb", "importance-head", "delim-head"):
        c = m.get(K(tk))
        if c is None:
            continue
        if hasattr(c, "named_parameters"):
            for pn, p in c.named_parameters():
                out[f"{tk}.{pn}"] = p
        elif hasattr(c, "weight"):
            out[f"{tk}.weight"] = c.weight
    _bkeys = ("norm1", "norm2", "q-proj", "k-proj-s", "v-proj-s", "k-proj-l", "v-proj-l",
              "o-proj", "gate-proj", "up-proj", "down-proj", "bank-query", "bank-feedback",
              "memory", "netbank", "long-gate", "carry")
    for i, blk in enumerate(m.get(K("blocks")) or []):
        for sk in _bkeys:
            comp = blk.get(K(sk))
            if comp is not None and hasattr(comp, "named_parameters"):
                for pn, p in comp.named_parameters():
                    if pn.endswith("V.weight"):
                        continue          # the bank VALUE tables (V_local / V_net) are
                                          # huge + persist via their mmap .bin files —
                                          # NEVER put them in dense_named.pt (else each
                                          # ckpt balloons by the full bank size).
                    out[f"b{i}.{sk}.{pn}"] = p
    return out


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


# THREADED BIRTHS (Phase G): when a wave's births run as THREADS in one process
# (genesis_threaded_wave.py sets MMLLM_THREADED_BUILD_LOCK=1) they share the ~10GB
# runtime but each builds its OWN small torch model (trunk dense params are tiny; V
# is a 1-row disk dummy under VSTREAM) and runs the UNMODIFIED train loop in full
# isolation — no shared mutable state, so no writeback race / recipe drift. The ONLY
# hazard is overlapping build_model spikes (what OOM-hangs the box), so this lock
# serializes the build_model→_extract span: one model build resident at a time;
# steady-state training overlaps freely. Default (env unset) → never acquired →
# byte-identical to the per-process path.
import threading as _threading
_BUILD_LOCK = _threading.Lock()
_build_lock_held = _threading.local()   # per-thread "I own the build lock" flag


def _release_build_lock_if_held():
    """Owner-safe release: a threaded birth whose build RAISED calls this from its
    except (same thread that acquired) so the lock can't deadlock its siblings."""
    if getattr(_build_lock_held, "v", False):
        try:
            _BUILD_LOCK.release()
        except RuntimeError:
            pass
        _build_lock_held.v = False


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
    # Batch-LR scaling: a B× larger batch averages the gradient over B× samples, so
    # the step must grow to convert the bigger batch into faster convergence — else
    # B>1 just burns tokens at the B=1 step size. √B (default) is the safe rule;
    # linear is aggressive. B=1 → ×1 (no-op). MMLLM_LR_BATCH_SCALE=sqrt|linear|none.
    _lr_bscale_mode = os.environ.get("MMLLM_LR_BATCH_SCALE", "sqrt")
    _lr_bscale = (B ** 0.5) if _lr_bscale_mode == "sqrt" else (float(B) if _lr_bscale_mode == "linear" else 1.0)
    if _lr_bscale != 1.0:
        print(f"  [mlx] LR batch-scale ({_lr_bscale_mode}): B={B} → lr ×{_lr_bscale:.2f}", flush=True)

    print(f"  [mlx] train_round: B={B} T={T} steps={n_steps} "
          f"lr_base={lr_base} (per-step schedule: pick-lr × {{bank,net,dense}}-mult)")

    # Serialize the build spike across threaded births (no-op unless threaded).
    _bl = _BUILD_LOCK if os.environ.get("MMLLM_THREADED_BUILD_LOCK", "").lower() in ("1", "true", "yes") else None
    if _bl is not None:
        _bl.acquire(); _build_lock_held.v = True
        print(f"  [mlx] threaded-build: acquired build lock (module={os.environ.get('MMLLM_NET_HOT_MODULE','?')})", flush=True)
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
        ps = list(params_fn(m))
        nload = 0
        # Module-growth-safe resume: a name-keyed sidecar (dense_named.pt) matches
        # params BY NAME, so a cold-add (a block's netbank gains a module → the
        # positional list shifts + same-shape params misalign across blocks) loads
        # cleanly and the new module's params stay at init. Falls back to the
        # legacy positional zip for pre-sidecar ckpts. (dense.pt stays for harvest.)
        _named_path = os.path.join(resume_dir, "dense_named.pt")
        if os.path.exists(_named_path):
            _named = torch.load(_named_path, map_location="cpu", weights_only=False)
            _new = 0; _build_names = set()
            for n, p in _named_params(m, K).items():
                _build_names.add(n)
                s = _named.get(n)
                if s is not None and tuple(p.shape) == tuple(s.shape):
                    p.data.copy_(s.to(p.dtype)); nload += 1
                elif s is None:
                    _new += 1                       # build param the seed lacks → init (arch GREW)
            _dropped = sum(1 for k in _named if k not in _build_names)   # seed param the build lacks → trained weights LOST (arch SHRANK)
            print(f"  [mlx] resumed {nload} dense params BY NAME from {_named_path} "
                  f"(module-growth safe; {_new} new at init, {_dropped} seed params dropped)")
            # ── ARCH-MISMATCH GUARD ──────────────────────────────────────────────────
            # A clean chain resume loads EVERY built param from the seed AND leaves no
            # seed param behind → _new == _dropped == 0. Nonzero means the build's
            # architecture differs from the chain (local-bank count, H-Net stack on/off,
            # netbank/router shape, …): mismatched params silently fall back to random
            # INIT and/or trained weights get dropped → the model is half-reset and the
            # chain corrupts. THIS IS EXACTLY what wrecked f256x at wave 53 (259 to init,
            # net_z 0.28→31.9, bpc 2.5→4.6). Refuse, unless the growth is intentional
            # (e.g. cold-adding a module) via MMLLM_ALLOW_ARCH_GROWTH=1.
            _arch_max = int(os.environ.get("MMLLM_ARCH_MISMATCH_MAX", "0"))
            if ((_new + _dropped) > _arch_max
                    and os.environ.get("MMLLM_ALLOW_ARCH_GROWTH", "").lower() not in ("1", "true", "yes")):
                raise SystemExit(
                    f"@@@ARCH-MISMATCH refusing to resume {_named_path}: build arch ≠ chain arch "
                    f"({_new} built params would load at random INIT, {_dropped} trained seed params would be "
                    f"DROPPED). Resuming would half-reset the model and corrupt the chain (this is the wave-53 "
                    f"f256x failure). Match the build config to the chain's arch (local-bank count, H-Net flags, "
                    f"etc.), or set MMLLM_ALLOW_ARCH_GROWTH=1 if this growth is deliberate.")
        else:
            saved = list(torch.load(resume, map_location="cpu", weights_only=False))
            for p, s in zip(ps, saved):
                if tuple(p.shape) == tuple(s.shape):
                    p.data.copy_(s.to(p.dtype)); nload += 1
            print(f"  [mlx] resumed {nload}/{len(ps)} dense params from {resume} (step {resume_step})")
        # WAKE. Lighter than the old zero-wipe: the LB carries across rounds via its
        # r+ mmap (write-through); at wake we blend in noise so it partially forgets
        # + stays plastic (no hard reset, no blank-LB poison). MMLLM_LOCAL_NOISE_FRAC
        # (e.g. 0.5 = half/half: V ← (1-p)·V + p·𝒩(0,std)). Falls back to the legacy
        # zero-wipe when NOISE_FRAC=0 (+ RESET_LOCAL) for backward-compat.
        _noise_frac = float(os.environ.get("MMLLM_LOCAL_NOISE_FRAC", "0"))
        if _noise_frac > 0:
            import torch as _t
            _nb = 0
            for blk in m.get(K("blocks")):
                mem = blk.get(K("memory"))
                if mem is not None:
                    V = mem.V.weight.data
                    std = float(V.std())
                    if std == 0.0:
                        std = 1.0                      # round-1 fresh LB → seed with unit noise
                    V.mul_(1.0 - _noise_frac).add_(_t.randn_like(V) * (std * _noise_frac))
                    _nb += 1
            print(f"  [mlx] LB wake: blended {int(_noise_frac*100)}% noise into {_nb} Local Banks "
                  f"(no wipe; LB carries via mmap)")
        elif os.environ.get("MMLLM_MLX_RESET_LOCAL", "true").lower() in ("1", "true"):
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
        # Guard the silent-fallback footgun: module_for_corpus returns None when a
        # corpus maps (via CORPUS_TO_MODULE) to a module NOT in MMLLM_NET_MODULES,
        # which routes to ALL modules (no isolation) with no error. Warn loudly so
        # a name mismatch (e.g. listing 'gsm8k' when it maps to 'amps-math') is
        # caught instead of silently disabling the skill partition.
        for _p, _mod in zip(_mix_paths, corpus_modules):
            if _mod is None:
                from mmllm.skill_modules import CORPUS_TO_MODULE as _C2M
                _ck = _corp_base(_p); _want = _C2M.get(_ck, _ck)
                print(f"  [mlx] WARNING: corpus {_ck!r} maps to module {_want!r} "
                      f"which is NOT in MMLLM_NET_MODULES={_net_modules} → it will "
                      f"train ALL modules (NO isolation). Add {_want!r} to the list.")

    # Always-active CORE set: modules kept in the forward every batch as frozen
    # context, so a NEW specialist learns its residual on top of the core (+trunk)
    # — the train-against-core regime that makes train-active-set ≈ inf-active-set
    # at composition time. Cool these via MMLLM_NET_COOL_MODULES so they stay
    # frozen. Empty by default (each batch routes to its own module only).
    _core_active = [m for m in os.environ.get("MMLLM_NET_CORE_MODULES", "").split(",")
                    if m.strip()] or None
    if _core_active:
        print(f"  [mlx] always-active core modules (frozen context): {_core_active}")
    # Co-train phase: with the router DRIVING, let it pick the active set during
    # training too (active=None → Level-1) so the train path == the inference path
    # (modules adapt to the routed, convex-weighted regime). Phase 1 (drive off)
    # aux-warms the router under corpus-tag isolation first.
    _drive_train = os.environ.get("MMLLM_NET_ROUTER_TRAIN_DRIVE",
                                  os.environ.get("MMLLM_NET_ROUTER_DRIVE", "false")).lower() in ("1", "true", "yes")
    if _drive_train and corpus_modules is not None:
        print("  [mlx] router DRIVE on → router picks the active set during training (co-train)")

    # ── STRATIFIED PACKING (MMLLM_STRATIFIED) ────────────────────────────────
    # Most windows short (cheap O(T) graph), a weighted tail long for long-range.
    # Windows are aligned to "\n\n" example boundaries (no mid-message cuts) and
    # pad+masked so the loss never trains on pad. Buckets: "T:w,..." (default skews
    # ~80% ≤256 so the memory savings actually show — a 1024 window is 8× a 256 one).
    _strat = os.environ.get("MMLLM_STRATIFIED", "").lower() in ("1", "true", "yes")
    _strat_T = []; _strat_W = None; _bounds = None; _PAD = 0
    if _strat:
        _pairs = [e.split(":") for e in
                  os.environ.get("MMLLM_STRAT_BUCKETS", "256:0.80,512:0.15,1024:0.04,2048:0.01").split(",")]
        _strat_T = [int(t) for t, _ in _pairs]
        _strat_W = np.array([float(w) for _, w in _pairs]); _strat_W = _strat_W / _strat_W.sum()
        # per-corpus "\n\n" boundaries → example start offsets. Chunked scan (64MB)
        # so the one-time build stays ~MB-bounded instead of allocating 1GB+ bool
        # masks over the whole corpus (which spiked RSS to ~4G).
        _bounds = []
        _CH = 1 << 26
        for c in corpora:
            _offs = []
            for _st0 in range(0, c.size - 1, _CH):
                _seg = c[_st0:_st0 + _CH + 1]                      # +1 overlap for edge "\n\n"
                _nn = np.where((_seg[:-1] == 10) & (_seg[1:] == 10))[0]
                if len(_nn): _offs.append(_nn + _st0 + 2)
            _st = np.concatenate(_offs) if _offs else np.array([], np.int64)
            _st = _st[_st < c.size - 8]
            _bounds.append(np.concatenate([[0], _st]).astype(np.int64))
        print(f"  [mlx] STRATIFIED packing: buckets={list(zip(_strat_T, _strat_W.round(3)))} "
              f"(boundary-aligned, pad+masked); avg T≈{int((np.array(_strat_T)*_strat_W).sum())}", flush=True)

    def _strat_window(c, bounds, T_s):
        """Pack whole \\n\\n-examples starting at a random boundary, ending at the
        last boundary that fits T_s; pad to T_s; return (x[T_s], y[T_s], mask[T_s])
        with mask=0 on pad. No mid-message cut."""
        bi = int(_rng.integers(0, len(bounds)))
        s = int(bounds[bi])
        if s > c.size - T_s - 1:
            s = max(0, c.size - T_s - 1)
        end_cap = s + T_s
        # last boundary strictly within (s, end_cap]; else fall back to full T_s (truncate)
        nb = bounds[(bounds > s) & (bounds <= end_cap)]
        real = int(nb[-1] - s) if len(nb) else min(T_s, c.size - s - 1)
        real = max(1, min(real, T_s, c.size - s - 1))
        x = np.full(T_s, _PAD, np.int64); y = np.full(T_s, _PAD, np.int64); m = np.zeros(T_s, np.float32)
        x[:real] = c[s:s + real]; y[:real] = c[s + 1:s + 1 + real]; m[:real] = 1.0
        return x, y, m

    def batch():
        if corpus_modules is not None:
            # MODULAR: one corpus for the whole batch → route all windows to its module.
            ci = int(_rng.choice(len(corpora), p=ws))
            _routed = corpus_modules[ci]
            # router aux-loss target: the routed module's index in the full list
            static["_router_target"] = (_net_modules.index(_routed)
                                        if (_routed in _net_modules) else None)
            if _drive_train:                    # co-train: router picks (Level-1) + weights (Level-2)
                static["_net_active"] = None
            elif _core_active is not None:      # active = core ∪ {routed specialist}
                _r = [_routed] if isinstance(_routed, str) else (list(_routed) if _routed else [])
                static["_net_active"] = list(dict.fromkeys(_core_active + _r))
            else:
                static["_net_active"] = _routed
            c = corpora[ci]
            if _strat:
                Ts = int(_rng.choice(_strat_T, p=_strat_W))           # one T per batch (shared shape)
                xb = np.empty((B, Ts), np.int64); yb = np.empty((B, Ts), np.int64); mb = np.empty((B, Ts), np.float32)
                for j in range(B):
                    xb[j], yb[j], mb[j] = _strat_window(c, _bounds[ci], Ts)
                static["_loss_mask"] = mx.array(mb)
                return mx.array(xb), mx.array(yb)
            xb = np.empty((B, T), dtype=np.int64); yb = np.empty((B, T), dtype=np.int64)
            for j in range(B):
                o = int(_rng.integers(0, c.size - T - 1))
                xb[j] = c[o:o + T]; yb[j] = c[o + 1:o + 1 + T]
            static["_loss_mask"] = None
            return mx.array(xb), mx.array(yb)
        # per-window mix (monolithic net): each of B samples its own corpus + window
        if _strat:
            Ts = int(_rng.choice(_strat_T, p=_strat_W))
            cis = _rng.choice(len(corpora), size=B, p=ws)
            xb = np.empty((B, Ts), np.int64); yb = np.empty((B, Ts), np.int64); mb = np.empty((B, Ts), np.float32)
            for j in range(B):
                ci = int(cis[j]); xb[j], yb[j], mb[j] = _strat_window(corpora[ci], _bounds[ci], Ts)
            static["_loss_mask"] = mx.array(mb)
            return mx.array(xb), mx.array(yb)
        cis = _rng.choice(len(corpora), size=B, p=ws)
        xb = np.empty((B, T), dtype=np.int64); yb = np.empty((B, T), dtype=np.int64)
        for j in range(B):
            c = corpora[int(cis[j])]; o = int(_rng.integers(0, c.size - T - 1))
            xb[j] = c[o:o + T]; yb[j] = c[o + 1:o + 1 + T]
        static["_loss_mask"] = None
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
    # Build span done — let the next threaded birth build. Training below overlaps.
    if _bl is not None:
        _bl.release(); _build_lock_held.v = False; _bl = None
        print(f"  [mlx] threaded-build: released build lock (module={os.environ.get('MMLLM_NET_HOT_MODULE','?')})", flush=True)

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

    # Router keys persist OUTSIDE the (fixed positional) dense.pt — like W_ctx —
    # in router-keys.<bi>.npy. The fresh torch model re-zero-inits them, so resume
    # the trained keys here (over the zeros) for cross-round learning + offline eval.
    _rdir = os.environ.get("MMLLM_SCRATCH") or ckpt_dir
    _rload = 0
    for _bi, tb in enumerate(trainable["blocks"]):
        if "router_keys" in tb:
            _rp = os.path.join(_rdir, f"router-keys.{_bi}.npy")
            if os.path.exists(_rp):
                _saved = mx.array(np.load(_rp)); _cur = tb["router_keys"]
                if tuple(_saved.shape) == tuple(_cur.shape):
                    tb["router_keys"] = _saved
                elif _saved.shape[0] < _cur.shape[0] and _saved.shape[1] == _cur.shape[1]:
                    # cold-add: module count grew → keep trained rows for the existing
                    # modules, new (appended) modules' rows stay at init.
                    tb["router_keys"] = mx.concatenate([_saved, _cur[_saved.shape[0]:]], axis=0)
                _rload += 1
    if _rload:
        print(f"  [mlx] resumed router keys for {_rload} blocks from {_rdir} "
              f"(grow-safe: existing modules' rows kept, new modules at init)")

    # AUX-LOSS-FREE bias buffers (gradient-free, live in `static`, parallel to
    # router_keys). Only allocated when MMLLM_NET_ROUTER_BIAS_U is set → default-off
    # leaves _router_sel_bias/_router_cap absent → _reassemble attaches sel_bias=None
    # (banks.py inert) and the train-loop branch is skipped → byte-identical behaviour.
    if float(os.environ.get("MMLLM_NET_ROUTER_BIAS_U", "0")):
        static["_router_sel_bias"] = {}
        static["_router_cap"] = {}
        _bload = 0
        for _bi, tb in enumerate(trainable["blocks"]):
            if "router_keys" not in tb:
                continue
            _N = int(tb["router_keys"].shape[0])           # module count from the router's keys
            _bias = mx.zeros([_N])                          # init-0 = inert
            _bp = os.path.join(_rdir, f"router-bias.{_bi}.npy")
            if os.path.exists(_bp):                         # grow-safe resume over zero-init
                _sv = mx.array(np.load(_bp))
                if _sv.ndim == 1 and _sv.shape[0] == _N:
                    _bias = _sv
                elif _sv.ndim == 1 and _sv.shape[0] < _N:  # module count grew → new modules at 0
                    _bias = mx.concatenate([_sv, _bias[_sv.shape[0]:]], axis=0)
                _bload += 1
            static["_router_sel_bias"][_bi] = _bias
            static["_router_cap"][_bi] = {}                # qbar capture slot, filled in forward
        print(f"  [mlx] AUX-FREE router-bias ENABLED (u={float(os.environ['MMLLM_NET_ROUTER_BIAS_U'])}): "
              f"{len(static['_router_sel_bias'])} blocks, resumed {_bload} from {_rdir}")

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
                if "V_net" in d:                      # streaming: V on disk, StreamV self-optimizes (skip)
                    sparse[(bi, ("netbanks", name, "V_net"))] = SparseAdam(
                        d["V_net"].shape[0], d["V_net"].shape[1], lr=lr_base)
        elif "V_net" in tb:
            sparse[(bi, ("V_net",))] = SparseAdam(tb["V_net"].shape[0],
                                                  tb["V_net"].shape[1], lr=lr_base)
    dense_opt = _DenseAdam(lr=lr_base)  # overwritten per-step by the schedule
    dense_opt.wd = float(os.environ.get("MMLLM_LR_DENSE_WD", "0.0"))   # trunk skill-shedding decay (skips router_keys)
    sparse_keys = {f".blocks.{bi}." + ".".join(path) for (bi, path) in sparse}
    # snapshot V tables at init for the consolidation/moved% check (CLAUDE.md
    # false-positive guard: real training -> moved% >> 1% AND cos(V,init) < 1).
    v_init = {(bi, path): np.array(_blk_get(trainable["blocks"][bi], path))
              for (bi, path) in sparse}

    z_coef = float(bvar("pick-z-loss-coef")())
    # Phase C: MTP byte-head loss config (read once). _mtp_coef==0 (default) ->
    # term skipped even if a head somehow exists. _mtp_heads matches the built
    # head's n (head weight is n*vocab wide).
    _mtp_coef = float(bvar("pick-mtp-coef")())
    _mtp_heads = int(bvar("pick-mtp-heads")())
    _mtp_decay = float(bvar("pick-mtp-decay")())
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
    # Phase B: H-Net chunk-ratio loss coefficient α (pins avg-chunk → N). The
    # ratio loss itself is computed inside model.forward and stashed on P["hnet"]
    # ("ratio_loss"); we add α·ratio_loss here. Default 0 → no contribution even
    # when the spine is built (the spine still chunks; the ratio is just untuned).
    _hnet_ratio_coef = float(os.environ.get("MMLLM_HNET_RATIO_COEF", "0"))
    # Skill-router aux CE: supervise the per-block module router with the known
    # corpus→module label so its keys become discriminative during genesis (the
    # router then drives Level-1/2 at inference). 0 disables.
    _router_aux_coef = float(os.environ.get("MMLLM_NET_ROUTER_AUX_COEF", "0.1"))
    # AUX-LOSS-FREE router load-balancing bias (DeepSeek-V3 style): a gradient-free
    # per-module bias on the Level-1 SELECTION logits, nudged toward the under-loaded
    # modules each step. ADDITIVE + DEFAULT-OFF: u=0 + init-0 bias == byte-identical
    # to current behaviour (banks.py adds nothing; the train-loop branch is skipped).
    # Lives entirely in `static` — NEVER enters loss_fn/value_and_grad/_DenseAdam.
    _router_bias_u = float(os.environ.get("MMLLM_NET_ROUTER_BIAS_U", "0"))

    _bf16 = os.environ.get("MMLLM_MLX_BF16", "").lower() in ("1", "true", "yes")
    def _cast_bf16(tr):
        if not _bf16: return tr
        return tree_map(lambda a: a.astype(mx.bfloat16) if (isinstance(a, mx.array) and a.dtype == mx.float32) else a, tr)
    if _bf16: print("  [mlx] BF16 mixed-precision forward (params→bf16 for compute, fp32 loss+optimizer)", flush=True)
    def loss_fn(tr):
        xb, yb = static["_xb"], static["_yb"]
        tr = _cast_bf16(tr)                        # mixed precision: bf16 forward, fp32 loss/optimizer
        P = _reassemble(tr, static, meta)
        logits, distill_total, z_total, net_z_total, router_logits, n_distill, mtp_logits = _model.forward(
            P, xb, collect_aux=True)
        lg = logits.reshape(-1, vocab).astype(mx.float32)
        logp = lg - mx.logsumexp(lg, axis=-1, keepdims=True)
        ce_tok = -mx.take_along_axis(logp, yb.reshape(-1)[:, None], axis=-1)   # [B*T,1] per-token CE
        _lm = static.get("_loss_mask")                                        # stratified pad mask or None
        if _lm is not None:
            _mm = _lm.reshape(-1)[:, None]
            ce = (ce_tok * _mm).sum() / mx.maximum(_mm.sum(), mx.array(1.0))
        else:
            ce = ce_tok.mean()
        loss = ce
        if mtp_logits is not None and _mtp_coef:               # Phase C: MTP byte heads
            loss = loss + _model.mtp_loss(mtp_logits, yb, _mtp_heads, _mtp_coef,
                                          _mtp_decay, vocab, _lm)
        if z_coef:
            loss = loss + z_coef * z_total
        if _net_z_coef:
            loss = loss + _net_z_coef * net_z_total
        if "hnet" in P and "ratio_loss" in P["hnet"]:                        # Phase B chunk-ratio
            static["_hnet_diag"] = (P["hnet"]["ratio_loss"], P["hnet"]["cut_rate"])   # telemetry
            if _hnet_ratio_coef:
                loss = loss + _hnet_ratio_coef * P["hnet"]["ratio_loss"]
        if _router_aux_coef and router_logits is not None and static.get("_router_target") is not None:
            rl = router_logits.reshape(-1, router_logits.shape[-1]).astype(mx.float32)   # (B*T, N) summed over blocks
            rlogp = rl - mx.logsumexp(rl, axis=-1, keepdims=True)
            loss = loss + _router_aux_coef * (-rlogp[:, static["_router_target"]].mean())
        if _kd_obj:
            # REAL LB->NB output distillation (Hinton soft-target KD):
            #   TEACHER = Local-only forward (sdpa+local, net OFF), the good/stable
            #     teacher (local just trained this round's data). Detached (stop_grad).
            #   STUDENT = net-only forward (sdpa+net, local OFF) — the future state.
            #   loss = KL(teacher_softT || student_softT) * T^2  (dark knowledge).
            # The net LEARNS to reproduce the local's OUTPUT DISTRIBUTION. Success is
            # this KL FALLING (net matches local) — not Δ_net.
            Ploc = _reassemble(tr, static, meta, drop_net=True)        # local-only teacher
            t_lg = _model.forward(Ploc, xb).reshape(-1, vocab).astype(mx.float32) / _kd_temp
            t_logp = mx.stop_gradient(t_lg - mx.logsumexp(t_lg, axis=-1, keepdims=True))
            t_p = mx.exp(t_logp)
            Pnet = _reassemble(tr, static, meta, student=_kd_freeze)   # net-only student (locals off)
            s_lg = _model.forward(Pnet, xb).reshape(-1, vocab).astype(mx.float32) / _kd_temp
            s_logp = s_lg - mx.logsumexp(s_lg, axis=-1, keepdims=True)
            kd_tok = (t_p * (t_logp - s_logp)).sum(-1)                        # [B*T] per-token KL
            if _lm is not None:
                _mk = _lm.reshape(-1)
                kd = (kd_tok * _mk).sum() / mx.maximum(_mk.sum(), mx.array(1.0)) * (_kd_temp * _kd_temp)
            else:
                kd = kd_tok.mean() * (_kd_temp * _kd_temp)
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
    # Router-key LR multiplier — applied independent of the trunk (dense) mult so
    # the router keeps learning when the trunk is frozen (extension). Default 1.0.
    _router_lr_mult = float(os.environ.get("MMLLM_NET_ROUTER_LR_MULT", "1.0"))

    def schedule(local_step):
        g = resume_step + local_step                       # global step in schedule
        cur = float(_lr_at_step(g, total, _pick_lr(), _warmup, _pick_lr_min())) * _lr_bscale
        return (cur * float(_bank_mult(g, total)),         # lr_bank (V_local)
                cur * float(_net_mult(g, total)),          # lr_net  (V_net)
                cur * float(_dense_mult(g, total)),        # lr_dense
                float(_distill(g, total)),                 # distill coef
                cur)                                       # base lr (for router)

    # ── Local-Bank LR controls (ported from torch optim.py) ──
    # LOCAL_MULT: global V_local LR reduction (default 0.05) — the LB is a routing
    #   PRIMITIVE that should learn SLOW (~20× below bank_lr); the V values it
    #   retrieves change fast, the routing decisions shouldn't.
    # LAYER_MULTS: per-LB-layer multipliers (stacked on LOCAL_MULT), tiled by the
    #   LB's ordinal position → the staggered U-shape so the 8 LBs SPECIALIZE
    #   instead of being redundant. (MLX previously ran all V_local at full bank_lr,
    #   uniform — this restores the torch behaviour.)
    _local_mult = float(os.environ.get("MMLLM_LR_LOCAL_MULT", "0.05"))
    _layer_mults = [float(x) for x in os.environ.get("MMLLM_LR_LAYER_MULTS", "").split(",") if x.strip()] or None
    _lb_bis = sorted(bi for (bi, path) in sparse if path[-1] == "V_local")
    _lb_ord = {bi: i for i, bi in enumerate(_lb_bis)}
    # WAKE→SLEEP LB-LR decay (within each round, no reset): the LB rides a high LR
    # at wake (learn the round's new data fast) decaying to a low LR at sleep (settle
    # while distilling into the NB). Whole-round linear decay LR_WAKE→LR_SLEEP.
    # Defaults 1.0/1.0 = flat (off, backward-compatible).
    _lr_wake = float(os.environ.get("MMLLM_LOCAL_LR_WAKE", "1.0"))
    _lr_sleep = float(os.environ.get("MMLLM_LOCAL_LR_SLEEP", "1.0"))
    def _wake_sleep(local_step):
        if n_steps <= 1:
            return _lr_wake
        return _lr_wake + (_lr_sleep - _lr_wake) * ((local_step - 1) / (n_steps - 1))
    def _vlocal_lr(bi, lb, local_step):
        m = _local_mult * _wake_sleep(local_step)
        if _layer_mults:
            m *= _layer_mults[_lb_ord[bi] % len(_layer_mults)]
        return lb * m
    # Post-reset POISON GUARD: V_local is zeroed each round (reset) → contributes 0.
    # Freeze its update for the first LOCAL_WARMUP steps so the blanked LB stays at
    # zero (no poison) while the trunk+NBs stabilize; then it unfreezes and learns
    # (with its per-layer LR). Default 0 = off (backward-compatible).
    _local_warmup = int(os.environ.get("MMLLM_LOCAL_WARMUP_STEPS", "0"))

    import resource as _res
    def _memprof(tag):
        if os.environ.get("MMLLM_MEM_PROFILE"):
            rss = _res.getrusage(_res.RUSAGE_SELF).ru_maxrss / 2**30
            print(f"  [MEM {tag}] mx_active={mx.get_active_memory()/2**30:.2f}G "
                  f"mx_peak={mx.get_peak_memory()/2**30:.2f}G rss_max={rss:.2f}G", flush=True)
            try: mx.reset_peak_memory()
            except Exception: pass
    if os.environ.get("MMLLM_MEM_PROFILE"):
        nb = sum(1 for b in meta["blocks"] if b.get("netbank"))
        print(f"  [MEM dims] blocks={len(meta['blocks'])} d_model={trainable['tok_emb'].shape[1]} "
              f"vocab={trainable['tok_emb'].shape[0]} netbank_blocks={nb} B={B} T={T}", flush=True)
    _memprof("post-build+extract")

    losses = []
    # HIGH-RES held-out mini-eval: a small fixed slice of the HELD-OUT val, eval'd every
    # eval_every steps → REAL held-out bpc at step resolution (not the optimistic per-batch
    # training loss). MMLLM_MINIEVAL_TOKS=0 disables. ~1% overhead.
    _mev_toks = int(os.environ.get("MMLLM_MINIEVAL_TOKS", str(16 * T)))
    try:
        _mev_data = load_corpus(val_path)[:_mev_toks] if _mev_toks > 0 else None
    except Exception:
        _mev_data = None
    # AUX-FREE bias telemetry: per-router-block cumulative selection counts (smoke).
    _rb_counts = ({_bi: np.zeros(int(tb["router_keys"].shape[0]))
                   for _bi, tb in enumerate(trainable["blocks"]) if "router_keys" in tb}
                  if _router_bias_u else {})
    # ── VQ DEAD-CODE REVIVE (MMLLM_NET_VQ_REVIVE, default OFF) ────────────────
    # The learned VQ block-router (banks.py block_codebook) routes each query to
    # one of n_blocks codes; codes that win ~no queries over a window leave their
    # V slices empty (only ~61/160 blocks fill). Periodically reset dead codes to a
    # perturbed copy of a busy centroid (standard VQ dead-code split) so coverage
    # spreads. Entirely gradient-free surgery on the codebook param (like the
    # router sel_bias path); OFF → static["_vq_usage"] absent → forward unchanged.
    _vq_revive = os.environ.get("MMLLM_NET_VQ_REVIVE", "").lower() in ("1", "true", "yes")
    _vq_every = max(1, int(os.environ.get("MMLLM_NET_VQ_REVIVE_EVERY", "200")))
    _vq_dead_thresh = int(os.environ.get("MMLLM_NET_VQ_REVIVE_DEAD", "0"))
    _vq_eps = float(os.environ.get("MMLLM_NET_VQ_REVIVE_EPS", "0.01"))
    _vq_counts = {}                              # (bi,name) -> np histogram over the window
    _trie_counts = {}                            # (bi,name) -> [per-level B^L histograms]
    if _vq_revive:
        static["_vq_usage"] = {}                 # _reassemble fills per (bi,name) capture lists
        print(f"  [mlx] VQ dead-code REVIVE on: every {_vq_every} steps, "
              f"dead<= {_vq_dead_thresh}, eps={_vq_eps} (block_codebook + trie_C/trie_A)", flush=True)
    # PHASE A: per-level leaf-fill % logging for the depth-D trie NetBank. On
    # whenever MMLLM_NET_TRIE_DEPTH>0; captures leaf ids in the forward and reports
    # distinct-node fraction per level every _trie_log_every steps.
    _trie_depth_env = int(os.environ.get("MMLLM_NET_TRIE_DEPTH", "0"))
    _trie_log_every = max(1, int(os.environ.get("MMLLM_NET_TRIE_LOG_EVERY", "50")))
    if _trie_depth_env > 0:
        static["_trie_usage"] = {}               # _reassemble fills per (bi,name) leaf-id lists
        _tb = int(os.environ.get("MMLLM_NET_TRIE_BRANCH", "32"))
        print(f"  [mlx] PHASE-A trie NetBank: branch={_tb} depth={_trie_depth_env} "
              f"leaves={_tb**_trie_depth_env}, leaf-fill logged every {_trie_log_every} steps", flush=True)
    for step in range(1, n_steps + 1):
        lb, ln, ld, dc, cur = schedule(step)
        static["_distill_coef"] = dc
        dense_opt.lr = ld
        dense_opt.router_lr = cur * _router_lr_mult     # router LR ≠ trunk (dense) LR
        for (bi, path), opt in sparse.items():
            opt.lr = _vlocal_lr(bi, lb, step) if path[-1] == "V_local" else ln
        xb, yb = batch()
        static["_xb"], static["_yb"] = xb, yb
        if step == 1 and os.environ.get("MMLLM_MEM_PROFILE"):
            _fl = loss_fn(trainable); mx.eval(_fl); del _fl
            _memprof("forward-ONLY (no grad retention)")
        if step == 1 and os.environ.get("MMLLM_MEM_TRACE"):
            from mmllm.mlx import banks as _bk; _bk._MEMTRACE.clear()
        loss, grads = mx.value_and_grad(loss_fn)(trainable)
        mx.eval(loss)
        if step == 1: _memprof("post-fwd+bwd (graph peak)")
        if step == 1 and os.environ.get("MMLLM_MEM_TRACE"):
            from mmllm.mlx import banks as _bk
            from collections import defaultdict
            _agg = defaultdict(lambda: [0, 0, ""])
            for _nm, _dt, _nb in _bk._MEMTRACE:
                _agg[_nm][0] += _nb; _agg[_nm][1] += 1; _agg[_nm][2] = _dt
            print("  [TRACE] tagged tensors by total bytes across the forward graph:", flush=True)
            for _nm, (_tot, _cnt, _dt) in sorted(_agg.items(), key=lambda kv: -kv[1][0])[:15]:
                print(f"  [TRACE] {_tot/2**20:9.1f} MB  x{_cnt:<4} {_dt:9} {_nm}", flush=True)
            print(f"  [TRACE] grand total tagged = {sum(v[0] for v in _agg.values())/2**30:.2f} G", flush=True)
        if step == 1 and os.environ.get("MMLLM_MEM_PROFILE"):
            _szs = []
            def _walk(o, path=""):
                if hasattr(o, "nbytes") and hasattr(o, "shape"):
                    _szs.append((o.nbytes, path, tuple(o.shape)))
                elif isinstance(o, dict):
                    for k, v in o.items(): _walk(v, f"{path}.{k}")
                elif isinstance(o, (list, tuple)):
                    for i, v in enumerate(o): _walk(v, f"{path}[{i}]")
            _walk(grads, "grads")
            for nb_, pth, shp in sorted(_szs, reverse=True)[:8]:
                print(f"  [GRAD] {nb_/2**20:8.1f} MB  {shp}  {pth}", flush=True)
        # sparse banks first (read grads before dense update rewrites the tree)
        for (bi, path), opt in sparse.items():
            if path[-1] == "V_local" and step <= _local_warmup:
                continue                       # poison guard: keep blanked LB frozen (zero) until warm
            gV = np.array(_blk_get(grads["blocks"][bi], path))
            rows = np.nonzero(np.abs(gV).sum(1) > 0)[0]
            if len(rows):
                _blk_set(trainable["blocks"][bi], path,
                         opt.step(_blk_get(trainable["blocks"][bi], path),
                                  mx.array(rows), mx.array(gV[rows])))
        trainable = dense_opt.step(trainable, grads, sparse_keys)
        mx.eval(tree_map(lambda a: a, trainable))
        losses.append(float(loss))
        if _vq_revive:
            # 1) drain this step's captured block assignments into per-codebook
            #    histograms (gradient-free; the lists were stashed in the forward).
            for (_bi, _nm), _lst in static.get("_vq_usage", {}).items():
                if not _lst:
                    continue
                _C = trainable["blocks"][_bi]["netbanks"][_nm]["net_block_codebook"]
                _nb_codes = int(_C.shape[0])
                _h = _vq_counts.setdefault((_bi, _nm), np.zeros(_nb_codes, dtype=np.int64))
                for _b in _lst:
                    _h += np.bincount(np.array(_b).reshape(-1), minlength=_nb_codes)
                _lst.clear()
            # 1b) drain captured trie leaf ids into PER-LEVEL node-usage histograms.
            #    The leaf id IS the full base-B path, so the chosen node at level
            #    L (heap base[L]=(B^L−1)/(B−1)) has within-level index
            #    floor(leaf / B^(D−L)); no extra forward capture needed.
            for (_bi, _nm), _lst in (static.get("_trie_usage") or {}).items():
                if not _lst:
                    continue
                _net = static["blocks"][_bi]["net"]
                _B = int(_net["net_trie_branch"]); _D = int(_net["net_trie_depth"])
                _hl = _trie_counts.get((_bi, _nm))
                if _hl is None:
                    _hl = [np.zeros(_B ** _L, dtype=np.int64) for _L in range(1, _D + 1)]
                    _trie_counts[(_bi, _nm)] = _hl
                for _b in _lst:                          # read-only: trie-logging block clears it
                    _leaf = np.array(_b).reshape(-1)
                    for _Li in range(_D):                # level L = _Li+1
                        _within = _leaf // (_B ** (_D - 1 - _Li))
                        _hl[_Li] += np.bincount(_within, minlength=_B ** (_Li + 1))
            # 2) every _vq_every steps: split busy centroids onto the dead codes.
            if step % _vq_every == 0:
                _revived = 0
                for (_bi, _nm), _h in _vq_counts.items():
                    _dead, _live = _vq_dead_live(_h, _vq_dead_thresh)
                    if len(_dead) == 0 or len(_live) == 0:
                        _h[:] = 0
                        continue
                    _Ck = np.array(trainable["blocks"][_bi]["netbanks"][_nm]["net_block_codebook"])
                    _vq_apply_split(_Ck, _dead, _live, _vq_eps)
                    trainable["blocks"][_bi]["netbanks"][_nm]["net_block_codebook"] = mx.array(_Ck)
                    _zero_adam_moments(dense_opt,
                                       f".blocks.{_bi}.netbanks.{_nm}.net_block_codebook", _dead)
                    _revived += len(_dead)
                    _h[:] = 0
                if _revived:
                    print(f"  [mlx] VQ revive step {step}: split {_revived} dead codes "
                          f"across {len(_vq_counts)} codebooks", flush=True)
                # 2b) PER-LEVEL trie revive: split each level's dead nodes (usage<=thresh)
                #     onto a busy donor at the SAME level (residual-VQ levels live in
                #     different residual spaces, so donors must match level). trie_A
                #     (shared ancestor) gets the same dead/live split as trie_C.
                _trie_revived = 0
                for (_bi, _nm), _hl in _trie_counts.items():
                    _B = int(static["blocks"][_bi]["net"]["net_trie_branch"])
                    _slot = trainable["blocks"][_bi]["netbanks"][_nm]
                    _Cfull = np.array(_slot["net_trie_C"])
                    _Afull = np.array(_slot["net_trie_A"])
                    _heap_dead = []
                    for _Li, _h in enumerate(_hl):
                        _L = _Li + 1
                        _base = (_B ** _L - 1) // (_B - 1)     # heap base of level L
                        _n = _h.shape[0]                       # = B^L nodes at level L
                        _dead, _live = _vq_dead_live(_h, _vq_dead_thresh)
                        if len(_dead) == 0 or len(_live) == 0:
                            _h[:] = 0
                            continue
                        _Csl = _Cfull[_base:_base + _n]
                        _Asl = _Afull[_base:_base + _n]
                        _vq_apply_split(_Csl, _dead, _live, _vq_eps)
                        _vq_apply_split(_Asl, _dead, _live, _vq_eps)
                        _Cfull[_base:_base + _n] = _Csl
                        _Afull[_base:_base + _n] = _Asl
                        _heap_dead.append(_base + _dead)       # heap-indexed dead rows
                        _trie_revived += len(_dead)
                        _h[:] = 0
                    if _heap_dead:
                        _rows = np.concatenate(_heap_dead)
                        _slot["net_trie_C"] = mx.array(_Cfull)
                        _slot["net_trie_A"] = mx.array(_Afull)
                        for _k in ("net_trie_C", "net_trie_A"):
                            _zero_adam_moments(dense_opt, f".blocks.{_bi}.netbanks.{_nm}.{_k}", _rows)
                if _trie_revived:
                    print(f"  [mlx] TRIE revive step {step}: split {_trie_revived} dead nodes "
                          f"across {len(_trie_counts)} trie codebooks", flush=True)
        if _trie_depth_env > 0 and static.get("_trie_usage"):
            # drain captured leaf ids → per-level distinct-node fill %. The leaf id
            # is the full base-B path, so node-local at level m = leaf // B^(D-m);
            # fill_m = distinct(that) / B^m. Logged for the first captured module.
            for (_bi, _nm), _lst in static["_trie_usage"].items():
                if _lst and step % _trie_log_every == 0:
                    _leaf = np.concatenate([np.array(x).reshape(-1) for x in _lst])
                    _net = static["blocks"][_bi]["net"]
                    _B = int(_net["net_trie_branch"]); _D = int(_net["net_trie_depth"])
                    _parts = []
                    for _m in range(1, _D + 1):
                        _nodes = len(np.unique(_leaf // (_B ** (_D - _m))))
                        _parts.append(f"L{_m}:{100.0 * _nodes / (_B ** _m):.1f}%")
                    print(f"  [TRIE] step {step} blk{_bi}/{_nm} leaf-fill {' '.join(_parts)} "
                          f"(distinct_leaf={len(np.unique(_leaf))}/{_B ** _D}, n={_leaf.size})", flush=True)
                _lst.clear()
        if "_hnet_diag" in static and step % _trie_log_every == 0:   # Phase B chunk-ratio telemetry
            _rl, _cr = static["_hnet_diag"]; _cr = float(_cr)
            print(f"  [HNET] step {step} ratio_loss={float(_rl):.4f} (α={_hnet_ratio_coef}) "
                  f"cut_rate={_cr:.3f} avg_chunk={1.0/max(_cr,1e-6):.2f} (target N={static['hnet']['target_n']:.0f})",
                  flush=True)
        if _router_bias_u:
            # AUX-LOSS-FREE load-balancing bias update (DeepSeek-V3 style). Entirely
            # gradient-free: recompute Level-1 selection from the qbar captured during
            # THIS step's loss forward (banks._router_modular stashed it in _router_cap),
            # then nudge sel_bias += u·sign(mean_load − load) toward under-used modules.
            # Lives in `static` only — never touched loss_fn/value_and_grad/_DenseAdam.
            for _bi, _capd in static.get("_router_cap", {}).items():
                _qbar = _capd.get("qbar")
                if _qbar is None:                          # this block didn't fire this step
                    continue
                _keys = trainable["blocks"][_bi]["router_keys"]
                _sb = static["_router_sel_bias"][_bi]
                _N = int(_keys.shape[0])
                _sc = _qbar @ _keys.T + _sb[None, :]        # (B, N) biased selection logits
                # k_load from the router config (same source _reassemble reads).
                _kl = static["blocks"][_bi].get("net", {}).get("router", {}).get("k_load")
                _k = _N if (not _kl or _kl >= _N) else int(_kl)
                _order = mx.argsort(_sc, axis=-1)           # ascending → (B, N)
                _topk = _order[:, -_k:]                     # (B, k_load) selected per sequence
                _counts = np.bincount(np.array(_topk).reshape(-1), minlength=_N).astype(np.float64)
                _load = mx.array(_counts)                   # (N,) selections this batch
                static["_router_sel_bias"][_bi] = _sb + _router_bias_u * mx.sign(_load.mean() - _load)
                mx.eval(static["_router_sel_bias"][_bi])
                _rb_counts[_bi] += _counts
            if step % 50 == 0 or step == n_steps:
                for _bi, _ct in _rb_counts.items():
                    _mn = _ct.mean(); _cv2 = (_ct.var() / (_mn * _mn)) if _mn > 0 else 0.0
                    _bn = float(np.linalg.norm(np.array(static["_router_sel_bias"][_bi])))
                    print(f"  [mlx] router-load bi={_bi}: counts={_ct.astype(int).tolist()} "
                          f"CV2={_cv2:.4f} ||sel_bias||={_bn:.4f}", flush=True)
        if step % max(1, eval_every) == 0 or step == n_steps:
            # DISTILL DIAGNOSTIC (smoke): separate forward outside the grad trace —
            # is distill firing? raw magnitude, layer coverage (24 vs 8 = topology
            # regression), per-layer, coef×contribution vs CE (over/under-firing).
            try:
                _lg, _dt, _zt, _nzt, _rl, _nd, _mtp = _model.forward(_reassemble(trainable, static, meta), xb, collect_aux=True)
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
            _mevb = None                                   # REAL held-out bpc at step resolution
            if _mev_data is not None:
                try: _mevb = _mlx_eval_bpc(trainable, static, meta, _mev_data, T, 4, 8 * T, None, vocab)
                except Exception: _mevb = None
            print(f"  [mlx] step {step}/{n_steps}  loss={losses[-1]:.4f}  "
                  + (f"minieval_bpc={_mevb:.4f}  " if _mevb is not None else "")
                  + f"lr_b={lb:.2e} lr_n={ln:.2e} lr_d={ld:.2e} distill_c={dc:.2f}{_dbg}")

    # POST-TRAINING diag: run the key-collapse diagnostic on the TRAINED trainable
    # (with the now-trained W_ctx if ctx-add was injected). Tests whether learned
    # content-discriminative queries de-collapsed retrieval, in-process (no resume).
    if os.environ.get("MMLLM_POST_DIAG"):
        _run_pkm_diag(_reassemble(trainable, static, meta), load_corpus, T)

    # write trained weights back into the torch model + save (harvest-compatible)
    _write_back(trainable, m, K)
    # DISK-STREAM: persist each StreamV's dirty cache rows to disk NOW. Without this
    # the netbank's per-round learning lives only in the in-memory LRU cache (eviction
    # never fires — touched rows ≪ cap) and is discarded when the next round recreates
    # StreamV from the still-zero file → netbank never accumulates (Δ_net≈0). Flushing
    # here makes the V on disk carry across rounds, like the resident path's mmap.
    _flushed = 0
    for _sb in static.get("blocks", []):
        for _sv in (_sb.get("net", {}).get("stream") or {}).values():
            try: _flushed += _sv.flush()
            except Exception as _e: print(f"  [mlx] StreamV flush failed: {_e}")
        for _ts in (_sb.get("net", {}).get("trie_stream") or {}).values():   # STREAMED trie nodes persist too
            for _sv in (_ts.get("C"), _ts.get("A")):
                try: _flushed += _sv.flush() if _sv is not None else 0
                except Exception as _e: print(f"  [mlx] trie StreamV flush failed: {_e}")
    if _flushed:
        print(f"  [mlx] StreamV persisted {_flushed} dirty rows to disk (cross-round netbank memory)")
    # PHASE D: copy-path-on-write versioning publish. Default OFF (env unset) → the
    # block is skipped entirely, in-place StreamV behaviour is byte-identical. When ON,
    # flush() above already SEALED this round's touched rows into a new immutable
    # version; here we (a) emit the sparse version-delta sidecar (rows the bird changed
    # vs the base snapshot — the harvest-as-delta-merge hook, consumed by
    # stream_v.merge_version_deltas) and (b) materialize the head into the V .bin so the
    # existing positional harvest path reads the latest snapshot. The base inode was
    # immutable for the whole round → any cold-share birth reading it was corruption-safe.
    if os.environ.get("MMLLM_NET_VERSIONING", "").lower() in ("1", "true", "yes"):
        _vdir = os.environ.get("MMLLM_SCRATCH") or ckpt_dir
        _npub = _nrows = 0
        for _bi, _sb in enumerate(static.get("blocks", [])):
            for _name, _sv in (_sb.get("net", {}).get("stream") or {}).items():
                if not getattr(_sv, "versioning", False):
                    continue
                try:
                    _delta = _sv.version_delta()              # {rowid -> vec}, sparse
                    if _delta:
                        _rows = np.array(sorted(_delta), np.int64)
                        _vals = np.stack([_delta[int(r)] for r in _rows]).astype(np.float32)
                        np.savez(os.path.join(_vdir, f"netver-delta.{_bi}.{_name}.npz"),
                                 rows=_rows, vals=_vals)
                        _nrows += len(_rows)
                    _sv.materialize()                         # publish head → base .bin (harvest-compat)
                    _npub += 1
                except Exception as _e:
                    print(f"  [mlx] StreamV version publish failed ({_bi}/{_name}): {_e}")
        if _npub:
            print(f"  [mlx] StreamV versioning: published {_npub} module snapshots, "
                  f"{_nrows} delta rows → netver-delta.*.npz (structural-sharing harvest)")
    # Save dense.pt into a step-<total> dir (the layout extend_chain.sh reads:
    # it copies the highest step-N/dense.pt out for delta-encode + push). Bank
    # bins stay at ckpt_dir level (matches save-checkpoint!).
    target_step = total
    step_dir = os.path.join(ckpt_dir, f"step-{target_step}")
    os.makedirs(step_dir, exist_ok=True)
    dense_path = os.path.join(step_dir, "dense.pt")
    torch.save([p.detach().clone() for p in params_fn(m)], dense_path)
    # name-keyed sidecar for module-growth-safe resume (cold-add); dense.pt stays
    # positional for the backend-agnostic harvest.
    torch.save({n: p.detach().clone() for n, p in _named_params(m, K).items()},
               os.path.join(step_dir, "dense_named.pt"))
    with open(os.path.join(step_dir, "step.txt"), "w") as _sf:
        _sf.write(str(target_step))
    # Self-cleaning: prune old step-N ckpt dirs, keep only the latest MMLLM_CKPT_KEEP
    # (default 2 — resume needs the max; 2 leaves one safety margin). Without this a
    # long run accumulates one ~dense.pt-sized dir PER ROUND and fills the disk.
    try:
        import glob as _g, re as _re, shutil as _sh
        _keep = max(1, int(os.environ.get("MMLLM_CKPT_KEEP", "2")))
        _dirs = sorted(((int(_re.search(r"step-(\d+)$", p).group(1)), p)
                        for p in _g.glob(os.path.join(ckpt_dir, "step-*"))
                        if _re.search(r"step-(\d+)$", p)), reverse=True)
        for _, _old in _dirs[_keep:]:
            _sh.rmtree(_old, ignore_errors=True)
        if len(_dirs) > _keep:
            print(f"  [mlx] ckpt prune: kept latest {_keep} step dirs, removed {len(_dirs)-_keep}")
    except Exception as _e:
        print(f"  [mlx] ckpt prune skipped: {_e}")
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
    # persist router keys across rounds (separate from positional dense.pt; the
    # harvester can FedAvg these per block alongside the V_net bins).
    _rhave = [_bi for _bi, tb in enumerate(trainable["blocks"]) if "router_keys" in tb]
    if _rhave:
        _rdir = os.environ.get("MMLLM_SCRATCH") or ckpt_dir
        for _bi in _rhave:
            np.save(os.path.join(_rdir, f"router-keys.{_bi}.npy"),
                    np.array(trainable["blocks"][_bi]["router_keys"]))
        _rn = float(np.linalg.norm(np.array(trainable["blocks"][_rhave[0]]["router_keys"])))
        print(f"  [mlx] router-keys save: {len(_rhave)} blocks; ||keys[0]||={_rn:.4f}")
    # AUX-FREE bias persists in router-bias.<bi>.npy (mirrors router-keys; NOT in
    # dense.pt, NOT FedAvg'd). Only present when bias was enabled this round.
    if _router_bias_u and static.get("_router_sel_bias"):
        _rdir = os.environ.get("MMLLM_SCRATCH") or ckpt_dir
        for _bi, _bias in static["_router_sel_bias"].items():
            np.save(os.path.join(_rdir, f"router-bias.{_bi}.npy"), np.array(_bias))
        _bn0 = float(np.linalg.norm(np.array(next(iter(static["_router_sel_bias"].values())))))
        print(f"  [mlx] router-bias save: {len(static['_router_sel_bias'])} blocks; ||bias[0]||={_bn0:.4f}")
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
        # Composition control: MMLLM_NET_EVAL_ACTIVE restricts the eval to a
        # chosen module set (comma list); "" / "all" → all modules (default
        # composition). Lets us measure a single module's standalone skill, or
        # whether composing an independently-trained module with an extended set
        # interferes (train-active-set ≠ eval-active-set). No-op on non-modular.
        _eval_active = os.environ.get("MMLLM_NET_EVAL_ACTIVE", "").strip()
        _names = (None if (not _eval_active or _eval_active.lower() == "all")
                  else [s.strip() for s in _eval_active.split(",") if s.strip()])
        if os.environ.get("MMLLM_NET_VSTREAM", "").lower() in ("1", "true", "yes"):
            # Disk-stream: torch V is a 1-row dummy → eval via the MLX StreamV path
            # (bounded LRU, hard eviction authority), not eval_bpc's torch forward.
            bpc = _mlx_eval_bpc(trainable, static, meta, vdata, T, eval_b, ev, _names, vocab)
            # Δ_net consolidation metric (THE number we track): re-eval with the
            # netbank OFF; Δ_net = ablated_bpc − ctrl_bpc = how much the netbank
            # carries. POSITIVE & rising = consolidation working.
            _abl = _mlx_eval_bpc(trainable, static, meta, vdata, T, eval_b, ev, _names, vocab, drop_net=True)
            result["delta_net"] = _abl - bpc
            print(f"  [mlx] eval net-active = {_names if _names else 'ALL'} (stream) | "
                  f"Δ_net={_abl - bpc:.4f} (ablated_bpc={_abl:.4f})")
        else:
            if _eval_active:
                _set = 0
                for _blk in (m.get(kw.keyword("blocks")) or []):
                    _nb = _blk.get(kw.keyword("netbank"))
                    if _nb is not None and hasattr(_nb, "set_active"):
                        _nb.set_active(_names); _set += 1
                print(f"  [mlx] eval net-active = {_names if _names else 'ALL'} "
                      f"({_set} modular blocks)")
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
