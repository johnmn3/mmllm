#!/usr/bin/env python3
"""Desktop start/stop widget + live graph for the 10GB-streaming training run.

RED + glowing/undulating  = training running   → click circle to STOP
COLD GREEN (flat)         = stopped             → click circle to START (RESUMES)

Graph (stacked panels), parsed live from the run log / bird .out files:
  bpc      (per-step held-out mini-eval; LOWER is better)
  Δ_net    (consolidation: ablated_bpc − ctrl_bpc; HIGHER = netbank carries more)
  [HNET] avg_chunk   (chunker health, target N≈6; collapse = bad)
  [TRIE] leaf-fill % (deep-memory fill; climbs after revive steps)
  [MTP]  mtp_loss    (multi-token-pred head)
Each panel autoscales to its own min/max (per-module colored lines + white avg);
ALL share one x-axis so a vertical slice correlates across panels. The last three
stay empty ("—") on old runs that predate the [HNET]/[TRIE]/[MTP] logging.

Stop = SIGTERM. Start = relaunch; the run is RESUME-AWARE (continues from the
last completed round, ~per-round granularity). So stop→start picks up, not restarts.

Launch:  /Users/john/src/mmllm/.venv/bin/python3 ~/train_widget.py &
"""
import tkinter as tk
import subprocess, math, os, re, glob

G    = os.path.expanduser("~/models/genesis")
TAG  = os.environ.get("WIDGET_TAG", "f256")  # which run to monitor (run_next.sh sets WIDGET_TAG/WIDGET_LOG)
LOG  = os.environ.get("WIDGET_LOG", G + "/logs/genesis_f256.log")   # stable; NEVER /tmp
PY   = "/Users/john/src/mmllm/.venv/bin/python3"
SRC  = G + "/mmllm-src"
PROC = "genesis_composed_chain.py"           # the working 10GB composed chain
SCRIPT = G + "/scripts/genesis_composed_chain.py"
# Start button → the teed-up launcher (RAM-gated pre-flight; Tier-1/2 features +
# structural sweep ON; continues off f256round100). Edit knobs in scripts/run_next.sh.
LAUNCH = f"zsh {G}/scripts/run_next.sh"

def is_running():
    # absolute pgrep path + try/except: a bare "pgrep" depends on PATH, which is
    # absent/minimal when the widget is auto-launched from the detached run session
    # → is_running wrongly returned False (showed STOPPED while the run was alive).
    for pg in ("/usr/bin/pgrep", "pgrep"):
        try:
            return subprocess.run([pg, "-f", PROC], capture_output=True).returncode == 0
        except FileNotFoundError:
            continue
        except Exception:
            return False
    return False

# ── log parsing (throttled) ──────────────────────────────────────────
MODS_O = ["text", "math", "agentic", "code"]
MODCOL = {"text":"#36d6e0", "math":"#e8b84b", "agentic":"#5fd96b", "code":"#c07cf0"}
MODLAB = {"text":"text", "math":"math", "agentic":"agent", "code":"code"}
_cache = {"bpc_m": {}, "dn_m": {}, "hnet_m": {}, "trie_m": {}, "mtp_m": {},
          "rnd": "-", "gstep": 0, "gtot": 0, "frame": -999}
LN2INV = 1.4426950408889634          # 1/ln2: per-step training loss (CE in nats) → bits-per-byte
def _ema(vals, a=0.25):              # light smoothing for the high-res per-step bpc curve
    out = []; e = None
    for v in vals:
        e = v if e is None else a * v + (1 - a) * e
        out.append(e)
    return out
def _stepseries(raw, PER):           # {mod:[(wave,step,val)]} → {mod:[(global_step,ema_val)]}
    # SAME global-step axis as bpc_m (x=(wave-1)*PER+step) so a vertical slice lines up
    # across ALL panels. Multiple lines/step (e.g. one [TRIE] per block) are averaged.
    out = {}
    for m in MODS_O:
        acc = {}
        for (w, s, v) in raw.get(m, []):
            acc.setdefault((w - 1) * PER + s, []).append(v)
        pts = sorted((x, sum(vs) / len(vs)) for x, vs in acc.items())
        xs = [x for x, _ in pts]; vs = _ema([v for _, v in pts])
        seq = list(zip(xs, vs))
        if len(seq) > 600: seq = seq[::max(1, len(seq) // 600)]
        out[m] = seq
    return out
def refresh(frame):
    if frame - _cache["frame"] < 18:          # ~1s at 55ms/frame
        return
    _cache["frame"] = frame
    try:
        txt = open(LOG).read()
        # COMPOSED-CHAIN log format: @@@BIRD ... composed_bpc=X (per bird per wave),
        # [progress] <module> N/M tbpc=Y, === <tag> WAVE w/N ===, @@@HARVEST.
        # bpc per module per wave — read from the PERSISTENT chain log ([wave] done
        # lines), so it survives bird-.out pruning. Track wave from the WAVE markers.
        # bpc AND Δ_net per module per wave — BOTH read from the bird .out files
        # (@@@BIRD composed_bpc=… and Δ_net=…), keyed by wave. The .out files persist
        # across relaunches; the chain log gets truncated on Start (`> log`), so reading
        # bpc from the log lost the curve. Sourcing both from .out → restart-proof,
        # rebuilds the full history.
        bm = {m: [] for m in MODS_O}; dm = {m: {} for m in MODS_O}; cb = {m: {} for m in MODS_O}
        # NEW per-step H-Net mechanics (raw (wave,step,val); built into series below).
        # DEFAULT-SAFE: old .out files have none of these → stays empty → panel shows "—".
        hn = {m: [] for m in MODS_O}; tr = {m: [] for m in MODS_O}; mp = {m: [] for m in MODS_O}
        for f in glob.glob(os.path.join(G, f"{TAG}b*-0.out")):
            mt = re.match(rf"{TAG}b(\d+)-(.+)-0\.out", os.path.basename(f))
            if not mt or mt.group(2) not in bm: continue
            w = int(mt.group(1)); mod = mt.group(2)
            try:
                t = open(f).read()
                # HIGH-RES bpc: per-step training loss (CE in nats) → bits/byte via ×1/ln2.
                # ~50 points/wave (every EVAL_EVERY) incl. the in-flight wave, vs 1/wave for
                # composed_bpc → live intra-wave movement. Restart-safe (.out files persist).
                for sm in re.finditer(r"step (\d+)/\d+.*?minieval_bpc=([0-9.]+)", t):
                    bm[mod].append((w, int(sm.group(1)), float(sm.group(2))))   # REAL held-out mini-eval bpc (already bits/byte, no ln2)
                dv = re.findall(r"Δ_net=(-?[0-9.]+)", t)   # Δ_net only exists at wave-end eval → stays per-wave
                if dv: dm[mod][w] = float(dv[-1])
                cbv = re.findall(r"composed_bpc=([0-9.]+)", t)   # EVAL bpc (held-out, per wave) — the real quality metric
                if cbv: cb[mod][w] = float(cbv[0])
                # H-NET mechanics, per-step (same step counter as minieval). trainer.py emits:
                #   [HNET] step N ... avg_chunk=5.20 ...      → chunker health (collapse = bad, target N≈6)
                #   [TRIE] step N blkB/name leaf-fill L1:8.3% L2:.. → deep-memory fill (climbs after revive)
                #   [MTP]  step N ... mtp_loss=1.20           → multi-token-pred head (fwd-compat; folded into loss today)
                for sm in re.finditer(r"\[HNET\] step (\d+).*?avg_chunk=([0-9.]+)", t):
                    hn[mod].append((w, int(sm.group(1)), float(sm.group(2))))
                for sm in re.finditer(r"\[TRIE\] step (\d+).*?leaf-fill L1:([0-9.]+)%", t):
                    tr[mod].append((w, int(sm.group(1)), float(sm.group(2))))
                for sm in re.finditer(r"\[MTP\] step (\d+).*?mtp_loss=([0-9.]+)", t):
                    mp[mod].append((w, int(sm.group(1)), float(sm.group(2))))
            except Exception: pass
        PER = 500   # steps/wave. ONE bpc line per module on a global-step axis: per-wave
        bpc_m = {}  # composed_bpc for early waves (no mini-eval) + per-step mini-eval for recent
        for m in MODS_O:                                       # waves → low-res early, hi-res recent, WHOLE history.
            hiw = {w for (w, _, _) in bm[m]}                   # waves that have the per-step mini-eval
            pts = [((w - 1) * PER + s, v) for (w, s, v) in bm[m]]
            pts += [(w * PER, cb[m][w]) for w in cb[m] if w not in hiw]   # early waves: one per-wave eval point
            pts.sort()
            xs = [x for x, _ in pts]; vs = _ema([v for _, v in pts])
            seq = list(zip(xs, vs))
            if len(seq) > 600: seq = seq[::max(1, len(seq) // 600)]
            bpc_m[m] = seq
        _cache["bpc_m"] = bpc_m
        _cache["dn_m"] = {m: [(w * PER, dm[m][w]) for w in sorted(dm[m])] for m in MODS_O}
        # NEW H-Net panels — same global-step axis as bpc (built via _stepseries).
        _cache["hnet_m"] = _stepseries(hn, PER)
        _cache["trie_m"] = _stepseries(tr, PER)
        _cache["mtp_m"]  = _stepseries(mp, PER)
        # ALL panels SHARE one x-domain → a vertical line correlates bpc / Δ_net / chunk / trie / mtp
        # (sleep/wake cycles). New series included so the slice spans the whole run; empty on old runs.
        _allx = [x for k in ("bpc_m", "dn_m", "hnet_m", "trie_m", "mtp_m")
                 for s in _cache[k].values() for x, _ in s]
        _cache["xdom"] = (min(_allx), max(_allx)) if _allx else (0, 1)
        wv = re.findall(r"WAVE (\d+)/(\d+)", txt)
        _cache["rnd"] = (f"wave {wv[-1][0]}/{wv[-1][1]}" if wv else "-")
        nwaves = int(wv[-1][1]) if wv else 20
        # step counter ticks every EVAL_EVERY (~10) from the SAME per-step lines the graph plots
        per = 500
        steps_seen = [(w, s) for m in MODS_O for (w, s, _) in bm[m]]
        lw, ls = max(steps_seen) if steps_seen else (1, 0)   # furthest-along (wave, in-wave step)
        _cache["gtot"] = nwaves * per
        _cache["gstep"] = min((lw - 1) * per + ls, _cache["gtot"])
        if "COMPOSED-GENESIS DONE" in txt: _cache["rnd"] = "DONE"
    except Exception:
        pass

def start():
    if is_running(): return
    subprocess.Popen(LAUNCH, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
def stop():
    subprocess.run(["pkill", "-f", PROC])
    subprocess.run(["pkill", "-f", "genesis_composed_bird.py"])   # birds run detached — Stop must kill them too, else they keep training/writing

# ── GUI ──────────────────────────────────────────────────────────────
W, H = 440, 560                # taller canvas: stacked panels grew 2 → 5 (bpc, Δ_net, HNET, TRIE, MTP)
GTOP, GBOT = 190, 548          # graph stack y-range (split into N even bands below)
root = tk.Tk()
root.title("training (10GB stream)")
root.attributes("-topmost", True)
root.resizable(False, False)
root.configure(bg="#0d0d0f")
cv = tk.Canvas(root, width=W, height=H, bg="#0d0d0f", highlightthickness=0)
cv.pack()
CX, CY, R0 = W // 2, 92, 52
t = [0.0]; _busy = [0]

def hit(e):
    if (e.x - CX) ** 2 + (e.y - CY) ** 2 <= (R0 + 16) ** 2 and not _busy[0]:
        _busy[0] = 12
        (stop if is_running() else start)()
cv.bind("<Button-1>", hit)

def panel_multi(title, sd, y0, y1, xdom=None):
    """One sub-panel. sd = {module: [(global_step, value)]}. Per-module lines + a white AVERAGE
    line. xdom=(xlo,xhi) is SHARED across panels so a vertical slice lines up between bpc and
    Δ_net → you can correlate them (read the sleep/wake cycle across both)."""
    x0, x1, lx = 12, W - 66, W - 62
    cv.create_rectangle(8, y0, W-8, y1, outline="#222", fill="#08080a")
    cv.create_text(11, y0+2, anchor="nw", text=title, fill="#aaa", font=("Helvetica Neue", 8, "bold"))
    allp = [p for s in sd.values() for p in s]
    if not allp:
        cv.create_text((8+W)//2, (y0+y1)//2, text="—", fill="#666", font=("Helvetica Neue", 9)); return
    lo, hi = min(v for _, v in allp), max(v for _, v in allp); rng = (hi - lo) or 1.0
    xlo, xhi = xdom if xdom else (min(x for x, _ in allp), max(x for x, _ in allp)); xrng = (xhi - xlo) or 1.0
    Y = lambda v: (y1-5) - ((y1-5) - (y0+5)) * ((v - lo) / rng)
    X = lambda x: x0 + (x1 - x0) * ((x - xlo) / xrng)         # SHARED time position → panels align
    yy = y0 + 11
    for mod in MODS_O:
        s = sd.get(mod, []); col = MODCOL[mod]
        if len(s) >= 2:
            pts = []
            for x, v in s: pts += [X(x), Y(v)]
            cv.create_line(*pts, fill=col, width=1, smooth=True)
        _lv = s[-1][1] if s else None
        cv.create_text(lx, yy, anchor="w", text=f"{MODLAB[mod]} {_lv:.3f}" if _lv is not None else f"{MODLAB[mod]} —",
                       fill=col, font=("Helvetica Neue", 8)); yy += 10
    # AVG on the common axis: at each x (union), mean of each module's latest value ≤ x (carry-forward).
    xset = sorted({x for s in sd.values() for x, _ in s})
    md = {m: dict(sd.get(m, [])) for m in MODS_O}; mlast = {m: None for m in MODS_O}; avg = []
    for x in xset:
        for m in MODS_O:
            if x in md[m]: mlast[m] = md[m][x]
        vs = [v for v in mlast.values() if v is not None]
        if vs: avg.append((x, sum(vs) / len(vs)))
    if len(avg) >= 2:
        pts = []
        for x, v in avg: pts += [X(x), Y(v)]
        cv.create_line(*pts, fill="#f2f2f2", width=2, smooth=True)
    cv.create_text(lx, yy, anchor="w", text=f"avg {avg[-1][1]:.3f}" if avg else "avg —",
                   fill="#f2f2f2", font=("Helvetica Neue", 8, "bold"))

def draw():
    t[0] += 1
    if _busy[0] > 0: _busy[0] -= 1
    refresh(t[0])
    cv.delete("all")
    run = is_running()
    # ── button ──
    if run:
        p = (math.sin(t[0] * 0.13) + 1) / 2
        r = R0 + 5 * p
        for gr, sh in ((r + 20, "#2a0d0f"), (r + 13, "#5a1418"), (r + 6, "#8c1c20")):
            cv.create_oval(CX-gr, CY-gr, CX+gr, CY+gr, fill=sh, outline="")
        core = int(190 + 60 * p)
        cv.create_oval(CX-r, CY-r, CX+r, CY+r, fill=f"#{core:02x}2a2c",
                       outline=f"#{min(255,core+30):02x}4044", width=2)
        big, hint = "RUNNING", "click to stop"
    else:
        cv.create_oval(CX-R0, CY-R0, CX+R0, CY+R0, fill="#27523c", outline="#163325", width=2)
        big, hint = "STOPPED", "click to start (resumes)"
    cv.create_text(CX, CY-14, text=big, fill="#f2f2f2", font=("Helvetica Neue", 14, "bold"))
    cv.create_text(CX, CY+5,  text=_cache["rnd"], fill="#e8e8e8", font=("Helvetica Neue", 10))
    cv.create_text(CX, CY+20, text=f"step {_cache['gstep']}/{_cache['gtot']}", fill="#e8e8e8",
                   font=("Helvetica Neue", 10))
    cv.create_text(CX, 165, text=hint, fill="#888", font=("Helvetica Neue", 9))
    # ── stacked graph panels (each its own y-scale; ALL share one xdom so a vertical
    #    slice correlates bpc ↔ Δ_net ↔ chunk-size ↔ trie-fill ↔ mtp across the run) ──
    # First two are the original panels (unchanged); the last three stream the H-Net
    # mechanics and stay empty ("—") on old runs that never logged [HNET]/[TRIE]/[MTP].
    PANELS = [("bpc · held-out (hi-res)",        "bpc_m"),   # whole-history bpc line (orig)
              ("Δ_net (per wave)",               "dn_m"),    # consolidation (orig)
              ("[HNET] avg_chunk (target N≈6)",  "hnet_m"),  # chunker health — collapse = bad
              ("[TRIE] leaf-fill % (L1)",        "trie_m"),  # deep-memory fill — climbs after revive
              ("[MTP] mtp_loss",                 "mtp_m")]   # multi-token-pred head
    n = len(PANELS); span = GBOT - GTOP; xd = _cache.get("xdom")
    for i, (title, key) in enumerate(PANELS):
        y0 = GTOP + round(i * span / n); y1 = GTOP + round((i + 1) * span / n)
        panel_multi(title, _cache.get(key, {}), y0 + (0 if i == 0 else 3), y1 - 3, xdom=xd)
    root.after(55, draw)

draw()
root.mainloop()
