"""Disk-streaming NetBank V for the 10GB+ path.

V (and its Adam state) live on disk, never resident. `stream_combine` is an
mx.custom_function: forward preads the touched rows and does the softmax-weighted
combine; its VJP returns d(top_scores) so the PKM keys still learn, and scatters the
V-row gradient to disk via a sparse Adam step (pwrite) as a side-effect. Single-pass —
no trainer two-pass needed. I/O follows ds4 (ds4-cold-expert-streaming-pread memory):
explicit pread/pwrite with F_NOCACHE to bypass the page cache (avoids the wired/
compressor thrash that file-mmap caused).
"""
import os, numpy as np, mmap as _mmap
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

    def __init__(self, path, N, c, lr, cap=None, b1=0.9, b2=0.999, eps=1e-8, readonly=False,
                 versioning=None):
        self.N, self.c, self.rb = int(N), int(c), int(c) * 4
        self.lr, self.b1, self.b2, self.eps, self.t = float(lr), b1, b2, eps, 0
        self.cap = int(cap or int(os.environ.get("MMLLM_NET_CACHE_ROWS", "65536")))
        self._dbgpath = path
        self.readonly = bool(readonly)
        # PHASE D: copy-path-on-write versioning. Default OFF (env unset) → every
        # branch below takes the original in-place pwrite path (byte-identical). When
        # ON, writes never mutate the base V file: touched rows are APPENDED to a
        # per-version overlay (.ver) and published via an atomic root index (.vidx);
        # the base inode stays immutable within a round → cold readers sharing it are
        # corruption-safe. Cold-share readonly handles are never versioned writers.
        if versioning is None:
            versioning = os.environ.get("MMLLM_NET_VERSIONING", "").lower() in ("1", "true", "yes")
        self.versioning = bool(versioning) and not self.readonly
        if self.readonly:
            # COLD-SHARE: a FROZEN cold module read by every PAR bird. We want the cache
            # SHARED across births (one copy, not per-bird) AND BOUNDED (it can't balloon
            # the box). So: mmap MAP_SHARED|PROT_READ → all births read ONE OS page-cache
            # copy of the bank; then a touched-PAGE LRU madvise(MADV_DONTNEED)s pages that
            # fall out of it, so the resident set stays ≈ the trie's HOT working set. The
            # trie is hierarchical (eve): every birth's queries converge on the same hot
            # nodes + a small leaf set, so the UNION of all births' signal is still small
            # → the shared cache stays bounded even as births scale. The old mmap had no
            # such bound and thrashed; per-bird pread bounded but UN-shared. This is both.
            self.fdm = self.fdv = None
            self.fdV = os.open(path, os.O_RDONLY)
            _len = self.N * self.rb
            self._mm = _mmap.mmap(self.fdV, _len, _mmap.MAP_SHARED, _mmap.PROT_READ)
            try: self._mm.madvise(_mmap.MADV_RANDOM)             # bank access is trie-scattered, not sequential
            except (AttributeError, OSError): pass
            self._buf = np.frombuffer(self._mm, np.float32, self.N * self.c).reshape(self.N, self.c)
            self._PS = _mmap.PAGESIZE
            self._rpp = max(1, self._PS // self.rb)              # rows per page
            _cap_rows = int(os.environ.get("MMLLM_NET_COLD_CACHE_ROWS", "65536"))
            self._cap_pages = max(8, _cap_rows // self._rpp)     # resident pages cap (shared working set)
            self._pages = OrderedDict()                          # page_idx -> None (LRU; oldest first)
            return
        self._mm = None
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
        if self.versioning:
            self._ver_init(path)

    # ───────────────────────── PHASE D versioning ─────────────────────────
    def _ver_init(self, path):
        """Set up the append-only overlay store + version index. Resumes from a
        prior .vidx if present (module-growth-safe: missing → fresh empty chain)."""
        self._ver_path = path + ".ver"          # append-only fp32 overlay rows
        self._vidx_path = path + ".vidx"        # version index (atomic root)
        self.overlays = []                       # [ {rowid -> ver_slot} ] newest last
        self._work = {}                          # uncommitted (this-round) rowid -> ver_slot
        self._ver_size = 0                       # bytes used in .ver
        self._ver_keep = max(1, int(os.environ.get(
            "MMLLM_NET_VERSION_KEEP", os.environ.get("MMLLM_CKPT_KEEP", "2"))))
        if os.path.exists(self._vidx_path):
            try:
                import json
                with open(self._vidx_path) as f:
                    meta = json.load(f)
                self.overlays = [{int(k): int(v) for k, v in ov.items()}
                                 for ov in meta.get("overlays", [])]
                self._ver_size = int(meta.get("ver_size", 0)) * self.rb
            except Exception:
                self.overlays = []; self._ver_size = 0
        self.fd_ver = os.open(self._ver_path, os.O_RDWR | os.O_CREAT, 0o644)
        if os.path.getsize(self._ver_path) < self._ver_size:
            os.ftruncate(self.fd_ver, self._ver_size)      # heal a truncated overlay file
        if fcntl is not None and _F_NOCACHE is not None:
            try: fcntl.fcntl(self.fd_ver, _F_NOCACHE, 1)
            except OSError: pass

    def _ver_src(self, rowid):                              # newest .ver slot holding rowid, or None (→ base)
        rowid = int(rowid)
        if rowid in self._work:
            return self._work[rowid]
        for ov in reversed(self.overlays):                  # newest version wins
            if rowid in ov:
                return ov[rowid]
        return None

    def _open_state(self, p):
        need = self.N * self.rb
        if not (os.path.exists(p) and os.path.getsize(p) == need):
            with open(p, "wb") as f:
                f.truncate(need)                            # sparse — no full write
        return os.open(p, os.O_RDWR)

    def _read_row(self, rowid, slot):                       # F_NOCACHE pread V,m,v → slot
        off = int(rowid) * self.rb
        if self.versioning:                                 # V from newest overlay slot, else immutable base
            vs = self._ver_src(rowid)
            if vs is not None:
                self.Vb[slot] = np.frombuffer(os.pread(self.fd_ver, self.rb, vs * self.rb), np.float32)
            else:
                self.Vb[slot] = np.frombuffer(os.pread(self.fdV, self.rb, off), np.float32)
        else:
            self.Vb[slot] = np.frombuffer(os.pread(self.fdV, self.rb, off), np.float32)
        self.mb[slot] = np.frombuffer(os.pread(self.fdm, self.rb, off), np.float32)   # Adam state stays writer-private/in-place
        self.vb[slot] = np.frombuffer(os.pread(self.fdv, self.rb, off), np.float32)

    def _write_row(self, rowid, slot):                      # F_NOCACHE pwrite V,m,v
        off = int(rowid) * self.rb
        if self.versioning:                                 # COW: append the new V row to .ver; base untouched (immutable)
            os.pwrite(self.fd_ver, self.Vb[slot].tobytes(), self._ver_size)
            self._work[int(rowid)] = self._ver_size // self.rb
            self._ver_size += self.rb
        else:
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
        if self.readonly:                                  # cold-share: gather from the SHARED mmap, then bound its page cache
            ri = np.asarray(rows, np.int64)
            out = np.asarray(self._buf[ri], dtype=np.float32)   # faults the touched (hot) pages into the shared page cache
            self._bound_pages(ri)
            return out
        self._ensure(rows)
        return self.Vb[self._slots(rows)].copy()

    def _bound_pages(self, rows):                           # touched-page LRU → madvise(DONTNEED) cold pages out of the SHARED cache
        P = self._pages; PS = self._PS
        for pg in np.unique((rows * self.rb) // PS):        # pages these rows live on → mark most-recently-used
            pg = int(pg); P.pop(pg, None); P[pg] = None
        while len(P) > self._cap_pages:                     # over the bound → drop the coldest pages (re-fault if touched again)
            old, _ = P.popitem(last=False)
            try: self._mm.madvise(_mmap.MADV_DONTNEED, old * PS, PS)
            except (OSError, ValueError): pass

    def adam_step(self, rows, g):                           # sparse Adam on the cached (hot) rows
        if self.readonly:                                  # cold-share: frozen module, never updated
            return
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
        if self.readonly:                                  # cold-share: nothing to persist (read-only)
            return 0
        # Without this the cache only reaches disk on eviction (cap full). Touched
        # rows/step (≈10²-10³) are far below cap, so eviction never fires and the
        # round's learning is lost when the next round recreates StreamV from the
        # (still-zero) file. MUST be called at each round's end. Keeps fds open.
        n = 0
        for r, slot in list(self.slot.items()):
            if self.dirty[slot]:
                self._write_row(r, slot); self.dirty[slot] = False; n += 1
        if self.versioning:                                 # seal this round's touched rows into a new immutable version
            self._seal()
        if os.environ.get("MMLLM_STREAM_DEBUG"):
            with open("/tmp/adam_calls.log", "a") as _f:
                _f.write(f"FLUSH id={id(self)} path={os.path.basename(self._dbgpath)} "
                         f"cached={len(self.slot)} flushed={n}\n")
        return n

    def close(self):                                        # flush + close fds
        if self.readonly:                                  # cold-share: release the shared mmap + read fd (no flush)
            self._buf = None
            try: self._mm.close()
            except Exception: pass
            try: os.close(self.fdV)
            except (OSError, TypeError, AttributeError): pass
            self._mm = None
            return
        self.flush()
        fds = [self.fdV, self.fdm, self.fdv]
        if self.versioning:
            fds.append(self.fd_ver)
        for fd in fds:
            try: os.close(fd)
            except OSError: pass

    # ───────────────────────── PHASE D version ops ─────────────────────────
    def _seal(self):
        """Publish this round's _work overlay as a new immutable version, atomically
        advancing the root. No-op if no rows changed (head unchanged)."""
        if self._work:
            self.overlays.append(dict(self._work))
            self._work = {}
            self._gc()                                      # bound retained versions
        self._persist_vidx()                                # atomic root index update

    def _gc(self):
        """Version-store growth GC: keep at most _ver_keep sealed versions. Oldest
        beyond the cap are FOLDED FORWARD into the next-kept version (newest value per
        row preserved) — the base inode is NEVER mutated here, so concurrent base
        readers stay safe. Then compact .ver to only still-referenced slots."""
        squashed = False
        while len(self.overlays) > self._ver_keep:
            old = self.overlays.pop(0)
            nxt = self.overlays[0]                          # new oldest kept (strictly newer than `old`)
            for rowid, vs in old.items():
                if rowid not in nxt:                        # nxt is newer → it already wins where present
                    nxt[rowid] = vs
            squashed = True
        if squashed:
            self._compact_ver()

    def _compact_ver(self):
        """Rewrite .ver to hold only slots referenced by live overlays/_work, remap
        the indices. Bounds overlay-file growth (drops dead/overridden rows)."""
        live = sorted({vs for ov in self.overlays for vs in ov.values()} | set(self._work.values()))
        if not live:
            self._ver_size = 0
            try: os.ftruncate(self.fd_ver, 0)
            except OSError: pass
            return
        remap = {old: i for i, old in enumerate(live)}
        buf = bytearray()
        for old in live:
            buf += os.pread(self.fd_ver, self.rb, old * self.rb)
        os.ftruncate(self.fd_ver, 0)
        os.pwrite(self.fd_ver, bytes(buf), 0)
        self._ver_size = len(buf)
        for ov in self.overlays:
            for k in list(ov.keys()):
                ov[k] = remap[ov[k]]
        for k in list(self._work.keys()):
            self._work[k] = remap[self._work[k]]

    def _persist_vidx(self):
        """Atomically publish the version index (the root). os.replace is atomic on
        POSIX → a reader either sees the old root or the new one, never a torn one."""
        import json, tempfile
        meta = {"head": len(self.overlays) - 1, "ver_size": self._ver_size // self.rb,
                "overlays": [{str(k): int(v) for k, v in ov.items()} for ov in self.overlays]}
        d = os.path.dirname(self._vidx_path) or "."
        fd, tmp = tempfile.mkstemp(dir=d, prefix=".vidx.")
        try:
            with os.fdopen(fd, "w") as f:
                json.dump(meta, f)
            os.replace(tmp, self._vidx_path)
        except Exception:
            try: os.unlink(tmp)
            except OSError: pass

    def version_delta(self):
        """Harvest hook: {rowid -> np.float32[c]} of rows changed vs the base snapshot
        (union of sealed overlays + uncommitted _work, newest value per row). Sparse —
        size == touched rows, not N → fixes the dense-delta degeneracy."""
        if not self.versioning:
            return {}
        src = {}
        for ov in self.overlays:
            src.update(ov)
        src.update(self._work)
        out = {}
        for rowid, vs in src.items():
            out[int(rowid)] = np.frombuffer(os.pread(self.fd_ver, self.rb, vs * self.rb), np.float32).copy()
        return out

    def materialize(self, target=None):
        """Publish the head version: write every touched row into the base V file so
        the existing harvest path (which reads the .bin) sees the latest snapshot, then
        reset the .ver scratch (base == head). Call at ROUND END, after the concurrent
        cold-read window — this is the only sanctioned base mutation."""
        if self.readonly or not self.versioning:
            return 0
        fd = self.fdV if target is None else os.open(target, os.O_RDWR | os.O_CREAT, 0o644)
        touched = {}
        for ov in self.overlays:
            touched.update(ov)
        touched.update(self._work)
        n = 0
        for rowid, vs in touched.items():
            os.pwrite(fd, os.pread(self.fd_ver, self.rb, vs * self.rb), int(rowid) * self.rb)
            n += 1
        if target is not None:
            os.close(fd)
        else:                                               # base is now the published snapshot → reset scratch
            self.overlays = []; self._work = {}; self._ver_size = 0
            try: os.ftruncate(self.fd_ver, 0)
            except OSError: pass
            self._persist_vidx()
        return n


def merge_version_deltas(base_path, N, c, deltas, reduce="mean"):
    """Harvest-as-version-delta-merge primitive. Given a base [N,c] snapshot and a
    list of per-bird version deltas (each {rowid -> vec} from StreamV.version_delta),
    combine ONLY the touched rows (structural sharing: untouched rows keep base). FedAvg
    semantics — 'mean' averages over the birds that touched each row, 'last' overwrites.
    Returns (merged [N,c] ndarray, sorted touched-row list)."""
    if os.path.exists(base_path):
        base = np.fromfile(base_path, np.float32, count=N * c).reshape(N, c).copy()
    else:
        base = np.zeros((N, c), np.float32)
    acc, cnt = {}, {}
    for d in deltas:
        for rowid, vec in d.items():
            rowid = int(rowid)
            acc[rowid] = acc.get(rowid, 0.0) + np.asarray(vec, np.float32)
            cnt[rowid] = cnt.get(rowid, 0) + 1
    touched = sorted(acc)
    for rowid in touched:
        base[rowid] = acc[rowid] / cnt[rowid] if reduce == "mean" else acc[rowid]
    return base, touched


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


def stream_node_read(sv: StreamV, rows, carrier):
    """Gather disk-resident node rows (trie C/A) by id; the gathered VALUES are
    differentiable — their gradient is scattered back to disk via sparse Adam, so the
    STREAMED trie nodes learn exactly like dense params. `rows`: int ids (any shape).
    `carrier`: a differentiable value already in the graph (the residual r) passed ONLY
    so MLX descends into this op's VJP (an int-id-only op has no differentiable input to
    backprop through). The forward ignores carrier; the VJP receives the gathered output's
    cotangent (the real value-gradient), scatter-accumulates it per unique node row, and
    pwrites the Adam update to disk. Returns mx float `rows.shape + (c,)`."""
    idx = np.asarray(rows).astype(np.int64).reshape(-1)
    uniq, inv = np.unique(idx, return_inverse=True)            # touched node rows + remap
    shape = tuple(rows.shape)
    local = inv.reshape(shape)
    Vrows = mx.array(sv.read_rows(uniq))                       # [U,c] disk read (bounded LRU), constant
    _localmx = mx.array(local)

    @mx.custom_function
    def _gather(carrier_in):                                  # carrier_in keeps the op in the graph
        return mx.take(Vrows, _localmx, axis=0)               # output = the gather (independent of carrier)

    @_gather.vjp
    def _gather_vjp(primals, cotangent, output):
        d_out = cotangent[0] if isinstance(cotangent, (tuple, list)) else cotangent
        d_flat = np.asarray(d_out, dtype=np.float32).reshape(-1, sv.c)
        d_uniq = np.zeros((len(uniq), sv.c), np.float32)
        np.add.at(d_uniq, local.reshape(-1), d_flat)          # accumulate grad per unique node row
        sv.adam_step(uniq, d_uniq)                            # pwrite Adam update to disk
        cin = primals[0] if isinstance(primals, (tuple, list)) else primals
        return (mx.zeros_like(cin),)                          # carrier gets no gradient

    return _gather(carrier)
