# FIM training contribution — JSON

Each contribution is one CPU run that trains FIM on JSON for ~30–45 min,
publishes a `dense.pt` + ablation trajectory into `workers/<HANDLE>/`,
and commits. Harvest happens out-of-band between rounds.

**Resume point** for the next dispatch: the latest `core/round-N/step-*/dense.pt`
in the repo. Preflight auto-discovers it; you don't need to set a path.

## Run

```bash
git fetch origin claude/analyze-repo-status-rN0vt
git checkout origin/claude/analyze-repo-status-rN0vt -- core/ workers/ src/ scripts/ docs/
pip install -e . --quiet

bash scripts/run_round2.sh <HANDLE>   # e.g. round3-a / round3-b
```

That's it. The orchestration script does preflight → corpus → train →
eval → stage → commit → push. Don't go off-script — anything worth
recovering from is handled inside the script, and any prerequisite
gap is caught by preflight before training starts.

## What's in this dispatch

Compared to round-2:

1. **NetBank V warm-start from Local V** (the round-2 mechanistic fix).
   `MMLLM_NET_V_WARMSTART_FROM_LOCAL=true` is now set in the script.
   At warm-start, Local's V is projected through the NetBank expander's
   pseudo-inverse and copied into NetBank's V[:n_copy]. Round-2 finding:
   Δ_net stayed at noise floor because V was random; only the addressing
   (K_a/K_b) was warm-started. This gives NetBank trained content at step 0.

2. **Flat global cosine** (`MMLLM_LR_MIN = MMLLM_LR = 3e-3`). Round-2
   finding: without this, NetBank's absolute effective LR only briefly
   peaked at midpoint because the base lr was decaying. Flatter cosine
   keeps NetBank at ~10× base during the entire sleep-cycle phase.

3. **Diversified synth corpus** (was contributing to memorization).
   `scripts/prep_xlam_synth.py` now varies system-prompt template,
   tool-catalog presentation, and 1–3 tool calls per record. Round-2
   finding: every record had the identical 200B sys-prompt prefix,
   model memorized it, FIM-eval went WORSE-than-random.

4. **Round-2 community core to resume from** (`core/round-2/step-20000/dense.pt`,
   harvested from round2-a + round2-b workers, weighted by `fim_quality`).
   Preflight auto-discovers and exports `RESUME_FROM`.

5. Same tracking machinery as round 2: `MMLLM_ABLATE_EVERY=1000`
   (5 ablation events across 5k steps), structured log preserved in
   `workers/<HANDLE>/step-5000/log.jsonl`, ablation trajectory parsed
   into `meta.fim.ablation_trajectory`.

## What success looks like

| metric | round 1 | round 2 | round 3 target |
|---|---|---|---|
| `Δ_net` end-of-run | ≈ 0 | +0.0005 (noise floor) | **> 0.01** (above noise) |
| `Δ_local` | +2.08 | +3.63 | comparable; ideally smaller (Local cedes to Net) |
| `consolidation_idx` | 0 | -0.78 (wrong direction) | **> 0** (Local→Net handoff) |
| FIM-bpc OVERALL | 4.80 | 3.58 | continued descent |
| FIM-bpc python (cross-lang) | 6.27 | 4.39 | continued descent |
| `format_validity` | 0 | 0 | still likely 0 at this scale |

The `Δ_net` and `consolidation_idx` columns are the round-3 headline:
V warm-start should move NetBank from "carries signal at noise floor"
to "carries signal you can see in one ablation". `format_validity > 0`
remains the long-horizon target — likely needs more rounds of
accumulation before it cracks.
