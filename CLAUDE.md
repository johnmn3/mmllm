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

## Active workstreams

- Shared-trunk option A is implemented and verified — `tests/test_shared_trunk.py`
  passes, engagement-fix recipe (commit `85a507a`) produces Δ_local > 0.
- Follow-ups in todo: thread trunk_ids through eval-bpc (so ablation
  measures the N-trunk pool not just trunk-0); fix save_to_mmap
  self-overwrite at end-of-train.
