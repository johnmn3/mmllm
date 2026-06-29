"""Composed-regime depth-push, old-4/new-4 double-buffer, PAR=4 at B=1.

Each round: 4 composed births (one HOT module each) train against the frozen-COLD
old-4 modules, with a SLOW-EVOLVING trunk + a LEARNING router — router driving,
train==inference. Harvest = per-module V UNION + trunk/router FedAvg'd across the 4
births (the trunk drifts slowly + sheds module-absorbed skills; the router learns
per-corpus routing, breaking the frozen-m4 code-monopoly). A drift monitor + composed
retention probe guard the trunk. Births report composed_bpc (router-routed, all-4).

Memory: composed B=1 bird ≈ 4.15GB → PAR=4 ≈ 16.6GB (fits 32GB w/ 12GB spare).
"""
import os, glob, shutil, time, re
import numpy as np, torch
# ── ALWAYS start the widget when this chain starts (engineered in — cannot launch
# the run without it). Idempotent, absolute pgrep, detached, explicit PATH. ──
import subprocess as _sp
def _ensure_widget():
    try:
        if _sp.run(["/usr/bin/pgrep", "-f", "train_widget.py"], capture_output=True).returncode != 0:
            _sp.Popen(["/Users/john/src/mmllm/.venv/bin/python3", "/Users/john/train_widget.py"],
                      stdout=_sp.DEVNULL, stderr=_sp.DEVNULL, start_new_session=True,
                      env={**os.environ, "PATH": "/usr/bin:/bin:" + os.environ.get("PATH", "")})
            print("@@@ widget launched", flush=True)
        else:
            print("@@@ widget already up", flush=True)
    except Exception as _e:
        print(f"@@@ widget launch failed: {_e}", flush=True)
_ensure_widget()
G = os.path.expanduser("~/models/genesis")
MODS  = os.environ.get("WAVE_MODULES", "tiny-stories,amps-math,dolly-instruct,code").split(",")
WAVES = int(os.environ.get("WAVE_N", "10"))
STEPS = int(os.environ.get("WAVE_STEPS", "1000"))
PAR   = int(os.environ.get("WAVE_PAR", "4"))
# Phase-G threaded births: run a wave's births as THREADS in ONE process (shared
# runtime + shared cold-share cache) instead of N bird processes. Default off →
# the per-process path is byte-unchanged. Validated: 16 concurrent births on a 32GB
# box stayed at healthy mem pressure (genesis_threaded_wave.py + trainer _BUILD_LOCK).
THREADED = os.environ.get("MMLLM_THREADED_BIRTHS", "").lower() in ("1", "true", "yes")
STAG  = int(os.environ.get("WAVE_STAGGER", "25"))
REPORT= int(os.environ.get("WAVE_REPORT", "20"))
TAG   = os.environ.get("WAVE_TAG", "cm")
SEED  = os.environ.get("WAVE_SEED", "m4")
NLAYERS = 32
PY = "/Users/john/src/mmllm/.venv/bin/python3"; SRC = f"{G}/mmllm-src"  # stable; NEVER /tmp (purged 2026-06-27, ate mmllm core.lpy)
RB = lambda w: f"{G}/{TAG}round{w}-bank"
RC = lambda w: f"{G}/{TAG}round{w}.ckpts"
ALLMODS = ",".join(MODS)

# ── ADAPTIVE TRUNK-LR CONTROLLER (per-module, saturation-aware) ────────
# John's spec: don't blindly anneal — DETECT when the trunk will take no more of a
# given module's signal, then REDIRECT that signal into the bank by cooling THAT
# module's bird trunk-LR. Signal = the net-ABLATED bpc (trunk+local only, banks off),
# printed by every bird as "ablated_bpc=…". If the trunk keeps DRIFTING (harvest
# Δtrunk>floor) but a module's ablated bpc stops improving, the trunk is saturated
# for that signal → cool its LR. trunk-LR is PER-MODULE because each module trains in
# its own bird process; the harvest FedAvg then lets only still-unsaturated modules
# nudge the shared trunk. Reversible: if a cooled module's ablated bpc REGRESSES, the
# trunk re-engages (re-warm). State persists to JSON so widget stop/start is seamless.
import json
from collections import deque
# RETUNED (cg5 post-mortem): the per-wave detector was DORMANT — 1 cool in 34 waves —
# because per-module ablated_bpc is noisy + NON-MONOTONIC (the trunk is FedAvg'd across
# all 4 birds each wave, so one module's trunk-only bpc bounces ±0.005-0.015), which
# swamped SAT_EPS=0.003 and the "2 consecutive sat waves" rule never held. Fixes:
#   (1) SMOOTH over a WINDOW of waves before thresholding (not per-wave),
#   (2) threshold ABOVE the noise floor,
#   (3) a LATE-training anneal floor so a deep domain that never quite saturates
#       (e.g. code, still −0.013 bpc/wave at w32) still consolidates into its bank.
INIT_MULT   = float(os.environ.get("WB_DENSE_MULT", "0.02"))                 # warm start
WINDOW      = int(os.environ.get("WAVE_SAT_WINDOW", "4"))                     # waves of ablated-bpc history to smooth over
SAT_EPS     = float(os.environ.get("WAVE_SAT_EPS", "0.01"))                  # min SMOOTHED improvement over the window = "trunk still learning" (above noise floor)
DRIFT_FLOOR = float(os.environ.get("WAVE_DRIFT_FLOOR", "1e-4"))              # trunk must have actually MOVED to call it saturated
COOL        = float(os.environ.get("WAVE_TRUNK_COOL", "0.5"))               # ×LR when saturated
WARM        = float(os.environ.get("WAVE_TRUNK_WARM", "1.6"))               # ×LR when regressing (re-engage)
MIN_MULT    = INIT_MULT * float(os.environ.get("WAVE_TRUNK_MINFRAC", "0.05"))# near-frozen floor (kept >0 so it's reversible)
LATE_FRAC   = float(os.environ.get("WAVE_LATE_FRAC", "0.7"))                 # past this fraction of the run, the trunk anneals every wave...
LATE_DECAY  = float(os.environ.get("WAVE_LATE_DECAY", "0.85"))              # ...×LR/wave regardless of saturation → forces bank consolidation by run end
# ── WAKE/SLEEP trunk cycle ──────────────────────────────────────────────────
# Instead of monotonically annealing the trunk to a floor (which dead-ends at ONE
# trunk/bank equilibrium), OSCILLATE it: a WARM (wake) phase lets the trunk re-absorb
# the general patterns the banks have consolidated (freeing bank capacity), then a
# COOL (sleep) phase lets the banks re-absorb specifics into that freed capacity
# (Δ_net rises). Each cycle should ratchet BOTH down past the single-equilibrium
# plateau. PERIOD=0 ⇒ disabled (fall back to the monotonic saturation/anneal mode).
CYCLE_PERIOD = int(os.environ.get("WAVE_TRUNK_CYCLE_PERIOD", "0"))            # waves per wake+sleep cycle; 0 = off
CYCLE_WARM   = int(os.environ.get("WAVE_TRUNK_CYCLE_WARM", "3"))             # WAKE (warm) waves at the start of each cycle
CYCLE_WMULT  = float(os.environ.get("WAVE_TRUNK_CYCLE_WARM_MULT", "0.5"))    # WAKE peak trunk-LR (ramp climbs floor→peak)
CYCLE_CMULT  = float(os.environ.get("WAVE_TRUNK_CYCLE_COOL_MULT", "0.05"))   # SLEEP floor trunk-LR (cool-down decays peak→floor)
CYCLE_CDECAY = float(os.environ.get("WAVE_TRUNK_CYCLE_COOL_DECAY", "0.6"))   # ×LR per SLEEP wave (the productive cool-down transit)
# JITTER: dither each ramp LR by ±JITTER (multiplicative) so cycles sample BANDS around
# the nominal shape, not 8 fixed points → dense productivity-vs-LR scatter to dial in the
# optimal shape over many cycles/runs. Seeded by (SALT, wave): resume-stable within a run,
# bump SALT for fresh bands next run. 0 = off (deterministic ramp).
CYCLE_JITTER = float(os.environ.get("WAVE_TRUNK_CYCLE_JITTER", "0"))
JITTER_SALT  = int(os.environ.get("WAVE_JITTER_SALT", "0"))                   # per-RUN seed offset (vary across runs to accumulate bands)
# STRUCTURAL SWEEP (instrument #2): draw a fresh cycle SHAPE each cycle — period /
# warm-length / crest / cool-decay — from ranges, seeded by (SALT, cycle-start) so it's
# resume-stable and fresh across runs. Regress net-ratchet vs shape → best CREST,
# WAVELENGTH, SLOPES. 0 = off → use the fixed CYCLE_* shape above (current behavior). Live-tunable.
SWEEP        = int(os.environ.get("WAVE_TRUNK_SWEEP", "0"))
SWEEP_PMIN   = int(os.environ.get("WAVE_SWEEP_PERIOD_MIN", "6"));     SWEEP_PMAX = int(os.environ.get("WAVE_SWEEP_PERIOD_MAX", "12"))
SWEEP_WMIN   = int(os.environ.get("WAVE_SWEEP_WARM_MIN", "2"));       SWEEP_WMAX = int(os.environ.get("WAVE_SWEEP_WARM_MAX", "4"))
SWEEP_CMIN   = float(os.environ.get("WAVE_SWEEP_CREST_MIN", "0.30")); SWEEP_CMAX = float(os.environ.get("WAVE_SWEEP_CREST_MAX", "0.80"))
SWEEP_DMIN   = float(os.environ.get("WAVE_SWEEP_DECAY_MIN", "0.50")); SWEEP_DMAX = float(os.environ.get("WAVE_SWEEP_DECAY_MAX", "0.75"))
_cycle_state = [None]                                                         # CURRENT cycle's drawn shape: {start, P, WN, peak, cdecay}
CTRL_PATH   = f"{G}/{TAG}_trunk_ctrl.json"
trunk_mult  = {m: INIT_MULT for m in MODS}
_ab_hist    = {m: deque(maxlen=WINDOW) for m in MODS}   # recent ablated_bpc per module (smoothing window)

# ── ONLINE DATA MIXING (ODM) — EXP3 bandit over per-module composed_bpc ─────────
# ADDITIVE, default-off. WAVE_ODM=0 ⇒ equal weighting (byte-identical to prior behavior).
# When on: each wave, reward the WORST (highest composed_bpc) modules with MORE training
# steps next wave (they need it most), via an EXP3 adversarial-bandit weight update. The
# returned per-module step multiplier is mean-normalized to 1.0 so TOTAL compute is neutral
# — we only RE-ALLOCATE the fixed step budget across modules, never inflate it.
WAVE_ODM   = int(os.environ.get("WAVE_ODM", "0"))            # 0 = current equal weighting
ODM_GAMMA  = float(os.environ.get("WAVE_ODM_GAMMA", "0.1"))
ODM_ETA    = float(os.environ.get("WAVE_ODM_ETA", "0.3"))
ODM_MIN    = float(os.environ.get("WAVE_ODM_MIN_FRAC", "0.3"))
ODM_MAX    = float(os.environ.get("WAVE_ODM_MAX_FRAC", "2.0"))
odm_w      = {m: 1.0 for m in MODS}
odm_prev   = {m: None for m in MODS}
ODM_PATH   = f"{G}/{TAG}_odm.json"

def odm_update(bpc_by_mod):
    """EXP3 bandit step. Reward = rank-normalized composed_bpc (worst module → 1.0).
    Returns a per-module step multiplier (mean-normalized to 1.0 = compute-neutral)."""
    n = len(MODS)
    Z = sum(odm_w[m] for m in MODS) or float(n)
    p = {m: (1.0 - ODM_GAMMA) * odm_w[m] / Z + ODM_GAMMA / n for m in MODS}
    # rank-normalize current bpc so worst (highest bpc) → reward 1, best → reward 0
    have = {m: bpc_by_mod.get(m) for m in MODS if bpc_by_mod.get(m) is not None}
    r = {m: 0.0 for m in MODS}
    if have:
        order = sorted(have, key=lambda m: have[m])           # ascending bpc (best→worst)
        denom = max(1, len(order) - 1)
        for rank, m in enumerate(order):
            r[m] = rank / denom                               # worst (last) → 1.0
    for m in MODS:
        odm_prev[m] = bpc_by_mod.get(m)
        odm_w[m] *= float(np.exp(ODM_ETA * ODM_GAMMA * (r[m] / p[m]) / n))
    # renormalize weights so Σ = n (keeps them bounded across waves)
    Zw = sum(odm_w[m] for m in MODS) or float(n)
    for m in MODS:
        odm_w[m] = odm_w[m] * n / Zw
    mult = {m: min(ODM_MAX, max(ODM_MIN, odm_w[m])) for m in MODS}
    mean = (sum(mult.values()) / n) or 1.0
    return {m: mult[m] / mean for m in MODS}                  # mean-normalized → compute-neutral

def _save_odm():
    try: json.dump({"odm_w": odm_w, "odm_prev": odm_prev}, open(ODM_PATH, "w"))
    except Exception: pass

def _load_odm():
    try:
        s = json.load(open(ODM_PATH))
        odm_w.update({k: float(v) for k, v in s.get("odm_w", {}).items() if k in odm_w})
        odm_prev.update({k: v for k, v in s.get("odm_prev", {}).items() if k in odm_prev})
        print(f"@@@ODM resumed weights: { {m: round(odm_w[m],3) for m in MODS} }", flush=True)
    except Exception:
        pass

def _load_ctrl():
    try:
        s = json.load(open(CTRL_PATH))
        trunk_mult.update({k: float(v) for k, v in s.get("trunk_mult", {}).items() if k in trunk_mult})
        for k, v in s.get("ab_hist", {}).items():
            if k in _ab_hist: _ab_hist[k] = deque(v[-WINDOW:], maxlen=WINDOW)
        if s.get("cycle_state") is not None: _cycle_state[0] = s["cycle_state"]  # preserve wake/sleep cycle shape+phase across restart
        print(f"@@@CTRL resumed trunk-LR: { {m: round(trunk_mult[m],5) for m in MODS} } cycle={_cycle_state[0]}", flush=True)
    except Exception:
        pass

def _save_ctrl():
    try: json.dump({"trunk_mult": trunk_mult, "ab_hist": {m: list(_ab_hist[m]) for m in MODS}, "cycle_state": _cycle_state[0]}, open(CTRL_PATH, "w"))
    except Exception: pass

# ── MID-RUN live config: re-read {TAG}_live.json at every wave boundary so knobs can
# be tweaked WITHOUT a stop/restart. Edit the json; the NEXT wave picks it up.
#   • controller knobs  → reassign the module globals (cool/warm/anneal/saturation)
#   • WAVE_STEPS         → steps-per-wave from the next wave on
#   • trunk_mult         → directly override the per-module trunk-LR (manual cool/warm)
#   • any other WB_*/MMLLM_* → passed through to the bird env (lr/wd/batch/eval/topk…)
#   • SHAPE-LOCKED knobs are REFUSED (would corrupt the already-sized banks/trunk).
LIVE_PATH = f"{G}/{TAG}_live.json"
LIVE_ENV  = {}                                  # safe bird-env passthrough, merged in spawn()
_LIVE_FORBIDDEN = {"WB_N_BLOCKS","WB_SQRT_N","WB_C_NET","WB_D_MODEL","WB_D_FF","WAVE_SAT_WINDOW",
                   "MMLLM_NET_N_BLOCKS","MMLLM_NET_SQRT_N","MMLLM_NET_C_NET"}  # tensor-shape / window-size: restart-only
_LIVE_GLOBALS = {"WAVE_SAT_EPS":"SAT_EPS","WAVE_TRUNK_COOL":"COOL","WAVE_TRUNK_WARM":"WARM",
                 "WAVE_LATE_FRAC":"LATE_FRAC","WAVE_LATE_DECAY":"LATE_DECAY","WAVE_DRIFT_FLOOR":"DRIFT_FLOOR",
                 "WAVE_TRUNK_CYCLE_PERIOD":"CYCLE_PERIOD","WAVE_TRUNK_CYCLE_WARM":"CYCLE_WARM",
                 "WAVE_TRUNK_CYCLE_WARM_MULT":"CYCLE_WMULT","WAVE_TRUNK_CYCLE_COOL_MULT":"CYCLE_CMULT",
                 "WAVE_TRUNK_CYCLE_COOL_DECAY":"CYCLE_CDECAY","WAVE_TRUNK_CYCLE_JITTER":"CYCLE_JITTER",
                 "WAVE_TRUNK_SWEEP":"SWEEP","WAVE_SWEEP_PERIOD_MIN":"SWEEP_PMIN","WAVE_SWEEP_PERIOD_MAX":"SWEEP_PMAX",
                 "WAVE_SWEEP_WARM_MIN":"SWEEP_WMIN","WAVE_SWEEP_WARM_MAX":"SWEEP_WMAX",
                 "WAVE_SWEEP_CREST_MIN":"SWEEP_CMIN","WAVE_SWEEP_CREST_MAX":"SWEEP_CMAX",
                 "WAVE_SWEEP_DECAY_MIN":"SWEEP_DMIN","WAVE_SWEEP_DECAY_MAX":"SWEEP_DMAX",
                 "WAVE_ODM_GAMMA":"ODM_GAMMA","WAVE_ODM_ETA":"ODM_ETA",
                 "WAVE_ODM_MIN_FRAC":"ODM_MIN","WAVE_ODM_MAX_FRAC":"ODM_MAX"}
_live_mtime = [0.0]
def _load_live(w):
    global SAT_EPS, COOL, WARM, LATE_FRAC, LATE_DECAY, DRIFT_FLOOR, STEPS
    try:
        if not os.path.exists(LIVE_PATH): return
        mt = os.path.getmtime(LIVE_PATH)
        if mt == _live_mtime[0]: return          # unchanged since last wave → skip
        _live_mtime[0] = mt
        s = json.load(open(LIVE_PATH))
    except Exception as e:
        print(f"@@@LIVE w{w}: unreadable ({e}) — keeping current config", flush=True); return
    applied, refused = {}, []
    for k, v in s.items():
        if k in _LIVE_FORBIDDEN: refused.append(k); continue
        if k in _LIVE_GLOBALS:   globals()[_LIVE_GLOBALS[k]] = float(v); applied[k] = v
        elif k == "WAVE_STEPS":  STEPS = int(v);  applied[k] = v
        elif k == "trunk_mult":                                  # direct per-module trunk-LR override
            for m, mv in (v or {}).items():
                if m in trunk_mult: trunk_mult[m] = max(MIN_MULT, float(mv)); applied[f"trunk_mult.{m}"] = trunk_mult[m]
        else:                    LIVE_ENV[k] = str(v); applied[k] = v   # passthrough to bird env
    if applied: print(f"@@@LIVE w{w}: applied {applied}", flush=True)
    if refused: print(f"@@@LIVE w{w}: REFUSED shape/window-locked (restart-only): {refused}", flush=True)

def trunk_controller(birds, w, dtrunk_pv):
    """After harvest(w): SMOOTHED per-module saturation detection → cool/warm NEXT wave's
    trunk LR, plus a late-training anneal floor (see retune note above)."""
    cur = {}
    for b in birds:
        ab = None
        try:
            for L in open(b["log"]):
                if "ablated_bpc=" in L: ab = float(L.split("ablated_bpc=")[-1].split(")")[0])
        except Exception: pass
        if ab is not None: cur.setdefault(b["module"], []).append(ab)
    moved = dtrunk_pv > DRIFT_FLOOR
    late  = w >= LATE_FRAC * WAVES
    msgs = []
    if int(CYCLE_PERIOD) > 0:                      # WAKE/SLEEP RAMPED cycle — overrides saturation/anneal
        nw = w + 1                                  # controller sets the NEXT wave's trunk-LR
        st = _cycle_state[0]
        if st is None or nw >= st["start"] + st["P"]:        # begin a NEW cycle → fix its SHAPE for the whole cycle
            if SWEEP:                                         # instrument #2: random shape (seeded by salt+start → resume-stable, fresh per run)
                rg = np.random.default_rng(JITTER_SALT * 7919 + nw)
                P  = int(rg.integers(int(SWEEP_PMIN), int(SWEEP_PMAX) + 1))
                WN = int(rg.integers(int(SWEEP_WMIN), max(int(SWEEP_WMIN), min(int(SWEEP_WMAX), P - 1)) + 1))
                pk = float(rg.uniform(SWEEP_CMIN, SWEEP_CMAX))
                cd = float(rg.uniform(SWEEP_DMIN, SWEEP_DMAX))
            else:                                             # fixed shape (current behavior)
                P, WN, pk, cd = int(CYCLE_PERIOD), int(CYCLE_WARM), CYCLE_WMULT, CYCLE_CDECAY
            st = {"start": nw, "P": P, "WN": WN, "peak": round(pk, 4), "cdecay": round(cd, 4)}
            _cycle_state[0] = st
            print(f"@@@SWEEP w{nw}: NEW cycle shape P={P} warm={WN} crest={pk:.3f} decay={cd:.3f}"
                  f"{' [swept]' if SWEEP else ' [fixed]'}", flush=True)
        P, WN, peak, cdecay = st["P"], st["WN"], st["peak"], st["cdecay"]
        floor = CYCLE_CMULT
        phase = nw - st["start"]
        if phase < WN:                              # WAKE: geometric warm-up floor→crest (gentle first step)
            frac = (phase + 1) / WN
            tgt  = floor * (peak / floor) ** frac if floor > 0 else peak * frac
            ph   = f"WAKE-ramp {phase+1}/{WN}"
        else:                                       # SLEEP: geometric cool-down crest→floor (the productive transit)
            j    = phase - WN
            tgt  = max(floor, peak * (cdecay ** (j + 1)))
            ph   = f"SLEEP-cool {j+1}/{P-WN}"
        nominal = tgt
        if CYCLE_JITTER > 0:                          # instrument #1: dither into a BAND (resume-stable: seeded by salt+wave)
            u   = float(np.random.default_rng(JITTER_SALT * 1000003 + nw).uniform(-1.0, 1.0))
            tgt = min(0.9, max(floor, tgt * (1.0 + CYCLE_JITTER * u)))
        for m in MODS:
            if m in cur: _ab_hist[m].append(sum(cur[m]) / len(cur[m]))   # keep history live for monitoring
            trunk_mult[m] = tgt
        jlog = f" (nom {nominal:.4f},±{CYCLE_JITTER:.0%})" if CYCLE_JITTER > 0 else ""
        print(f"@@@CYCLE w{w}→{nw}: {ph} [cyc@{st['start']} P{P} crest{peak:.2f} dec{cdecay:.2f}] → trunk-LR={tgt:.4f}{jlog}", flush=True)
        _save_ctrl()
        return
    for m in MODS:
        if m not in cur: continue
        _ab_hist[m].append(sum(cur[m]) / len(cur[m]))
        h = list(_ab_hist[m]); action = "hold"
        if len(h) >= WINDOW and moved:
            half = len(h) // 2
            # SMOOTHED improvement over the window: old-half mean − new-half mean (>0 = bpc still dropping)
            imp = sum(h[:half]) / half - sum(h[half:]) / (len(h) - half)
            # DEGRADATION FIX (cg6 post-mortem): cooling a trunk whose ablated bpc is going
            # NEGATIVE froze `text` at the floor while it kept losing ground. Now ANY negative
            # imp re-engages the trunk (never freeze a losing trunk); cool only when genuinely
            # flat-AND-not-degrading (0 ≤ imp < SAT_EPS).
            if imp < 0:                         # DEGRADING → re-engage the trunk
                trunk_mult[m] = min(INIT_MULT, max(MIN_MULT, trunk_mult[m] * WARM)); action = f"REWARM(imp{imp:+.4f})"
            elif imp < SAT_EPS:                 # flat/saturated (not degrading) → cool, redirect to bank
                trunk_mult[m] = max(MIN_MULT, trunk_mult[m] * COOL); action = f"COOL(imp{imp:+.4f})"
            else:                               # still learning → keep warm
                action = f"learn(imp{imp:+.4f})"
        if late:                                # endgame anneal regardless of saturation
            trunk_mult[m] = max(MIN_MULT, trunk_mult[m] * LATE_DECAY); action += "+late"
        msgs.append(f"{m}:{action}→{trunk_mult[m]:.4f}")
    _save_ctrl()
    print(f"@@@CTRL w{w} trunk-LR (moved={moved}, late={late}, Δtrunk={dtrunk_pv:.2e}): " + "  ".join(msgs), flush=True)

def latest_step(ckdir): return max(glob.glob(f"{ckdir}/step-*"), key=lambda d:int(d.split('-')[-1]))

def seed_round0():
    for f in glob.glob(RB(0)+"*"): os.remove(f)
    if os.path.isdir(RC(0)): shutil.rmtree(RC(0))
    sb = f"{G}/{SEED}-bank"; sbn = os.path.basename(sb)
    for f in glob.glob(f"{sb}-net.*.bin"): os.system(f"cp -c {f!r} {RB(0)}{os.path.basename(f)[len(sbn):]!r}")
    src = latest_step(f"{G}/{SEED}.ckpts"); os.makedirs(RC(0), exist_ok=True)
    shutil.copytree(src, f"{RC(0)}/{os.path.basename(src)}")
    print(f"round0 (old-4) seeded from {SEED}: {len(glob.glob(RB(0)+'*net*'))} slices + frozen trunk/router", flush=True)

# CPU/GPU SPLIT (per-process): the first WAVE_CPU_BIRDS modules (by MODS order) run their
# bird with MMLLM_MLX_DEVICE=cpu; the rest on the GPU. Each bird is its own process → its
# own Metal context (no shared-context buffer limit), same memory as today's PAR=2, but a
# CPU bird and a GPU bird run on SEPARATE compute units in PARALLEL. cpu indices are spread
# so a PAR window mixes devices (1 cpu + 1 gpu). Default 0 → all-GPU (unchanged).
_N_CPU_BIRDS = max(0, min(int(os.environ.get("WAVE_CPU_BIRDS", "0")), len(MODS)))
_CPU_MODS = {MODS[int(round(j * len(MODS) / _N_CPU_BIRDS))] for j in range(_N_CPU_BIRDS)} if _N_CPU_BIRDS else set()

def spawn(w, module, k, total, steps=STEPS):
    base = {**os.environ, **LIVE_ENV}            # live overrides win over launch-time env; derived MMLLM_* read from base
    env = dict(base)
    env.update({"WB_W":str(w),"WB_MODULE":module,"WB_K":str(k),"WB_TOTAL":str(total),
                "WB_DENSE_MULT":f"{trunk_mult[module]:.5f}",   # per-module saturation-aware trunk LR (see trunk_controller)
                "WB_STEPS":str(steps),"WB_ALLMODS":ALLMODS,"WAVE_TAG":TAG,"PYTHONPATH":SRC,
                "PYTHONUNBUFFERED":"1","MMLLM_BATCH":base.get("WB_BATCH","1"),"MMLLM_GRAD_CKPT":"false",
                "MMLLM_MLX_DEVICE":("cpu" if module in _CPU_MODS else "gpu"),   # heterogeneous per-process split
                "MLX_CACHE_MB":base.get("MLX_CACHE_MB","512"),
                "MMLLM_EVAL_EVERY":base.get("MMLLM_EVAL_EVERY","10"),
                "MMLLM_ABLATION_EVAL_CAP":base.get("MMLLM_ABLATION_EVAL_CAP","8192")})
    log = open(f"{G}/{TAG}b{w}-{module}-{k}.out", "w")
    import subprocess
    p = subprocess.Popen([PY, f"{G}/scripts/genesis_composed_bird.py"], env=env, stdout=log, stderr=subprocess.STDOUT)
    return {"proc":p, "module":module, "k":k, "log":log.name, "dev":("cpu" if module in _CPU_MODS else "gpu"),
            "pfx":f"{G}/{TAG}b{w}-{module}-{k}-bank", "ck":f"{G}/{TAG}b{w}-{module}-{k}.ckpts"}

def run_wave(specs):
    done, running, i, last_spawn, last_rep = [], [], 0, 0.0, 0.0
    while i < len(specs) or running:
        now = time.time()
        if i < len(specs) and len(running) < PAR and now - last_spawn >= STAG:
            running.append(spawn(*specs[i])); i += 1; last_spawn = now
            print(f"  [wave] +{running[-1]['module']}[{running[-1]['dev']}] ({len(running)} live)", flush=True)
        time.sleep(2)
        if running and now - last_rep >= REPORT:
            last_rep = now
            for b in running:
                last = None
                try:
                    with open(b["log"]) as fh:
                        for L in fh:
                            if "[mlx] step" in L: last = L
                except Exception: pass
                if last:
                    st=(re.search(r"step (\d+/\d+)",last) or [None,"?"])[1]
                    tb=(re.search(r"teacher_bpc=([\d.]+)",last) or [None,"?"])[1]
                    print(f"  [progress] {b['module']:<14} {st} tbpc={tb}", flush=True)
                else:
                    print(f"  [progress] {b['module']:<14} startup", flush=True)
        still = []
        for b in running:
            if b["proc"].poll() is None: still.append(b); continue
            bpc="?"
            try:
                for L in open(b["log"]):
                    if "@@@BIRD" in L: bpc=L.split("composed_bpc=")[-1].split()[0]
            except Exception: pass
            b["bpc"] = float(bpc) if bpc not in (None, "?", "") else None
            print(f"  [wave] {b['module']} done rc={b['proc'].returncode} composed_bpc={bpc}", flush=True)
            if b["proc"].returncode != 0:
                print("  [wave] FAILED — tail:", flush=True); os.system(f"tail -6 {b['log']}")
            done.append(b)
        running = still
    return done

def run_wave_threaded(specs):
    """Phase-G: run `specs` as THREADS in ONE genesis_threaded_wave.py process. The first
    WAVE_CPU_BIRTHS births run on their own mx.cpu streams, the rest on the GPU — CPU and
    GPU are separate units on shared unified memory, run in PARALLEL within ONE runtime
    (two separate cohort PROCESSES blow the 32GB box at ~11GB runtime each; one process
    shares it). Writes the SAME per-module files spawn() does → harvest() byte-unchanged.
    One proc → rc!=0 → WAVE ABORT, like the per-process any(rc!=0). ODM/trunk-LR via maps."""
    import subprocess
    w = specs[0][0]
    n_cpu = max(0, min(int(os.environ.get("WAVE_CPU_BIRTHS", "0")), len(specs)))
    env = {**os.environ, **LIVE_ENV}
    env.update({
        "MMLLM_THREADED_BIRTHS":"1", "WB_CPU_BIRTHS":str(n_cpu),
        "WB_W":str(w), "WB_K":"0", "WAVE_TAG":TAG, "WB_ALLMODS":ALLMODS,
        "WB_MODULES":",".join(f"{s[1]}:{s[2]}" for s in specs),
        "WB_TOTAL":str(max(s[3] for s in specs)), "WB_STEPS":str(STEPS),
        "WB_STEPS_MAP":",".join(f"{s[1]}:{s[4]}" for s in specs),
        "WB_TOTAL_MAP":",".join(f"{s[1]}:{s[3]}" for s in specs),
        "WB_DENSE_MULT_MAP":",".join(f"{m}:{trunk_mult[m]:.5f}" for m in MODS),
        "PYTHONPATH":SRC, "PYTHONUNBUFFERED":"1", "MMLLM_BATCH":env.get("WB_BATCH","1")})
    log = open(f"{G}/{TAG}b{w}-threaded.out", "w")
    p = subprocess.Popen([PY, f"{G}/scripts/genesis_threaded_wave.py"], env=env,
                         stdout=log, stderr=subprocess.STDOUT)
    print(f"  [wave] threaded: 1 process, {len(specs)} births ({n_cpu} CPU + {len(specs)-n_cpu} GPU)", flush=True)
    last_rep = 0.0
    while p.poll() is None:
        time.sleep(2); now = time.time()
        if now - last_rep >= REPORT:
            last_rep = now
            try:
                nd = sum(1 for L in open(log.name) if "@@@BIRD w" in L)
                lvl = subprocess.run(["sysctl","-n","kern.memorystatus_level"], capture_output=True, text=True).stdout.strip()
                print(f"  [progress] threaded {nd}/{len(specs)} births done (mem={lvl}%)", flush=True)
            except Exception: pass
    birds = []
    for (ww, m, kk, total, steps) in specs:
        bpc = None
        try:
            for L in open(log.name):
                if f"@@@BIRD w{w} {m}.k{kk}:" in L:
                    bpc = float(L.split("composed_bpc=")[-1].split()[0])
        except Exception: pass
        birds.append({"proc":p, "module":m, "k":kk, "log":log.name,
                      "pfx":f"{G}/{TAG}b{w}-{m}-{kk}-bank", "ck":f"{G}/{TAG}b{w}-{m}-{kk}.ckpts", "bpc":bpc})
    print(f"  [wave] threaded done rc={p.returncode}", flush=True)
    return birds

def harvest(birds, w):
    rb, rc = RB(w), RC(w)
    for f in glob.glob(rb+"*"): os.remove(f)
    if os.path.isdir(rc): shutil.rmtree(rc)
    by_mod = {}
    for b in birds: by_mod.setdefault(b["module"], []).append(b)
    # per-module V UNION (within-module FedAvg if K>1)
    for m, bs in by_mod.items():
        for L in range(NLAYERS):
            files = [f"{b['pfx']}-net.{m}.{L}.bin" for b in bs if os.path.exists(f"{b['pfx']}-net.{m}.{L}.bin")]
            if not files: continue
            if len(files) == 1: os.system(f"cp -c {files[0]!r} {rb}-net.{m}.{L}.bin")
            else: np.mean([np.fromfile(f,dtype=np.float32) for f in files],axis=0).astype(np.float32).tofile(f"{rb}-net.{m}.{L}.bin")
    # trunk+router: FedAvg the 4 birds' TRAINED dense_named (was frozen-carry from m4).
    # dense_named excludes the V tables (they persist via .bin + are unioned above) but
    # INCLUDES the trunk, router.module_keys, gates, norms — so averaging it harvests
    # both the slow-evolving trunk AND the per-corpus-aux-trained routers, breaking the
    # frozen-router monopoly that stranded the specialist banks.
    bird_steps = [latest_step(b["ck"]) for b in birds if glob.glob(f"{b['ck']}/step-*")]
    prev = latest_step(RC(w-1)); os.makedirs(rc, exist_ok=True)
    base = bird_steps[0] if bird_steps else prev
    shutil.copytree(base, f"{rc}/{os.path.basename(base)}")          # ckpt dir structure
    dst = f"{rc}/{os.path.basename(base)}/dense_named.pt"
    nds = [torch.load(f"{s}/dense_named.pt", map_location="cpu", weights_only=False) for s in bird_steps]
    ref = nds[0] if nds else torch.load(f"{prev}/dense_named.pt", map_location="cpu", weights_only=False)
    merged = {}
    for k, v in ref.items():
        ts = [nd[k] for nd in nds if k in nd and nd[k].shape == v.shape]
        merged[k] = (torch.stack([t.float() for t in ts]).mean(0).to(v.dtype)
                     if len(ts) > 1 else v)
    torch.save(merged, dst)
    # DRIFT monitor (trunk is NO LONGER frozen — Δ>0 is expected & desired). Track vs m4
    # (cumulative shed) AND vs prev wave (per-wave step) so we can watch the trunk
    # evolve slowly and catch runaway drift before the retention probe does.
    m4 = torch.load(f"{latest_step(G+'/'+SEED+'.ckpts')}/dense_named.pt", map_location="cpu", weights_only=False)
    pnd = torch.load(f"{prev}/dense_named.pt", map_location="cpu", weights_only=False)
    rk = "b0.netbank.router.module_keys"
    def _maxabs(a, b, skip_router=False):
        vals = [float((merged[k].float()-b[k].float()).abs().max())
                for k in a if k in b and a[k].shape == b[k].shape
                and not (skip_router and k.endswith("router_keys"))]
        return max(vals) if vals else 0.0
    dtrunk_m4 = _maxabs(merged, m4, skip_router=True)
    dtrunk_pv = _maxabs(merged, pnd, skip_router=True)
    drouter   = (float((merged[rk].float()-m4[rk].float()).abs().max())
                 if rk in merged and rk in m4 and merged[rk].shape == m4[rk].shape else 0.0)
    print(f"@@@HARVEST {TAG} w{w}: {len(glob.glob(rb+'*net*'))} V slices unioned + trunk/router FedAvg'd ({len(nds)} birds) | "
          f"DRIFT: max|Δtrunk vs {SEED}|={dtrunk_m4:.2e} max|Δtrunk vs w{w-1}|={dtrunk_pv:.2e} max|Δrouter vs {SEED}|={drouter:.2e}", flush=True)
    gc_old_waves(w)            # ── disk janitor: engineered INTO harvest so it can NEVER be dropped again ──
    return dtrunk_pv           # per-wave trunk drift → feeds the saturation controller

# ── DISK JANITOR ──────────────────────────────────────────────────────
# Engineered into harvest() (NOT a separate script that can be forgotten/deleted).
# The hog is the per-bird sparse-Adam moment files (.adm/.adv). TWO retention tiers:
#   • BIRD scratch (.bin/.adm/.adv/.ckpts/.log.jsonl): harvest(w) has ALREADY consumed
#     it (V slices→round, dense_named→FedAvg) and it is NEVER read again — resume +
#     next-wave births reseed from harvested ROUNDS, not bird banks — so it's deleted
#     the instant its wave is harvested. This is ~all the disk.
#   • Harvested ROUNDS (round bank + ckpt): the rollback points — keep the last `keep`
#     so a botched wave can be recovered; GC older. (harvest(w) needs RC(w-1) as prev,
#     always within the kept window.)
# The .out metric files are TINY text and the widget's full bpc/Δ_net curve reads them
# across ALL waves → ALWAYS kept.
KEEP_WAVES = int(os.environ.get("WAVE_KEEP", "3"))
def gc_old_waves(w, keep=KEEP_WAVES):
    freed = 0
    def _rm(f):
        nonlocal freed
        try:
            if os.path.isdir(f):
                for root, _, fs in os.walk(f):
                    for fn in fs:
                        try: freed += os.path.getsize(os.path.join(root, fn))
                        except OSError: pass
                shutil.rmtree(f)
            else:
                freed += os.path.getsize(f); os.remove(f)
        except OSError: pass
    # (1) Consumed BIRD scratch for every wave ≤ w (idempotent sweep, resume-safe).
    #     The `b{g}-` literal dash prevents b1 matching b10 etc. .out kept (widget curve).
    for g in range(0, w + 1):
        for f in glob.glob(f"{G}/{TAG}b{g}-*-bank*"): _rm(f)     # .bin + .adm + .adv  (the hog)
        for f in glob.glob(f"{G}/{TAG}b{g}-*.log.jsonl"): _rm(f)
        for d in glob.glob(f"{G}/{TAG}b{g}-*.ckpts"): _rm(d)
    # (2) Harvested ROUNDS — keep the last `keep` (rollback points), GC older.
    cutoff = w - keep + 1
    for g in range(0, max(cutoff, 0)):
        for f in glob.glob(f"{RB(g)}*"): _rm(f)
        _rm(RC(g))
    if freed:
        print(f"@@@JANITOR {TAG} w{w}: dropped consumed bird scratch (≤w{w}) + GC'd rounds "
              f"<{max(cutoff,0)} (kept last {keep} rounds), freed {freed/2**30:.2f}GB  "
              f"[disk free: {shutil.disk_usage(G).free/2**30:.1f}GB]", flush=True)

# RESUME-aware: stop→start continues from the last HARVESTED wave instead of
# restarting from round0. A wave w is "done" if its harvested bank+ckpt exist.
def _round_done(w):
    return os.path.isdir(RC(w)) and bool(glob.glob(f"{RB(w)}-net.*.bin"))
# HIGHEST harvested wave — NOT a contiguous walk from 0. Intermediate rounds may be
# reclaimed for disk (we keep only the latest harvest), so scan top-down and resume
# from the latest one that exists. Only seed round0 if NOTHING is harvested yet.
done = 0
for _w in range(WAVES, 0, -1):
    if _round_done(_w):
        done = _w; break
if done == 0 and not _round_done(0):
    seed_round0()                       # fresh start: seed round0 from the SEED model
elif done == 0:
    print(f"@@@ RESUME: round0 already seeded", flush=True)
else:
    print(f"@@@ RESUME from wave {done} (latest harvested; intermediate rounds may be pruned; waves {done+1}..{WAVES} remain)", flush=True)
_load_ctrl()                              # resume saturation-aware trunk-LR state (no-op on fresh start)
_load_odm()                               # resume ODM bandit weights (no-op on fresh start / when WAVE_ODM off)
total = int(os.environ.get("WAVE_BASE_STEP", "1437")) + done * len(MODS) * STEPS
steps_mult = {m: 1.0 for m in MODS}           # ODM per-module step re-allocation (1.0 = equal; off ⇒ stays 1.0)
for w in range(done + 1, WAVES+1):
    _load_live(w)                             # MID-RUN: pick up {TAG}_live.json edits before this wave
    steps_by_mod = {m: max(1, int(STEPS * steps_mult[m])) for m in MODS}
    # WAVE_BIRTHS_PER_MODULE>1 → ENSEMBLE: K births per module (distinct k → distinct
    # scratch), FedAvg-harvested per module for gradient diversity. =1 → today's 1/module.
    # This is what feeds a high PAR (4 modules × K) for the threaded CPU/GPU split.
    BPM = max(1, int(os.environ.get("WAVE_BIRTHS_PER_MODULE", "1")))
    specs = [(w, m, k, (total := total + STEPS), steps_by_mod[m]) for m in MODS for k in range(BPM)]
    print(f"=== {TAG} WAVE {w}/{WAVES}: {len(specs)} composed births (HOT each, B=1, "
          f"{'THREADED 1-proc' if THREADED else f'PAR={PAR}'}) "
          f"trunk-LR={ {m: round(trunk_mult[m],5) for m in MODS} } ===", flush=True)
    birds = run_wave_threaded(specs) if THREADED else run_wave(specs)
    if any(b["proc"].returncode != 0 for b in birds): print("WAVE ABORT", flush=True); break
    dpv = harvest(birds, w)
    trunk_controller(birds, w, dpv)       # detect per-module trunk saturation → redirect signal to banks
    if WAVE_ODM:                          # ODM: re-allocate NEXT wave's steps toward the worst modules
        bpc_by_mod = {b["module"]: b.get("bpc") for b in birds}
        steps_mult = odm_update(bpc_by_mod)
        print(f"@@@ODM w{w}: steps_mult={ {m: round(steps_mult[m],3) for m in MODS} } "
              f"weights={ {m: round(odm_w[m],3) for m in MODS} }", flush=True)
        _save_odm()
print("COMPOSED-GENESIS DONE", flush=True)
