# FIM training contribution — JSON

Each contribution is one CPU run that trains FIM on JSON for ~30–45 min,
publishes a `dense.pt` + ablation trajectory + per-layer telemetry into
`workers/<HANDLE>/`, and commits. Harvest happens out-of-band between
rounds.

**Resume point**: the latest `core/round-N/step-*/dense.pt` in the repo.
Preflight auto-discovers it; you don't need to set a path. Round-4
contributors will resume from `core/round-2/step-20000/dense.pt`
(round-3 was not harvested — it ran under a broken regime, see below).

## Run

```bash
git fetch origin claude/analyze-repo-status-rN0vt
git checkout origin/claude/analyze-repo-status-rN0vt -- core/ workers/ src/ scripts/ docs/
pip install -e . --quiet

bash scripts/run_round2.sh <HANDLE>   # e.g. round4-a / round4-b / round4-c
```

That's it. The orchestration script does preflight → corpus → train →
eval → stage → commit → push. Don't go off-script — anything worth
recovering from is handled inside the script, and any prerequisite
gap is caught by preflight before training starts.

## What's in this dispatch (round 4)

Round 3 ran with the architectural router silently disabled — `SumGate`
sums sdpa + mem + net with equal weight and exposes no routing decision,
so `MMLLM_DISTILL_COEF=0.1` had nothing to compute against and
distillation loss read `0.0000` in every train log. Plus the resume
seed was being staged at `step-0/` which `core.lpy` silently ignores,
so every "round-3 resumed from round-2" agent actually trained from
random init. Both bugs are fixed. Round 4 is the first dispatch
where the consolidation mechanism is actually wired.

Concrete changes since round-3:

1. **3-way SwitchGate + per-head `alpha_net`** — `MMLLM_LONG_TIER_MIX=switch`
   and `MMLLM_ALPHA_NET=true` are now set in the orchestration. The gate
   computes `softmax(q · gate_proj_3) → (w_sdpa, w_local, w_net)` per
   (head, position), stashes `last_local_out` / `last_net_out` for the
   distillation loss to consume, and exposes a per-head trainable scale
   on the Net path. Distill loss now flows non-zero from step 1.

2. **Resume from step-1, not step-0** — `core.lpy`'s resume gate is
   `(when (pos? start-step) …)` so step-0 ckpts were skipped. Fixed in
   the orchestration. Verified in smoke: model now loads `core/round-2`
   weights, training begins at step 1 → 5000.

3. **NetBank V warm-start from Local V** (round-3's proposed fix, now
   actually exercised because resume works). Projects Local V through
   the expander's pseudo-inverse → NetBank V[:n_copy].

4. **Flat global cosine** (`MMLLM_LR_MIN = MMLLM_LR = 3e-3`) so NetBank's
   absolute effective LR stays high through the sleep cycle.

5. **Diversified synth corpus** — 10 system-prompt variants × 4 catalog
   styles × 1–3 tool calls per record. Mitigates round-2's memorization
   regression.

6. **NetBank forward 5.4× faster** + synthetic PCIe delay skipped in
   eval mode. Doesn't change training behavior; recovers inference
   speed for `eval-agent`.

7. **Push 413 fixed** — orchestration no longer copies the 128 MB
   NetBank V binaries into the worker payload (per `WORKERS.md`, only
   `dense.pt` + `meta.json` belong).

8. **Per-layer NetBank telemetry** at every ablation cadence. Each
   `netbank_telemetry` JSONL event records, per layer:

       local_out_norm, net_out_norm        residual contribution L2 norms
       net_v_grad_norm                     sparse-aware V gradient norm
       net_ka_grad_norm, net_kb_grad_norm  routing key gradient norms
       gate_w_sdpa, gate_w_local, gate_w_net  3-way softmax routing weights
       alpha_net_mean                      mean per-head Net scale

   These are the headline diagnostic for "is NetBank actually being
   adopted as a function tier?" — and they only exist because of the
   SwitchGate enable in change (1).

9. **meta.json parser fixes** — regexes now match the actual train-log
   formats for val_bpc / Δ_local / Δ_net; tokens_trained derived from
   step count; `agent_*` populated (was null in round-3 due to a
   pre-existing crash on malformed envelopes — now guarded).

## What success looks like

| metric | round 1 | round 2 | round 4 target |
|---|---|---|---|
| `Δ_net` end-of-run | ≈ 0 | +0.0005 (noise) | **> 0.01** (above noise) |
| `Δ_local` | +2.08 | +3.63 | comparable; ideally smaller |
| `consolidation_idx` | 0 | -0.78 (wrong direction) | **> 0** (Local→Net handoff) |
| `gate_w_net` mean across layers | n/a (SumGate) | n/a (SumGate) | **> 0.10** (Net actually routed to) |
| `distill_loss` mean during training | 0.0000 | 0.0000 | **> 0** (Net learning from Local) |
| FIM-bpc OVERALL | 4.80 | 3.58 | continued descent |
| `format_validity` | 0 | 0 | still likely 0 at this scale |

The `Δ_net > 0.01`, `gate_w_net > 0.10`, and `distill_loss > 0` columns
are the round-4 headline. If those three move, the consolidation
mechanism is genuinely engaged for the first time and round-5 can
build on a community core that's actually accumulating.

`format_validity > 0` remains the long-horizon target.

## How to interpret the telemetry

After your run, look at `workers/<HANDLE>/step-5000/log.jsonl`:

- 5 `ablation_intermediate` events at steps 1000/2000/3000/4000/5000
- 5 `netbank_telemetry` events at the same cadence
- 1 `ablation` (end-of-run)

The chain of "is NetBank being adopted?":

  1. `gate_w_net ≈ 0` → the gate isn't routing to Net → starved gradient
  2. `alpha_net_mean ≈ 0` → gate routes but scales output to zero
  3. `net_out_norm ≈ 0` despite the above → forward path collapsing
  4. `net_v_grad_norm ≈ 0` → no gradient → V can't learn regardless of init
  5. All four healthy AND `Δ_net` still ≈ 0 → V is learning but redundant
     with Local

Round-4 is the first time we'll see real values down this chain.
