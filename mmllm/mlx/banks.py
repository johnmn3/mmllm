"""MLX implementations of the two PKM bank forwards — the novel, retrieval-heavy
part of the model (the spike measured these 4.5x faster than torch-MPS).

Both mirror the EVAL forward of their torch counterparts (no training-only
telemetry: z-loss, bincount hit-counters, last_output_norm — all skipped):

  NetBank (netbank.py:295):  q_norm -> q_a@K_a.T / q_b@K_b.T -> topk(sub_top_k)
    -> outer-sum -> topk(top_k) -> decode global idx -> gather V_net (c_net)
    -> softmax-weighted einsum -> expander Linear -> q_dim.
  Local PKM (memory.py):     same pipeline but V rows are q_dim directly (no
    expander), optional per-router (trunk) index offset, no q_norm.

The output is permutation-invariant over the selected top-k set (the softmax
einsum sums over k), so MLX's unordered argpartition matches torch's sorted topk
as long as the selected sets agree — boundary ties are the only divergence, and
the parity gate tolerates them (top-1 > 99.5%).
"""
from __future__ import annotations

import os as _os
import mlx.core as mx

# ── memory tracer: tag tensors with (name, dtype, nbytes); aggregated by name in
# the trainer. Gated by MMLLM_MEM_TRACE (zero overhead otherwise). _mt(name, arr)
# records the graph node's footprint so we can see WHERE the autograd graph's
# memory actually goes, per component, instead of guessing.
_MEMTRACE = []
def _mt(name, a):
    if _os.environ.get("MMLLM_MEM_TRACE") and hasattr(a, "nbytes"):
        _MEMTRACE.append((name, str(a.dtype), int(a.nbytes)))
    return a


def _rms_norm(x, weight, eps):
    # Matches torch RMSNorm: x / sqrt(mean(x^2,-1)+eps) * weight
    return (x * mx.rsqrt(mx.mean(x * x, axis=-1, keepdims=True) + eps)) * weight


def _topk_idx(a, k):
    """Top-k (by value, descending-set) indices along the last axis + their
    values. Unordered within the k — fine, the downstream contraction is
    permutation-invariant. argpartition(-a, k)[:k] gives the k largest."""
    idx = mx.argpartition(-a, k, axis=-1)[..., :k]
    return mx.take_along_axis(a, idx, axis=-1), idx


def _trie_descend(p, q, want_z=False):
    """DYNAMIC-DEPTH, B-way residual-VQ trie descent over a heap-indexed C/A pair.

    A balanced max-depth-D heap, but each token TERMINATES EARLY when its running
    residual is already well-explained (||r|| < stop_tau) — so the EFFECTIVE depth
    is PER-TOKEN VARIABLE: complex / dense content keeps descending (fine resolution),
    simple / sparse content stops shallow (coarse). The query value = path-sum of the
    ancestor A's down to its STOP node; the V leaf slab is the STOP node's heap id (so
    every node is a potential leaf, V is sized to n_nodes, not just B^D bottom leaves).
    stop_tau (MMLLM_NET_TRIE_STOP_TAU) tunes the average depth toward the target; 0 →
    never stops early (= the old fixed full-depth behaviour, but leaf is now the bottom
    node's heap id rather than its within-level index).

    Per level ℓ (while alive): code = argmax(r·C_childrenᵀ); descend to that child;
    acc += A[child]; r -= C[child]; then stop the token if ||r|| < stop_tau.
    Returns (leaf [B,T] heap-id, acc [B,T,q_dim] path-sum, z VQ loss or None)."""
    B = int(p["net_trie_branch"]); D = int(p["net_trie_depth"])
    C = p["net_trie_C"]; A = p["net_trie_A"]          # [n_nodes, q_dim] heap-indexed
    tau = float(p.get("net_trie_stop_tau", 0.0))      # residual-norm early-stop threshold (0 = full depth)
    arangeB = mx.arange(B)
    r = q
    local = mx.zeros(q.shape[:-1], dtype=mx.int32)     # within-level path index (base-B)
    leaf = mx.zeros(q.shape[:-1], dtype=mx.int32)      # STOP-node heap id (root=0 default)
    acc = mx.zeros_like(q)
    alive = mx.ones(q.shape[:-1], dtype=q.dtype)       # 1.0 while still descending, → 0 once stopped
    depth = mx.zeros(q.shape[:-1], dtype=q.dtype)      # effective per-token depth (telemetry)
    z = None
    base_l = 0                                         # base[0] = 0 (root)
    for l in range(D):
        base_next = base_l + B ** l                    # base[ℓ+1]
        first = base_next + local * B                  # [B,T] first child heap id
        cand_idx = first[..., None] + arangeB          # [B,T,B] sibling heap ids
        Cand = mx.take(C, cand_idx, axis=0)            # [B,T,B,q_dim]
        scores = mx.einsum("btkd,btd->btk", Cand, r)   # [B,T,B] nearest-centroid
        code = mx.argmax(scores, axis=-1).astype(mx.int32)
        chosen = first + code                          # [B,T] chosen child heap id
        cc = mx.take(C, chosen, axis=0)                # [B,T,q_dim]
        am = alive[..., None]
        acc = acc + am * mx.take(A, chosen, axis=0)    # path-sum — only contributes while alive
        leaf = mx.where(alive > 0.5, chosen, leaf)     # leaf = deepest node reached before stopping
        depth = depth + alive
        if want_z:                                     # masked per-level commitment+codebook VQ loss
            zl = (mx.mean(alive * mx.sum((mx.stop_gradient(r) - cc) ** 2, axis=-1))
                  + 0.25 * mx.mean(alive * mx.sum((r - mx.stop_gradient(cc)) ** 2, axis=-1)))
            z = zl if z is None else z + zl
        r = r - am * cc                                # residual shrinks only while alive
        local = mx.where(alive > 0.5, local * B + code, local)
        base_l = base_next
        if tau > 0.0:                                  # DYNAMIC STOP: terminate where the residual is explained
            rn = mx.sqrt(mx.sum(r * r, axis=-1) + 1e-12)
            alive = alive * (rn > tau).astype(alive.dtype)
    _tu = p.get("trie_usage")                          # leaf-fill telemetry (no-op when absent)
    if _tu is not None:
        _tu.append(mx.stop_gradient(leaf))
    _td = p.get("trie_depth_acc")                      # effective-depth telemetry (avg-depth tuning)
    if _td is not None:
        _td.append(mx.stop_gradient(depth))
    return leaf, acc, z


def _pkm_select(q_a, q_b, K_a, K_b, sqrt_n, sub_top_k, top_k):
    """Shared score -> sub-topk -> outer-sum -> topk -> global-index decode.
    Returns (top_scores [B,T,top_k], top_global [B,T,top_k] int32)."""
    scores_a = _mt("pkm.scores_a", q_a @ K_a.T)          # [B,T,sqrt_n]
    scores_b = _mt("pkm.scores_b", q_b @ K_b.T)
    top_a_s, top_a_i = _topk_idx(scores_a, sub_top_k)   # [B,T,sub_top_k]
    top_b_s, top_b_i = _topk_idx(scores_b, sub_top_k)
    # outer-sum re-rank over the sub_top_k^2 grid
    comb = (top_a_s[..., :, None] + top_b_s[..., None, :])
    comb = _mt("pkm.comb", comb.reshape(comb.shape[0], comb.shape[1], -1))   # [B,T,sub_top_k^2]
    top_scores, top_local = _topk_idx(comb, top_k)
    top_scores = _mt("pkm.top_scores", top_scores)
    a_within = top_local // sub_top_k
    b_within = top_local - a_within * sub_top_k
    top_a_global = mx.take_along_axis(top_a_i, a_within, axis=-1)
    top_b_global = mx.take_along_axis(top_b_i, b_within, axis=-1)
    top_global = top_a_global * sqrt_n + top_b_global
    return top_scores, top_global


def netbank_forward(p, q, want_z=False):
    """MLX NetBank eval forward.

    p: dict of mx.array params {q_norm_w, K_a, K_b, V, expander_w} + ints/floats
       {sub_dim, sqrt_n, sub_top_k, top_k, eps}. q: [B,T,q_dim] -> [B,T,q_dim].

    When want_z, also returns a LOAD-BALANCING loss on the sub-keys (CV² of per-key
    routing importance, summed over the K_a and K_b axes). The NetBank historically
    had NO anti-collapse term, so its keys collapsed (all corpora retrieve a shared
    ~1% hot row set, Jaccard ~0.7). The router-entropy z-loss (logsumexp²) was tried
    and FAILED: it flattens score peaks but top-k is argmax, so it never reorders the
    winners. CV²(importance) penalizes keys that ACCUMULATE soft routing mass, pushing
    that mass toward uniform → under-used keys win the top-k → product rows spread →
    corpora get distinct V_net storage (a prerequisite for cross-round consolidation).
    """
    q = _rms_norm(q, p["q_norm_w"], p["eps"])
    q_a = q[..., : p["sub_dim"]]
    q_b = q[..., p["sub_dim"]:]
    z = None
    if want_z and "block_codebook" not in p and not p.get("net_trie_depth"):  # CV² (skipped in VQ/trie mode; z carries the VQ loss)
        def _cv2(s):                                    # coeff-of-variation² of key importance
            P = mx.softmax(s, axis=-1)                  # [...,sqrt_n] soft routing prob
            imp = P.mean(axis=tuple(range(P.ndim - 1)))  # [sqrt_n] mean mass per key
            return imp.var() / (imp.mean() ** 2 + 1e-9)
        z = _cv2(q_a @ p["K_a"].T) + _cv2(q_b @ p["K_b"].T)
    top_scores, top_global = _pkm_select(
        q_a, q_b, p["K_a"], p["K_b"], p["sqrt_n"], p["sub_top_k"], p["top_k"]
    )
    # Content-addressed hard partition (MMLLM_NET_N_BLOCKS). The NetBank's keys
    # collapse — all content retrieves a shared ~1% hot row set (banks.py:64),
    # and the soft CV² z-loss can't fix it (flattens importance but never
    # reorders the top-k argmax winners). This forces coverage structurally:
    # route q to one of n_blocks contiguous sqrt_n² V slices via a FIXED random
    # projection (LSH), so distinct content lands in distinct physical rows ->
    # no cross-content overwrite. Mirrors the Local PKM n_trunks offset
    # (banks.py:200) but the block id is per-token CONTENT (argmax q@block_proj),
    # not a per-sequence data-shard trunk id. No-op when block_proj absent.
    coarse_out = None
    if p.get("n_blocks", 1) > 1:
        if p.get("net_trie_depth"):             # PHASE A: depth-D B-way residual-VQ trie
            blk, coarse_out, _zt = _trie_descend(p, q, want_z)
            if want_z:
                z = _zt
        elif "coarse_codebook" in p:            # RESIDUAL-VQ PATH-SUM (depth 2 or 3)
            def _vq(a, b):                       # VQ codebook + commitment loss
                return mx.mean((mx.stop_gradient(a) - b) ** 2) + 0.25 * mx.mean((a - mx.stop_gradient(b)) ** 2)
            C0 = p["coarse_codebook"]; T0 = p["coarse_value"]
            code0 = mx.argmax(q @ C0.T, axis=-1)         # [B,T] coarse cluster
            c0 = mx.take(C0, code0, axis=0)
            r = q - c0                                   # running residual
            coarse_out = mx.take(T0, code0, axis=0)      # level-0 SHARED ancestor contribution
            z = _vq(q, c0) if want_z else None
            path = code0
            if "coarse2_codebook" in p:                  # depth-3: second coarse level
                C2 = p["coarse2_codebook"]; T1 = p["coarse2_value"]; m1 = C2.shape[0]
                code1 = mx.argmax(r @ C2.T, axis=-1)
                c1 = mx.take(C2, code1, axis=0)
                path = code0 * m1 + code1
                coarse_out = coarse_out + mx.take(T1, path, axis=0)      # + level-1 shared contribution
                if want_z: z = z + _vq(r, c1)
                r = r - c1
            Cf = p["fine_codebook"]; fpc = Cf.shape[0]
            fine = mx.argmax(r @ Cf.T, axis=-1)          # leaf fine code (within the path)
            blk = path * fpc + fine                      # [B,T] leaf block (the full path)
            if want_z:
                cf = mx.take(Cf, fine, axis=0)
                z = z + _vq(r, cf)
        elif "block_codebook" in p:             # Stage-1 LEARNED VQ routing
            C = p["block_codebook"]             # [n_blocks, q_dim] trained centroids
            blk = mx.argmax(q @ C.T, axis=-1)   # [B,T] nearest centroid (cosine; q rms-normed)
            # VQ dead-code REVIVE (MMLLM_NET_VQ_REVIVE): when the trainer attaches a
            # capture list (vq_usage), stash this layer's per-token block assignments
            # so the step loop can bincount them and reset codes that win ~no queries.
            # No-op when absent (key only present when the gate is on) → byte-identical.
            _vu = p.get("vq_usage")
            if _vu is not None:
                _vu.append(mx.stop_gradient(blk))
            if want_z:                          # VQ loss on the net_z channel (weight = MMLLM_NET_Z_COEF)
                cb = mx.take(C, blk, axis=0)    # [B,T,q_dim] assigned centroid
                z = (mx.mean((mx.stop_gradient(q) - cb) ** 2)            # codebook term: pull C → q
                     + 0.25 * mx.mean((q - mx.stop_gradient(cb)) ** 2))  # commitment: pull q → C
        elif "block_proj" in p:                 # fixed random LSH (Stage 0)
            blk = mx.argmax(q @ p["block_proj"], axis=-1)
        else:
            blk = None
        if blk is not None:
            top_global = top_global + blk[..., None] * (p["sqrt_n"] * p["sqrt_n"])
    if "V_stream" in p:                                 # mode 3: DISK-STREAM (10GB path)
        # V is NOT resident — it lives on disk in p["V_stream"] (a StreamV handle).
        # The custom op preads the touched rows and does the softmax-weighted combine;
        # its VJP returns d(top_scores) so the PKM keys learn, and scatters the V-row
        # gradient to disk via sparse Adam (pwrite). Single-pass, no V in the autograd
        # tree. ds4 pread+F_NOCACHE pattern (no page-cache thrash). See mlx/stream_v.py.
        from mmllm.mlx.stream_v import stream_combine
        weighted_latent = stream_combine(p["V_stream"], top_global, top_scores)
    else:
        if "V_mmap" in p:                               # mode 2: NetBank V on disk (EVAL-only)
            # mmap'd V; gather only the top-k rows on host. NOTE: np gather breaks
            # autograd → eval/inference only, not training.
            import numpy as np
            Vm = p["V_mmap"]
            idx = np.asarray(top_global).reshape(-1)
            rows = np.asarray(Vm[idx], dtype=np.float32)
            latent = mx.array(rows).reshape(*top_global.shape, Vm.shape[1])
        else:                                           # mode 1: V resident on GPU
            latent = mx.take(p["V"], top_global, axis=0).astype(mx.float32)
        weights = mx.softmax(top_scores, axis=-1)
        weighted_latent = mx.einsum("btkc,btk->btc", latent, weights)
    out = _mt("nb.out", weighted_latent @ p["expander_w"].T)   # expander Linear (bias=False)
    if coarse_out is not None:                          # Stage-2 path-sum: + shared ancestor contribution
        out = out + coarse_out
    return (out, z) if want_z else out


def _router_logits(router, q):
    """Per-token module logits (B,T,N) = q @ keys.T, for the aux loss. q is
    detached so the router adapts its KEYS to the query representation rather
    than reshaping queries (which would perturb the LM objective)."""
    return mx.stop_gradient(q) @ router["keys"].T


def _router_preselect(router, q, all_names):
    """Level 1: mean-pool q over T, score all N modules, return the union of
    per-sequence top-k_load module names (the LRU hot-set). Python-side select
    (inference path; not in the grad graph)."""
    k = router.get("k_load")
    if not k or k >= len(all_names):
        return list(all_names)
    qbar = mx.mean(q, axis=1)                          # (B, qdim)
    scores = qbar @ router["keys"].T
    b = router.get("sel_bias")
    if b is not None: scores = scores + b[None, :]     # [N] bias on SELECTION logits; init-0 = inert
    order = mx.argsort(scores, axis=-1)                # ascending → (B, N)
    top = order[:, -k:]                                # (B, k_load)
    keep = sorted(set(int(i) for i in top.flatten().tolist()))
    return [all_names[i] for i in keep]


def _router_weights(router, q, names, all_names):
    """Level 2: per-token module weights (B,T,len(names)) over `names`.
    softmax (default): convex top-k_tok (sums to 1, fixed-k choice).
    sigmoid: independent per-module gate in [0,1] — variable effective-k so
    OVERLAPPING skills co-fire/self-suppress instead of competing in a softmax."""
    idx = [all_names.index(n) for n in names]
    logits = q @ router["keys"][mx.array(idx)].T       # (B,T,m)
    if router.get("gate", "softmax") == "sigmoid":
        return mx.sigmoid(logits)
    m = len(names)
    k = min(int(router.get("k_tok", m)), m)
    if k < m:                                          # mask all but top-k per token
        thresh = mx.sort(logits, axis=-1)[..., -k][..., None]   # k-th largest
        logits = mx.where(logits >= thresh, logits, -mx.inf)
    return mx.softmax(logits, axis=-1)


def netbank_forward_modular(banks, active, q, want_z=False, router=None):
    """Modular MLX NetBank — Apple-Silicon-local-bird counterpart of the torch
    ModularNetBank (mmllm.netbank).

    `banks`:  {module_name: netbank_params_dict} — each dict is exactly what
              netbank_forward() consumes (q_norm_w/K_a/K_b/V|V_mmap/expander_w/…).
    `active`: list of module names to consult (corpus tag at genesis; learned
              router later); None → all modules (composition).
    `router`: optional {"keys","names","k_load","k_tok","drive"} — the learned
              two-level skill router (banks.py:_router_*). When drive and active
              is None it picks the active set (Level 1); the per-token convex
              weights (Level 2) bound the magnitude and zero off-domain modules.
              Mirrors mmllm.netbank.ModuleRouter.

    Returns out, or (out, z, router_logits) when want_z (router_logits is None
    if no router — used by the genesis aux loss)."""
    if isinstance(active, str):         # single module name → one-element route
        active = [active]               # (else a bare str iterates as characters,
                                        #  matches nothing, and falls back to ALL —
                                        #  silently defeating per-batch isolation)
    all_names = list(banks)
    # AUX-LOSS-FREE bias: gradient-free capture of the per-block mean-pooled query
    # (qbar) so the trainer can recompute selection counts + nudge sel_bias OUTSIDE
    # the autograd tree. Active only when the router carries a `cap` dict (bias on).
    _cap = router.get("cap") if router is not None else None
    if _cap is not None:
        _cap["qbar"] = mx.stop_gradient(mx.mean(q, axis=1))     # (B, qdim), detached
    if router is not None and router.get("drive") and active is None:
        names = _router_preselect(router, q, all_names)        # Level 1
    else:
        names = all_names if active is None else [a for a in active if a in banks]
        if not names:                   # routed to nothing present → consult all
            names = all_names
    rlogits = _router_logits(router, q) if (router is not None and want_z) else None
    # Level 2 only when the router is DRIVING (so drive=False == plain-sum baseline).
    w = (_router_weights(router, q, names, all_names)
         if (router is not None and router.get("drive") and len(names) > 1) else None)
    out = None
    z = None
    for i, n in enumerate(names):
        r = netbank_forward(banks[n], q, want_z=want_z)
        o = r[0] if want_z else r
        if w is not None:               # Level 2: per-token convex weighting
            o = o * w[..., i:i + 1]
        out = o if out is None else out + o
        if want_z and r[1] is not None:
            z = r[1] if z is None else z + r[1]
    return (out, z, rlogits) if want_z else out


def local_forward(p, q, trunk_ids=None, want_z=False):
    """MLX Local PKM eval forward. Like NetBank but V rows are q_dim (no
    expander) and an optional per-router (trunk) row offset selects the
    router's slice of the shared V table. Applies q_norm like memory.py:forward.

    When want_z, also returns the PKM z-loss (mean lse_a^2 + lse_b^2 over the
    full sub-key scores) — the router-entropy regularizer (memory.py:958)."""
    q = _rms_norm(q, p["q_norm_w"], p["eps"])
    q_a = q[..., : p["sub_dim"]]
    q_b = q[..., p["sub_dim"]:]
    z = None
    if want_z:
        sa = _mt("local.z_sa", q_a @ p["K_a"].T)
        sb = _mt("local.z_sb", q_b @ p["K_b"].T)
        z = (mx.logsumexp(sa, axis=-1) ** 2).mean() + (mx.logsumexp(sb, axis=-1) ** 2).mean()
    top_scores, top_global = _pkm_select(
        q_a, q_b, p["K_a"], p["K_b"], p["sqrt_n"], p["sub_top_k"], p["top_k"]
    )
    if trunk_ids is not None and p.get("n_trunks", 1) > 1:
        # each router owns a contiguous sqrt_n^2 block of rows
        offset = (trunk_ids * (p["sqrt_n"] * p["sqrt_n"])).reshape(
            trunk_ids.shape[0], 1, 1
        )
        top_global = top_global + offset
    values = _mt("local.values", mx.take(p["V"], top_global, axis=0).astype(mx.float32))  # [B,T,top_k,q_dim]
    weights = mx.softmax(top_scores, axis=-1)
    out = _mt("local.out", mx.einsum("btkd,btk->btd", values, weights))
    return (out, z) if want_z else out
