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

import os

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F


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
        """Mark pages containing these row indices as dirty.

        Called from forward() at lookup time — every row we touch is
        guaranteed to receive a sparse-grad update on backward, so
        flagging at lookup is both correct and cheap (no extra GPU↔CPU
        sync; the indices are already on hand).

        Returns the number of newly-flagged pages (for logging).
        """
        before = len(self._dirty_pages)
        flat = row_indices.detach().flatten().to("cpu", dtype=torch.int64)
        # // is integer division; .unique() keeps the dirty set small
        # even when the same page is touched many times per step.
        pages = (flat // self.page_rows).unique().tolist()
        self._dirty_pages.update(pages)
        return len(self._dirty_pages) - before

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
                 mmap_path: str | None = None):
        super().__init__()
        assert q_dim % 2 == 0, "q_dim must be even"
        self.q_dim = q_dim
        self.sub_dim = q_dim // 2
        self.sqrt_n = sqrt_n
        self.n = sqrt_n * sqrt_n
        self.top_k = top_k
        self.sub_top_k = min(sub_top_k, sqrt_n)
        self.mmap_path = mmap_path

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

    def dense_parameters(self):
        """Parameters with dense gradients (route to AdamW)."""
        return [self.K_a, self.K_b]

    def sparse_parameters(self):
        """Parameters with sparse gradients (route to SparseAdam)."""
        return [self.V.weight]

    def zero_bank(self) -> None:
        """Zero V.weight in-place (ablation utility)."""
        with torch.no_grad():
            self.V.weight.zero_()

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

        Returns total bytes written.
        """
        n, dim = self.V.weight.shape
        expected_bytes = n * dim * 4  # float32
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

    def forward(self, q: torch.Tensor) -> torch.Tensor:
        """q: (B, T, q_dim) → (B, T, q_dim) softmax-weighted retrieval.

        When V.weight is on a different device than q (e.g. q on cuda
        while V is CPU-pinned mmap), the top_k indices are moved to
        V's device, gathered there, and the resulting (B, T, top_k, D)
        tensor is moved to q's device. Autograd handles the .to()
        boundary so the sparse gradient lands on V on its native device.
        """
        B, T, D = q.shape
        q_a = q[..., :self.sub_dim]
        q_b = q[..., self.sub_dim:]

        # Sub-key search — on q's device (K_a, K_b follow the parent module)
        scores_a = q_a @ self.K_a.T
        scores_b = q_b @ self.K_b.T
        top_a_s, top_a_i = scores_a.topk(self.sub_top_k, dim=-1)
        top_b_s, top_b_i = scores_b.topk(self.sub_top_k, dim=-1)

        # Outer-sum scores; index via i = i_a * sqrt_n + i_b
        combined_scores = (top_a_s.unsqueeze(-1) + top_b_s.unsqueeze(-2))
        combined_scores = combined_scores.flatten(-2)

        idx_a = top_a_i.unsqueeze(-1).expand(-1, -1, -1, self.sub_top_k)
        idx_b = top_b_i.unsqueeze(-2).expand(-1, -1, self.sub_top_k, -1)
        combined_idx = (idx_a * self.sqrt_n + idx_b).flatten(-2)

        # Top-K from candidates — still on q's device
        top_scores, top_local = combined_scores.topk(self.top_k, dim=-1)
        top_global = combined_idx.gather(-1, top_local)            # (B, T, top_k)

        # Cross-device V gather: when V is pinned to CPU but q is on GPU,
        # move only top_k indices over (~64 KB), gather rows on V's
        # device, then move (B, T, top_k, D) back. Autograd records
        # both .to() hops so the sparse gradient flows back to V.
        v_device = self.V.weight.device
        if v_device != q.device:
            top_global_v = top_global.to(v_device)
            # Mark pages we're about to touch as dirty (they WILL get a
            # sparse-grad update on backward). Cheap — we already have
            # the indices on CPU after the .to(v_device) hop above for
            # the bank lookup.
            if self._storage is not None:
                self._storage.track_dirty_rows(top_global_v)
            values_v = self.V(top_global_v)                        # (B, T, top_k, D) on V's device
            values = values_v.to(q.device)
        else:
            if self._storage is not None:
                self._storage.track_dirty_rows(top_global)
            values = self.V(top_global)                            # (B, T, top_k, D)

        weights = F.softmax(top_scores, dim=-1).unsqueeze(-1)
        return (weights * values).sum(dim=-2)
