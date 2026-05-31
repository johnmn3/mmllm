"""Paged, LRU-evicted, sparse-read mmap-backed long-term KV cache.

Each layer's storage is divided into N fixed-size pages of `page_tokens`
tokens each. Pages are allocated in arbitrary order (not appended).
Attention reads the top-K most-recently-accessed pages — sparse, so
we never read all GBs every step. Reads bump access timestamps.
Writes get a free slot if one exists, else evict the LRU page.

This is a proper LRU cache, not a FIFO log:

  * `read_pages`  — bumps access counters on every page touched
  * `allocate`    — picks a free slot OR evicts the LRU slot
  * `select_top_k_mru` — sparse selection by recency for attention

File layout:

    header (32 bytes):
        magic              u32   0x76424c43 ('vBLC')
        version            u32   1
        n_layers           u32
        n_kv               u32
        head_dim           u32
        page_tokens        u32
        n_pages_per_layer  u32
        access_counter     u64   monotonic global

    per-layer block (repeated n_layers times):
        page metadata array:  n_pages_per_layer × 16 bytes
            valid             u8
            n_tok             u16
            pad1              u8
            last_access       u64
            pad2              u32
        page data array:      n_pages_per_layer × 2 × n_kv × page_tokens
                              × head_dim × 4 bytes (fp32)

torch tensors returned by `read_pages` are zero-copy views into the
mmap region.
"""

from __future__ import annotations

import builtins
import mmap
import struct

import numpy as np
import torch

MAGIC = 0x76424C43
HEADER_FMT = "<IIIIIIIQ"  # magic, version, n_layers, n_kv, head_dim, page_tokens, n_pages, access_ctr
HEADER_SIZE = struct.calcsize(HEADER_FMT)
assert HEADER_SIZE == 36
ACCESS_CTR_OFFSET = HEADER_SIZE - 8  # u64 access_ctr is the last header field

PAGE_META_FMT = "<BHBQI"  # valid, n_tok, pad1, last_access, pad2
PAGE_META_SIZE = struct.calcsize(PAGE_META_FMT)
assert PAGE_META_SIZE == 16

DTYPE = np.float32
ELEM_SIZE = 4


# ─────────────────────── byte math ───────────────────────

def _page_data_bytes(n_kv: int, page_tokens: int, head_dim: int) -> int:
    return 2 * n_kv * page_tokens * head_dim * ELEM_SIZE


def _layer_meta_bytes(n_pages: int) -> int:
    return n_pages * PAGE_META_SIZE


def _layer_data_bytes(n_pages: int, n_kv: int, page_tokens: int, head_dim: int) -> int:
    return n_pages * _page_data_bytes(n_kv, page_tokens, head_dim)


def _total_bytes(n_layers: int, n_pages: int, n_kv: int, page_tokens: int, head_dim: int) -> int:
    layer_bytes = (
        _layer_meta_bytes(n_pages)
        + _layer_data_bytes(n_pages, n_kv, page_tokens, head_dim)
    )
    return HEADER_SIZE + n_layers * layer_bytes


def _layer_offset(layer: int, n_pages: int, n_kv: int, page_tokens: int, head_dim: int) -> int:
    layer_bytes = (
        _layer_meta_bytes(n_pages)
        + _layer_data_bytes(n_pages, n_kv, page_tokens, head_dim)
    )
    return HEADER_SIZE + layer * layer_bytes


def _bytes_human(n: float) -> str:
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if n < 1024:
            return f"{n:.1f} {unit}"
        n /= 1024
    return f"{n:.1f} PB"


# ─────────────────────── create / open ───────────────────────

def create(path: str, n_layers: int, n_kv: int, head_dim: int,
           page_tokens: int = 64, n_pages_per_layer: int = 8192) -> dict:
    """Create a new paged-LRU long-cache file, zero-filled."""
    total = _total_bytes(n_layers, n_pages_per_layer, n_kv, page_tokens, head_dim)
    with builtins.open(path, "w+b") as f:
        f.truncate(total)
        f.seek(0)
        f.write(struct.pack(HEADER_FMT, MAGIC, 1, n_layers, n_kv, head_dim,
                            page_tokens, n_pages_per_layer, 0))
    return open_cache(path)


def open_cache(path: str) -> dict:
    """Open an existing paged-LRU long-cache file."""
    f = builtins.open(path, "r+b")
    f.seek(0, 2)
    size = f.tell()
    f.seek(0)
    mm = mmap.mmap(f.fileno(), size)
    fields = struct.unpack(HEADER_FMT, mm[:HEADER_SIZE])
    magic, version, n_layers, n_kv, head_dim, page_tokens, n_pages, access_ctr = fields
    if magic != MAGIC:
        raise ValueError(f"bad magic 0x{magic:08x} in {path}")

    # Numpy view of every layer's page-data block, shape (n_pages, 2, n_kv, page_tokens, head_dim)
    layer_data_views = []
    for layer in range(n_layers):
        data_offset = _layer_offset(layer, n_pages, n_kv, page_tokens, head_dim) \
                      + _layer_meta_bytes(n_pages)
        n_floats = _layer_data_bytes(n_pages, n_kv, page_tokens, head_dim) // ELEM_SIZE
        view = np.frombuffer(mm, dtype=DTYPE, count=n_floats, offset=data_offset).reshape(
            n_pages, 2, n_kv, page_tokens, head_dim
        )
        layer_data_views.append(view)

    # Per-layer page state read from disk into RAM (faster than re-reading every access)
    page_state = []
    for layer in range(n_layers):
        layer_state = []
        meta_offset = _layer_offset(layer, n_pages, n_kv, page_tokens, head_dim)
        for p in range(n_pages):
            o = meta_offset + p * PAGE_META_SIZE
            valid, n_tok, _, last_access, _ = struct.unpack(
                PAGE_META_FMT, mm[o:o + PAGE_META_SIZE]
            )
            layer_state.append({"valid": valid, "n_tok": n_tok, "last_access": last_access})
        page_state.append(layer_state)

    return {
        "path": path,
        "file": f,
        "mmap": mm,
        "size_bytes": size,
        "n_layers": n_layers,
        "n_kv": n_kv,
        "head_dim": head_dim,
        "page_tokens": page_tokens,
        "n_pages": n_pages,
        "access_counter": access_ctr,
        "layer_data": layer_data_views,
        "page_state": page_state,
        # Per-layer in-RAM partial page being filled. Flushed to a slot when full.
        "current_pages": [
            {"k": np.zeros((n_kv, 0, head_dim), dtype=DTYPE),
             "v": np.zeros((n_kv, 0, head_dim), dtype=DTYPE)}
            for _ in range(n_layers)
        ],
    }


# ─────────────────────── header / metadata writers ───────────────────────

def _bump_counter(cache: dict) -> int:
    """Bump the global access counter and persist to mmap header."""
    cache["access_counter"] += 1
    cache["mmap"][ACCESS_CTR_OFFSET:HEADER_SIZE] = struct.pack(
        "<Q", cache["access_counter"]
    )
    return cache["access_counter"]


def _write_meta(cache: dict, layer: int, page: int, valid: int, n_tok: int, last_access: int) -> None:
    """Persist a single page's metadata to mmap and update RAM state."""
    o = _layer_offset(layer, cache["n_pages"], cache["n_kv"],
                      cache["page_tokens"], cache["head_dim"]) \
        + page * PAGE_META_SIZE
    cache["mmap"][o:o + PAGE_META_SIZE] = struct.pack(
        PAGE_META_FMT, valid, n_tok, 0, last_access, 0
    )
    s = cache["page_state"][layer][page]
    s["valid"] = valid
    s["n_tok"] = n_tok
    s["last_access"] = last_access


# ─────────────────────── core LRU operations ───────────────────────

def allocate(cache: dict, layer: int) -> int:
    """Find a slot for a new page in the given layer.

    Prefers a free (invalid) slot; falls back to evicting the LRU
    valid slot (smallest last_access). Returns the slot index.
    """
    state = cache["page_state"][layer]
    for i, ps in enumerate(state):
        if not ps["valid"]:
            return i
    # All slots full; pick the LRU
    return min(range(len(state)), key=lambda i: state[i]["last_access"])


def select_top_k_mru(cache: dict, layer: int, k: int) -> list[int]:
    """Return the k most-recently-accessed VALID page indices for a layer."""
    state = cache["page_state"][layer]
    valid_pages = [(i, ps["last_access"]) for i, ps in enumerate(state) if ps["valid"]]
    valid_pages.sort(key=lambda x: -x[1])  # newest first
    return [i for i, _ in valid_pages[:k]]


def read_pages(cache: dict, layer: int, page_indices: list[int]):
    """Concat K, V from selected pages and bump their access counters.

    Returns (k_tensor, v_tensor) of shape
    (1, n_kv, len(pages) * page_tokens, head_dim)
    or (None, None) if no pages were selected.
    Reads zero-copy via torch.from_numpy on the mmap views.
    """
    if not page_indices:
        return None, None
    layer_data = cache["layer_data"][layer]
    state = cache["page_state"][layer]

    # Sort by last_access ascending so we present older→newer in time order
    page_indices = sorted(page_indices, key=lambda i: state[i]["last_access"])
    k_np = np.concatenate([layer_data[p, 0] for p in page_indices], axis=1)
    v_np = np.concatenate([layer_data[p, 1] for p in page_indices], axis=1)

    # Bump access on every touched page
    ac = _bump_counter(cache)
    for p in page_indices:
        _write_meta(cache, layer, p, valid=1,
                    n_tok=state[p]["n_tok"], last_access=ac)

    return torch.from_numpy(k_np).unsqueeze(0), torch.from_numpy(v_np).unsqueeze(0)


def write_tokens(cache: dict, layer: int, k_new: np.ndarray, v_new: np.ndarray) -> None:
    """Buffer new K, V tokens for `layer` and flush full pages.

    K, V shapes: (n_kv, T, head_dim).
    Tokens accumulate in the per-layer current page (RAM). When the
    current page reaches page_tokens, it's written into a slot
    (free or LRU-evicted) and a new partial page begins.
    """
    cur = cache["current_pages"][layer]
    cur["k"] = np.concatenate([cur["k"], k_new], axis=1)
    cur["v"] = np.concatenate([cur["v"], v_new], axis=1)
    page_tokens = cache["page_tokens"]
    while cur["k"].shape[1] >= page_tokens:
        # Allocate a slot (LRU eviction if all full)
        page_idx = allocate(cache, layer)
        cache["layer_data"][layer][page_idx, 0] = cur["k"][:, :page_tokens, :]
        cache["layer_data"][layer][page_idx, 1] = cur["v"][:, :page_tokens, :]
        ac = _bump_counter(cache)
        _write_meta(cache, layer, page_idx, valid=1,
                    n_tok=page_tokens, last_access=ac)
        cur["k"] = cur["k"][:, page_tokens:, :]
        cur["v"] = cur["v"][:, page_tokens:, :]


# ─────────────────────── high-level wrappers ───────────────────────

def to_forward_arg(cache: dict, top_k_mru: int = 16):
    """For each layer, return [k, v] tensors of the top-K MRU pages.

    Returns a Python list of n_layers entries (each is [k_tensor, v_tensor]
    or None for an empty layer), or None if every layer is empty.
    """
    result = []
    any_data = False
    for layer in range(cache["n_layers"]):
        page_indices = select_top_k_mru(cache, layer, top_k_mru)
        if not page_indices:
            result.append(None)
        else:
            any_data = True
            k_t, v_t = read_pages(cache, layer, page_indices)
            result.append([k_t, v_t])
    return result if any_data else None


def commit_new_tokens(cache: dict, new_long_caches, new_T: int) -> None:
    """After a forward step, write the LAST new_T tokens of each layer's
    long cache to the mmap (via write_tokens → page flush → LRU eviction).

    Using new_T instead of prev_long_T means we don't depend on every
    layer having an identical prior-cache size — `to_forward_arg` may
    return different page counts per layer (early on, while filling).
    """
    if new_T <= 0:
        return
    for layer, kv in enumerate(new_long_caches):
        if kv is None:
            continue
        k, v = kv
        k_np = k[0, :, -new_T:, :].detach().contiguous().numpy()
        v_np = v[0, :, -new_T:, :].detach().contiguous().numpy()
        write_tokens(cache, layer, k_np, v_np)


# ─────────────────────── reporting ───────────────────────

def stats(cache: dict) -> str:
    valid_per_layer = [sum(1 for ps in state if ps["valid"])
                       for state in cache["page_state"]]
    total_valid = sum(valid_per_layer)
    total_pages = cache["n_layers"] * cache["n_pages"]
    return (
        f"  path:       {cache['path']}\n"
        f"  layout:     {cache['n_layers']} layers × {cache['n_pages']:,} pages "
        f"× {cache['page_tokens']} tok/page × {cache['n_kv']} kv-heads × {cache['head_dim']} dim, fp32\n"
        f"  occupancy:  {total_valid:,}/{total_pages:,} pages valid "
        f"({100 * total_valid / max(total_pages, 1):.1f}%)\n"
        f"  per layer:  {valid_per_layer}\n"
        f"  file size:  {_bytes_human(cache['size_bytes'])}\n"
        f"  access ctr: {cache['access_counter']:,}"
    )


def close_cache(cache: dict) -> None:
    """Flush + close the mmap. If torch tensors handed out via read_pages
    still hold buffer views, mmap.close() raises BufferError — that's
    benign, the OS will unmap at process exit and the data is already
    flushed."""
    cache["mmap"].flush()
    try:
        cache["mmap"].close()
    except BufferError:
        pass
    cache["file"].close()
