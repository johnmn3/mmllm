"""Where on the trunk-LR slope does the bpc improvement concentrate?
Pairs each wave's trunk-LR (from WAVE banners across all f256 logs) with that wave's
avg composed_bpc (from bird .out files), computes per-wave Δbpc (improvement), and bins
by trunk-LR — separating WARM-UP (LR rising vs prev wave) from COOL-DOWN (LR falling),
since the productive regime may show hysteresis (cool-down was the money phase historically).
Re-run anytime as cycles accumulate."""
import os, re, glob
G = os.path.expanduser("~/models/genesis")
MODS = ("text", "math", "agentic", "code")

# trunk-LR per wave: scan ALL logs (current + rotated backups) for WAVE banners
lr = {}
for lg in sorted(glob.glob("/tmp/genesis_f256*.log")):
    for L in open(lg, errors="ignore"):
        m = re.search(r"WAVE (\d+)/100.*?trunk-LR=\{[^}]*?'text': ([0-9.]+)", L)
        if m: lr[int(m.group(1))] = float(m.group(2))

# avg bpc per wave from bird .out files (persist across restarts)
bpc = {}
for w in range(1, 101):
    v = []
    for mod in MODS:
        f = f"{G}/f256b{w}-{mod}-0.out"
        if os.path.exists(f):
            b = re.findall(r"composed_bpc=([0-9.]+)", open(f).read())
            if b: v.append(float(b[-1]))
    if len(v) == 4: bpc[w] = sum(v) / 4

# pair (trunk-LR, Δbpc, direction) per wave
rows = []
for w in sorted(bpc):
    if w - 1 in bpc and w in lr:
        rows.append((w, lr[w], bpc[w - 1] - bpc[w],            # Δbpc>0 = improvement
                     "warm" if (w - 1 in lr and lr[w] > lr[w - 1] + 1e-9) else "cool"))

# bin by trunk-LR
BINS = [(0.0, 0.07), (0.07, 0.12), (0.12, 0.20), (0.20, 0.30),
        (0.30, 0.45), (0.45, 0.65), (0.65, 0.85), (0.85, 1.01)]
print(f"  {'trunk-LR band':>14} | {'n':>3} {'mean Δbpc':>10} {'best':>7} | by direction")
print("  " + "-" * 64)
for lo, hi in BINS:
    seg = [r for r in rows if lo <= r[1] < hi]
    if not seg: continue
    d = [r[2] for r in seg]
    warm = [r[2] for r in seg if r[3] == "warm"]; cool = [r[2] for r in seg if r[3] == "cool"]
    wm = f"warm {sum(warm)/len(warm):+.3f}(n{len(warm)})" if warm else ""
    cm = f"cool {sum(cool)/len(cool):+.3f}(n{len(cool)})" if cool else ""
    bar = "#" * max(0, int((sum(d)/len(d)) * 300))
    print(f"  [{lo:.2f},{hi:.2f}) | {len(d):>3} {sum(d)/len(d):>+10.4f} {max(d):>+7.3f} | {wm} {cm}  {bar}")

# headline: which band has the highest mean improvement
best = max(BINS, key=lambda b: (lambda s: sum(r[2] for r in s)/len(s) if s else -9)(
    [r for r in rows if b[0] <= r[1] < b[1]]))
seg = [r for r in rows if best[0] <= r[1] < best[1]]
print(f"\n  >>> peak productivity regime: trunk-LR ∈ [{best[0]:.2f},{best[1]:.2f})  "
      f"mean Δbpc={sum(r[2] for r in seg)/len(seg):+.4f}/wave  (n={len(seg)})")
print(f"  >>> waves analyzed: {len(rows)} (LR range {min(r[1] for r in rows):.3f}–{max(r[1] for r in rows):.3f})")
