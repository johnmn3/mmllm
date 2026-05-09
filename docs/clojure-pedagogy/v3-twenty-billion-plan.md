# v3 — 20B-token phased training plan

Sequel to `v2-real-data-findings.md`. The format-anchor failure at
~6.3B real-world tokens motivated the pivot to synthetic curriculum.
The original pivot recipe called for five corpora (TinyStories,
tiny-lambda, tiny-code, tiny-tool-call, tiny-capstone); this plan
collapses to three because the aesop curriculum is itself the
tiny-capstone AND already contains tiny-lambda + tiny-code patterns
(every record IS a parametric Clojure form), and xLAM provides the
tiny-tool-call signal (varied tool names + arg shapes). Four
training-distinct corpora total: TinyStories, Fables (= capstone),
xLAM (= tool-call), and a Code/Web/Textbook bundle for general
capability. This document is the runbook + tracker for the 20-phase
20B-token curriculum.

## Thesis

Brute-force the format-anchor by ramping xLAM (Tool) hard. v2's
format failure was the symptom of under-weighted xLAM in a noisy
real-world mix. v3 inverts that: keep growing xLAM weight by
+5pp/phase until **either** the model starts passing structural
agentic tests (format_validity climbs off zero) **or** Tool hits
a 50% cap. As soon as the structural skill arrives, fade Tool
back gradually to a 10% skill-keepalive floor, while Web
(FineWeb-Edu) enters and grows to support general capability.

Phase 0 (the first 1B, currently running) is fables-heavy from
random init to anchor the byte-LM on the cleanest synthetic
shape. Phases 1-11 ramp xLAM 2% → 50%. Phases 12-19 fade Tool
back while folding in Web + more Code.

No corpus changes weight by more than **±5 percentage points
between adjacent phases** — so the gradient distribution shifts
smoothly across the 20B run, never violently.

## Phase mix (20 × 1B-token phases)

Columns are integer percentages summing to 100. Single H100 H/W
session per phase, ~1.5-2 h, ~$5-6.

### Ramp (compressed): brute-force to xLAM 50% in 3 phases

The ±5pp/phase budget was too cautious for the format-anchor
problem. v3 uses a compressed ramp: introduce xLAM at 2% to
prime the embedding, then jump directly to 50% by Phase 3.

| #  | tokens     | Fables | TS  | Cos | Web | Tool | Code | Notes |
|----|------------|-------:|----:|----:|----:|-----:|-----:|---|
|  0 | 0–0.5B     |   60   | 15  | 15  |  0  |  0   | 10   | (done) format-anchor target: format_validity > 0.0 |
|  1 | 0.5–1.1B   |   58   | 15  | 15  |  0  |  2   | 10   | (done) xLAM enters; format_validity unchanged |
|  2 | 1.1–1.4B   |   54   | 15  | 15  |  0  |  6   | 10   | (stopped early at step 80k — too cautious) |
|  3 | 1.4–2.0B   |   20   | 10  | 10  |  0  | 50   | 10   | **xLAM 50% cap**: brute-force structural learning |
|  4 |  2-3B      |   20   | 10  | 10  |  0  | 50   | 10   | hold if format_validity still 0; else start fade |
|  5 |  3-4B      |   20   | 10  | 10  |  0  | 50   | 10   | continued hold if needed |

**Hold policy at 50%**: stay at the Phase 3 mix until *either*
`format_validity ≥ 0.05` triggers fade-back, *or* ablation Δ has
plateaued for 3 consecutive eval batteries (signal of bank
saturation → architectural pivot to v3.1).

If format still 0 after 4-5 phases at 50% Tool, that's evidence
the ~70M-class capacity is the ceiling; fall back to v3.1 with
sqrt_n=4096 fp16 (~37GB bank) before continuing the curriculum.

### Fade-back (Phase 12-19): Tool retreats, Web enters

Assumes ramp completed at Phase 11 (Tool 50%). If ramp exited
earlier at Phase X (5-10), jump into the fade-back table at the
row where Tool matches what the ramp left at. The trajectory
shape is the same; the entry point depends on when format passed.

| #  | tokens   | Fables | TS  | Cos | Web | Tool | Code | Notes |
|----|----------|-------:|----:|----:|----:|-----:|-----:|---|
| 12 | 12–13B   |   12   | 15  | 15  |  3  | 45   | 10   | Web enters at 3%, Tool starts fading |
| 13 | 13–14B   |   13   | 15  | 14  |  7  | 40   | 11   | |
| 14 | 14–15B   |   13   | 14  | 14  | 11  | 35   | 13   | |
| 15 | 15–16B   |   13   | 12  | 14  | 15  | 30   | 16   | **Decision gate B**: tool_args_match > 0.3? else hold an extra phase |
| 16 | 16–17B   |   12   | 11  | 13  | 19  | 25   | 20   | |
| 17 | 17–18B   |   12   |  9  | 13  | 23  | 20   | 23   | |
| 18 | 18–19B   |   12   |  7  | 12  | 26  | 15   | 28   | **Decision gate C**: ablation Δ still climbing? else stop early |
| 19 | 19–20B   |   11   |  6  | 12  | 30  | 10   | 31   | end-state, Tool at 10% skill-keepalive floor |

End-state weights at Phase 19: fables 11% (capstone-floor),
TS 6% (grammar-floor), Cos 12% (textbook), Web 30% (general),
Tool 10% (skill-keepalive floor), Code 31% (working language).
Total 100%.

Maximum corpus shift between adjacent phases: 5 percentage
points (Tool always shifts ±5 in the ramp/fade phases; other
corpora shift ±0-3 to absorb).

## Corpus map (column → byte-bin paths)

Each "column" expands to one or more `--mix` entries, with
weights split among the constituents.

| Column | Constituents | Weight split within column |
|---|---|---|
| **Fables** | `/data/aesop-curriculum.bin.train.bin` | 100% (this IS the tiny-capstone; it ALREADY contains tiny-lambda + tiny-code patterns + uniform eval-tool-call shape) |
| **TS** | `/data/tiny-stories.bin.train.bin` | 100% |
| **Cos** | `/data/agent-corpus-v2/cosmopedia.bin.train.bin` | 100% |
| **Web** | `/data/agent-corpus-v2/fineweb-edu.bin.train.bin` | 100% |
| **Tool** | `/data/agent-corpus-v2/xlam.bin.train.bin` | 100% (gated; needs HF token; provides varied tool names + arg shapes which the curriculum's uniform `eval` tool doesn't) |
| **Code** | `/data/agent-corpus-v2/commitpackft-py.bin.train.bin` (50%), `/data/agent-corpus-v2/commitpackft-clj.bin.train.bin` (20%), `/data/agent-corpus-v2/magicoder.bin.train.bin` (20%), `/data/agent-corpus-v2/theorem-qa.bin.train.bin` (10%) | 50/20/20/10 |

The original v2-real-data-findings.md pivot recipe called for
five corpora: tiny-stories, tiny-lambda, tiny-code, tiny-tool-call,
tiny-capstone. This plan collapses to four: TinyStories, Fables
(= tiny-capstone, which already covers tiny-lambda and tiny-code
because every record IS a small Clojure form parametric over
scalar pools), and xLAM (= tiny-tool-call, which already provides
varied tool names + arg shapes — the toy-catalog signal we'd
otherwise have authored from scratch).

## Pre-flight (one-time, before Phase 0)

1. Aesop curriculum byte-bin:
   ```bash
   modal run modal_app.py::build_aesop_curriculum --n-per-example 200
   ```
   ~600 MB — sized to support ≥1B fable tokens through Phase 7.

2. The remaining wired corpora (TS, Cos, Web, xLAM, CommitPackFT,
   Magicoder, TheoremQA) — `prepare_for_prod` stages them all in
   one shot:
   ```bash
   modal run --detach modal_app.py::prepare_for_prod
   ```

3. Confirm symlinks at `/data/agent-corpus-v2.bin.{train,val,test}.bin`
   (the train-long pipeline needs them for in-training eval-bpc).

## Per-phase launch command

Replace `<MIX_STRING>` with the row from the table below, then:

```bash
PHASE=N      # e.g. 1, 2, 3, ...
MIX="<row N from MIX strings table>"

modal run --detach modal_app.py::train_with_bank \
  --base /data/aesop-v3.bin \
  --bank /data/aesop-v3-bank \
  --total-steps 1000000 \
  --max-hours 2.5 \
  --eval-every 2500 \
  --ckpt-every 2500 \
  --batch 128 \
  --sqrt-n 2048 \
  --cpu-offload \
  --lr 1.4e-3 \
  --lr-warmup 3000 \
  --bank-query-mode ctx-add \
  --bank-feedback-mode feedback \
  --ablate-every 5000 \
  --publish-after \
  --tag-prefix aesop-v3 \
  --mix "$MIX"
```

`--total-steps 1000000` is a high cap; sessions exit cleanly on
`max_hours=2.5` (~1.5h training + eval/ckpt overhead) covering
~1B tokens at 22k steps/h × 0.7 (eval+ckpt overhead) × ~256
bytes/seq × 128 batch ≈ 1.0B-1.2B per session.

## MIX strings (full per-phase)

Each below is the `--mix` arg for that phase. Weights are
percentages × 100 to keep integer arithmetic; the sampler
normalizes.

The Code split (10% total) within ramp phases is held constant
at commitpackft-py:5, commitpackft-clj:2, magicoder:2,
theorem-qa:1. In fade-back phases the Code budget grows; the
table below shows a proportional split favoring py over clj.

```
PHASE 0 (Fables 60, TS 15, Cos 15, Tool 0, Code 10):  ← currently running
/data/aesop-curriculum.bin.train.bin:60,/data/tiny-stories.bin.train.bin:15,/data/agent-corpus-v2/cosmopedia.bin.train.bin:15,/data/agent-corpus-v2/commitpackft-py.bin.train.bin:5,/data/agent-corpus-v2/commitpackft-clj.bin.train.bin:2,/data/agent-corpus-v2/magicoder.bin.train.bin:2,/data/agent-corpus-v2/theorem-qa.bin.train.bin:1

PHASE 1 (Fables 58, TS 15, Cos 15, Tool 2, Code 10):
/data/aesop-curriculum.bin.train.bin:58,/data/tiny-stories.bin.train.bin:15,/data/agent-corpus-v2/cosmopedia.bin.train.bin:15,/data/agent-corpus-v2/xlam.bin.train.bin:2,/data/agent-corpus-v2/commitpackft-py.bin.train.bin:5,/data/agent-corpus-v2/commitpackft-clj.bin.train.bin:2,/data/agent-corpus-v2/magicoder.bin.train.bin:2,/data/agent-corpus-v2/theorem-qa.bin.train.bin:1

PHASE 2 (Fables 54, TS 15, Cos 15, Tool 6, Code 10):
/data/aesop-curriculum.bin.train.bin:54,/data/tiny-stories.bin.train.bin:15,/data/agent-corpus-v2/cosmopedia.bin.train.bin:15,/data/agent-corpus-v2/xlam.bin.train.bin:6,/data/agent-corpus-v2/commitpackft-py.bin.train.bin:5,/data/agent-corpus-v2/commitpackft-clj.bin.train.bin:2,/data/agent-corpus-v2/magicoder.bin.train.bin:2,/data/agent-corpus-v2/theorem-qa.bin.train.bin:1

PHASE 3 (Fables 20, TS 10, Cos 10, Tool 50, Code 10):  ← 50% cap brute-force
/data/aesop-curriculum.bin.train.bin:20,/data/tiny-stories.bin.train.bin:10,/data/agent-corpus-v2/cosmopedia.bin.train.bin:10,/data/agent-corpus-v2/xlam.bin.train.bin:50,/data/agent-corpus-v2/commitpackft-py.bin.train.bin:5,/data/agent-corpus-v2/commitpackft-clj.bin.train.bin:2,/data/agent-corpus-v2/magicoder.bin.train.bin:2,/data/agent-corpus-v2/theorem-qa.bin.train.bin:1

PHASE 4 (Fables 45, TS 15, Cos 15, Tool 15, Code 10):
/data/aesop-curriculum.bin.train.bin:45,/data/tiny-stories.bin.train.bin:15,/data/agent-corpus-v2/cosmopedia.bin.train.bin:15,/data/agent-corpus-v2/xlam.bin.train.bin:15,/data/agent-corpus-v2/commitpackft-py.bin.train.bin:5,/data/agent-corpus-v2/commitpackft-clj.bin.train.bin:2,/data/agent-corpus-v2/magicoder.bin.train.bin:2,/data/agent-corpus-v2/theorem-qa.bin.train.bin:1

PHASE 5 (Fables 40, TS 15, Cos 15, Tool 20, Code 10):  ← Early-exit check
/data/aesop-curriculum.bin.train.bin:40,/data/tiny-stories.bin.train.bin:15,/data/agent-corpus-v2/cosmopedia.bin.train.bin:15,/data/agent-corpus-v2/xlam.bin.train.bin:20,/data/agent-corpus-v2/commitpackft-py.bin.train.bin:5,/data/agent-corpus-v2/commitpackft-clj.bin.train.bin:2,/data/agent-corpus-v2/magicoder.bin.train.bin:2,/data/agent-corpus-v2/theorem-qa.bin.train.bin:1

PHASE 6 (Fables 35, TS 15, Cos 15, Tool 25, Code 10):
/data/aesop-curriculum.bin.train.bin:35,/data/tiny-stories.bin.train.bin:15,/data/agent-corpus-v2/cosmopedia.bin.train.bin:15,/data/agent-corpus-v2/xlam.bin.train.bin:25,/data/agent-corpus-v2/commitpackft-py.bin.train.bin:5,/data/agent-corpus-v2/commitpackft-clj.bin.train.bin:2,/data/agent-corpus-v2/magicoder.bin.train.bin:2,/data/agent-corpus-v2/theorem-qa.bin.train.bin:1

PHASE 7 (Fables 30, TS 15, Cos 15, Tool 30, Code 10):
/data/aesop-curriculum.bin.train.bin:30,/data/tiny-stories.bin.train.bin:15,/data/agent-corpus-v2/cosmopedia.bin.train.bin:15,/data/agent-corpus-v2/xlam.bin.train.bin:30,/data/agent-corpus-v2/commitpackft-py.bin.train.bin:5,/data/agent-corpus-v2/commitpackft-clj.bin.train.bin:2,/data/agent-corpus-v2/magicoder.bin.train.bin:2,/data/agent-corpus-v2/theorem-qa.bin.train.bin:1

PHASE 8 (Fables 25, TS 15, Cos 15, Tool 35, Code 10):
/data/aesop-curriculum.bin.train.bin:25,/data/tiny-stories.bin.train.bin:15,/data/agent-corpus-v2/cosmopedia.bin.train.bin:15,/data/agent-corpus-v2/xlam.bin.train.bin:35,/data/agent-corpus-v2/commitpackft-py.bin.train.bin:5,/data/agent-corpus-v2/commitpackft-clj.bin.train.bin:2,/data/agent-corpus-v2/magicoder.bin.train.bin:2,/data/agent-corpus-v2/theorem-qa.bin.train.bin:1

PHASE 9 (Fables 20, TS 15, Cos 15, Tool 40, Code 10):
/data/aesop-curriculum.bin.train.bin:20,/data/tiny-stories.bin.train.bin:15,/data/agent-corpus-v2/cosmopedia.bin.train.bin:15,/data/agent-corpus-v2/xlam.bin.train.bin:40,/data/agent-corpus-v2/commitpackft-py.bin.train.bin:5,/data/agent-corpus-v2/commitpackft-clj.bin.train.bin:2,/data/agent-corpus-v2/magicoder.bin.train.bin:2,/data/agent-corpus-v2/theorem-qa.bin.train.bin:1

PHASE 10 (Fables 15, TS 15, Cos 15, Tool 45, Code 10):
/data/aesop-curriculum.bin.train.bin:15,/data/tiny-stories.bin.train.bin:15,/data/agent-corpus-v2/cosmopedia.bin.train.bin:15,/data/agent-corpus-v2/xlam.bin.train.bin:45,/data/agent-corpus-v2/commitpackft-py.bin.train.bin:5,/data/agent-corpus-v2/commitpackft-clj.bin.train.bin:2,/data/agent-corpus-v2/magicoder.bin.train.bin:2,/data/agent-corpus-v2/theorem-qa.bin.train.bin:1

PHASE 11 (Fables 10, TS 15, Cos 15, Tool 50, Code 10):  ← Tool cap
/data/aesop-curriculum.bin.train.bin:10,/data/tiny-stories.bin.train.bin:15,/data/agent-corpus-v2/cosmopedia.bin.train.bin:15,/data/agent-corpus-v2/xlam.bin.train.bin:50,/data/agent-corpus-v2/commitpackft-py.bin.train.bin:5,/data/agent-corpus-v2/commitpackft-clj.bin.train.bin:2,/data/agent-corpus-v2/magicoder.bin.train.bin:2,/data/agent-corpus-v2/theorem-qa.bin.train.bin:1

PHASE 12 (Fables 12, TS 15, Cos 15, Web 3, Tool 45, Code 10):  ← Fade-back begins; Web enters
/data/aesop-curriculum.bin.train.bin:12,/data/tiny-stories.bin.train.bin:15,/data/agent-corpus-v2/cosmopedia.bin.train.bin:15,/data/agent-corpus-v2/fineweb-edu.bin.train.bin:3,/data/agent-corpus-v2/xlam.bin.train.bin:45,/data/agent-corpus-v2/commitpackft-py.bin.train.bin:5,/data/agent-corpus-v2/commitpackft-clj.bin.train.bin:2,/data/agent-corpus-v2/magicoder.bin.train.bin:2,/data/agent-corpus-v2/theorem-qa.bin.train.bin:1

PHASE 13 (Fables 13, TS 15, Cos 14, Web 7, Tool 40, Code 11):
/data/aesop-curriculum.bin.train.bin:13,/data/tiny-stories.bin.train.bin:15,/data/agent-corpus-v2/cosmopedia.bin.train.bin:14,/data/agent-corpus-v2/fineweb-edu.bin.train.bin:7,/data/agent-corpus-v2/xlam.bin.train.bin:40,/data/agent-corpus-v2/commitpackft-py.bin.train.bin:6,/data/agent-corpus-v2/commitpackft-clj.bin.train.bin:2,/data/agent-corpus-v2/magicoder.bin.train.bin:2,/data/agent-corpus-v2/theorem-qa.bin.train.bin:1

PHASE 14 (Fables 13, TS 14, Cos 14, Web 11, Tool 35, Code 13):
/data/aesop-curriculum.bin.train.bin:13,/data/tiny-stories.bin.train.bin:14,/data/agent-corpus-v2/cosmopedia.bin.train.bin:14,/data/agent-corpus-v2/fineweb-edu.bin.train.bin:11,/data/agent-corpus-v2/xlam.bin.train.bin:35,/data/agent-corpus-v2/commitpackft-py.bin.train.bin:7,/data/agent-corpus-v2/commitpackft-clj.bin.train.bin:3,/data/agent-corpus-v2/magicoder.bin.train.bin:2,/data/agent-corpus-v2/theorem-qa.bin.train.bin:1

PHASE 15 (Fables 13, TS 12, Cos 14, Web 15, Tool 30, Code 16):  ← Decision gate B
/data/aesop-curriculum.bin.train.bin:13,/data/tiny-stories.bin.train.bin:12,/data/agent-corpus-v2/cosmopedia.bin.train.bin:14,/data/agent-corpus-v2/fineweb-edu.bin.train.bin:15,/data/agent-corpus-v2/xlam.bin.train.bin:30,/data/agent-corpus-v2/commitpackft-py.bin.train.bin:9,/data/agent-corpus-v2/commitpackft-clj.bin.train.bin:3,/data/agent-corpus-v2/magicoder.bin.train.bin:3,/data/agent-corpus-v2/theorem-qa.bin.train.bin:1

PHASE 16 (Fables 12, TS 11, Cos 13, Web 19, Tool 25, Code 20):
/data/aesop-curriculum.bin.train.bin:12,/data/tiny-stories.bin.train.bin:11,/data/agent-corpus-v2/cosmopedia.bin.train.bin:13,/data/agent-corpus-v2/fineweb-edu.bin.train.bin:19,/data/agent-corpus-v2/xlam.bin.train.bin:25,/data/agent-corpus-v2/commitpackft-py.bin.train.bin:11,/data/agent-corpus-v2/commitpackft-clj.bin.train.bin:4,/data/agent-corpus-v2/magicoder.bin.train.bin:3,/data/agent-corpus-v2/theorem-qa.bin.train.bin:2

PHASE 17 (Fables 12, TS 9, Cos 13, Web 23, Tool 20, Code 23):
/data/aesop-curriculum.bin.train.bin:12,/data/tiny-stories.bin.train.bin:9,/data/agent-corpus-v2/cosmopedia.bin.train.bin:13,/data/agent-corpus-v2/fineweb-edu.bin.train.bin:23,/data/agent-corpus-v2/xlam.bin.train.bin:20,/data/agent-corpus-v2/commitpackft-py.bin.train.bin:13,/data/agent-corpus-v2/commitpackft-clj.bin.train.bin:5,/data/agent-corpus-v2/magicoder.bin.train.bin:3,/data/agent-corpus-v2/theorem-qa.bin.train.bin:2

PHASE 18 (Fables 12, TS 7, Cos 12, Web 26, Tool 15, Code 28):  ← Decision gate C
/data/aesop-curriculum.bin.train.bin:12,/data/tiny-stories.bin.train.bin:7,/data/agent-corpus-v2/cosmopedia.bin.train.bin:12,/data/agent-corpus-v2/fineweb-edu.bin.train.bin:26,/data/agent-corpus-v2/xlam.bin.train.bin:15,/data/agent-corpus-v2/commitpackft-py.bin.train.bin:15,/data/agent-corpus-v2/commitpackft-clj.bin.train.bin:6,/data/agent-corpus-v2/magicoder.bin.train.bin:4,/data/agent-corpus-v2/theorem-qa.bin.train.bin:3

PHASE 19 (Fables 11, TS 6, Cos 12, Web 30, Tool 10, Code 31):  ← end-state
/data/aesop-curriculum.bin.train.bin:11,/data/tiny-stories.bin.train.bin:6,/data/agent-corpus-v2/cosmopedia.bin.train.bin:12,/data/agent-corpus-v2/fineweb-edu.bin.train.bin:30,/data/agent-corpus-v2/xlam.bin.train.bin:10,/data/agent-corpus-v2/commitpackft-py.bin.train.bin:16,/data/agent-corpus-v2/commitpackft-clj.bin.train.bin:7,/data/agent-corpus-v2/magicoder.bin.train.bin:5,/data/agent-corpus-v2/theorem-qa.bin.train.bin:3
```

## Decision gates

The strategy is **data-gated**: at the end of every ramp phase
(1-11) the operator checks format_validity, and the moment it
crawls off zero, the run jumps from the ramp into the fade-back.
Three named checkpoints below mark the structural decisions.

### Early-exit check — every ramp phase

Read `/data/aesop-v3.bin.eval.jsonl` for the latest `eval_battery`
rows on `xlam` (and secondarily `commitpackft-py`). Trigger
fade-back the moment:

- `format_validity ≥ 0.05` on xLAM, **or**
- `tool_name_match ≥ 0.20` on xLAM (even with format_validity
  still 0 — name matching means the JSON shape is partially
  formed)

If triggered at end of ramp phase N: launch Phase 12 next (the
fade-back's first row). The fade-back assumes the entry Tool
weight is whatever the ramp left at; if you exited at Phase 5
(Tool 20%), launch the row from the fade-back table that has
Tool=20% next, NOT the literal Phase 12 row. The doc's table
shows the canonical post-cap fade; for an early exit, find the
row whose Tool % matches your exit and continue from there.

If neither triggered by end of Phase 11 (Tool=50%): you've
exhausted the "more xLAM" lever. **HOLD** at Phase 11 mix for
ONE more 1B (Phase 11.5) before declaring architectural failure
and pivoting to v3.1 (bigger bank or chat-template revision).

### Decision gate B — end of Phase 15 (15B if no early exit)

Required (mid fade-back, Tool at 30%):

- `format_validity ≥ 0.8` on xLAM
- `tool_args_match ≥ 0.3` on xLAM
- `exact_match ≥ 0.1` on commitpackft-py

If all three: proceed to Phase 16.

If only `format_validity` is met: **HOLD** at Phase 15 mix for
another 1B (give tool_args_match more time to climb before
fading Tool further).

If `format_validity < 0.5`: the ramp didn't actually consolidate
the structural skill. Roll back to the latest pre-fade ckpt and
hold the ramp's peak mix longer.

### Decision gate C — end of Phase 18 (18B)

Required:

- Bank ablation Δ still climbing (compare ablate-every entries
  in the train log; Δ should not have plateaued)
- BPC on FineWeb-Edu ≤ 1.6
- `exact_match ≥ 0.25` on commitpackft-py

If all three: proceed to Phase 19 (end-state lock-in).

If Δ has plateaued: model has saturated current architecture.
Stop at Phase 18 and consider v3.1 with bigger bank
(`sqrt_n=4096 fp16`, ~37 GB) per `parallelization-and-bank-sizing.md`.

## Differential learning rates (router vs bank)

The hypothesis (see `docs/router-bank-lr-decoupling.md`): once the
dense modules — q-projection + K_a/K_b — have learned to route
queries to good bank rows, further updates risk regressing the
router as semantic content shifts. Cool the dense lr after ~9-12B
tokens; cool the bank lr only at the very end.

Implementation has landed (`MMLLM_LR_DENSE_MULT` /
`MMLLM_LR_BANK_MULT` env vars; `--lr-dense-mult` /
`--lr-bank-mult` CLI flags on `train_with_bank`). Defaults
remain `1.0` / `1.0` so Phase 0-8 are unchanged from a
single-lr regime. After the Phase 10-11 empirical test confirms
the hypothesis, switch to the schedule below.

| phase     | tokens   | lr_dense_mult | lr_bank_mult |
|----------:|---------:|--------------:|-------------:|
| 0-8       |  0-9B    |          1.0  |         1.0  |
| 9-11      |  9-12B   |          0.7  |         1.0  |
| 12-14     | 12-15B   |          0.4  |         1.0  |
| 15-17     | 15-18B   |          0.2  |         0.7  |
| 18-19     | 18-20B   |          0.1  |         0.3  |

Adoption is contingent on the Phase 10-11 fork test (one 1B
side-run with `lr_dense_mult=0.5` against the main run; compare
ablation Δ + format_validity + BPC).

## Per-phase tracker

Update this table after each session. `eval-watcher` writes the
metric snapshots; pull them via `progress_report` or read the
last 50 lines of `<base>.eval.jsonl` directly.

| Phase | Tool % | Status      | Date       | wall-h | $    | step at end | lr_d_mult | lr_b_mult | format_validity | tool_args_match | BPC web | BPC cos | ablation Δ | Notes |
|------:|-------:|-------------|------------|-------:|-----:|------------:|----------:|----------:|----------------:|----------------:|--------:|--------:|-----------:|---|
|     0 |   0    | done        | 2026-05-09 |  2.56  |  ~5  |     33,733  |     1.0   |     1.0   |          0.0    |          0.0    |   2.20  |   1.63  |  +2.31     | format-anchor cold (expected; 0% xLAM); bank Δ healthy |
|     1 |   2    | done        | 2026-05-09 |  2.56  |  ~5  |     66,716  |     1.0   |     1.0   |          0.0    |          0.0    |   2.12  |   1.53  |  +5.50     | xLAM 2% — too sparse to move format; bank Δ doubled |
|     2 |   6    | killed      | 2026-05-09 |  ~1.0  |  ~3  |     ~80k    |     1.0   |     1.0   |          0.0    |          0.0    |   2.10  |   1.52  |  +5.25     | killed early — ramp too cautious; user requested compress to 50% by Phase 3 |
|     3 |  50    | done        | 2026-05-09 |  2.55  |  ~5  |    123,153  |     1.0   |     1.0   |          0.0    |          0.0    |   2.11  |   1.53  |  +6.62     | brute-force xLAM 50% on old code; Δ kept climbing but format still 0 |
|     4 |  50*   | pending     |            |        |      |             |     1.0   |    10.0   |                 |                 |         |         |            | NetBank ON (sqrt=8192, c_net=64, +5× lr); Local 10×; switch-3way; xLAM/Glaive/ToolACE/fmt-anchor diverse mix |
|     4 |  15    | pending     |            |        |      |             |     1.0   |     1.0   |                 |                 |         |         |            |   |
|     5 |  20    | pending     | early-exit?|        |      |             |     1.0   |     1.0   |                 |                 |         |         |            | check format_validity |
|     6 |  25    | pending     |            |        |      |             |     1.0   |     1.0   |                 |                 |         |         |            |   |
|     7 |  30    | pending     |            |        |      |             |     1.0   |     1.0   |                 |                 |         |         |            |   |
|     8 |  35    | pending     |            |        |      |             |     1.0   |     1.0   |                 |                 |         |         |            |   |
|     9 |  40    | pending     |            |        |      |             |     0.7   |     1.0   |                 |                 |         |         |            | dense lr cools |
|    10 |  45    | pending     |            |        |      |             |     0.7   |     1.0   |                 |                 |         |         |            |   |
|    11 |  50    | pending     | (Tool cap) |        |      |             |     0.7   |     1.0   |                 |                 |         |         |            | architectural pivot if format still 0 |
|    12 |  45    | pending     | fade-back  |        |      |             |     0.4   |     1.0   |                 |                 |         |         |            | Web enters at 3% |
|    13 |  40    | pending     |            |        |      |             |     0.4   |     1.0   |                 |                 |         |         |            |   |
|    14 |  35    | pending     |            |        |      |             |     0.4   |     1.0   |                 |                 |         |         |            |   |
|    15 |  30    | pending     | (gate B)   |        |      |             |     0.2   |     0.7   |                 |                 |         |         |            |   |
|    16 |  25    | pending     |            |        |      |             |     0.2   |     0.7   |                 |                 |         |         |            |   |
|    17 |  20    | pending     |            |        |      |             |     0.2   |     0.7   |                 |                 |         |         |            |   |
|    18 |  15    | pending     | (gate C)   |        |      |             |     0.1   |     0.3   |                 |                 |         |         |            |   |
|    19 |  10    | pending     | (end)      |        |      |             |     0.1   |     0.3   |                 |                 |         |         |            | skill-keepalive floor |

## Budget estimate

- Per phase: ~$5-6 (1.5-2h H100 + eval watcher)
- 20 phases: **~$100-120 total**
- Within the original $100/wk slow-walk budget; whole curriculum
  fits in 2-3 weeks of $50/wk pace.

## What's wired vs. what needs building

| Item | Status | When |
|---|---|---|
| `build_aesop_curriculum` Modal function | ✓ committed (this branch) | now |
| `prepare_for_prod` Modal function | ✓ exists in `modal_app.py` | now |
| `train_with_bank` with `--mix` | ✓ exists | now |
| `eval_watcher` for in-flight metrics | ✓ exists | now |

## Risks

1. **Format-anchor failure repeats**: same as v2. The capstone
   curriculum is denser-format than the real-world mix v2 used,
   but if `format_validity` doesn't crawl off zero by Phase 5, the
   problem is architectural not data-related and Gate A's pivot
   path applies.
2. **Mid-Phase distribution shock**: each phase's `--mix` is
   static for the duration of the session, so the gradient
   distribution is constant within a 1B-token chunk. The
   between-session shifts (max 5pp per corpus) are the only
   dynamic. This is gentler than v2's "session 3 reshape to 40%
   xLAM" which clearly burned BPC on every other dataset (v2
   findings line 70-83).
3. **Bank Δ flatline before Phase 18**: the bank may saturate at
   sqrt_n=2048 with this much data. Gate C handles this — pivot
   to v3.1 with a bigger bank (`sqrt_n=4096 fp16`, ~37 GB) per
   `parallelization-and-bank-sizing.md`.

## Next action (when ready)

1. Confirm `prepare_for_prod` + `build_aesop_curriculum` have run
   (`modal volume ls mmllm-data /agent-corpus-v2`).
2. Launch the next phase (substitute the desired phase number):
   ```bash
   PHASE=1
   MIX="$(grep "^PHASE ${PHASE} " docs/clojure-pedagogy/v3-twenty-billion-plan.md | head -1 | cut -d':' -f2-)"
   modal run --detach modal_app.py::train_with_bank \
     --base /data/aesop-v3.bin --bank /data/aesop-v3-bank \
     --total-steps 1000000 --max-hours 2.5 \
     --eval-every 2500 --ckpt-every 2500 \
     --batch 128 --sqrt-n 2048 --cpu-offload \
     --lr 1.4e-3 --lr-warmup 3000 \
     --bank-query-mode ctx-add --bank-feedback-mode feedback \
     --ablate-every 5000 --publish-after --tag-prefix aesop-v3 \
     --mix "$MIX"
   ```
3. In a second terminal:
   ```bash
   modal run --detach modal_app.py::eval_watcher \
     --base /data/aesop-v3.bin --bank /data/aesop-v3-bank \
     --sqrt-n 2048 \
     --bank-query-mode ctx-add --bank-feedback-mode feedback \
     --bpc-evals "fineweb-edu:/data/agent-corpus-v2/fineweb-edu.bin.test.bin,cosmopedia:/data/agent-corpus-v2/cosmopedia.bin.test.bin,tinystories:/data/agent-corpus-v2/tinystories.bin.test.bin,aesop:/data/aesop-curriculum.bin.test.bin" \
     --agent-evals "xlam:/data/agent-corpus-v2/xlam.bin.test.bin,commitpackft-py:/data/agent-corpus-v2/commitpackft-py.bin.test.bin,commitpackft-clj:/data/agent-corpus-v2/commitpackft-clj.bin.test.bin"
   ```
4. After each session ends, update the tracker table and decide
   whether to launch the next phase.
