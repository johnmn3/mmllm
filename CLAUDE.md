# Working notes for Claude on this repo

## Baseline conduct

No attacks. No destruction of private property. No defacing customer
goods or digital objects. No corrupting data. No damaging persons,
places, or things. Basic human decency.

Concretely in this repo: don't delete or overwrite files, branches,
ckpts, journals, or code I didn't put there myself, and didn't get
explicit authorization to touch. Don't run destructive git operations
(reset --hard, force push, branch -D, clean -f) without explicit
authorization. Don't run shell commands that mutate state outside
this repo's working tree without explicit authorization. If a fix
seems to require breaking something existing, stop and ask.

## Reporting discipline (post-it note)

When a test or training run is in flight:

1. **Stream events live.** Arm a Monitor with `tail -F | grep --line-buffered -E ...`
   targeted at the actual signal lines the run emits (step prints, eval bpc,
   ablation Δ, control/ablated bpc, Δ_local/Δ_net, training complete, errors).
   Don't poll for memory every 60s — that's noise.

2. **Report each result as it lands.** When a step print, eval, or ablation
   event fires, send a brief message with the numbers. Don't wait for the
   end. Don't go silent during a run.

3. **Watch for failure signatures.** The grep filter MUST cover Traceback,
   RuntimeError, AssertionError, ZeroDivisionError, Killed, OOM, FAILED,
   WARN. Silence on a known failure mode is silence on real failure.

4. **Summarize at the end.** When the run completes, post a clean summary
   table with the salient metrics (training trajectory, eval bpc,
   ablation Δ, wall time, peak memory) and any caveats.

5. **Don't claim something is done until you've proven it.** "Implementation
   done" requires a run that demonstrates the behavior is correct, not just
   code that type-checks. Verification is part of the task, not a follow-up.

6. **Don't waste compute on configs we've already ruled out.** Before
   launching, mentally check: do we already know this OOMs / fails / is
   duplicate? If yes, skip it. State the cost and expected new info before
   each launch.

7. **Don't break existing property.** Anything in the codebase — env vars,
   recipes, gating choices, schedules, init patterns — is there on
   purpose. The previous agent / the user did not put it there by accident.
   Before removing or changing ANY existing line, two things must hold:
     a. I have an explicit instruction from the user to change *that
        specific thing*, OR I have read enough of the design history
        (commit messages, journals, related code) to understand why it
        was added and have a defensible reason to undo it.
     b. The change is the smallest possible diff that addresses the
        stated goal. Don't "clean up" adjacent lines while you're there.
   When a fix to one thing seems to require removing another, that's a
   signal to investigate the adjacent thing's purpose, not a license to
   remove it. Default: leave it alone, work around it, ask if unsure.

## Project shorthand

- **spork** = shared-trunk spoon (option A architecture). 100-step training
  run at the shared-trunk recipe.
- **spoon** = 100-step training run at the cpu-tiny recipe.
- **chain** = N sporks back-to-back, V_local zero-init each round, V_net
  and dense.pt carried forward across rounds.

## What to watch in a 100-step run — and when

The wake/sleep schedule has TWO phases. Don't conflate them. Don't call a
bank "mute" because you looked at the wrong tier at the wrong time.

- **Steps 0 → ~70 (Local phase).** Bank LR is high (warmup ramp-up, then
  30× wake plateau). Net LR is essentially zero. Distill coef is at its
  floor. The hill climber is filling **Local Bank** in this window.
  → **Δ_local is the signal.** Δ_net is *expected* to be zero here. Don't
  report Δ_net = 0 as a finding during the Local phase — that's the
  design, not a problem.

- **Steps ~70 → 100 (Distillation / Net phase).** lr_b cosines down to
  0.001× (Local freezes). lr_n ramps up to 0.1× (Net wakes). Distill
  coef rises toward DISTILL_COEF_END. Whatever Local accumulated in
  phase 1 should now flow into Net via the MSE distillation loss.
  → **Δ_net is the signal.** A successful run shows Δ_net rising from
  ~0 toward Δ_local during this window. The end-of-train summary's
  Δ_net is the headline number.

When reporting mid-train ablations:
- Pre-step-70 events: lead with Δ_local. Mention Δ_net only if it's
  unexpectedly nonzero.
- Post-step-70 events: lead with Δ_net (and Δ_net / Δ_local ratio as
  the distillation transfer fraction). Δ_local is expected to be
  approximately frozen.

## Δ-ablation is NOT proof that the bank's V learned anything

Caught lying about this on 2026-05-13. When V_local / V_net are
Gaussian-initialized, the **ablation Δ can be non-zero even when V
literally has not moved from seed init** (cos(V_current, V_seed)=1.000000,
L2(Δ)/L2(init) < 0.1%). The Δ signal comes from THREE places, only one
of which is V training:

  (a) The Gaussian-init V itself contributes to retrieval. Zeroing it
      removes that contribution → non-zero Δ regardless of training.
  (b) K_a / K_b sub-key matrices are dense params (in opt-dense, NOT in
      opt-sparse), trained at lr_d_mult. The retrieval pattern evolves
      every step even if V is frozen.
  (c) SwitchGate's gate_proj_3 is dense, trained every step. The model
      learns to ROUTE mass through Local / Net based on context — the
      gate output changes even with frozen V.

Δ_local > 0 / Δ_net > 0 only proves "some part of the bank tier matters."
To prove "bank V was trained" you need to additionally check, AFTER
end-of-train save/restore is complete:

  python3 -c '
  import numpy as np
  curr = np.memmap(<bank_path>, ...).copy()
  init = <regenerate seed Gaussian with same seed>
  l2d = np.linalg.norm(curr - init)
  cos = np.dot(curr.ravel(), init.ravel()) / (norm(curr) * norm(init))
  print(f"moved% = {l2d / np.linalg.norm(init):.4%}  cos = {cos:.6f}")
  '

If `cos ≈ 1.000000` and `moved% < 1%`, V hasn't been trained meaningfully.
The Δ you reported was false positive from (a)+(b)+(c). Don't claim
"distillation works" or "Local is learning" until V has moved.

Also: CPUSparseSGD with index_add_(-lr * grad) has been observed moving
V by < 0.1% even at lr_b = 6e-2 wake plateau, on cpu-tiny + N=1 +
Gaussian σ=0.02 init. The gradient magnitude relative to init magnitude
is what determines net movement — small grads × small lr × small steps
= no meaningful displacement.

**Fixed 2026-05-13.** Reverted MMLLM_SPARSE_OPT default from `sgd` back
to `adam-cpu` in run_shared_trunk.sh. Comparison at 100 steps cpu-tiny
N=1 B=4, identical recipe and Gaussian-init banks otherwise:

  | optimizer | V_local moved% | Δ_local end | Δ_net end | ctrl bpc |
  |-----------|----------------|-------------|-----------|----------|
  | sgd       | 0.00%          | +0.0006     | +0.0022   | 4.60     |
  | adam-cpu  | 373.80%        | +1.6838     | +0.0011   | 3.78     |

sgd's "Δ_net=+0.0022" was the false-positive contribution from
Gaussian-init V × trained K_a/K_b × trained gates — V_net itself never
moved. With adam-cpu, V_local is real (max|v|=3-6 vs Gaussian σ=0.02
init, 400× growth in 100 steps) and Δ_local is meaningful.

Net distillation transfer is still weak even with adam-cpu (V_net
local-attached layers moved 4.81% vs net-only 2.45% — asymmetric
signature is present but Δ_net stays at ~+0.001). Root cause:
MMLLM_SKIP_NETBANK_WARMSTART=true keeps Net's K_a/K_b random, so Net
retrieves at different addresses than Local. Distill MSE pushes V_net at
Net's row addresses, which don't align with Local's — V_net learns
averaged Local content at the wrong rows. Fixing requires either
enabling warm-start or wiring distill to push K_a/K_b alignment — both
are recipe-level changes that need user sign-off.

sgd is still available as `MMLLM_SPARSE_OPT=sgd` for N>8 OOM cases, but
the distillation effectively breaks at that setting. Document the
trade-off in any launcher script that targets shared-trunk N>8.

## Active workstreams

- Shared-trunk option A is implemented and verified — `tests/test_shared_trunk.py`
  passes, engagement-fix recipe (commit `85a507a`) produces Δ_local > 0.
- Follow-ups in todo: thread trunk_ids through eval-bpc (so ablation
  measures the N-trunk pool not just trunk-0); fix save_to_mmap
  self-overwrite at end-of-train.

## Winning bank-engagement recipes (sweep results, 2026-05-13)

Established via the sweep_distill infrastructure (scripts/build_distill_base.sh
+ scripts/sweep_distill.sh, resume-from-step-70 iteration). All numbers
from cpu-tiny N=1 B=4 100-step runs with adam-cpu sparse optimizer +
warm-start enabled + Gaussian σ=0.02 bank init.

Baseline (spike-6 verbatim) was: ctrl bpc=3.78, Δ_local=+1.64,
Δ_net=+0.0018, synergy=+0.008 (Net effectively not training).

Two Pareto-optimal recipes, depending on what we need from the trained model:

### **stack-3e-2-5.0** — "end-of-spork model" / best raw bpc
Overrides on top of spike-6:
  - MMLLM_LR=3e-2  (10× baseline; with LR_MIN=3e-2)
  - MMLLM_LR_NET_MULT_END=5.0 (50× baseline 0.1)

Result: ctrl bpc=**2.59** (-32% vs baseline), Δ_local=+1.07, Δ_net=+0.052
(29× baseline), Δ_both=+1.30, synergy=+0.18. Balanced — both banks
contribute, Net has started absorbing Local's role but hasn't taken over.

Use when: deploying the spork as a standalone trained model. Best
language-modeling bpc.

### **stack-1e-1-5.0** — "chain-round seed" / peak Net consolidation
Overrides on top of spike-6:
  - MMLLM_LR=1e-1  (33× baseline; with LR_MIN=1e-1)
  - MMLLM_LR_NET_MULT_END=5.0

Result: ctrl bpc=2.80, Δ_local=**+0.52** (Local mostly silent),
Δ_net=**+0.33** (185× baseline), Δ_both=+1.19, synergy=+0.34. Net has
absorbed most of Local's role — exactly what a chain round needs so
the next round's V_local-reset doesn't lose the learned features.

Use when: this spork is round-N of a chain and we want V_net to be the
durable carrier of features across rounds. The slightly higher ctrl
bpc (2.80 vs 2.59) is the cost of consolidation; we eat that locally
to gain durability across rounds.

### Future inference model
When we eventually package an inference checkpoint, we want
stack-3e-2-5.0 settings for the FINAL spork (best raw bpc), preceded
by some number of stack-1e-1-5.0 chain rounds (so V_net carries
consolidated features through). The inference model's V_local is then
reset to small Gaussian and won't be trained at inf time — Net carries
the learned content.

### Knobs that DON'T matter (saturated)
At this scale, neither MMLLM_DISTILL_COEF_END (5→20→50 all give same
Δ_net) nor MMLLM_DISTILL_MAGNITUDE_COEF (off vs on=1.0 same) affects
Δ_net. The distill MSE gradient is already plenty; what's gated is
V_net's per-step movement, controlled by LR_NET_MULT × base LR.
