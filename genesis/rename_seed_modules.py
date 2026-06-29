"""Rename the m4 seed's module identities → text·math·agentic·code, producing a NEW
seed `s4` warm-started from m4. The matured-corpora run seeds from s4.

The rename is a pure STRING remap in two places (router.module_keys is POSITIONAL —
order preserved → no tensor edit):
  1. net V slice filenames: m4-bank-net.{old}.{L}.bin → s4-bank-net.{new}.{L}.bin  (APFS clone, sparse)
  2. dense_named.pt keys: '…netbank.banks.{old}.…' → '…netbank.banks.{new}.…'

Order is preserved (tiny-stories→text=idx0, amps-math→math=1, dolly-instruct→agentic=2,
code→code=3) so router.module_keys[idx] stays aligned with each module.

Usage:  dry  → report what would change   |   run → actually create the s4 seed
NOTE: the matured run also needs WAVE_MODULES="text,math,agentic,code" and the bird's
CORP map → {text:text-10g, math:math-10g, agentic:agentic-10g, code:code-10g} (launch config).
"""
import os, sys, glob, shutil, torch
G = os.path.expanduser("~/models/genesis")
RENAME = {"tiny-stories": "text", "amps-math": "math", "dolly-instruct": "agentic", "code": "code"}
dry = (sys.argv[1] if len(sys.argv) > 1 else "dry") == "dry"
SRC = sys.argv[2] if len(sys.argv) > 2 else "m4"     # e.g. cg5round40 to carry 40 waves forward
DST = sys.argv[3] if len(sys.argv) > 3 else "s4"

# 1. net V slices ──────────────────────────────────────────────────────
slices = glob.glob(f"{G}/{SRC}-bank-net.*.bin")
print(f"net slices: {len(slices)} (expect 128 = 4 modules × 32 layers)")
remapped = {}
for f in slices:
    rest = os.path.basename(f)[len(f"{SRC}-bank-net."):]   # {module}.{L}.bin
    mod, L, ext = rest.rsplit(".", 2)                       # module names have no dots → safe
    new = RENAME.get(mod, mod)
    dst = f"{G}/{DST}-bank-net.{new}.{L}.{ext}"
    remapped.setdefault((mod, new), 0)
    remapped[(mod, new)] += 1
    if not dry:
        os.system(f"cp -c {f!r} {dst!r}")                  # APFS clone (sparse, instant)
for (mod, new), n in sorted(remapped.items()):
    print(f"  {mod:<14} → {new:<8} : {n} layers")

# 2. ckpt + dense_named key remap ──────────────────────────────────────
src_ck, dst_ck = f"{G}/{SRC}.ckpts", f"{G}/{DST}.ckpts"
steps = glob.glob(f"{src_ck}/step-*")
print(f"\nckpt steps: {len(steps)}  ({src_ck} → {dst_ck})")
sample_remap = []
def remap_keys(nd):
    out, nchg = {}, 0
    for k, v in nd.items():
        nk = k
        for old, new in RENAME.items():
            if old != new and f".banks.{old}." in nk:
                nk = nk.replace(f".banks.{old}.", f".banks.{new}."); nchg += 1
                if not sample_remap: sample_remap.append((k, nk))
                break
        out[nk] = v
    return out, nchg
if dry:
    _, nchg = remap_keys(torch.load(f"{steps[0]}/dense_named.pt", map_location="cpu", weights_only=False))
    print(f"  would remap {nchg} bank keys × {len(steps)} steps (DRY — nothing written)")
else:
    if os.path.isdir(dst_ck): shutil.rmtree(dst_ck)
    shutil.copytree(src_ck, dst_ck)
    total = 0
    for dn in glob.glob(f"{dst_ck}/step-*/dense_named.pt"):
        out, nchg = remap_keys(torch.load(dn, map_location="cpu", weights_only=False))
        torch.save(out, dn); total += nchg
    print(f"  remapped {total} bank keys across {len(glob.glob(f'{dst_ck}/step-*'))} steps")
    # STEP-COUNTER RESET — a seed from a LATE round carries a high step-N dir name, which
    # collides with the chain's per-round budget (n_steps = min(max(1,total-resume_step),cap))
    # → 1-step waves (the cg6 bug). Keep only the latest ckpt, relabel it to RESET_STEP so the
    # budget works; WEIGHTS untouched. Makes seeding from any round step-safe by construction.
    RESET_STEP = int(os.environ.get("RESET_STEP", "1397"))
    sdirs = sorted(glob.glob(f"{dst_ck}/step-*"), key=lambda p: int(os.path.basename(p).split("step-")[1]))
    for old in sdirs[:-1]: shutil.rmtree(old)                       # keep only the latest ckpt
    tgt = os.path.join(dst_ck, f"step-{RESET_STEP}")
    if sdirs[-1] != tgt: os.rename(sdirs[-1], tgt)
    _stp = os.path.join(tgt, "step.txt")
    if os.path.exists(_stp): open(_stp, "w").write(str(RESET_STEP))
    print(f"  step counter reset → step-{RESET_STEP} (kept latest ckpt; avoids the 1-step collision)")
if sample_remap:
    print(f"\nkey remap example: {sample_remap[0][0]}\n              →    {sample_remap[0][1]}")
print("\n" + ("DRY RUN — nothing written. Re-run with `run` to create the s4 seed." if dry
              else f"DONE — s4 seed created: {len(glob.glob(f'{G}/{DST}-bank-net.*.bin'))} slices + {DST}.ckpts"))
