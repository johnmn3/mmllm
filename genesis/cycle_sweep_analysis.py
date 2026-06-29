"""Instrument #2: which CYCLE SHAPE ratchets best?
Reads @@@SWEEP cycle records (start wave + drawn P/warm/crest/decay) from all f256 logs,
pairs each cycle with its bpc ratchet (trough-to-trough drop = how much that cycle's shape
moved the floor down), and reports which crest / wavelength / warm-len / decay produce the
biggest ratchet — i.e. the best crest, wavelength, and slope shape. Run after sweep cycles exist."""
import os, re, glob
G = os.path.expanduser("~/models/genesis"); MODS = ("text", "math", "agentic", "code")

# cycle shapes from @@@SWEEP lines
cycles = []
for lg in sorted(glob.glob("/tmp/genesis_f256*.log")):
    for L in open(lg, errors="ignore"):
        m = re.search(r"@@@SWEEP w(\d+): NEW cycle shape P=(\d+) warm=(\d+) crest=([0-9.]+) decay=([0-9.]+)", L)
        if m: cycles.append({"start": int(m[1]), "P": int(m[2]), "WN": int(m[3]),
                             "crest": float(m[4]), "decay": float(m[5])})
cycles = {c["start"]: c for c in cycles}; cycles = [cycles[k] for k in sorted(cycles)]   # dedupe by start

# avg bpc per wave
bpc = {}
for w in range(1, 400):
    v = [float(re.findall(r"composed_bpc=([0-9.]+)", open(f).read())[-1])
         for mod in MODS for f in [f"{G}/f256b{w}-{mod}-0.out"]
         if os.path.exists(f) and re.findall(r"composed_bpc=([0-9.]+)", open(f).read())]
    if len(v) == 4: bpc[w] = sum(v) / 4

# each cycle's trough (min bpc over its waves) → ratchet = prev trough − this trough
rows = []
for c in cycles:
    ws = [w for w in range(c["start"], c["start"] + c["P"]) if w in bpc]
    if ws: c["trough"] = min(bpc[w] for w in ws); c["entry"] = bpc.get(c["start"] - 1)
for prev, c in zip(cycles, cycles[1:]):
    if "trough" in prev and "trough" in c:
        rows.append((c, prev["trough"] - c["trough"]))   # >0 = floor moved DOWN this cycle

if not rows:
    print(f"  no completed sweep cycles yet ({len(cycles)} shapes logged, need ≥2 with bpc). "
          f"Run with WAVE_TRUNK_SWEEP=1 first."); raise SystemExit

print(f"  {len(rows)} sweep cycles analyzed\n")
print(f"  {'start':>5} {'P':>3} {'warm':>4} {'crest':>6} {'decay':>6} | {'ratchet':>8}")
for c, r in sorted(rows, key=lambda x: -x[1]):
    print(f"  {c['start']:>5} {c['P']:>3} {c['WN']:>4} {c['crest']:>6.2f} {c['decay']:>6.2f} | {r:>+8.4f}")

# crude per-knob signal: split each knob at its median, compare mean ratchet
def split(key):
    vals = sorted(c[key] for c, _ in rows); med = vals[len(vals)//2]
    lo = [r for c, r in rows if c[key] <= med]; hi = [r for c, r in rows if c[key] > med]
    if lo and hi: return med, sum(lo)/len(lo), sum(hi)/len(hi)
    return med, None, None
print(f"\n  knob       median  mean-ratchet(≤med)  mean-ratchet(>med)   → favors")
for k, lab in [("crest","crest"),("P","wavelength"),("WN","warm-len"),("decay","decay")]:
    med, lo, hi = split(k)
    if lo is not None:
        fav = "higher" if hi > lo else "lower"
        print(f"  {lab:9} {med:>6.2f}  {lo:>+16.4f}  {hi:>+17.4f}   → {fav}")
print("\n  (more cycles → cleaner signal; accumulate across runs by bumping WAVE_JITTER_SALT)")
