"""Product-Key Memory layer (Lample et al. 2019), optionally mmap-backed.

A learned key-value bank with sub-linear top-K retrieval. Two
sub-key matrices factor an N = M*M entry bank into 2*M sub-keys,
so search is O(sqrt(N)) regardless of N. Storage:

  * sub-key matrices  K_a, K_b: 2 * M * (q_dim/2)  — small, RAM
  * value bank        V:        M*M * q_dim         — can scale to GB,
                                                       optionally mmap-backed

Per query:
  1. Split q into halves q_a, q_b
  2. Top sub_top_k indices in K_a (q_a · K_a.T)
  3. Top sub_top_k indices in K_b (q_b · K_b.T)
  4. Re-rank sub_top_k * sub_top_k candidate (i_a, i_b) pairs by
     full key score (= score_a[i_a] + score_b[i_b])
  5. Top-K from re-ranking → fetch values → softmax-weighted sum

V is an `nn.Embedding(sparse=True)`. Backward produces a *sparse*
gradient (only the touched rows), so we can use SparseAdam for
SGD updates that only write the touched rows back to the mmap.
Otherwise a dense gradient would be a full N × q_dim tensor in
RAM and the whole bank would be re-written every step.

For mmap-backing, pass mmap_path: the V.weight tensor is then a
zero-copy view into the file. Forward reads cause page-cache
loads of just the top-K rows; SparseAdam writes touch only those
rows back to disk.

CROSS-DEVICE: when mmap_path is set, V is wrapped in a
CPUPinnedEmbedding whose `_apply` is a no-op — so a parent
`module.to('cuda')` moves K_a/K_b to GPU but leaves V on CPU.
forward() detects the device mismatch and streams only the top-K
rows CPU→GPU per query (~7 MB per layer per training step at
shape (4,128,16,224) — well under PCIe bandwidth). Sparse-grad
backward flows GPU→CPU through `.to()` and lands on V on CPU,
where SparseAdam writes touched rows back through the mmap.
"""

from __future__ import annotations

import builtins
import os
import struct

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

from ._pkm_autograd import HAS_CPP_KERNELS, PKMGather, PKMFusedTopK, pkm_inference_forward


def _mmap_value_tensor(path: str, n: int, dim: int,
                       init_scale: float = 0.02,
                       chunk_rows: int = 4096) -> torch.Tensor:
    """Open or create an (n, dim) float32 memmap-backed torch tensor.

    If the file exists at the right size, opens it. Otherwise creates,
    initialises with N(0, init_scale^2), and flushes. Returns a torch
    tensor whose storage is the mmap; mutations write back to disk.

    Init is chunked: numpy.random.standard_normal returns float64,
    so a one-shot (n, dim) gen would peak at n*dim*8 bytes of RAM
    before the float32 cast. At the 10 GB target (sqrt_n ≈ 1448,
    dim 224) that's 3.7 GB per layer before any disk page is
    written. Chunking by `chunk_rows` bounds the transient at
    chunk_rows * dim * 8 bytes regardless of n.
    """
    expected_bytes = n * dim * 4  # float32
    if os.path.exists(path) and os.path.getsize(path) == expected_bytes:
        arr = np.memmap(path, dtype=np.float32, mode="r+", shape=(n, dim))
    else:
        arr = np.memmap(path, dtype=np.float32, mode="w+", shape=(n, dim))
        for i in range(0, n, chunk_rows):
            end = min(i + chunk_rows, n)
            arr[i:end] = (np.random.standard_normal((end - i, dim))
                          * init_scale).astype(np.float32)
        arr.flush()
    return torch.from_numpy(arr)


def prepare_bank_files(bank_path_prefix: str, n_layers: int,
                       sqrt_n: int, q_dim: int,
                       init_scale: float = 0.02,
                       chunk_rows: int = 4096) -> dict:
    """Pre-create + initialize the bank V mmap files at the right
    size, idempotently. Designed for multi-trainer scenarios where
    N concurrent trainers each open the same files in mode='r+';
    running this once first avoids the race where two trainers
    simultaneously call `_mmap_value_tensor(...mode='w+')` and
    truncate each other's data.

    Idempotent: a file at the correct size is left untouched
    (presumed already-initialized by an earlier prepare_bank or
    train run); otherwise it's created and Gaussian-init'd.
    """
    n = sqrt_n * sqrt_n
    expected_bytes = n * q_dim * 4  # float32
    out = []
    for i in range(n_layers):
        path = f"{bank_path_prefix}.{i}.bin"
        if os.path.exists(path) and os.path.getsize(path) == expected_bytes:
            out.append({"path": path, "bytes": expected_bytes, "cached": True})
            continue
        # Reuse the existing single-file init helper; we discard the
        # returned tensor since we just want the file on disk.
        _mmap_value_tensor(path, n, q_dim, init_scale, chunk_rows)
        out.append({"path": path, "bytes": expected_bytes, "cached": False})
    return {"paths": out, "n_layers": n_layers,
            "total_bytes": expected_bytes * n_layers,
            "sqrt_n": sqrt_n, "q_dim": q_dim}


class CPUPinnedEmbedding(nn.Embedding):
    """nn.Embedding whose .weight stays on CPU regardless of parent
    `module.to(device)` calls. Used for the mmap-backed bank V so
    that K_a/K_b/dense modules can move to GPU while V remains
    page-faulted from disk. forward() works the same as nn.Embedding;
    callers handle cross-device gather via `.to(device)` on outputs.
    """

    def _apply(self, fn, recurse=True):
        # No-op — parent module's recursive .to()/.cuda()/etc. won't
        # walk into us. K_a, K_b in the parent ProductKeyMemory still
        # move normally because they're parameters at the parent level.
        return self


class PagedMmapStorage:
    """Thin virtual paging layer over an mmap-backed bank tensor.

    Why this exists
    ---------------
    The bank V is mmap'd so its size can exceed RAM. On a single Linux
    host with multiple processes, that mmap is shared real-time — writes
    by process A are visible to process B via the shared page cache.
    Hogwild as described in the literature relies on exactly this.

    Modal Volumes (and any FUSE-over-distributed-storage backend) DO NOT
    provide live cross-container sharing. Per Modal's docs:

      "Unlike a normal filesystem, you need to explicitly reload the
       Volume to see changes made since it was first mounted."

    So workers that mmap the same file from different containers each
    see their *own* private copy. Updates require explicit commit +
    reload on each side. This layer adds the bookkeeping needed for that
    pattern, while keeping the user-facing API identical to a plain
    mmap-backed tensor.

    Concepts
    --------
    The bank is logically divided into pages of `page_rows` rows each.
    `track_dirty_rows(row_indices)` is called from the forward (where
    we know which rows are about to receive sparse-grad updates) and
    marks the containing pages dirty. `sync(volume)` then:

      1. commit() — pushes our local writes to the volume backend
         (Modal handles the file-level delta upload).
      2. reload() — pulls other workers' commits down (last-writer-wins
         for same-page conflicts; accepted as Hogwild noise).
      3. Re-open the file via np.memmap to get a fresh view of the
         post-reload content, then swap the torch tensor's underlying
         storage to point at the new mapping via Tensor.set_(). Tensor
         IDENTITY is preserved, so any optimizer (SparseAdam) keying
         state by id(weight) keeps its momentum/variance buffers.

    Page-level tracking is currently informational — Modal commits
    whatever bytes changed in the file, regardless of which "pages" we
    flagged. The future evolution is to split the bank into per-page
    files so commit-time delta is bounded by `len(dirty_pages) *
    bytes_per_page`, and reload pulls only files other workers
    committed.
    """

    def __init__(self, path: str, n: int, dim: int,
                 page_rows: int = 1024, init_scale: float = 0.02):
        self.path = path
        self.n = n
        self.dim = dim
        self.page_rows = page_rows
        self.n_pages = (n + page_rows - 1) // page_rows
        self._dirty_pages: set[int] = set()
        # Tiered residence: cap the number of *pages* held in RAM via
        # an LRU eviction list. Set via MMLLM_BANK_RESIDENT_BYTES (per-
        # bank cap in bytes). When unset (default), no cap — kernel page
        # cache uses its own LRU under memory pressure only. When set
        # smaller than the bank's full byte size, pages outside the LRU
        # set are MADV_DONTNEED'd, forcing them back to disk; next access
        # to them takes a page fault.
        #
        # The page_rows×dim×4 bytes determine actual per-page byte size.
        import os as _os
        resident_bytes = int(_os.environ.get("MMLLM_BANK_RESIDENT_BYTES", "0"))
        if resident_bytes > 0:
            bytes_per_page = page_rows * dim * 4  # fp32 row stride × page_rows
            self._resident_pages_cap = max(1, resident_bytes // bytes_per_page)
        else:
            self._resident_pages_cap = 0  # 0 = no cap
        # LRU order: most-recently-used at the end. Dedup on insert.
        from collections import OrderedDict as _OrderedDict
        self._lru_pages: "_OrderedDict[int, None]" = _OrderedDict()
        # `_tensor` is what we hand out via .tensor. After remap, its
        # storage gets swapped via Tensor.set_(). However, when the
        # caller wraps this tensor in a Parameter (e.g.
        # nn.Embedding.from_pretrained does Parameter(t)), the Parameter
        # is a NEW Tensor object that shares storage with `_tensor` —
        # not the same Tensor instance. set_() only swaps storage on
        # the specific tensor it's called on, so any downstream copies
        # (V.weight especially) would keep pointing at the OLD storage
        # and never see other workers' writes.
        #
        # To handle this, callers register their wrapping tensor via
        # register_owner() so we can swap their storage in turn during
        # remap. Typical callers register both the V.weight Parameter
        # and any other long-lived references.
        self._owners: list[torch.Tensor] = []
        self._tensor: torch.Tensor | None = None
        self._array: "np.memmap | None" = None
        # File-init: ensure the bank file exists at the right size,
        # Gaussian-init if missing, then DROP the open handle so the
        # subsequent _open_mmap() is the only live mapping. This matters
        # for Modal Volumes — commit() refuses to run while ANY file
        # handle on the volume is open, so PagedMmapStorage maintains
        # exactly ONE handle (self._array) and closes it explicitly
        # around every sync.
        self._init_file_if_missing(init_scale)
        self._open_mmap()

    def _init_file_if_missing(self, init_scale: float, chunk_rows: int = 4096) -> None:
        expected_bytes = self.n * self.dim * 4  # float32
        if os.path.exists(self.path) and os.path.getsize(self.path) == expected_bytes:
            return
        # Create + Gaussian-init. Open, write, flush, EXPLICITLY release.
        arr = np.memmap(self.path, dtype=np.float32, mode="w+",
                        shape=(self.n, self.dim))
        for i in range(0, self.n, chunk_rows):
            end = min(i + chunk_rows, self.n)
            arr[i:end] = (np.random.standard_normal((end - i, self.dim))
                          * init_scale).astype(np.float32)
        arr.flush()
        # Drop the OS mmap so this handle isn't open when sync() later
        # calls volume.commit().
        if hasattr(arr, "_mmap") and arr._mmap is not None:
            arr._mmap.close()
        del arr

    def _open_mmap(self) -> None:
        """Open the file for use; populate self._tensor + self._array.

        Called at construction and after every sync's reload. Two opens
        ARE NOT made — only one np.memmap handle is alive at a time
        (so volume.commit can run when needed)."""
        self._array = np.memmap(self.path, dtype=np.float32, mode="r+",
                                shape=(self.n, self.dim))
        self._tensor = torch.from_numpy(self._array)

    def _close_mmap(self) -> None:
        """Release ALL references to the mmap'd file so Modal's
        commit() can run without 'open files preventing the operation'.

        Steps:
          1. set_() every torch tensor (self._tensor + every owner) to
             a tiny throwaway storage so they no longer reference the
             mmap's buffer.
          2. Explicitly close the underlying mmap.mmap object via
             self._array._mmap.close() — np.memmap exposes the OS-level
             mmap as ._mmap, and closing it releases the file handle
             immediately rather than waiting for GC (which is non-
             deterministic and may not run before commit()).
          3. Drop our refs so the numpy array can be GC'd cleanly.
        """
        with torch.no_grad():
            empty = torch.empty(0, dtype=torch.float32)
            if self._tensor is not None:
                self._tensor.set_(empty)
            for owner in self._owners:
                owner.set_(empty)
        self._tensor = None
        if self._array is not None:
            mmap_obj = getattr(self._array, "_mmap", None)
            if mmap_obj is not None:
                mmap_obj.close()
            self._array = None

    @property
    def tensor(self) -> torch.Tensor:
        """The mmap-backed tensor view. Pass to nn.Embedding/from_pretrained."""
        return self._tensor

    def register_owner(self, tensor: torch.Tensor) -> None:
        """Register a long-lived tensor that shares this storage and
        needs to be re-bound on every sync.

        The canonical case: nn.Embedding.from_pretrained(self.tensor)
        creates a Parameter that wraps `self.tensor`'s storage but is
        a separate Tensor instance. Without registration, post-sync
        Tensor.set_() on `self._tensor` swaps OUR view to the fresh
        mmap, but the Embedding's V.weight keeps pointing at the
        stale mapping. Registering V.weight ensures it gets re-bound
        too. Pass V.weight (the Parameter), not V.weight.data — both
        work, but the Parameter is the canonical handle the optimizer
        keys state by.
        """
        self._owners.append(tensor)

    def track_dirty_rows(self, row_indices: torch.Tensor) -> int:
        """Mark pages containing these row indices as dirty AND update the
        LRU residency set.

        Called from forward() at lookup time — every row we touch is
        guaranteed to receive a sparse-grad update on backward, so
        flagging at lookup is both correct and cheap (no extra GPU↔CPU
        sync; the indices are already on hand).

        When MMLLM_BANK_RESIDENT_BYTES is set, this method also evicts
        the oldest pages once the LRU exceeds the byte cap, by issuing
        MADV_DONTNEED on their byte range. Evicted pages are reloaded
        from disk on next access (page fault via the existing mmap).

        Returns the number of newly-flagged pages (for logging).
        """
        before = len(self._dirty_pages)
        flat = row_indices.detach().flatten().to("cpu", dtype=torch.int64)
        # // is integer division; .unique() keeps the dirty set small
        # even when the same page is touched many times per step.
        pages = (flat // self.page_rows).unique().tolist()
        self._dirty_pages.update(pages)
        # Update LRU: move touched pages to "most recent". OrderedDict's
        # move_to_end + popitem(last=False) gives O(1) LRU ops.
        if self._resident_pages_cap > 0:
            for p in pages:
                self._lru_pages.pop(p, None)
                self._lru_pages[p] = None
            # Evict oldest pages until under cap.
            while len(self._lru_pages) > self._resident_pages_cap:
                old_page, _ = self._lru_pages.popitem(last=False)
                self._evict_page(old_page)
        return len(self._dirty_pages) - before

    def _evict_page(self, page_idx: int) -> None:
        """Issue MADV_DONTNEED on the byte range of one page.

        Next access pages it back in from disk via the existing mmap.
        Used by the LRU eviction path to keep resident set bounded.
        """
        if self._array is None:
            return
        mm = getattr(self._array, "_mmap", None)
        if mm is None or not hasattr(mm, "madvise"):
            return
        try:
            mm_dontneed = _mmap_module.MADV_DONTNEED
        except AttributeError:
            return
        bytes_per_page = self.page_rows * self.dim * 4
        off = page_idx * bytes_per_page
        length = bytes_per_page
        # Last page may be partial; clamp length to file end.
        total_size = self.n * self.dim * 4
        if off + length > total_size:
            length = total_size - off
        if length <= 0:
            return
        try:
            mm.madvise(mm_dontneed, off, length)
        except OSError:
            pass  # kernel may reject some advise ops; benign

    def n_dirty_pages(self) -> int:
        return len(self._dirty_pages)

    def sync(self, volume) -> dict:
        """One-shot sync for a single storage: close + commit + reload
        + re-open + remap.

        For models with multiple banks (one per layer), prefer the
        module-level sync_banks(layers, volume) — it closes ALL banks
        first, does ONE shared commit + reload, then re-opens each.

        Why close before commit: Modal's volume.commit() refuses to
        run while any file in the volume has an open handle (the
        np.memmap counts). So we close the mmap, run commit/reload,
        then re-open. The re-open also picks up any post-reload
        content from other workers (cross-worker bank sharing — the
        whole point of this layer).

        The `volume` argument is duck-typed: any object with .commit()
        and .reload() works (modal.Volume satisfies this). Pass None
        to skip the commit/reload but still close + re-open the mmap
        (useful for local single-process testing or after an out-of-
        band reload).
        """
        stats = self._pre_sync_stats()
        self._close_mmap()
        if volume is not None:
            volume.commit()
            volume.reload()
        self._remap_after_reload()
        stats["resynced_to_fresh_mmap"] = True
        return stats

    def _pre_sync_stats(self) -> dict:
        return {
            "dirty_pages_at_sync": len(self._dirty_pages),
            "total_pages": self.n_pages,
            "page_rows": self.page_rows,
            "bytes_per_page": self.page_rows * self.dim * 4,
        }

    def _remap_after_reload(self) -> None:
        """Re-open the mmap to pick up post-reload file content; swap
        every owner's storage to the new mapping.

        Called by sync() and by the batched module-level helper after
        a shared volume.reload(). Pre-condition: _close_mmap() has
        been called (so volume.commit could run). This re-opens the
        file and binds owners to the fresh storage.

        Tensor.set_() rebinds storage in-place; Parameter identity
        survives, so SparseAdam state (keyed by id(weight)) is intact.
        """
        self._open_mmap()  # populates self._array + self._tensor
        with torch.no_grad():
            for owner in self._owners:
                # Same fresh storage for every owner. Tensor identity
                # survives so the optimizer's state dict (keyed by
                # id(parameter)) remains valid across syncs.
                owner.set_(self._tensor)
        self._dirty_pages.clear()


def sync_banks(memory_layers, volume) -> dict:
    """Batched sync across multiple ProductKeyMemory layers: close ALL
    layers, run ONE shared commit + reload, then re-open all.

    Pass any iterable of ProductKeyMemory; layers without an mmap'd
    bank are silently skipped.

    Modal's volume.commit() and .reload() are global to the volume,
    so calling them per-layer (5×) would do 4× of needless round
    trips AND would fail because earlier layers' mmaps would still
    be open when the next layer's commit ran. This helper closes
    every layer's mmap up front so the single commit sees zero open
    handles, then re-opens each layer in turn after the reload.
    """
    layers = [m for m in memory_layers if getattr(m, "_storage", None) is not None]
    if not layers:
        return {"skipped": "no mmap'd banks", "n_layers": 0}
    pre = [m._storage._pre_sync_stats() for m in layers]
    total_dirty = sum(s["dirty_pages_at_sync"] for s in pre)
    # Close every layer's mmap FIRST so Modal's commit sees no open
    # file handles. Per-layer close is cheap (set_() to empty + close
    # the OS mmap), and we batch them so commit is a single call.
    for m in layers:
        m._storage._close_mmap()
    if volume is not None:
        volume.commit()
        volume.reload()
    for m in layers:
        m._storage._remap_after_reload()
    return {
        "n_layers_synced": len(layers),
        "total_dirty_pages": total_dirty,
        "per_layer": pre,
    }


class ProductKeyMemory(nn.Module):
    """Product-Key Memory.

    q_dim       — dimension of incoming query (and of values)
    sqrt_n      — sqrt of total entries; bank holds M = sqrt_n * sqrt_n
    top_k       — final retrieved entries per query
    sub_top_k   — sub-keys retained per half before re-ranking
    mmap_path   — optional path; if set, V.weight is mmap-backed
                  (and pinned to CPU; cross-device gather happens
                  in forward())
    """

    def __init__(self, q_dim: int, sqrt_n: int,
                 top_k: int = 16, sub_top_k: int = 32,
                 mmap_path: str | None = None,
                 n_trunks: int = 1):
        super().__init__()
        assert q_dim % 2 == 0, "q_dim must be even"
        assert n_trunks >= 1, f"n_trunks must be >= 1, got {n_trunks}"
        self.q_dim = q_dim
        self.sub_dim = q_dim // 2
        self.sqrt_n = sqrt_n
        # Per-trunk addressable row count = sqrt_n². With n_trunks>1, V holds
        # n_trunks copies of this row space — different (i_a, i_b) → same
        # per-trunk row, but each trunk_id has its own slice. Routing inside
        # forward() adds (trunk_id * n_per_trunk) to top_global before gather.
        self.n_per_trunk = sqrt_n * sqrt_n
        self.n_trunks = n_trunks
        self.n = n_trunks * self.n_per_trunk
        self.top_k = top_k
        self.sub_top_k = min(sub_top_k, sqrt_n)
        self.mmap_path = mmap_path

        # Query normalization before sub-key lookup. Lample 2019 + PEER 2024
        # both find this is critical for slot utilization at large bank size:
        # without it, queries cluster in a low-dim subspace and most rows are
        # never selected. We use RMSNorm (matches the rest of the model);
        # PEER originally used BatchNorm. q_norm runs on the full q_dim
        # then we split into halves — gives both q_a and q_b consistent scale.
        self.q_norm = nn.RMSNorm(q_dim)

        # Sub-key matrices — small, always RAM, follow parent device
        self.K_a = nn.Parameter(torch.randn(sqrt_n, self.sub_dim) * 0.02)
        self.K_b = nn.Parameter(torch.randn(sqrt_n, self.sub_dim) * 0.02)

        # Value bank — sparse Embedding for sparse-gradient updates.
        #
        # Two modes for V:
        #
        #   bank_on_gpu = True (default): regular nn.Embedding. .to('cuda')
        #     moves V to GPU with the rest of the model. Bank size limited
        #     to GPU VRAM but no cross-device transfer per query → fast.
        #     Use this when bank fits VRAM (≤ ~30 GB on A100 80GB etc).
        #
        #   bank_on_gpu = False: CPUPinnedEmbedding wrapping mmap-backed
        #     storage. .to('cuda') is a no-op on V; forward() detects
        #     device mismatch and gathers top-K rows CPU→GPU per query.
        #     ~10× slower per step at B=64 but bank size unbounded by VRAM.
        #
        # Set via MMLLM_BANK_ON_GPU env var ("true"/"false"). For now,
        # default is True (we're at 1.17 GB, fits VRAM trivially).
        bank_on_gpu = os.environ.get(
            "MMLLM_BANK_ON_GPU", "true",
        ).lower() in ("1", "true", "yes")

        # _storage is the virtual paging layer over the mmap; only
        # populated when V is mmap-backed. Its sync() method is how
        # multi-container Hogwild becomes feasible on Modal Volumes.
        self._storage: PagedMmapStorage | None = None

        # Cross-N migration: if mmap_path exists at the N=1 byte size while
        # this instance is N>1, tile the old contents across all N trunks
        # in-place (replicate trunk-0's V into trunks 1..N-1). Without
        # this, PagedMmapStorage._init_file_if_missing would silently
        # overwrite the old bank with a fresh Gaussian at the new size.
        if mmap_path is not None and self.n_trunks > 1:
            self._maybe_migrate_v_file_to_n_trunks(
                mmap_path, self.n_per_trunk, self.n_trunks, q_dim,
            )

        if mmap_path is not None and not bank_on_gpu:
            self._storage = PagedMmapStorage(mmap_path, self.n, q_dim)
            self.V = CPUPinnedEmbedding.from_pretrained(
                self._storage.tensor, freeze=False, sparse=True,
            )
            # nn.Embedding.from_pretrained wraps the tensor in a fresh
            # Parameter — same storage, different Tensor instance. We
            # need PagedMmapStorage to know about this wrapping tensor
            # so it can rebind V.weight's storage on every sync (not
            # just the internal _tensor handle).
            self._storage.register_owner(self.V.weight)
        else:
            # Either no mmap_path, or bank_on_gpu=True → V follows parent.
            # If mmap_path was given but ignored, log it once to avoid silent surprise.
            if mmap_path is not None:
                print(
                    f"  (ProductKeyMemory: mmap_path={mmap_path} ignored "
                    f"because MMLLM_BANK_ON_GPU=true; V will live on GPU)"
                )
            self.V = nn.Embedding(self.n, q_dim, sparse=True)
            with torch.no_grad():
                self.V.weight.normal_(0, 0.02)

        # Slot-usage tracking. K_a/K_b sub-key hit counts per row over a
        # rolling window — used by `reinit_dead_slots()` to find rows
        # never (or rarely) selected and re-init them, and by metrics
        # to log per-layer utilization entropy. register_buffer so they
        # survive .to(device) but aren't optimized.
        self.register_buffer("ka_hits", torch.zeros(sqrt_n, dtype=torch.long), persistent=False)
        self.register_buffer("kb_hits", torch.zeros(sqrt_n, dtype=torch.long), persistent=False)
        # `last_z_loss` is set every forward to the query z-loss term
        # (logsumexp²) for K_a + K_b — picked up by the train loop and
        # added to the main loss with a small coefficient (~1e-5).
        self.last_z_loss: torch.Tensor | None = None
        # Paired with NetBank.last_output_norm — mean L2 norm of this
        # tier's residual contribution per (B,T) position, captured at
        # the end of forward(). Compare Local vs Net to see if NetBank
        # is being adopted as a tier.
        self.last_output_norm: float = 0.0

    def dense_parameters(self):
        """Parameters with dense gradients (route to AdamW). Returns ONLY
        K_a/K_b — q_norm.weight is exposed separately via `q_norm_parameters`
        so the train-loop can place it at the END of the model's flat
        parameter list (after all blocks' core params). Positional ckpt
        load from a pre-q_norm ckpt then aligns cleanly across all
        per-block tensors; q_norm stays at fresh init (scale 1.0) on
        first load."""
        return [self.K_a, self.K_b]

    def q_norm_parameters(self):
        """Just q_norm.weight, separate from dense_parameters so it can be
        placed at the end of the model's flat param list for backward-
        compat loading of pre-q_norm ckpts."""
        return [self.q_norm.weight]

    def sparse_parameters(self):
        """Parameters with sparse gradients (route to SparseAdam)."""
        return [self.V.weight]

    def zero_bank(self) -> None:
        """Zero V.weight in-place (ablation utility)."""
        with torch.no_grad():
            self.V.weight.zero_()

    def slot_usage_stats(self) -> dict:
        """Per-layer utilization summary computed from the rolling hit
        counters. Returns:
          - dead_a/dead_b: # of K_a/K_b rows with zero hits in the window
          - entropy_a/entropy_b: Shannon entropy of normalized hit dist
            (max = log2(sqrt_n) ≈ 11 for sqrt_n=2048; uniform = max)
          - kl_uniform: KL(hits_norm || uniform), 0 if perfectly uniform
        Caller should reset_slot_usage() after reading to start a new
        window.
        """
        with torch.no_grad():
            ka_total = self.ka_hits.sum().item()
            kb_total = self.kb_hits.sum().item()
            stats = {
                "dead_a":     int((self.ka_hits == 0).sum().item()),
                "dead_b":     int((self.kb_hits == 0).sum().item()),
                "ka_total":   ka_total,
                "kb_total":   kb_total,
            }
            if ka_total > 0:
                pa = self.ka_hits.float() / ka_total
                pa_pos = pa[pa > 0]
                ent_a = -(pa_pos * pa_pos.log2()).sum().item()
                stats["entropy_a"]      = ent_a
                stats["entropy_a_max"]  = float(torch.tensor(self.sqrt_n).log2())
            if kb_total > 0:
                pb = self.kb_hits.float() / kb_total
                pb_pos = pb[pb > 0]
                ent_b = -(pb_pos * pb_pos.log2()).sum().item()
                stats["entropy_b"]      = ent_b
            return stats

    def reset_slot_usage(self) -> None:
        """Zero the hit counters. Call after reading slot_usage_stats()
        to start a fresh window."""
        with torch.no_grad():
            self.ka_hits.zero_()
            self.kb_hits.zero_()

    def reinit_dead_slots(self, hit_threshold: int = 0,
                          k_init_scale: float = 0.02,
                          v_init_scale: float = 0.02) -> dict:
        """Find K_a/K_b rows below `hit_threshold` and re-init with small
        Gaussian noise. Lample 2019 + PEER 2024 use this as the PKM
        analog to MoE load-balancing — periodic kick to redistribute
        unused capacity. Returns a dict with the count of rows touched.

        For dead K_a row i: also reset all V rows i*sqrt_n..(i+1)*sqrt_n
        (the entire i-th K_b stripe) since those are unreachable when
        K_a[i] is the dead key. Same for dead K_b.

        NOTE: V reset only happens when the bank is GPU-resident (no mmap).
        With mmap-backed V we'd need to flush dirty pages — skipped for
        now; in practice the slot-collapse problem is most severe early
        in training when bank_on_gpu=True is the typical config.
        """
        with torch.no_grad():
            ka_dead_mask = self.ka_hits <= hit_threshold
            kb_dead_mask = self.kb_hits <= hit_threshold
            n_a = int(ka_dead_mask.sum().item())
            n_b = int(kb_dead_mask.sum().item())
            if n_a > 0:
                noise_a = torch.randn(
                    n_a, self.sub_dim, device=self.K_a.device, dtype=self.K_a.dtype,
                ) * k_init_scale
                self.K_a.data[ka_dead_mask] = noise_a
            if n_b > 0:
                noise_b = torch.randn(
                    n_b, self.sub_dim, device=self.K_b.device, dtype=self.K_b.dtype,
                ) * k_init_scale
                self.K_b.data[kb_dead_mask] = noise_b
            # Reset corresponding V rows (only when V on GPU)
            if self._storage is None and (n_a > 0 or n_b > 0):
                ka_dead_idx = ka_dead_mask.nonzero(as_tuple=True)[0]
                kb_dead_idx = kb_dead_mask.nonzero(as_tuple=True)[0]
                # i in unreachable set if i//sqrt_n in ka_dead OR i%sqrt_n in kb_dead.
                # Build index tensor of unreachable V rows. Cap to avoid OOM
                # in pathological cases.
                rows_to_reset = []
                if len(ka_dead_idx) > 0:
                    base = ka_dead_idx.unsqueeze(-1) * self.sqrt_n
                    offsets = torch.arange(self.sqrt_n, device=base.device)
                    rows_to_reset.append((base + offsets).flatten())
                if len(kb_dead_idx) > 0:
                    base = torch.arange(self.sqrt_n, device=kb_dead_idx.device) * self.sqrt_n
                    rows = (base.unsqueeze(-1) + kb_dead_idx.unsqueeze(0)).flatten()
                    rows_to_reset.append(rows)
                if rows_to_reset:
                    # Dead-key rows are in [0, n_per_trunk). With n_trunks>1,
                    # broadcast across all trunks so each trunk's slice gets
                    # the same dead-row noise refresh (K_a/K_b are shared, so
                    # unreachability is shared too).
                    per_trunk_rows = torch.unique(torch.cat(rows_to_reset))
                    if self.n_trunks > 1:
                        trunk_offsets = (torch.arange(self.n_trunks,
                                                      device=per_trunk_rows.device)
                                         * self.n_per_trunk)
                        all_rows = (per_trunk_rows.unsqueeze(0)
                                    + trunk_offsets.unsqueeze(-1)).flatten()
                    else:
                        all_rows = per_trunk_rows
                    # Cap reset to avoid touching > 25% of V at once
                    cap = self.n // 4
                    if all_rows.numel() > cap:
                        perm = torch.randperm(all_rows.numel(), device=all_rows.device)[:cap]
                        all_rows = all_rows[perm]
                    noise_v = torch.randn(
                        all_rows.numel(), self.q_dim,
                        device=self.V.weight.device, dtype=self.V.weight.dtype,
                    ) * v_init_scale
                    self.V.weight.data[all_rows] = noise_v
            return {"n_ka_reinit": n_a, "n_kb_reinit": n_b}

    def sync_bank(self, volume) -> dict:
        """Sync this layer's bank to/from a Modal Volume (or any
        commit/reload-shaped object). No-op when V is on GPU or when
        no mmap_path was given.

        See PagedMmapStorage.sync for details.
        """
        if self._storage is None:
            return {"skipped": "bank not mmap'd"}
        return self._storage.sync(volume)

    def n_dirty_pages(self) -> int:
        """Number of bank pages this worker has touched since the
        last sync. Useful for adaptive sync-frequency policies."""
        if self._storage is None:
            return 0
        return self._storage.n_dirty_pages()

    def save_to_mmap(self, path: str) -> int:
        """Dump V.weight to a numpy float32 memmap at `path`, in the
        same (n, q_dim) layout that `_mmap_value_tensor` reads back.

        Used at end of training (when V is on GPU) so inference can
        re-mount via CPUPinnedEmbedding + mmap and run with the bank
        page-faulted from disk.

        Also called from train-long's save-checkpoint! per-ckpt to
        capture in-VRAM bank state to disk — without this, a
        crash+resume loses V because checkpoints don't otherwise
        persist nn.Embedding contents (only the optimizer's m, v
        moments). The path passed by save-checkpoint! is fixed (one
        file per layer, overwritten each ckpt) so the on-disk cost
        is bounded to ~bank size, not per-step accumulating.

        Self-overwrite guard: when `path` is the SAME file that V's
        live mmap is already bound to (the bank_on_gpu=False + mmap
        case), there's nothing to do — V.weight is the on-disk file's
        content. Opening it again as mode='w+' would truncate, which
        leaves the live mmap's pages stale and the copy reads zeros,
        which then propagate to disk. Just flush and return early.

        Returns total bytes written (or expected_bytes when the live
        mmap is already the destination).
        """
        n, dim = self.V.weight.shape
        expected_bytes = n * dim * 4  # float32
        # If V is already mmap-backed at this path, the bank is already
        # on disk — flush the OS page cache and return.
        if self._storage is not None:
            try:
                live_path = os.path.realpath(self._storage.path)
                want_path = os.path.realpath(path)
            except OSError:
                live_path = want_path = None
            if live_path == want_path:
                self._storage.flush() if hasattr(self._storage, "flush") else None
                return expected_bytes
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
        # Pull to CPU once; chunk the write so we don't peak at 2× memory.
        weight_cpu = self.V.weight.detach().to("cpu", copy=False).numpy()
        arr = np.memmap(path, dtype=np.float32, mode="w+", shape=(n, dim))
        chunk_rows = 4096
        for i in range(0, n, chunk_rows):
            end = min(i + chunk_rows, n)
            arr[i:end] = weight_cpu[i:end]
        arr.flush()
        del arr
        return expected_bytes

    def load_from_mmap(self, path: str) -> int:
        """Restore V.weight from a numpy float32 memmap at `path`,
        the inverse of save_to_mmap. Used by train-long's
        load-checkpoint! to recover in-VRAM bank state on resume.

        Idempotent on shape: errors if the file size doesn't match
        (n × q_dim × 4 bytes), so a stale or wrong-config bank file
        fails loud rather than silently corrupting V.

        Cross-N migration: when the on-disk file is at the N=1 byte size
        (n_per_trunk × q_dim × 4) but this instance is n_trunks>1, load
        once and tile across all trunks — old single-trunk content gets
        replicated to seed every trunk's V identically. They then diverge
        during training.

        Returns total bytes read.
        """
        n, dim = self.V.weight.shape
        expected_bytes = n * dim * 4  # float32
        if not os.path.exists(path):
            raise FileNotFoundError(f"bank checkpoint not found: {path}")
        actual_bytes = os.path.getsize(path)
        # Cross-N migration path: on-disk file at N=1 size, model at N>1.
        n_per_trunk_bytes = self.n_per_trunk * dim * 4
        if (actual_bytes == n_per_trunk_bytes
                and expected_bytes == self.n_trunks * n_per_trunk_bytes
                and self.n_trunks > 1):
            print(
                f"  ckpt migration: {path} is N=1 size ({actual_bytes} B); "
                f"tiling to N={self.n_trunks} ({expected_bytes} B) in V.weight"
            )
            arr = np.memmap(path, dtype=np.float32, mode="r",
                            shape=(self.n_per_trunk, dim))
            with torch.no_grad():
                src = torch.from_numpy(np.asarray(arr))  # (n_per_trunk, dim)
                src_dev = src.to(self.V.weight.device)
                # Tile across the N-axis by repeating row block N times.
                self.V.weight.data.view(
                    self.n_trunks, self.n_per_trunk, dim
                ).copy_(src_dev.unsqueeze(0).expand(self.n_trunks, -1, -1))
            del arr
            return actual_bytes
        if actual_bytes != expected_bytes:
            raise ValueError(
                f"bank checkpoint {path} has {actual_bytes} bytes; "
                f"expected {expected_bytes} for shape ({n}, {dim}). "
                f"sqrt_n / q_dim mismatch with the model config?"
            )
        # Stream via memmap → np.array (CPU copy) → torch.from_numpy →
        # .copy_ into V.weight.data. The intermediate np.array is
        # necessary because torch.from_numpy on a memmap returns a
        # non-writable view, and we want a writable owning tensor for
        # the cross-device .copy_ that follows.
        arr = np.memmap(path, dtype=np.float32, mode="r", shape=(n, dim))
        with torch.no_grad():
            src = torch.from_numpy(np.asarray(arr))
            self.V.weight.data.copy_(src.to(self.V.weight.device))
        del arr
        return expected_bytes

    @staticmethod
    def _maybe_migrate_v_file_to_n_trunks(path: str,
                                          n_per_trunk: int,
                                          n_trunks: int,
                                          q_dim: int) -> None:
        """Tile an old N=1-shaped V mmap file in-place to N-trunk shape.

        No-op when:
          - the file doesn't exist (PagedMmapStorage will Gaussian-init)
          - the file is already at the N-trunk size
          - the file is at neither the N=1 nor the N-trunk size (let the
            downstream init/load raise — wrong sqrt_n or q_dim)

        When the file is at the N=1 size, atomically rewrite to N-trunk
        size by reading the contents, allocating a sibling tmp file at
        the new size, tiling, fsync'ing, and renaming over the original.
        Subsequent PagedMmapStorage opens see a file at the right size
        and skip its Gaussian-init.
        """
        n1_bytes  = n_per_trunk * q_dim * 4
        nN_bytes  = n_trunks * n1_bytes
        if not os.path.exists(path):
            return
        actual = os.path.getsize(path)
        if actual == nN_bytes:
            return  # already migrated / freshly created at new size
        if actual != n1_bytes:
            return  # not the N=1 size either; let downstream raise
        print(
            f"  bank migration: {path} from N=1 ({n1_bytes} B) to "
            f"N={n_trunks} ({nN_bytes} B) — tiling trunk-0 into all trunks"
        )
        # Read old contents into a CPU-resident copy so the source mmap
        # can be closed before we rewrite the file.
        old_arr = np.memmap(path, dtype=np.float32, mode="r",
                            shape=(n_per_trunk, q_dim))
        old_data = np.array(old_arr)  # owning copy
        if hasattr(old_arr, "_mmap") and old_arr._mmap is not None:
            old_arr._mmap.close()
        del old_arr
        tmp_path = path + ".migrating"
        new_arr = np.memmap(tmp_path, dtype=np.float32, mode="w+",
                            shape=(n_trunks * n_per_trunk, q_dim))
        for t in range(n_trunks):
            new_arr[t * n_per_trunk:(t + 1) * n_per_trunk] = old_data
        new_arr.flush()
        if hasattr(new_arr, "_mmap") and new_arr._mmap is not None:
            new_arr._mmap.close()
        del new_arr
        os.replace(tmp_path, path)

    def forward(self, q: torch.Tensor,
                trunk_ids: torch.Tensor | None = None) -> torch.Tensor:
        """q: (B, T, q_dim) → (B, T, q_dim) softmax-weighted retrieval.

        `trunk_ids` (optional, (B,) long): per-batch-row routing into V's
        per-trunk slices. When n_trunks > 1, the gather is offset by
        `trunk_ids[i] * n_per_trunk` for batch row i, so each row reads
        from its trunk's V slice while sharing K_a, K_b, q_norm. Pass None
        when n_trunks == 1 (the offset would be 0 anyway). The sub-key
        scoring stays unchanged — same addressing scheme across trunks;
        only the value bank specializes.

        When V.weight is on a different device than q (e.g. q on cuda
        while V is CPU-pinned mmap), the top_k indices are moved to
        V's device, gathered there, and the resulting (B, T, top_k, D)
        tensor is moved to q's device. Autograd handles the .to()
        boundary so the sparse gradient lands on V on its native device.
        """
        # Inference fast path: one C++ call fuses score → sub-topk →
        # outer-sum-topk → gather → softmax → weighted-sum. Drops ~30
        # ATen-op dispatches + Python-orchestration overhead per layer.
        # Only safe when not training (no autograd recording in C++) and
        # V is on CPU fp32 (the only path the fused kernel supports).
        #
        # Skips: training z-loss, sub-key hit counters, dirty-row
        # tracking, .item() telemetry — all training-only side effects.
        # last_z_loss / last_output_norm stay at their previous values
        # (typically None / unread at inference).
        if (not self.training
                and HAS_CPP_KERNELS
                and self.V.weight.is_cpu
                and self.V.weight.dtype == torch.float32):
            return pkm_inference_forward(self, q, trunk_ids=trunk_ids)

        B, T, D = q.shape
        q = self.q_norm(q)
        q_a = q[..., :self.sub_dim]
        q_b = q[..., self.sub_dim:]

        # Sub-key search — on q's device (K_a, K_b follow the parent module)
        scores_a = q_a @ self.K_a.T
        scores_b = q_b @ self.K_b.T

        # Query z-loss: penalty on logsumexp magnitude of sub-key scores.
        # Cheap stability term from ST-MoE; keeps query magnitudes from
        # drifting into numerically unstable regimes during long runs.
        # The training loop reads `last_z_loss` and adds it to the main
        # loss with a small coefficient (~1e-5). Only computed in training
        # mode to skip the per-step overhead during eval.
        if self.training:
            lse_a = torch.logsumexp(scores_a, dim=-1)
            lse_b = torch.logsumexp(scores_b, dim=-1)
            self.last_z_loss = (lse_a.square().mean() + lse_b.square().mean())
        else:
            self.last_z_loss = None

        top_a_s, top_a_i = scores_a.topk(self.sub_top_k, dim=-1)
        top_b_s, top_b_i = scores_b.topk(self.sub_top_k, dim=-1)

        # Update sub-key hit counters for slot-utilization metrics +
        # dead-slot reinit. Only in training mode; bincount on each pass
        # is cheap (sqrt_n=2048 buckets, ~B*T*sub_top_k inputs).
        if self.training:
            with torch.no_grad():
                self.ka_hits.add_(
                    torch.bincount(top_a_i.view(-1), minlength=self.sqrt_n)
                )
                self.kb_hits.add_(
                    torch.bincount(top_b_i.view(-1), minlength=self.sqrt_n)
                )

        # F3: fused outer-sum + top-K. C++ kernel scans S² pairs with a
        # per-row min-heap, skipping the (B, T, sub_top_k²) temp. Python
        # fallback when extension didn't build or V isn't on CPU.
        if HAS_CPP_KERNELS and top_a_s.is_cpu:
            top_scores, top_global = PKMFusedTopK.apply(
                top_a_s, top_a_i, top_b_s, top_b_i, self.sqrt_n, self.top_k,
            )
        else:
            combined_scores = (top_a_s.unsqueeze(-1) + top_b_s.unsqueeze(-2)).flatten(-2)
            idx_a = top_a_i.unsqueeze(-1).expand(-1, -1, -1, self.sub_top_k)
            idx_b = top_b_i.unsqueeze(-2).expand(-1, -1, self.sub_top_k, -1)
            combined_idx = (idx_a * self.sqrt_n + idx_b).flatten(-2)
            top_scores, top_local = combined_scores.topk(self.top_k, dim=-1)
            top_global = combined_idx.gather(-1, top_local)          # (B, T, top_k); per-trunk row in [0, n_per_trunk)

        # Multi-trunk routing: offset each batch row's indices by its trunk's
        # base row. After this, top_global indexes into the flat (N*n_per_trunk,
        # q_dim) V — each batch row hits its own trunk's slice. At N=1 this is
        # skipped (offset would be 0). trunk_ids must be a (B,) long tensor.
        if self.n_trunks > 1 and trunk_ids is not None:
            offsets = (trunk_ids.to(device=top_global.device, dtype=top_global.dtype)
                                * self.n_per_trunk).view(B, 1, 1)
            top_global = top_global + offsets

        # Cross-device V gather: when V is pinned to CPU but q is on GPU,
        # move only top_k indices over (~64 KB), gather rows on V's
        # device, then move (B, T, top_k, D) back. Autograd records
        # both .to() hops so the sparse gradient flows back to V.
        v_device = self.V.weight.device
        if v_device != q.device:
            top_global_v = top_global.to(v_device)
            # Phase-4b prefetch: kernel async-starts paging the rows
            # we're about to gather. Only meaningful when V is mmap-
            # backed; the helper checks for ._mmap and no-ops otherwise.
            if self._storage is not None:
                _madvise_top_k_pages(
                    self._storage._array, top_global_v,
                    row_stride_bytes=self.q_dim * 4,  # fp32
                )
                # Mark pages we're about to touch as dirty (they WILL
                # get a sparse-grad update on backward). Cheap — we
                # already have the indices on CPU after the .to() hop.
                self._storage.track_dirty_rows(top_global_v)
            # F2: contiguous-block gather with parallel memcpy. Replaces
            # F.embedding's per-row aten::index_select. CPU-only path.
            if HAS_CPP_KERNELS and v_device.type == "cpu":
                values_v = PKMGather.apply(self.V.weight, top_global_v)
            else:
                values_v = self.V(top_global_v)                    # (B, T, top_k, D) on V's device
            values = values_v.to(q.device)
        else:
            if self._storage is not None:
                self._storage.track_dirty_rows(top_global)
            if HAS_CPP_KERNELS and v_device.type == "cpu":
                values = PKMGather.apply(self.V.weight, top_global)
            else:
                values = self.V(top_global)                        # (B, T, top_k, D)

        weights = F.softmax(top_scores, dim=-1).unsqueeze(-1)
        out = (weights * values).sum(dim=-2)
        # Instrumentation paired with NetBank.last_output_norm — gives a
        # direct Local-vs-Net residual-contribution comparison. ONLY in
        # training mode: at inference .item() is a per-layer CPU sync
        # that was ~30µs × 3200 PKM calls / decode = 5% of wall, with
        # zero functional value (telemetry only read by training-loop
        # callers and the sweep ablation logs).
        if self.training:
            with torch.no_grad():
                self.last_output_norm = float(
                    out.detach().pow(2).sum(-1).sqrt().mean().item()
                )
        return out


# ─────────────────────── madvise prefetch helper (Phase 4b) ───────────────────────

import mmap as _mmap_module


def _madvise_top_k_pages(
    np_memmap: "np.memmap",
    top_indices_cpu: torch.Tensor,
    row_stride_bytes: int,
    base_offset: int = 0,
    page_size: int = 4096,
) -> int:
    """Issue MADV_WILLNEED on pages containing the rows in `top_indices_cpu`.

    The product-key search produces top-K row IDs *before* the actual
    gather. By the time the gather happens (~µs later for the matmul-
    based search), the kernel has typically started paging the rows in
    asynchronously — so the gather hits warm pages instead of cold-
    cache page faults.

    Page boundary alignment: we round each row's start down to the
    nearest 4 KB page, then dedupe so we only issue madvise once per
    unique page. Per-layer cost: ~16 row indices → ~4-16 unique pages
    × ~µs per syscall ≈ small, easily worth a 2-5× win on cold-cache
    tokens.

    Args:
      np_memmap:        the np.memmap whose ._mmap holds the OS handle
      top_indices_cpu:  row indices, shape (..., top_k); flattened here
      row_stride_bytes: bytes per row in the underlying file
      base_offset:      byte offset in the file where the row data
                        starts (e.g., int8 bank's header+scales)

    Returns:
      number of unique pages we hinted on (for stats / logging).
    """
    mm = getattr(np_memmap, "_mmap", None)
    if mm is None:
        return 0
    if not hasattr(mm, "madvise"):
        return 0  # platform without madvise (e.g., older Windows)
    if not hasattr(_mmap_module, "MADV_WILLNEED"):
        return 0  # no MADV constants on this platform
    flat = top_indices_cpu.detach().flatten().to(dtype=torch.int64).tolist()
    seen = set()
    for i in flat:
        byte_off = base_offset + i * row_stride_bytes
        page_off = (byte_off // page_size) * page_size
        seen.add(page_off)
    # Issue one madvise per unique page covering at least one row.
    # Round the length up to the next page boundary so a row that
    # straddles a page boundary still gets both pages hinted.
    n_hinted = 0
    span = ((row_stride_bytes + page_size - 1) // page_size) * page_size
    file_size = mm.size()
    for off in seen:
        # mmap.madvise expects (option, start, length). Length must
        # not exceed the mapped region.
        length = min(span, file_size - off)
        if length <= 0:
            continue
        try:
            mm.madvise(_mmap_module.MADV_WILLNEED, off, length)
            n_hinted += 1
        except OSError:
            # Some kernels reject WILLNEED on certain mappings;
            # ignore and continue — this is a hint, not a requirement.
            pass
    return n_hinted


# ─────────────────────── int8 quantized bank V (Phase 3) ───────────────────────

INT8_BANK_MAGIC = 0x49_4E_54_38  # b'INT8' as little-endian u32 ← 0x38544E49 in LE bytes
INT8_BANK_VERSION = 1
INT8_BANK_HEADER_SIZE = 16  # bytes: magic(4) + version(4) + n_rows(4) + q_dim(4)


def quantize_fp32_bank_to_int8(in_path: str, out_path: str) -> dict:
    """Convert one fp32 bank V file to int8 + per-row fp16 scale.

    Reads the fp32 bank from `in_path` (raw fp32 array, n_rows × q_dim).
    Writes the int8 quantized version to `out_path` with this layout:

        [INT8_BANK_HEADER_SIZE bytes header]
            magic    u32  0x494E5438 (b'INT8')
            version  u32  1
            n_rows   u32
            q_dim    u32
        [n_rows × 2 bytes : fp16 per-row scales]
        [n_rows × q_dim bytes : int8 row data]

    Quantization: per-row symmetric int8.
        scale = max(|row|) / 127
        int8 = round(row / scale).clip(-127, 127)

    Decode: fp32_row = scale * int8_row.

    Returns a stats dict with file sizes and quantization summary.
    """
    if not os.path.exists(in_path):
        raise FileNotFoundError(f"input bank not found: {in_path}")
    file_bytes = os.path.getsize(in_path)
    if file_bytes % 4 != 0:
        raise ValueError(f"input file size {file_bytes} not divisible by 4 (fp32)")
    # We don't know n_rows/q_dim from the file alone — caller must
    # know. For our case the caller (CLI) knows from the trained model
    # config. We infer n_rows × q_dim = file_bytes / 4 and require the
    # caller to pass q_dim implicitly via the dense ckpt's K_a shape.
    # Simpler interface: read the file as a flat fp32, infer shape from
    # the file_path's trained-config implicit q_dim.
    raise NotImplementedError(
        "use quantize_fp32_bank_to_int8_shaped() — q_dim is needed to "
        "infer the row count from raw bytes"
    )


def quantize_fp32_bank_to_int8_shaped(in_path: str, out_path: str,
                                       q_dim: int,
                                       chunk_rows: int = 16384) -> dict:
    """Like quantize_fp32_bank_to_int8 but with explicit `q_dim` so we
    can stream the file in chunks instead of mapping the whole thing
    into RAM. At sqrt_n=2048 + q_dim=224, the input is 18.8 GB —
    chunking keeps peak RAM bounded.
    """
    if not os.path.exists(in_path):
        raise FileNotFoundError(f"input bank not found: {in_path}")
    elem_bytes = 4  # fp32
    file_bytes = os.path.getsize(in_path)
    if file_bytes % (q_dim * elem_bytes) != 0:
        raise ValueError(
            f"input file size {file_bytes} not divisible by q_dim*4={q_dim*elem_bytes}; "
            f"q_dim mismatch?"
        )
    n_rows = file_bytes // (q_dim * elem_bytes)
    out_bytes = INT8_BANK_HEADER_SIZE + n_rows * 2 + n_rows * q_dim
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)

    src = np.memmap(in_path, dtype=np.float32, mode="r", shape=(n_rows, q_dim))
    # Pre-allocate output file at full size so we can mmap regions.
    with builtins.open(out_path, "wb") as f:
        f.truncate(out_bytes)
    # Header
    header = struct.pack("<IIII",
                         INT8_BANK_MAGIC, INT8_BANK_VERSION, n_rows, q_dim)
    out_handle = builtins.open(out_path, "r+b")
    out_handle.seek(0)
    out_handle.write(header)
    out_handle.flush()
    # Memmap the scale + int8 regions of the output file
    scales = np.memmap(out_path, dtype=np.float16, mode="r+",
                       offset=INT8_BANK_HEADER_SIZE, shape=(n_rows,))
    int8_rows = np.memmap(out_path, dtype=np.int8, mode="r+",
                          offset=INT8_BANK_HEADER_SIZE + n_rows * 2,
                          shape=(n_rows, q_dim))

    # Stream chunks from src → quantize → write to scales + int8_rows
    max_abs_overall = 0.0
    n_clamped = 0
    for i in range(0, n_rows, chunk_rows):
        end = min(i + chunk_rows, n_rows)
        chunk = src[i:end].astype(np.float32, copy=False)
        # Per-row max abs; floor at tiny epsilon to avoid div-by-zero
        max_abs = np.maximum(np.abs(chunk).max(axis=1), 1e-12)
        scale = max_abs / 127.0
        # Quantize: round and clamp
        q = np.round(chunk / scale[:, None])
        n_clamped += int(((q > 127) | (q < -127)).sum())
        q_clipped = np.clip(q, -127, 127).astype(np.int8)
        # Write
        scales[i:end] = scale.astype(np.float16)
        int8_rows[i:end] = q_clipped
        max_abs_overall = max(max_abs_overall, float(max_abs.max()))

    scales.flush()
    int8_rows.flush()
    del scales
    del int8_rows
    del src
    out_handle.close()

    return {
        "in_path": in_path,
        "out_path": out_path,
        "n_rows": n_rows,
        "q_dim": q_dim,
        "in_bytes": file_bytes,
        "out_bytes": out_bytes,
        "compression_ratio": file_bytes / out_bytes,
        "max_abs_overall": max_abs_overall,
        "n_clamped": n_clamped,
    }


def _read_int8_bank_header(path: str) -> tuple[int, int]:
    """Open `path`, validate header magic+version, return (n_rows, q_dim)."""
    with builtins.open(path, "rb") as f:
        header = f.read(INT8_BANK_HEADER_SIZE)
    if len(header) != INT8_BANK_HEADER_SIZE:
        raise ValueError(f"int8 bank file too short: {path}")
    magic, version, n_rows, q_dim = struct.unpack("<IIII", header)
    if magic != INT8_BANK_MAGIC:
        raise ValueError(
            f"bad magic 0x{magic:08x} in int8 bank file {path} "
            f"(expected 0x{INT8_BANK_MAGIC:08x})"
        )
    if version != INT8_BANK_VERSION:
        raise ValueError(
            f"unsupported int8 bank version {version} in {path} "
            f"(this build expects {INT8_BANK_VERSION})"
        )
    return n_rows, q_dim


class _MmapInt8Storage(nn.Module):
    """Wraps the scales + int8_rows tensors of an mmap-backed int8 bank.
    Override _apply to keep the storage CPU-pinned regardless of any
    parent .to('cuda') call — analogous to CPUPinnedEmbedding for the
    fp32 path. The Int8ProductKeyMemory's K_a/K_b still move normally
    because they're parameters at the parent level.

    Holds the underlying np.memmap as well so Phase-4b madvise prefetch
    can reach the OS mmap handle (.scales_np._mmap)."""

    def __init__(self, scales: torch.Tensor, int8_rows: torch.Tensor,
                 scales_np: "np.memmap", int8_np: "np.memmap"):
        super().__init__()
        self.scales = scales
        self.int8_rows = int8_rows
        # Plain attributes — not registered. Used by madvise.
        self.scales_np = scales_np
        self.int8_np = int8_np

    def _apply(self, fn, recurse=True):
        return self


class Int8ProductKeyMemory(nn.Module):
    """Inference-only int8-quantized product-key memory.

    Same K_a, K_b sub-keys (fp32 parameters), same product-key search,
    same softmax-weighted retrieval. Difference: V is stored as
    per-row int8 + per-row fp16 scale. ~4× smaller on disk and in RAM
    than fp32, with negligible BPC drift in practice (target +0.005).

    NOT trainable — `sparse_parameters()` returns []. Use the fp32
    `ProductKeyMemory` for training; quantize once after training via
    `mmllm bank-quantize`.

    File layout per layer (`<bank_path>.<i>.int8.bin`):
        16-byte header (magic 'INT8', version, n_rows, q_dim)
        n_rows × 2 bytes : fp16 per-row scales
        n_rows × q_dim bytes : int8 row data
    """

    def __init__(self, q_dim: int, sqrt_n: int,
                 top_k: int = 16, sub_top_k: int = 32,
                 mmap_path: str | None = None,
                 n_trunks: int = 1):
        super().__init__()
        assert q_dim % 2 == 0, "q_dim must be even"
        # Int8 path is inference-only; multi-trunk only matters at training,
        # where the fp32 ProductKeyMemory is the one in use. Accept the
        # kwarg so memory-cls stays polymorphic, but assert N=1 — at
        # inference each request runs on a single trunk's bank.
        assert n_trunks == 1, (
            f"Int8ProductKeyMemory only supports n_trunks=1 (inference path), "
            f"got n_trunks={n_trunks}"
        )
        self.q_dim = q_dim
        self.sub_dim = q_dim // 2
        self.sqrt_n = sqrt_n
        self.n = sqrt_n * sqrt_n
        self.top_k = top_k
        self.sub_top_k = min(sub_top_k, sqrt_n)
        self.mmap_path = mmap_path

        # Query normalization — must match ProductKeyMemory so int8
        # inference picks up the trained q_norm.weight from the dense ckpt.
        self.q_norm = nn.RMSNorm(q_dim)

        # Sub-key matrices — same as fp32 path
        self.K_a = nn.Parameter(torch.randn(sqrt_n, self.sub_dim) * 0.02)
        self.K_b = nn.Parameter(torch.randn(sqrt_n, self.sub_dim) * 0.02)

        # Storage placement matches MMLLM_BANK_ON_GPU. When mmap-backed
        # and not on GPU, scales + int8 stay CPU-pinned; cross-device
        # gather happens in forward() per query (same pattern as fp32).
        bank_on_gpu = os.environ.get(
            "MMLLM_BANK_ON_GPU", "true",
        ).lower() in ("1", "true", "yes")

        self._storage: _MmapInt8Storage | None = None
        if mmap_path is not None and not bank_on_gpu:
            scales, int8_rows, scales_np, int8_np = (
                self._load_or_init_int8_mmap(mmap_path, q_dim)
            )
            self._storage = _MmapInt8Storage(scales, int8_rows, scales_np, int8_np)
        else:
            if mmap_path is not None:
                # mmap+on-GPU: load the int8 file once into VRAM.
                scales, int8_rows, _, _ = self._load_or_init_int8_mmap(mmap_path, q_dim)
                self.register_buffer("scales", scales.clone())
                self.register_buffer("int8_rows", int8_rows.clone())
            else:
                # No mmap_path: zero-init buffers (testing only — real
                # int8 banks come from quantize_fp32_bank_to_int8_shaped).
                self.register_buffer(
                    "scales", torch.zeros(self.n, dtype=torch.float16),
                )
                self.register_buffer(
                    "int8_rows", torch.zeros(self.n, q_dim, dtype=torch.int8),
                )

    def _load_or_init_int8_mmap(self, path: str, q_dim: int):
        """Open an existing int8 bank file via mmap. Returns
        (scales_tensor, int8_rows_tensor, scales_np, int8_np) — torch
        tensors AND the underlying np.memmap arrays (the latter so
        Phase-4b madvise can reach the OS mmap handle).
        Raises if the file doesn't exist or has bad header."""
        n_rows, file_q_dim = _read_int8_bank_header(path)
        if n_rows != self.n:
            raise ValueError(
                f"int8 bank {path} has n_rows={n_rows} but model expects "
                f"sqrt_n²={self.n}"
            )
        if file_q_dim != q_dim:
            raise ValueError(
                f"int8 bank {path} has q_dim={file_q_dim} but model expects {q_dim}"
            )
        scales_np = np.memmap(path, dtype=np.float16, mode="r",
                              offset=INT8_BANK_HEADER_SIZE, shape=(n_rows,))
        int8_np = np.memmap(path, dtype=np.int8, mode="r",
                            offset=INT8_BANK_HEADER_SIZE + n_rows * 2,
                            shape=(n_rows, q_dim))
        return (
            torch.from_numpy(scales_np), torch.from_numpy(int8_np),
            scales_np, int8_np,
        )

    def _scales(self) -> torch.Tensor:
        return self._storage.scales if self._storage is not None else self.scales

    def _int8_rows(self) -> torch.Tensor:
        return self._storage.int8_rows if self._storage is not None else self.int8_rows

    def dense_parameters(self):
        return [self.K_a, self.K_b]

    def sparse_parameters(self):
        # int8 bank is read-only: no gradient flows back into the rows.
        return []

    def zero_bank(self) -> None:
        """Zero the int8 rows + scales (ablation utility)."""
        with torch.no_grad():
            scales = self._scales()
            int8_rows = self._int8_rows()
            # Mmap-backed views are read-only; can't zero them in place.
            # For ablation we'd swap a separate zero buffer in. For now,
            # emit a clear error so callers know int8 bank ablation
            # needs more work.
            if self._storage is not None:
                raise NotImplementedError(
                    "Int8ProductKeyMemory.zero_bank not implemented for "
                    "mmap-backed banks (read-only mmap). Run ablation on "
                    "the fp32 bank and quantize separately."
                )
            scales.zero_()
            int8_rows.zero_()

    def forward(self, q: torch.Tensor) -> torch.Tensor:
        """q: (B, T, q_dim) → (B, T, q_dim) softmax-weighted retrieval,
        identical math to ProductKeyMemory.forward but with on-the-fly
        int8 → fp32 dequantization at the gather step.
        """
        B, T, D = q.shape
        q = self.q_norm(q)
        q_a = q[..., :self.sub_dim]
        q_b = q[..., self.sub_dim:]

        # Sub-key search — same as fp32
        scores_a = q_a @ self.K_a.T
        scores_b = q_b @ self.K_b.T
        top_a_s, top_a_i = scores_a.topk(self.sub_top_k, dim=-1)
        top_b_s, top_b_i = scores_b.topk(self.sub_top_k, dim=-1)
        combined_scores = (top_a_s.unsqueeze(-1) + top_b_s.unsqueeze(-2)).flatten(-2)
        idx_a = top_a_i.unsqueeze(-1).expand(-1, -1, -1, self.sub_top_k)
        idx_b = top_b_i.unsqueeze(-2).expand(-1, -1, self.sub_top_k, -1)
        combined_idx = (idx_a * self.sqrt_n + idx_b).flatten(-2)
        top_scores, top_local = combined_scores.topk(self.top_k, dim=-1)
        top_global = combined_idx.gather(-1, top_local)            # (B, T, top_k)

        scales = self._scales()
        int8_rows = self._int8_rows()
        v_device = scales.device
        if v_device != q.device:
            top_global_v = top_global.to(v_device)
            # Phase-4b prefetch on the int8 row data (the larger of
            # the two regions — scales is 1/112 of int8_rows at
            # q_dim=224, dominates cache pressure).
            if self._storage is not None:
                _madvise_top_k_pages(
                    self._storage.int8_np, top_global_v,
                    row_stride_bytes=self.q_dim,
                )
            top_scales = scales[top_global_v].float()              # (B, T, top_k) fp32
            top_int8 = int8_rows[top_global_v].float()             # (B, T, top_k, D) fp32
            values_v = top_scales.unsqueeze(-1) * top_int8         # (B, T, top_k, D)
            values = values_v.to(q.device)
        else:
            top_scales = scales[top_global].float()
            top_int8 = int8_rows[top_global].float()
            values = top_scales.unsqueeze(-1) * top_int8

        weights = F.softmax(top_scores, dim=-1).unsqueeze(-1)
        return (weights * values).sum(dim=-2)


def quantize_bank_files(in_prefix: str, out_prefix: str,
                        n_layers: int, q_dim: int) -> list[dict]:
    """Bulk-quantize a multi-layer bank, file-per-layer:

        <in_prefix>.<i>.bin       (fp32, raw)
        →
        <out_prefix>.<i>.int8.bin (int8 + scales + header)

    Returns a list of per-layer stats dicts (see
    quantize_fp32_bank_to_int8_shaped).
    """
    out = []
    for i in range(n_layers):
        in_path = f"{in_prefix}.{i}.bin"
        out_path = f"{out_prefix}.{i}.int8.bin"
        stats = quantize_fp32_bank_to_int8_shaped(in_path, out_path, q_dim)
        out.append(stats)
    return out
