# v2 real-data slow-walk findings (2026-04 → 2026-05)

Three slow-walk training sessions on `agent-corpus-v2.bin` (mmllm three-tier
attention + sqrt_n=2048 PKM bank, ctx-add + feedback). Stopped at step 198,450
to pivot to a TinyStories-style synthetic-curriculum approach.

## Sessions

| # | step range | wall | mix | notes |
|---|---|---|---|---|
| 1 | 0 → 33,817 | 2.05h | Clojure warmup (coal-mine + clojars + commitpackft-clj + algebraic-stack) | max_hours stop |
| 2 | 33,817 → 162,294 | 8.06h | broader proportional (fineweb-edu, cosmopedia, open-web-math, code-contests, magicoder, …) | max_hours stop |
| 3 | 162,294 → ~198,450 | 2.4h | format-imprint specialization (40% xLAM + 20% commitpackft-py + 12% commitpackft-clj + …) | manual stop — see findings |

Total wall: ~12.5h. Total cost: ~$40 of the $100/wk budget.
Cumulative tokens: ~6.3B (192k steps × 128 batch × ~256 seq_len).

## What worked

### Bank ablation Δ — architectural validation
The PKM bank is doing real work. Δ = `bpc(ablated) − bpc(control)` grew
monotonically across all three sessions:

```
step 5,000   Δ=+0.087   (random-init bank)
step 50,000  Δ=+1.760
step 100,000 Δ=+3.676
step 165,000 Δ=+4.633
step 190,000 Δ=+4.035
```

Without the bank, BPC would be ~4 bits/byte higher. The three-tier-attention
+ product-key-memory architecture is contributing measurably to predictive
capability. **This is the primary positive result.**

### BPC capability across 9 datasets (sessions 1+2)
fineweb-edu BPC fell from 2.97 (step 10k) to 1.72 (step 162k) — solid
pretraining-style learning. Other datasets followed similar trajectories.

### Pipeline maturity
By session 3 the pipeline was production-quality:
- Multi-corpus weighted sampler (`MMLLM_MIX`)
- Modal-driven dataset prep + train + eval
- Auto-publish to GitHub Releases at session end
- Eval watcher with batched basilisp verb (`eval-battery-on-ckpt`)
- Greedy-eval mode for format-critical evaluation
- Per-prediction observability dump

## What didn't work — the format-anchor failure

`format_validity = 0.000` across **every checkpoint, every dataset, every
session.** 60+ ckpt evaluations from step 2,500 → 182,500. Both multinomial
(default) and greedy decoding produce the same result.

### Per-byte argmax at the format-anchor position is wrong
After `<|asst|>\n`, training records ALWAYS start with `{` (verified: 100%
of 1,314 xLAM records, 100% of 649 commitpackft-py records). The model's
greedy argmax for that position is `\t` (Python prompts), `\n` (Markdown
prompts), or alphabet soup (xlam prompts). It has not learned the most basic
format anchor in 192k steps.

### Greedy generation is degenerate
At step 175k under greedy decode:
- commitpackft-py: `\t\t\t\t\t...` (tab loop)
- commitpackft-md: `\n\n\n\n...` (newline loop)
- xlam: `" a |e a an adena  "\n " arin "...` (alphabet soup)

`avg_pred_len = 256.0` exactly — model never emits `\n<|end|>\n` to terminate.

### Session 3 cost without benefit
Session 3's format-imprint mix (40% xLAM + 20% commitpackft-py + 12% clj + …)
regressed BPC on every other dataset:

| dataset | step 162.5k | step 182.5k | Δ |
|---|---|---|---|
| fineweb-edu | 1.76 | 1.89 | +0.13 |
| cosmopedia | 1.38 | 1.47 | +0.09 |
| open-web-math | 1.85 | 2.03 | +0.18 |
| code-contests | 1.41 | 1.70 | +0.29 |
| algebraic-stack | 1.71 | 1.82 | +0.11 |
| theorem-qa | 1.63 | 1.69 | +0.06 |

20k steps of format-specialization paid real BPC cost; format gain remained
zero.

## Diagnosis

The model's effective active capacity (~70M dense + sparse bank gather) is
in the Pythia-70M class — known not to support reliable QA / instruction
following / structured generation under any vanilla pretraining recipe, even
with 300B tokens (Pythia 70M's training volume). Our 6.3B tokens × byte-level
vocab (which makes structural learning ~4× harder per "decision" than BPE)
makes it strictly worse than Pythia 70M for structural-output tasks.

Real-world data (xLAM, commitpackft, magicoder) has poor signal-to-noise
ratio for format-anchor learning: the JSON envelope is 30-40 bytes per
record but every sample also has hundreds of bytes of variable content.
The model spends its capacity learning content distribution and never
sharpens enough on `<|asst|>\n → {`.

## Pivot direction

TinyStories (Eldan & Li 2023) showed 1M-33M parameter models *can* produce
coherent grammatical English **when trained on a curated synthetic
corpus** with constrained vocab and uniform shape. The Phi family extended
this to code via "textbook quality" synthetic data.

Applied to our problem: replace real-world data with a five-corpus synthetic
curriculum, balanced from random init:

1. tiny-stories — English grammar (existing HF corpus)
2. tiny-lambda — `(let […] …) ;=> N` β-reduction
3. tiny-code — small Clojure expressions in isolation
4. tiny-tool-call — fixed toy tool catalog with uniform JSON shape
5. tiny-capstone (heaviest weight) — story + code + tool-call triples
   that semantically entail each other (the cross-modal grounding signal)

Hypothesis: clean synthetic data + joint capstone signal will let the
architecture learn structure that real-world data could not impart.

## Artifacts kept on volume

- `/data/agent-corpus-v2.bin.ckpts/step-{...}/` — all session-1/2/3 ckpts
- `/data/agent-bank-v2.{0..4}.bin` — bank V at session-3 stop point
- `/data/agent-corpus-v2.bin.eval.jsonl` — 847 row eval log
- `/data/agent-corpus-v2.bin.log.jsonl` — train log incl. ablation Δ trajectory
- GitHub Releases `agent-step-N` + `agent-latest` for the published ckpts

These remain as a comparison baseline for the new run: "trained on real-world
mix" vs "trained on clean synthetic curriculum" at matched step counts.
