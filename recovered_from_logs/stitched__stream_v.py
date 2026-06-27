"""Disk-streaming NetBank V for the 10GB+ path.

V (and its Adam state) live on disk, never resident. `stream_combine` is an
mx.custom_function: forward preads the touched rows and does the softmax-weighted
combine; its VJP returns d(top_scores) so the PKM keys still learn, and scatters the
V-row gradient to disk via a sparse Adam step (pwrite) as a side-effect. Single-pass —
no trainer two-pass needed. I/O follows ds4 (ds4-cold-expert-streaming-pread memory):
explicit pread/pwrite with F_NOCACHE to bypass the page cache (avoids the wired/
compressor thrash that file-mmap caused).
"""
import os, numpy as np
from collections import OrderedDict
import mlx.core as mx

try:
    import fcntl
    _F_NOCACHE = 48  # macOS fcntl cmd
except Exception:
    fcntl = None
    _F_NOCACHE = None


class StreamV:
    """Disk V[N,c] + Adam m,v with a BOUNDED LRU row cache (ds4 slab model).

    Only `cap` rows are ever resident — a fixed (V,m,v) buffer of `cap` slots. A
    cache miss preads the row from disk (F_NOCACHE → the kernel never page-caches
    it); when the buffer is full the least-recently-used slot is evicted, pwriting
    it back first if dirty. So RAM == cap·c·4·3 bytes, a CONSTANT independent of N:
    the disk table can be 10GB, 100GB, a TB — resident footprint is unchanged. This
    is the correct bounded LRU (the earlier memmap/page-cache version had no bound
    and thrashed). cap defaults to hold a full step's touched set + margin."""

    def __init__(self, path, N, c, lr, cap=None, b1=0.9, b2=0.999, eps=1e-8):
        self.N, self.c, self.rb = int(N), int(c), int(c) * 4
        self.lr, self.b1, self.b2, self.eps, self.t = float(lr), b1, b2, eps, 0
        self.cap = int(cap or int(os.environ.get("MMLLM_NET_CACHE_ROWS", "65536")))
        self._dbgpath = path
        self.fdV = os.open(path, os.O_RDWR)
        self.fdm = self._open_state(path + ".adm")
        self.fdv = self._open_state(path + ".adv")
        for fd in (self.fdV, self.fdm, self.fdv):
            if fcntl is not None and _F_NOCACHE is not None:
                try: fcntl.fcntl(fd, _F_NOCACHE, 1)        # kernel never page-caches
                except OSError: pass
        self.Vb = np.zeros((self.cap, self.c), np.float32)
        self.mb = np.zeros((self.cap, self.c), np.float32)
        self.vb = np.zeros((self.cap, self.c), np.float32)
        self.slot = {}                                     # rowid -> slot index
        self.row_at = np.full(self.cap, -1, np.int64)      # slot -> rowid
        self.dirty = np.zeros(self.cap, bool)
        self.order = OrderedDict()                          # rowid -> None (LRU; oldest first)
        self.free = list(range(self.cap))

    def _open_state(self, p):
        need = self.N * self.rb
        if not (os.path.exists(p) and os.path.getsize(p) == need):
            with open(p, "wb") as f:
                f.truncate(need)                            # sparse — no full write
        return os.open(p, os.O_RDWR)

    def _read_row(self, rowid, slot):                       # F_NOCACHE pread V,m,v → slot
        off = int(rowid) * self.rb
        self.Vb[slot] = np.frombuffer(os.pread(self.fdV, self.rb, off), np.float32)
        self.mb[slot] = np.frombuffer(os.pread(self.fdm, self.rb, off), np.float32)
        self.vb[slot] = np.frombuffer(os.pread(self.fdv, self.rb, off), np.float32)

    def _write_row(self, rowid, slot):                      # F_NOCACHE pwrite V,m,v
        off = int(rowid) * self.rb
        os.pwrite(self.fdV, self.Vb[slot].tobytes(), off)
        os.pwrite(self.fdm, self.mb[slot].tobytes(), off)
        os.pwrite(self.fdv, self.vb[slot].tobytes(), off)

    def _evict(self):                                       # LRU: pop oldest, writeback if dirty
        old, _ = self.order.popitem(last=False)
        slot = self.slot.pop(old)
        if self.dirty[slot]:
            self._write_row(old, slot); self.dirty[slot] = False
        self.row_at[slot] = -1
        return slot

    def _ensure(self, rows):                                # load rows into cache (pread misses)
        for r in rows:
            r = int(r)
            if r in self.slot:
                self.order.move_to_end(r)                   # touch (most-recently-used)
                continue
            slot = self.free.pop() if self.free else self._evict()
            self._read_row(r, slot)
            self.slot[r] = slot; self.row_at[slot] = r; self.order[r] = None

    def _slots(self, rows):
        return np.fromiter((self.slot[int(r)] for r in rows), np.int64, len(rows))

    def read_rows(self, rows):                              # forward gather (cache hits free; misses pread)
        self._ensure(rows)
        return self.Vb[self._slots(rows)].copy()

    def adam_step(self, rows, g):                           # sparse Adam on the cached (hot) rows
        if os.environ.get("MMLLM_STREAM_DEBUG"):
            with open("/tmp/adam_calls.log", "a") as _f:
                _f.write(f"adam id={id(self)} path={os.path.basename(self._dbgpath)} rows={len(rows)} mean|g|={float(np.abs(g).mean()):.3e}\n")
        if len(rows) == 0:
            return
        self.t += 1
        self._ensure(rows)
        s = self._slots(rows)
        self.mb[s] = self.b1 * self.mb[s] + (1 - self.b1) * g
        self.vb[s] = self.b2 * self.vb[s] + (1 - self.b2) * (g * g)
        mhat = self.mb[s] / (1 - self.b1 ** self.t); vhat = self.vb[s] / (1 - self.b2 ** self.t)
        self.Vb[s] = self.Vb[s] - self.lr * mhat / (np.sqrt(vhat) + self.eps)
        self.dirty[s] = True

    def flush(self):                                        # persist all dirty cached rows to disk
        # Without this the cache only reaches disk on eviction (cap full). Touched
        # rows/step (≈10²-10³) are far below cap, so eviction never fires and the
        # round's learning is lost when the next round recreates StreamV from the
        # (still-zero) file. MUST be called at each round's end. Keeps fds open.
        n = 0
        for r, slot in list(self.slot.items()):
            if self.dirty[slot]:
                self._write_row(r, slot); self.dirty[slot] = False; n += 1
        if os.environ.get("MMLLM_STREAM_DEBUG"):
            with open("/tmp/adam_calls.log", "a") as _f:
                _f.write(f"FLUSH id={id(self)} path={os.path.basename(self._dbgpath)} "
                         f"cached={len(self.slot)} flushed={n}\n")
        return n

    def close(self):                                        # flush + close fds
        self.flush()
        for fd in (self.fdV, self.fdm, self.fdv):
            try: os.close(fd)
            except OSError: pass


def stream_combine(sv: StreamV, top_global, top_scores):
    """Softmax-weighted gather of disk-resident V rows. Differentiable in top_scores
    (so PKM keys learn); V learns via the VJP scattering to disk (sparse Adam).
    top_global: mx int [B,T,K] (global row ids).  top_scores: mx [B,T,K].
    Returns weighted_latent mx [B,T,c]."""
    idx = np.asarray(top_global).astype(np.int64).reshape(-1)
    uniq, inv = np.unique(idx, return_inverse=True)        # touched rows + remap
    shape = tuple(top_global.shape)                        # (B,T,K)
    local = inv.reshape(shape)
    Vrows = mx.array(sv.read_rows(uniq))                   # [U,c] constant (disk), not in graph
    Vg = mx.take(Vrows, mx.array(local), axis=0)           # [B,T,K,c] gathered values

    @mx.custom_function
    def _combine(top_scores):
        w = mx.softmax(top_scores, axis=-1)
        return mx.einsum("btkc,btk->btc", Vg, w)

    @_combine.vjp
    def _combine_vjp(primals, cotangent, output):
        ts = primals[0] if isinstance(primals, (tuple, list)) else primals
        d_wl = cotangent[0] if isinstance(cotangent, (tuple, list)) else cotangent
        w = mx.softmax(ts, axis=-1)                        # [B,T,K]
        # grad wrt softmax weights → grad wrt top_scores (softmax jacobian)
        d_w = mx.einsum("btc,btkc->btk", d_wl, Vg)
        d_ts = w * (d_w - mx.sum(d_w * w, axis=-1, keepdims=True))
        # grad wrt the gathered V rows → accumulate per unique row → disk sparse Adam
        d_Vg = mx.einsum("btc,btk->btkc", d_wl, w)         # [B,T,K,c]
        d_flat = np.asarray(d_Vg, dtype=np.float32).reshape(-1, sv.c)
        dV_uniq = np.zeros((len(uniq), sv.c), np.float32)
        np.add.at(dV_uniq, local.reshape(-1), d_flat)      # scatter-accumulate by row
        sv.adam_step(uniq, dV_uniq)                        # pwrite update to disk V
        return (d_ts,)

    return _combine(top_scores)
