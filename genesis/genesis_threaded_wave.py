"""THREADED-BIRTHS launcher (Phase G). Runs a wave's module-births as worker
THREADS in ONE process instead of N separate bird processes — so they share the
single ~10.5GB Python/MLX/torch runtime + Metal context + allocator pool (proven
the bulk of a birth's RSS), paying only ~0.43GB private state per extra birth.
Goal: lift PAR past the 2-process memory wall (swap-thrash) toward 6-8+.

Used by genesis_composed_chain.py ONLY when MMLLM_THREADED_BIRTHS=1; default path
(N separate genesis_composed_bird.py processes) is untouched. Each thread does
EXACTLY what the per-process bird does (clone hot bank via cold-share, build cfg,
run_round, write dense.pt + bank bins) so the chain's harvest is unchanged.

Per-module config that the trainer reads from PROCESS-GLOBAL env (HOT_MODULE,
COOL_MODULES, MIX, PROBE) would race across threads — so we install a thread-local
overlay on os.environ.get/os.getenv: each worker registers its own values keyed by
thread id; everything else falls through to the real (shared, identical) env.

Env: WB_W WB_TOTAL WB_STEPS WB_ALLMODS [WB_MODULES=all] [WB_K=0] + the same WB_*/
MMLLM_* the bird reads. Threads staggered (WB_THREAD_STAGGER, default 8s) so the
basilisp build-model phase doesn't run concurrently (only the training overlaps).
"""
import os, glob, shutil, time, threading
import mlx.core as mx
mx.set_cache_limit(int(os.environ.get("MLX_CACHE_MB", "512")) << 20)
_T0 = time.monotonic()
G = os.path.expanduser("~/models/genesis")
W = int(os.environ["WB_W"]); K = int(os.environ.get("WB_K", "0"))
TOTAL = int(os.environ["WB_TOTAL"]); STEPS = int(os.environ["WB_STEPS"])
ALLMODS = os.environ["WB_ALLMODS"]
MODULES = os.environ.get("WB_MODULES", ALLMODS).split(",")  # which modules to run as threads
TAG = os.environ.get("WAVE_TAG", "cm")
CORP = {"tiny-stories":"tiny-stories-big","amps-math":"open-web-math","dolly-instruct":"cosmopedia",
        "text":"text-10g","math":"math-10g","agentic":"agentic-10g","code":"code-10g"}
RB = lambda w: f"{G}/{TAG}round{w}-bank"
RC = lambda w: f"{G}/{TAG}round{w}.ckpts"

# ── thread-local env overlay (the only reason this can't be N naive threads) ──
# Patch os.environ.get / os.getenv so a worker thread sees ITS per-module config;
# all other keys + all other threads fall through to the real shared env. The
# trainer reads the per-module keys via os.environ.get (verified: HOT_MODULE,
# MMLLM_MIX, MMLLM_PROBE, COOL_MODULES), so this catches them with no trainer edit.
_real_get = os.environ.get
_tov = {}  # thread-id -> {key: val}
def _patched_get(key, default=None):
    ov = _tov.get(threading.get_ident())
    if ov is not None and key in ov:
        return ov[key]
    return _real_get(key, default)
os.environ.get = _patched_get          # os._Environ.get is per-instance-overridable
os.getenv = lambda key, default=None: _patched_get(key, default)

# ── COMMON env (identical across all module-births), set ONCE process-global ──
# = the per-process bird's env dict MINUS the 4 per-module keys (those go per-thread).
_COLD_SHARE = _real_get("MMLLM_NET_COLD_SHARE", "").lower() in ("1", "true", "yes")
rb = RB(W-1); rbn = os.path.basename(rb)
if _COLD_SHARE:
    os.environ["MMLLM_NET_COLD_SHARE_RB_PREFIX"] = f"{rb}-net"  # same round bank for all
os.environ.update({
    "MMLLM_DEVICE":"cpu","MMLLM_NETBANK_ENABLED":"true","MMLLM_NET_MODULES":ALLMODS,
    "MMLLM_BATCH":_real_get("WB_BATCH","1"),          # MUST match the chain (WB_BATCH=1); default pick-batch=4 → 4× activation RAM
    "MMLLM_NET_SQRT_N":"256","MMLLM_NET_C_NET":"8",
    "MMLLM_NET_TOP_K":_real_get("WB_TOP_K","128"),"MMLLM_NET_SUB_TOP_K":_real_get("WB_SUB_TOP_K","16"),
    "MMLLM_NET_CACHE_ROWS":_real_get("WB_CACHE_ROWS","262144"),
    "MMLLM_MEMORY_SUB_TOP_K":_real_get("WB_MEM_SUB_TOP_K","16"),
    "MMLLM_MEMORY_TOP_K":_real_get("WB_MEM_TOP_K","16"),
    "MMLLM_NET_N_BLOCKS":_real_get("WB_N_BLOCKS","160"),"MMLLM_NET_VSTREAM":"true","MMLLM_NET_STREAM_LR":"0.003",
    "MMLLM_NET_VQ":"true","MMLLM_NET_Z_COEF":"0.1",
    "MMLLM_EVAL_BATCH":"4",
    "MMLLM_NET_DELAY_MIN":"0","MMLLM_NET_DELAY_MAX":"0","MMLLM_BANK_ON_GPU":"false","MMLLM_NET_BANK_ON_GPU":"false",
    "MMLLM_DISTILL_OBJECTIVE":_real_get("MMLLM_DISTILL_OBJECTIVE","logitkd"),"MMLLM_KD_TEMP":"2.0","MMLLM_KD_COEF":"1.0","MMLLM_KD_FREEZE":"trunk",
    "MMLLM_NET_ROUTER":"true","MMLLM_NET_ROUTER_AUX_COEF":"0.3","MMLLM_NET_ROUTER_K_LOAD":"4","MMLLM_NET_ROUTER_K_TOK":"2",
    "MMLLM_NET_ROUTER_DRIVE":"true","MMLLM_NET_ROUTER_TRAIN_DRIVE":"false",
    "MMLLM_NET_CORE_MODULES":"","MMLLM_NET_EVAL_ACTIVE":"",
    "MMLLM_LR_ROUND_BASE":str(TOTAL-STEPS),"MMLLM_MLX_MAX_STEPS":str(STEPS),
    "MMLLM_LR_DENSE_MULT":_real_get("WB_DENSE_MULT","0.03"),"MMLLM_LR_DENSE_WD":_real_get("WB_DENSE_WD","1e-4"),
    "MEMCAP_PRESSURE_KILL":"5","MMLLM_CKPT_KEEP":"2",
    "MMLLM_LR_LOCAL_MULT":_real_get("WB_LOCAL_MULT","0.05"),"MMLLM_LR_LAYER_MULTS":"2.0,1.0,0.5,1.0,2.0",
    "MMLLM_LOCAL_NOISE_FRAC":"0.5","MMLLM_LOCAL_LR_WAKE":"20.0","MMLLM_LOCAL_LR_SLEEP":"1.0",
    # Phase-G: serialize the per-thread build_model→_extract spike (deterministic,
    # replaces the unreliable RAM-gate). One build resident at a time; training overlaps.
    "MMLLM_THREADED_BUILD_LOCK":"1",
})

import basilisp.main; basilisp.main.init()
import mmllm.core as C, mmllm.mlx as mlxbk
import mmllm.mlx.trainer as _TR          # for owner-safe build-lock release on birth failure
import basilisp.lang.keyword as kw

_results = {}; _errs = {}
def worker(SPEC):
    # SPEC is "module" or "module:K" — the K suffix lets us run SEVERAL births of the
    # SAME module concurrently (distinct K → distinct scratch paths → no collision), so
    # PAR can exceed the module count (4 modules × N births = an ensemble per module,
    # FedAvg-harvested for gradient diversity). Bare "module" → the common WB_K.
    MODULE, Kv = (SPEC.split(":", 1)[0], int(SPEC.split(":", 1)[1])) if ":" in SPEC else (SPEC, K)
    try:
        pfx, ck = f"{G}/{TAG}b{W}-{MODULE}-{Kv}-bank", f"{G}/{TAG}b{W}-{MODULE}-{Kv}.ckpts"
        for p in (pfx, ck):
            for f in glob.glob(p + "*"): (shutil.rmtree if os.path.isdir(f) else os.remove)(f)
        _clone_glob = f"{rb}-net.{MODULE}.*.bin" if _COLD_SHARE else f"{rb}-net.*.bin"
        for f in glob.glob(_clone_glob):
            os.system(f"cp -c {f!r} {pfx}{os.path.basename(f)[len(rbn):]!r}")
        _steps = glob.glob(f"{RC(W-1)}/step-*")
        if not _steps:
            print(f"@@@DBG {MODULE}: RC(W-1)={RC(W-1)!r} cwd={os.getcwd()!r} W={W} G={G!r} steps={_steps}", flush=True)
            raise RuntimeError(f"no resume ckpt under {RC(W-1)}")
        latest = max(_steps, key=lambda d: int(d.split('-')[-1]))
        os.makedirs(ck, exist_ok=True); shutil.copytree(latest, f"{ck}/{os.path.basename(latest)}")
        cool = ",".join(m for m in ALLMODS.split(",") if m != MODULE)
        CORPUS = CORP[MODULE]
        _ov = {                                      # this thread's per-module config
            "MMLLM_NET_HOT_MODULE": MODULE,
            "MMLLM_NET_COOL_MODULES": cool,
            "MMLLM_MIX": f"{G}/{CORPUS}.bin.train.bin:10",
            "MMLLM_PROBE": f"{G}/{CORPUS}.bin.val.bin",
        }
        # Per-module trunk-LR (saturation-aware, from the chain's trunk_controller):
        # WB_DENSE_MULT_MAP="text:1.0,math:0.5,..." → this thread's MMLLM_LR_DENSE_MULT.
        # Keeps the threaded path recipe-faithful to the per-process spawn() (which
        # passes a per-module WB_DENSE_MULT). Absent → falls through to the common value.
        _dmap = dict(e.split(":") for e in _real_get("WB_DENSE_MULT_MAP", "").split(",") if ":" in e)
        if MODULE in _dmap:
            _ov["MMLLM_LR_DENSE_MULT"] = _dmap[MODULE]
        # Per-module steps + total (ODM re-allocates steps per module; the chain also
        # advances the global step counter per bird). Maps keep the threaded path
        # recipe-faithful to spawn() which passes per-bird WB_STEPS/WB_TOTAL. Absent →
        # fall through to the common WB_STEPS/WB_TOTAL. MMLLM_MLX_MAX_STEPS caps n_steps
        # and MMLLM_LR_ROUND_BASE positions the LR schedule (both read via env.get).
        _smap = dict(e.split(":") for e in _real_get("WB_STEPS_MAP", "").split(",") if ":" in e)
        _ttmap = dict(e.split(":") for e in _real_get("WB_TOTAL_MAP", "").split(",") if ":" in e)
        _steps_m = int(_smap.get(MODULE, STEPS))
        _total_m = int(_ttmap.get(MODULE, TOTAL))
        _ov["MMLLM_MLX_MAX_STEPS"] = str(_steps_m)
        _ov["MMLLM_LR_ROUND_BASE"] = str(_total_m - _steps_m)
        _tov[threading.get_ident()] = _ov
        cfg = C.default_config_cpu_mini.assoc(kw.keyword("memory-mmap-path"), pfx)
        if _real_get("WB_SEQ_LEN"): cfg = cfg.assoc(kw.keyword("seq-len"), int(os.environ["WB_SEQ_LEN"]))
        if _real_get("WB_D_MODEL"): cfg = cfg.assoc(kw.keyword("d-model"), int(os.environ["WB_D_MODEL"]))
        if _real_get("WB_D_FF"):    cfg = cfg.assoc(kw.keyword("d-ff"), int(os.environ["WB_D_FF"]))
        base = f"{G}/{CORPUS}.bin"
        _EVAL_EVERY = int(_real_get("MMLLM_EVAL_EVERY", "50"))
        r = mlxbk.run_round(cfg, f"{base}.train.bin", f"{base}.val.bin", ck,
                            f"{G}/{TAG}b{W}-{MODULE}-{Kv}.log.jsonl", _total_m, _EVAL_EVERY, 1000000)
        _results[SPEC] = r.get('ctrl_bpc')
        print(f"@@@BIRD w{W} {MODULE}.k{Kv}: composed_bpc={r.get('ctrl_bpc'):.4f} (threaded)", flush=True)
    except Exception as e:
        # If this birth died DURING its build (lock held), release it from THIS
        # (owning) thread so siblings queued on the build lock don't deadlock.
        _TR._release_build_lock_if_held()
        import traceback; _errs[SPEC] = repr(e)
        print(f"@@@BIRD-ERR w{W} {SPEC}: {e}\n{traceback.format_exc()}", flush=True)

import subprocess, re as _re
# Memory guard uses macOS's OWN pressure accounting, NOT raw "free RAM". Cold-share
# mmaps ~8GB of readonly V bins that page in during the netbank forward; those are
# CLEAN, RECLAIMABLE file-cache pages, but raw free(=free+inactive+speculative) reads
# the trough as exhaustion and false-aborts (the per-process chain tolerates the
# identical trough because it has no such gate). kern.memorystatus_level (% available,
# counts reclaimable cache) + kern.memorystatus_vm_pressure_level (1=normal,2=warn,
# 4=critical) are what the kernel itself uses to decide real pressure → gate on those.
def _sysctl_int(name, default):
    try: return int(subprocess.run(["sysctl","-n",name], capture_output=True, text=True).stdout.strip())
    except Exception: return default
def _mem_level():       return _sysctl_int("kern.memorystatus_level", 100)          # % available (reclaim-aware)
def _pressure():        return _sysctl_int("kern.memorystatus_vm_pressure_level", 1)  # 1/2/4
def _free_gb():
    try:
        out = subprocess.run(["vm_stat"], capture_output=True, text=True).stdout
        def g(p):
            m = _re.search(p + r":\s+(\d+)", out); return int(m.group(1)) * 4096 if m else 0
        return (g("Pages free") + g("Pages inactive") + g("Pages speculative")) / 1073741824
    except Exception:
        return 99.0
# Hard safety: abort only on GENUINE pressure (kernel critical, or available% below a
# low floor) — the real box-hang guard — not on reclaimable file-cache troughs.
_FLOOR_PCT = float(_real_get("WB_MEM_FLOOR_PCT", "6"))   # abort if memorystatus_level% < this
_GATE_PCT  = float(_real_get("WB_MEM_GATE_PCT", "15"))   # hold next thread start until level% clears this
_STAGGER   = float(_real_get("WB_THREAD_STAGGER", "2"))  # spacing between starts (build lock orders the builds)
_abort = threading.Event()
def _poller():
    while not _abort.wait(3):
        lvl, pr = _mem_level(), _pressure()
        if pr >= 4 or lvl < _FLOOR_PCT:
            print(f"@@@ABORT mem pressure: level={lvl}% (floor {_FLOOR_PCT}%) pressure={pr} "
                  f"raw_free={_free_gb():.1f}GB — killing threaded-wave", flush=True)
            os._exit(137)
threading.Thread(target=_poller, daemon=True).start()

# Build serialization is now DETERMINISTIC via the trainer's _BUILD_LOCK (set by
# MMLLM_THREADED_BUILD_LOCK above): every thread starts, races for the build lock,
# and only ONE build_model→_extract is resident at a time; training overlaps freely.
# So we just stagger the starts for clean ordering, with a light RAM-backpressure
# valve so accumulating TRAINING residents can't pile past the floor before the
# poller trips. The lock — not this gate — prevents the build spike.
threads = []
for i, SPEC in enumerate(MODULES):
    if i > 0:
        time.sleep(_STAGGER)
        _t0 = time.monotonic()
        while _mem_level() < _GATE_PCT and time.monotonic() - _t0 < 300 and not _abort.is_set():
            time.sleep(3)
    t = threading.Thread(target=worker, args=(SPEC,), name=f"birth-{SPEC}")
    t.start(); threads.append(t)
    print(f"  [threaded-wave] +{SPEC} ({i+1}/{len(MODULES)} live, level={_mem_level()}% free={_free_gb():.1f}GB)", flush=True)
for t in threads: t.join()
_abort.set()
print(f"@@@THREADED-WAVE w{W} done in {time.monotonic()-_T0:.0f}s: ok={list(_results)} err={list(_errs)}", flush=True)
if _errs: raise SystemExit(1)
