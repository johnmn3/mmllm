"""Disk-streamed NetBank V (RECONSTRUCTED 2026-06-27).

The trend lineage kept each skill-module's V_net (sqrt_n²·n_blocks rows × c_net)
on disk and pulled only the touched rows into a small in-memory cache, so a 10 GB
bank costs ~(rows-touched-per-round × c_net) of RAM instead of 10 GB resident.
This file (lost with the /tmp working copy) is rebuilt to the exact interface its
surviving consumers require:

  • mmllm.mlx.trainer._extract  →  StreamV(mmap_path, n, c_net, lr=...)   (one per module)
  • mmllm.mlx.banks            →  stream_combine(handle, top_global, top_scores) -> latent
  • mmllm.mlx.trainer (round end) →  handle.flush() -> #dirty rows persisted

Design (ds4 cold-expert pattern): V lives in a float32 file on disk; a forward
preads only the unique touched rows into a bounded row-cache; the custom-op VJP
returns d(top_scores) so the PKM keys still learn, and scatters the V-row
gradient straight into the cache (SGD at `lr`, marked dirty). flush() writes the
dirty rows back to disk so the bank accumulates across rounds. Resident footprint
= rows touched this round (≪ n), never the whole bank.
"""
import os
import numpy as np
import mlx.core as mx


class StreamV:
    def __init__(self, mmap_path, n, c_net, lr=0.003, cache_cap=200000):
        self.path = mmap_path
        self.n = int(n)
        self.c_net = int(c_net)
        self.lr = float(lr)
        self.cache_cap = int(cache_cap)
        # float32 file of shape (n, c_net); create (zeros) if missing.
        if mmap_path and not os.path.exists(mmap_path):
            os.makedirs(os.path.dirname(mmap_path) or ".", exist_ok=True)
            np.memmap(mmap_path, dtype=np.float32, mode="w+",
                      shape=(self.n, self.c_net)).flush()
        self._mm = (np.memmap(mmap_path, dtype=np.float32, mode="r+",
                              shape=(self.n, self.c_net))
                    if mmap_path else
                    np.zeros((self.n, self.c_net), np.float32))
        self._cache = {}        # row_idx -> np.float32[c_net] (live value)
        self._dirty = set()     # rows whose cache value differs from disk

    # ── row I/O ────────────────────────────────────────────────────────────
    def _load(self, uniq):
        """Return [len(uniq), c_net] float32 for the given unique rows, paging
        misses in from disk via an explicit read (bounded by touched rows)."""
        out = np.empty((len(uniq), self.c_net), np.float32)
        miss = []
        for j, r in enumerate(uniq):
            v = self._cache.get(int(r))
            if v is None:
                miss.append((j, int(r)))
            else:
                out[j] = v
        for j, r in miss:
            v = np.array(self._mm[r], dtype=np.float32)   # pread one row
            self._cache[r] = v
            out[j] = v
        return out

    def _evict_if_needed(self):
        # keep the cache bounded: drop clean rows (LRU-ish: arbitrary clean rows)
        if len(self._cache) <= self.cache_cap:
            return
        for r in list(self._cache.keys()):
            if len(self._cache) <= self.cache_cap:
                break
            if r not in self._dirty:
                del self._cache[r]

    # ── gradient scatter (SGD on touched rows) ──────────────────────────────
    def _scatter(self, uniq, inv, grad_flat):
        """grad_flat[i] is dL/dV for gathered position i (inv[i] -> uniq row).
        Accumulate per unique row and apply an SGD step into the cache."""
        gu = np.zeros((len(uniq), self.c_net), np.float32)
        np.add.at(gu, inv, grad_flat)
        for j, r in enumerate(uniq):
            r = int(r)
            cur = self._cache.get(r)
            if cur is None:                       # ensure present (paged in forward, but be safe)
                cur = np.array(self._mm[r], dtype=np.float32)
            self._cache[r] = cur - self.lr * gu[j]
            self._dirty.add(r)
        self._evict_if_needed()

    def flush(self):
        """Persist dirty cache rows to disk. Returns #rows written."""
        if not self._dirty:
            return 0
        for r in self._dirty:
            self._mm[r] = self._cache[r]
        if hasattr(self._mm, "flush"):
            self._mm.flush()
        k = len(self._dirty)
        self._dirty.clear()
        return k


def stream_combine(sv, top_global, top_scores):
    """softmax(top_scores)-weighted combine of the V rows named by top_global,
    with V streamed from disk. Differentiable w.r.t. top_scores (PKM keys learn);
    the V-row gradient is scattered into sv's cache as a side effect (SGD@lr).

    top_global: [B,T,k] int row indices.  top_scores: [B,T,k] float logits.
    returns:    [B,T,c_net] float32.
    """
    idx = np.asarray(top_global).reshape(-1).astype(np.int64)
    uniq, inv = np.unique(idx, return_inverse=True)
    rows = sv._load(uniq)                                   # [U, c_net], disk-paged
    shp = tuple(top_global.shape)
    V_rows = mx.array(rows[inv].reshape(*shp, sv.c_net))    # [B,T,k,c_net] constant

    @mx.custom_function
    def _combine(scores):
        w = mx.softmax(scores, axis=-1)
        return mx.einsum("btkc,btk->btc", V_rows, w)

    @_combine.vjp
    def _combine_vjp(primals, cotan, _out):
        scores = primals[0] if isinstance(primals, (tuple, list)) else primals
        if isinstance(cotan, (tuple, list)):
            cotan = cotan[0]
        w = mx.softmax(scores, axis=-1)                     # [B,T,k]
        # d/d w_k = <cotan, V_k> (sum over c); then softmax jacobian → d/d scores
        gw = mx.sum(cotan[..., None, :] * V_rows, axis=-1)  # [B,T,k]
        gs = w * (gw - mx.sum(w * gw, axis=-1, keepdims=True))
        # V-row gradient: dL/dV_k = w_k * cotan  → scatter into the disk cache (SGD@lr)
        gV = w[..., None] * cotan[..., None, :]             # [B,T,k,c]
        sv._scatter(uniq, inv, np.asarray(gV).reshape(-1, sv.c_net).astype(np.float32))
        return (gs,)

    return _combine(top_scores)
