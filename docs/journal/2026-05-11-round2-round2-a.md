# Round 2 worker — round2-a (JSON FIM, sleep-cycle schedule)

## Setup

- date (UTC): 2026-05-11 00:03 → 01:03 (≈59 min wall for training only)
- handle: `round2-a`
- language: json
- source corpus: glaive-function-calling-v2, 20 000 docs already unpacked
  from round 1 — xlam still HF-gated (placeholder token in the prompt was
  the literal `hf_YOUR_READ_TOKEN_HERE`, so substitution carried forward)
- splitter: `json-value-boundary`
- fim_ratio: 0.7  /  psm_ratio: 0.5
- corpus: 13 930 FIM + 6 070 raw-causal docs, train=30.8 MB
- bank: cpu-tiny mmap (Local), in-RAM NetBank (sqrt-n=1024, c_net=32, fp32)
- resume from: round-1's `/tmp/mmllm-cpu/fim-json.ckpts/step-10000/dense.pt`
  (substituted for missing `core/round-1/step-60/dense.pt` — no community
  core was ever published from round 1)

## Schedule

Total span: steps 10 000 → 20 000 (10 000 new training steps with sleep
cycle on top of round 1's 10 000 warmup).

Env vars set for the sleep-cycle schedule:
```
MMLLM_NETBANK_ENABLED=true
MMLLM_NET_SQRT_N=1024       # vs default 8192 (which would be 17GB/layer)
MMLLM_NET_C_NET=32          # vs default 64 (smaller bottleneck)
MMLLM_NET_DTYPE=fp32        # fp16 caused NaN on first step; reverted
MMLLM_NETBANK_ON_GPU=false  # CPU box
MMLLM_LR_WARMUP=15000       # cosine on mults starts at absolute step 15000
MMLLM_LR_BANK_MULT=10       # Local Bank LR 10× (start)
MMLLM_LR_BANK_MULT_END=1    # Local Bank LR 1× (end of cosine)
MMLLM_LR_NET_MULT=1         # NetBank LR 1× (start)
MMLLM_LR_NET_MULT_END=10    # NetBank LR 10× (end of cosine)
MMLLM_ABLATE_EVERY=1000     # report Δ_local and Δ_net at every ckpt
```

Resolved effective LR trajectory (cur-lr is global linear-warmup-then-cosine
between max-lr=3e-3 and min-lr=3e-4):

| step | cur-lr | lr_bank | lr_net | notes |
|------|--------|---------|--------|-------|
| 10000 | 2.0e-3 | 2.0e-2 | 2.0e-3 | round 2 start; Local dominant |
| 15000 | 3.0e-3 | 3.0e-2 | 3.0e-3 | warmup peak; mult cosine begins |
| 17500 | 1.65e-3 | 9.07e-3 | 9.07e-3 | **mult crossover (≈peak lr_net)** |
| 20000 | 3.0e-4 | 3.0e-4 | 3.0e-3 | Local cooled 100× from peak |

**Caveat I want to flag up front**: `MMLLM_LR_WARMUP` controls _both_
the global linear-warmup→cosine decay on `cur-lr` _and_ the start of
the mult cosines, with default `min-lr = max-lr / 10`. That means
NetBank's _absolute_ effective LR doesn't stay high in the last
2 500 steps the way the spec sketched — it peaks ≈9e-3 near step 17500
then descends back to ~3e-3 by step 20000. To get a strict "NetBank
trains at high LR for the last 2 500 steps" I'd need `MMLLM_LR_MIN=MMLLM_LR`
(flatten the global cosine). I picked the trajectory above as a
forward-progress compromise rather than restart from scratch.

## Pipeline issues hit (no in-flight patches; documented per scope rules)

1. **HF_TOKEN was placeholder**, xlam stayed gated, fell back to
   round 1's already-prepared glaive corpus.
2. **`core/round-1/step-60/dense.pt` doesn't exist**: round 1 never
   published a community core. Substituted my own round-1
   `step-10000/dense.pt`.
3. **NetBank default `sqrt_n=8192` × `c_net=64` × fp32 ≈ 17 GB/layer**.
   First launch filled /tmp and crashed bash for several tool calls
   until I cleaned up. Reconfigured to `sqrt_n=1024, c_net=32` (≈ 128MB
   per layer, 512MB total) and retried.
4. **fp16 NetBank → NaN on first step** (`loss=nan (ce=nan plain=nan)
   is NaN or Inf — model may be poisoned`). Reverted to fp32 and it
   trained cleanly.
5. **`load-checkpoint: opt-dense state skipped (topology change?)`** —
   expected, since round 1's dense.pt has no NetBank params; the
   tolerant loader skips the mismatch and the NetBank warm-start
   branch fires (NetBank K_a/K_b copied from Local Bank's K_a/K_b in
   all 4 layers).

## Results (raw)

### Ablation trajectory

| step | ctrl bpc | Δ_local | Δ_net | Δ_both | consolidation_idx |
|------|---------|---------|-------|--------|-------------------|
| 11000 | 1.3264 | +2.1097 | -0.0005 | +2.1199 | baseline |
| 12000 | 1.2551 | +2.0200 | -0.0002 | +2.0262 | +0.0425 |
| 13000 | 1.3040 | +2.7711 | -0.0005 | +2.7930 | -0.3135 |
| 14000 | 1.2753 | +2.5321 | -0.0014 | +2.5419 | -0.2002 |
| 15000 | 1.1720 | +2.9343 | -0.0002 | +3.0648 | -0.3908 |
| 16000 | 1.1738 | +3.0865 | -0.0017 | +3.1163 | -0.4630 |
| 17000 | 1.0745 | +3.3067 | -0.0006 | +3.3370 | -0.5673 |
| 18000 | 1.0053 | +3.4852 | -0.0000 | +3.5079 | -0.6520 |
| 19000 | 0.9457 | +3.6348 | **+0.0001** | +3.6453 | -0.7229 |
| 20000 | 0.9258 | +3.7618 | **+0.0005** | +3.7705 | -0.7831 |

**Δ_net trajectory**: stayed at -0.0005 to -0.0017 for the entire
warmup phase (steps 11k–18k), then crept to +0.0001 at step 19000 and
+0.0005 at step 20000. The crossing IS technically in the right
direction, but it's well within run-to-run noise (round 1 had Δ_net
fluctuating between similar tiny negative values).

**Δ_local trajectory**: grew monotonically from +2.11 to +3.76 (Local
Bank carries 1.65 bpc MORE signal at end of round 2 than at end of
round 1). The consolidation index went the wrong direction — Local is
becoming MORE essential, not less. The sleep cycle did not transfer
signal from Local to NetBank.

### Train trajectory

- final train loss (step 20000): 1.041
- final val_bpc (control): **1.0626** (vs round-1's 1.5675 — 32 % drop)
- val_bpc with Local zeroed: 4.6900 (Δ_local = +3.6274 end-of-run)
- tps (steady state): ~2 000 tok/sec (slower than round 1's ~5 000
  because of NetBank's extra forward + simulated 1–10 ms WAN delay)
- total wall (train only): 3 540 s (≈ 59 min)
- energy estimate: 0.0659 kWh / 36 gCO₂eq

### FIM eval (step 20 000)

```
=== FIM eval summary (11 examples) ===
  language     n   bytes     bpc    exact%
   clojure     3      67   4.653       0.0
   generic     1      16   3.326       0.0
      json     5     147   2.955       0.0
    python     2      30   4.385       0.0
   OVERALL  ----     260   3.580       0.0
```

Compared to round 1 (step 10 000):

| row | round 1 | round 2 | Δ |
|------|---------|---------|---|
| OVERALL bpc | 4.802 | 3.580 | -1.22 |
| json bpc | 3.846 | 2.955 | -0.89 |
| clojure bpc | 6.315 | 4.653 | -1.66 |
| python bpc | 6.270 | 4.385 | -1.89 |
| generic bpc | 4.496 | 3.326 | -1.17 |
| OVERALL exact% | 0.0 | 0.0 | 0.0 |

All languages improved (even unseen ones — cross-language generalization
is real). Still no exact-match FIM completions.

### Agent eval (glaive, 10 usable samples)

```
eval-agent[glaive]: ckpt=20000 test=...glaive.test.bin n=100 gen=128
iter_eval_samples returned 10 samples (max_prompt_bytes=376)
→ format=0.000  name=0.000  args=0.000  exact=0.000  (9.5s)
```

Same caveats as round 1: glaive.test.bin has zero positive-class
samples and only 10 of 1 994 prompts fit cpu-tiny's 376-byte window.
`format_validity` is the only metric here that could move; it stayed
at 0.

Representative decoded outputs at step 20 000 (greedy, gen-len 128):

```
[sample 0]
  PRED: '<|> helpri adasistratimoimemotillolemenucheementacethenomess
          toforenchect raconsessabutet, tifiluotres tythith fisen taseveret t'
  GOLD: "I'm sorry, but as an AI, I don't have the capability..."

[sample 4]
  PRED: 'The a hitin tas f tacorandatot", is art wonda, tevet ranurarestrenieathani
          thomass woprith pisen masefuest ", tesureract..."
```

The model has accumulated more recognizable pseudo-English now (still
no valid JSON envelope). Notably, samples 0/2/8/9 all produce the
*same* output ("helpri adasistratim..."), suggesting modest memorization
of a refusal-class pattern for "Can you order a pizza?" prompts.

## Decision

**Δ_net target (> 0): technically met, but signal is within noise.**
The headline value at step 20 000 is +0.0005 bpc — positive, but only
by a hair, and round-to-round natural variance in this measurement is
on the same order of magnitude.

**val_bpc target (≤ round 1): substantially exceeded.** 1.5675 →
1.0626 is a 32 % drop. The doubled training compute (10 k → 20 k
cumulative steps) does most of the work here; the LR schedule isn't
strictly necessary for this improvement.

**Δ_local target (still strong): yes.** +2.11 → +3.76. Local Bank
strengthened across round 2, which makes sense given it ran at 10× LR
through the warmup phase.

**consolidation_idx (intended direction): went the wrong way.** Started
at baseline (0.0), ended at −0.78. Negative = Local is _more_ essential
than before. The sleep cycle did not transfer signal Local → NetBank
the way the plan called for.

**Mechanistic note (for the round-3 prompter):** NetBank's V starts at
fresh init (only K_a/K_b are warm-started from Local Bank). For NetBank
to carry signal, V must accumulate trained content via SparseAdam +
the c_net=32 → q_dim expander. Even at NetBank's effective LR peak
(~9e-3 around step 17 500), 2 500 steps × batch 4 × seq 128 = ~1.3 M
tokens isn't enough updates per retrieved row to move V meaningfully
above zero. The sleep cycle works as a _scheduling_ pattern but the
NetBank tier needs either a longer warm phase or a non-zero V init
(perhaps copying Local Bank's V into NetBank's first 64 k rows alongside
the K_a/K_b copy that already happens) for Δ_net to escape the noise
floor.

## Notes / surprises

- **Δ_local kept GROWING through round 2.** I expected it to plateau or
  drop slightly (since Local LR cools 100× during the sleep cycle).
  Instead it climbed from +2.93 at step 15 000 to +3.76 at step 20 000.
  Interpretation: even cooled Local LR (3e-4) is doing real work; the
  retrieved-row Adam updates with momentum carry the bank forward.
- **Cross-language FIM-bpc improvement is real.** All four languages
  dropped 0.89–1.89 bpc, despite training only on JSON. Suggests the
  byte-level prior is doing more than language-specific routing.
- **Glaive.test.bin filter inefficiency**: median prompt is 1 487 B vs
  cpu-tiny's 376 B usable window → 0.5% pass rate. The 10 usable
  samples are all refusal-class (no tool_calls in gold). Agent eval is
  measuring `format_validity` (can model spontaneously emit valid
  JSON?) but cannot measure `name_match` / `args_match` / `exact_match`
  — they're pinned at 0 by data, not by model.
- **Per-sample prediction memorization.** Multiple "Can you order a
  pizza?" prompts get _identical_ 128-byte gibberish responses
  ("helpri adasistratim..."). The model has memorized a refusal-class
  byte sequence; it's repeating that sequence reliably; it just isn't
  a valid JSON envelope.

## Artifacts

- ckpt: `/tmp/mmllm-cpu/fim-json.ckpts/step-20000/dense.pt` (12 MB) →
  copied to `workers/round2-a/step-20000/dense.pt`
- bank V: `/tmp/mmllm-cpu/fim-bank.{0..3}.bin` (Local), in-RAM only
  for NetBank (not saved as separate worker artifact per scope rules
  about not committing per-worker bank state)
- meta.json: `workers/round2-a/step-20000/meta.json`
- train log: `/tmp/mmllm-cpu/fim-json.round2.train.log`
- FIM-eval log: `/tmp/mmllm-cpu/fim-json.round2.fim-eval.txt`
- agent-eval log: `/tmp/mmllm-cpu/fim-json.round2.agent-eval.txt`
- agent-eval verbose (predictions): `/tmp/mmllm-cpu/fim-json.round2.agent-eval-verbose.txt`
