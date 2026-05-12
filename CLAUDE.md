# Working notes for Claude on this repo

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

## Project shorthand

- **spork** = shared-trunk spoon (option A architecture). 100-step training
  run at the shared-trunk recipe.
- **spoon** = 100-step training run at the cpu-tiny recipe.
- **chain** = N sporks back-to-back, V_local zero-init each round, V_net
  and dense.pt carried forward across rounds.

## Active workstreams

- Shared-trunk option A is implemented and verified — `tests/test_shared_trunk.py`
  passes, engagement-fix recipe (commit `85a507a`) produces Δ_local > 0.
- Follow-ups in todo: thread trunk_ids through eval-bpc (so ablation
  measures the N-trunk pool not just trunk-0); fix save_to_mmap
  self-overwrite at end-of-train.
