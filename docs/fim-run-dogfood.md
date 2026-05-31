# FIM training contribution — JSON

Each contribution is one CPU run that trains FIM on JSON for ~30–45 min,
publishes a `dense.pt` + ablation trajectory + per-layer telemetry +
NetBank V (fp16) into `workers/<HANDLE>/`, and commits. Harvest happens
out-of-band between rounds.

**Resume point**: the latest `core/round-N/step-*/dense.pt` in the repo.
Preflight auto-discovers it; you don't need to set a path. Round-5
contributors will resume from `core/round-2/step-20000/dense.pt`
(rounds 3 and 4 were not harvested — both ran with mechanism bugs that
made cross-round inheritance worse than the round-2 baseline).

## Run

```bash
git fetch origin claude/analyze-repo-status-rN0vt
git checkout origin/claude/analyze-repo-status-rN0vt -- core/ workers/ src/ scripts/ docs/
pip install -e . --quiet

bash scripts/run_round2.sh <HANDLE>   # e.g. round5-a / round5-b / round5-c
```

That's it. The orchestration script does preflight → corpus → train →
eval → stage → commit → push. Don't go off-script — anything worth
recovering from is handled inside the script, and any prerequisite
gap is caught by preflight before training starts.

## What's in this dispatch (round 5)

Round 4 demonstrated the consolidation mechanism is *wired*
(`gate_w_net` 0.27–0.40, `distill_loss` flowing, `synergy > 0`) but
`Δ_net` stayed pinned at the noise floor (+0.0002 vs target +0.01).
A five-agent deep-dive on the trained tensors and code paths found
three upstream bugs that telemetry alone couldn't surface. All three
are fixed in this dispatch.

1. **LR-schedule guard dropped** (`core.lpy:3241`). The previous
   `(when (pos? warmup) ...)` wrapper around `set-opt-lr!` skipped
   applying any schedule whenever `MMLLM_LR_WARMUP=0` (the default —
   never set in the orchestration). Result: rounds 1–4 all printed
   `lr_b=3e-02 lr_n=3e-02` per step while the optimizer's actual
   `param_group.lr` stayed at base `3e-3` the whole run. **The
   sleep-cycle LR rotation was a ghost across 4 rounds.** Smoke
   verified: end-of-run `opt-sparse-net.lr = 2.99e-02` (was 3e-3).

2. **`MMLLM_DISTILL_DIRECTION_ONLY=false`** in orchestration. Round-4
   deep-dive (Agent D, measured from dense.pt) found Net's output
   direction converged to **99.95% cosine alignment with Local** —
   the distillation loss minimized by matching direction, putting
   zero pressure on `‖V‖`. Net became a low-rank projection of Local
   pointing the same way → redundant by construction → `alpha_net`
   correctly decayed → V never accumulated content. Magnitude-aware
   distill puts MSE pressure on `‖V‖` too, breaks the redundancy basin.
   Smoke verified: distill loss is now `~0.002` (was `~0.0003` in r4).

3. **NetBank V persistence as fp16**. Until round-5, the harvester
   merged `bank-net-latest.<i>.bin` if present, but workers never
   uploaded them — the orchestration script stripped them out because
   128 MB fp32 per layer exceeds GitHub's 100 MB blob limit. **Every
   round retrained NetBank V from scratch; cross-round consolidation
   was operationally impossible.** Fixed by converting fp32 → fp16
   at upload (64 MB per layer, fits under 100 MB) and expanding
   fp16 → fp32 at resume.

Plus everything from round-4 (3-way SwitchGate, `alpha_net`, V
warm-start from Local, resume-from-step-1, ckpt-dir wipe, fp16-cost
NetBank speedup, telemetry event, parser fixes).

## What success looks like

| metric | round 4 | round 5 target |
|---|---|---|
| `Δ_net` end-of-run | +0.0002 (noise floor) | **> +0.01** (above noise) |
| `‖net_out‖ / ‖local_out‖` | 5–10% | **> 30%** (V growing magnitude) |
| `alpha_net_mean` end-of-run | bifurcates per-head, half at ~0.006 | **stays > 0.3** (Net no longer suppressed) |
| `consolidation_idx` | -0.54 to -0.68 | **> 0** (Local → Net handoff) |
| `gate_w_net` mean | 0.27–0.40 | comparable or higher |
| `distill_loss` mean | ~3e-4 (direction-only) | **~2e-3** (magnitude-aware) |
| FIM-bpc OVERALL | 6.7–7.4 | continued descent (round-2: 3.58) |
| `format_validity` | 0 | still likely 0 |

The four bolded targets are the round-5 hypothesis: with the
sleep-cycle LR actually firing, magnitude-aware distill, and (for the
*next* round, since round-5 still has no community NetBank V to
resume) at least NetBank V *staged* for round-6 to inherit — `Δ_net`
should escape the noise floor for the first time.

## How to read your telemetry

After your run, `workers/<HANDLE>/step-5000/log.jsonl` contains:
- 5 `ablation_intermediate` events (one per 1000 steps)
- 5 `netbank_telemetry` events alongside, with these per-layer fields:

      local_out_norm, net_out_norm        residual contribution L2 norms
      net_v_grad_norm                     sparse-aware V gradient norm
      net_ka_grad_norm, net_kb_grad_norm  routing key gradient norms
      gate_w_sdpa, gate_w_local, gate_w_net  3-way softmax routing weights
      alpha_net_mean                      mean per-head Net residual scale

The diagnostic chain for "is NetBank being adopted now?":

  1. `gate_w_net ≈ 0`        → gate isn't routing → starved gradient
  2. `alpha_net_mean ≈ 0`    → gate routes but scales output to zero
  3. `net_out_norm ≈ 0`      → forward path collapsing despite above
  4. `net_v_grad_norm ≈ 0`   → no gradient → V can't learn
  5. all four healthy, `Δ_net` still ~0 → V learning but redundant
     with Local (this is what round-4 hit)

Round-5 is the first time that chain has been observable from
mechanism-actually-engaged training. If `Δ_net` still pins at noise
floor with all upstream metrics healthy, the next architectural
change is residual distill (Net learns Local's *complement*, not its
twin) — but try the easier fixes first.
