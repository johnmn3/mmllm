# v3 — 20B-token phased training plan

Sequel to `v2-real-data-findings.md`. The format-anchor failure at
~6.3B real-world tokens motivated the pivot to synthetic curriculum
(TinyStories / tiny-lambda / tiny-code / tiny-tool-call /
tiny-capstone). This document is the runbook + tracker for the
20-phase 20B-token curriculum.

## Thesis

Train-up the structural-output capability on a clean synthetic
curriculum first (Phase 1-5: 5B tokens, fables-heavy), then
gradually fold in real-world web text and code while holding the
locked-in skills at floor weights so they don't decay (Phase
6-20: 15B tokens, gradual broadening).

No corpus changes weight by more than **±5 percentage points
between adjacent phases** — so the gradient distribution shifts
smoothly across the 20B run, never violently.

## Phase mix (20 × 1B-token phases)

Columns are integer percentages summing to 100. Single H100 H/W
session per phase, ~1.5-2 h, ~$5-6.

| #  | tokens   | Fables | TS  | Cos | Web | Mini | Tool | Code | Notes |
|----|----------|-------:|----:|----:|----:|-----:|-----:|-----:|---|
|  1 |  0–1B    |   60   | 15  | 15  |  0  |  0   |  0   | 10   | format-anchor target: format_validity > 0.1 |
|  2 |  1–2B    |   60   | 15  | 15  |  0  |  0   |  0   | 10   | hold; consolidate |
|  3 |  2–3B    |   58   | 15  | 15  |  0  |  0   |  2   | 10   | xLAM (Tool) enters at 2% |
|  4 |  3–4B    |   55   | 14  | 16  |  0  |  0   |  4   | 11   | Tool grows; build tiny-lambda **before this phase** |
|  5 |  4–5B    |   50   | 13  | 17  |  0  |  3   |  5   | 12   | Mini (tiny-lambda + tiny-code + tiny-tool-call) enters at 3% |
|  6 |  5–6B    |   45   | 12  | 18  |  2  |  5   |  5   | 13   | **Decision gate A**: web (FineWeb-Edu) enters at 2% if format_validity > 0.5 |
|  7 |  6–7B    |   40   | 12  | 18  |  4  |  7   |  5   | 14   | Fables fade begins |
|  8 |  7–8B    |   35   | 11  | 18  |  6  |  9   |  5   | 16   | Mini grows |
|  9 |  8–9B    |   30   | 10  | 18  |  9  | 11   |  5   | 17   | Web grows |
| 10 |  9–10B   |   25   | 10  | 18  | 12  | 12   |  5   | 18   | midpoint |
| 11 | 10–11B   |   20   |  9  | 18  | 15  | 13   |  5   | 20   | **Decision gate B**: tool_args_match > 0.3? if not, hold P10 mix another 1B |
| 12 | 11–12B   |   17   |  8  | 17  | 18  | 13   |  5   | 22   | code starts growing |
| 13 | 12–13B   |   14   |  8  | 16  | 21  | 12   |  5   | 24   | |
| 14 | 13–14B   |   12   |  7  | 15  | 23  | 11   |  5   | 27   | |
| 15 | 14–15B   |   10   |  7  | 14  | 26  | 10   |  5   | 28   | |
| 16 | 15–16B   |    8   |  6  | 13  | 28  | 10   |  5   | 30   | **Decision gate C**: ablation Δ still climbing? else may be saturating |
| 17 | 16–17B   |    7   |  6  | 13  | 30  |  9   |  4   | 31   | |
| 18 | 17–18B   |    6   |  5  | 12  | 32  |  8   |  4   | 33   | end-state lock-in begins |
| 19 | 18–19B   |    5   |  5  | 12  | 33  |  8   |  4   | 33   | |
| 20 | 19–20B   |    5   |  5  | 12  | 34  |  7   |  4   | 33   | end of curriculum |

End-state weights at Phase 20: fables 5% (skill-floor),
TS 5% (grammar-floor), Cos 12% (textbook), Web 34% (general),
Mini 7% (skill-floor), Tool 4% (format-floor), Code 33% (working
language). Total 100%.

## Corpus map (column → byte-bin paths)

Each "column" expands to one or more `--mix` entries, with
weights split among the constituents.

| Column | Constituents | Weight split within column |
|---|---|---|
| **Fables** | `/data/aesop-curriculum.bin.train.bin` | 100% |
| **TS** | `/data/agent-corpus-v2/tinystories.bin.train.bin` | 100% |
| **Cos** | `/data/agent-corpus-v2/cosmopedia.bin.train.bin` | 100% |
| **Web** | `/data/agent-corpus-v2/fineweb-edu.bin.train.bin` | 100% |
| **Mini** | `/data/tiny-lambda.bin.train.bin` (40%), `/data/tiny-code.bin.train.bin` (30%), `/data/tiny-tool-call.bin.train.bin` (30%) | 40/30/30 |
| **Tool** | `/data/agent-corpus-v2/xlam.bin.train.bin` | 100% (gated; needs HF token) |
| **Code** | `/data/agent-corpus-v2/commitpackft-py.bin.train.bin` (50%), `/data/agent-corpus-v2/commitpackft-clj.bin.train.bin` (20%), `/data/agent-corpus-v2/magicoder.bin.train.bin` (20%), `/data/agent-corpus-v2/theorem-qa.bin.train.bin` (10%) | 50/20/20/10 |

## Pre-flight (one-time, before Phase 1)

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

## Pre-flight before Phase 5 (build the Mini corpora)

The pivot recipe calls for tiny-lambda, tiny-code, tiny-tool-call
as standalone synthetic corpora. They don't yet exist — must be
built before Phase 5 begins (i.e. during Phase 4 wallclock).

Recommended shape (each ~50-100 MB byte-bin, generated parametrically):

- **`tiny-lambda`** — `(let [x N] expr)` reduction examples in
  isolation (no fable prose). Pulls from `mmllm.aesop.curriculum.
  scalar_pools` for slot draws; renders the form + `; => <value>`.
- **`tiny-code`** — small Clojure expressions in isolation
  (atom literals, single-op forms, short HOF compositions). Same
  pool as fables but no narrative wrapper.
- **`tiny-tool-call`** — fixed toy tool catalog (e.g.,
  `add(a:int,b:int)`, `concat(s:str,t:str)`) with uniform JSON
  shape `{"tool_calls":[{"name":"add","args":{"a":3,"b":4}}]}`.
  Tens of thousands of (prompt, tool-call) pairs.

Pseudocode for the Modal function (deferred; build during Phase 4):

```python
@app.function(image=image, volumes={"/data": volume},
              timeout=3600, cpu=4.0, memory=16384)
def build_tiny_corpora():
    """Generate /data/tiny-lambda.bin etc. via parametric draws
    over scalar_pools. Each ~50-100 MB byte-bin. Splits via
    mmllm.corpus.split_pile_github."""
    # ... (impl deferred to Phase 4 wallclock)
```

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

```
PHASE 1+2 (60/15/15/0/0/0/10):
/data/aesop-curriculum.bin.train.bin:60,/data/agent-corpus-v2/tinystories.bin.train.bin:15,/data/agent-corpus-v2/cosmopedia.bin.train.bin:15,/data/agent-corpus-v2/commitpackft-py.bin.train.bin:5,/data/agent-corpus-v2/commitpackft-clj.bin.train.bin:2,/data/agent-corpus-v2/magicoder.bin.train.bin:2,/data/agent-corpus-v2/theorem-qa.bin.train.bin:1

PHASE 3 (58/15/15/0/0/2/10):
/data/aesop-curriculum.bin.train.bin:58,/data/agent-corpus-v2/tinystories.bin.train.bin:15,/data/agent-corpus-v2/cosmopedia.bin.train.bin:15,/data/agent-corpus-v2/xlam.bin.train.bin:2,/data/agent-corpus-v2/commitpackft-py.bin.train.bin:5,/data/agent-corpus-v2/commitpackft-clj.bin.train.bin:2,/data/agent-corpus-v2/magicoder.bin.train.bin:2,/data/agent-corpus-v2/theorem-qa.bin.train.bin:1

PHASE 4 (55/14/16/0/0/4/11):
/data/aesop-curriculum.bin.train.bin:55,/data/agent-corpus-v2/tinystories.bin.train.bin:14,/data/agent-corpus-v2/cosmopedia.bin.train.bin:16,/data/agent-corpus-v2/xlam.bin.train.bin:4,/data/agent-corpus-v2/commitpackft-py.bin.train.bin:6,/data/agent-corpus-v2/commitpackft-clj.bin.train.bin:2,/data/agent-corpus-v2/magicoder.bin.train.bin:2,/data/agent-corpus-v2/theorem-qa.bin.train.bin:1

PHASE 5 (50/13/17/0/3/5/12) — Mini enters; build /data/tiny-* before this phase:
/data/aesop-curriculum.bin.train.bin:50,/data/agent-corpus-v2/tinystories.bin.train.bin:13,/data/agent-corpus-v2/cosmopedia.bin.train.bin:17,/data/tiny-lambda.bin.train.bin:1,/data/tiny-code.bin.train.bin:1,/data/tiny-tool-call.bin.train.bin:1,/data/agent-corpus-v2/xlam.bin.train.bin:5,/data/agent-corpus-v2/commitpackft-py.bin.train.bin:6,/data/agent-corpus-v2/commitpackft-clj.bin.train.bin:3,/data/agent-corpus-v2/magicoder.bin.train.bin:2,/data/agent-corpus-v2/theorem-qa.bin.train.bin:1

PHASE 6 (45/12/18/2/5/5/13):
/data/aesop-curriculum.bin.train.bin:45,/data/agent-corpus-v2/tinystories.bin.train.bin:12,/data/agent-corpus-v2/cosmopedia.bin.train.bin:18,/data/agent-corpus-v2/fineweb-edu.bin.train.bin:2,/data/tiny-lambda.bin.train.bin:2,/data/tiny-code.bin.train.bin:2,/data/tiny-tool-call.bin.train.bin:1,/data/agent-corpus-v2/xlam.bin.train.bin:5,/data/agent-corpus-v2/commitpackft-py.bin.train.bin:7,/data/agent-corpus-v2/commitpackft-clj.bin.train.bin:3,/data/agent-corpus-v2/magicoder.bin.train.bin:2,/data/agent-corpus-v2/theorem-qa.bin.train.bin:1

PHASE 7 (40/12/18/4/7/5/14):
/data/aesop-curriculum.bin.train.bin:40,/data/agent-corpus-v2/tinystories.bin.train.bin:12,/data/agent-corpus-v2/cosmopedia.bin.train.bin:18,/data/agent-corpus-v2/fineweb-edu.bin.train.bin:4,/data/tiny-lambda.bin.train.bin:3,/data/tiny-code.bin.train.bin:2,/data/tiny-tool-call.bin.train.bin:2,/data/agent-corpus-v2/xlam.bin.train.bin:5,/data/agent-corpus-v2/commitpackft-py.bin.train.bin:7,/data/agent-corpus-v2/commitpackft-clj.bin.train.bin:3,/data/agent-corpus-v2/magicoder.bin.train.bin:3,/data/agent-corpus-v2/theorem-qa.bin.train.bin:1

PHASE 8 (35/11/18/6/9/5/16):
/data/aesop-curriculum.bin.train.bin:35,/data/agent-corpus-v2/tinystories.bin.train.bin:11,/data/agent-corpus-v2/cosmopedia.bin.train.bin:18,/data/agent-corpus-v2/fineweb-edu.bin.train.bin:6,/data/tiny-lambda.bin.train.bin:4,/data/tiny-code.bin.train.bin:3,/data/tiny-tool-call.bin.train.bin:2,/data/agent-corpus-v2/xlam.bin.train.bin:5,/data/agent-corpus-v2/commitpackft-py.bin.train.bin:8,/data/agent-corpus-v2/commitpackft-clj.bin.train.bin:3,/data/agent-corpus-v2/magicoder.bin.train.bin:3,/data/agent-corpus-v2/theorem-qa.bin.train.bin:2

PHASE 9 (30/10/18/9/11/5/17):
/data/aesop-curriculum.bin.train.bin:30,/data/agent-corpus-v2/tinystories.bin.train.bin:10,/data/agent-corpus-v2/cosmopedia.bin.train.bin:18,/data/agent-corpus-v2/fineweb-edu.bin.train.bin:9,/data/tiny-lambda.bin.train.bin:4,/data/tiny-code.bin.train.bin:4,/data/tiny-tool-call.bin.train.bin:3,/data/agent-corpus-v2/xlam.bin.train.bin:5,/data/agent-corpus-v2/commitpackft-py.bin.train.bin:9,/data/agent-corpus-v2/commitpackft-clj.bin.train.bin:3,/data/agent-corpus-v2/magicoder.bin.train.bin:3,/data/agent-corpus-v2/theorem-qa.bin.train.bin:2

PHASE 10 (25/10/18/12/12/5/18):
/data/aesop-curriculum.bin.train.bin:25,/data/agent-corpus-v2/tinystories.bin.train.bin:10,/data/agent-corpus-v2/cosmopedia.bin.train.bin:18,/data/agent-corpus-v2/fineweb-edu.bin.train.bin:12,/data/tiny-lambda.bin.train.bin:5,/data/tiny-code.bin.train.bin:4,/data/tiny-tool-call.bin.train.bin:3,/data/agent-corpus-v2/xlam.bin.train.bin:5,/data/agent-corpus-v2/commitpackft-py.bin.train.bin:9,/data/agent-corpus-v2/commitpackft-clj.bin.train.bin:4,/data/agent-corpus-v2/magicoder.bin.train.bin:3,/data/agent-corpus-v2/theorem-qa.bin.train.bin:2

PHASE 11 (20/9/18/15/13/5/20):
/data/aesop-curriculum.bin.train.bin:20,/data/agent-corpus-v2/tinystories.bin.train.bin:9,/data/agent-corpus-v2/cosmopedia.bin.train.bin:18,/data/agent-corpus-v2/fineweb-edu.bin.train.bin:15,/data/tiny-lambda.bin.train.bin:5,/data/tiny-code.bin.train.bin:5,/data/tiny-tool-call.bin.train.bin:3,/data/agent-corpus-v2/xlam.bin.train.bin:5,/data/agent-corpus-v2/commitpackft-py.bin.train.bin:10,/data/agent-corpus-v2/commitpackft-clj.bin.train.bin:4,/data/agent-corpus-v2/magicoder.bin.train.bin:4,/data/agent-corpus-v2/theorem-qa.bin.train.bin:2

PHASE 12 (17/8/17/18/13/5/22):
/data/aesop-curriculum.bin.train.bin:17,/data/agent-corpus-v2/tinystories.bin.train.bin:8,/data/agent-corpus-v2/cosmopedia.bin.train.bin:17,/data/agent-corpus-v2/fineweb-edu.bin.train.bin:18,/data/tiny-lambda.bin.train.bin:5,/data/tiny-code.bin.train.bin:5,/data/tiny-tool-call.bin.train.bin:3,/data/agent-corpus-v2/xlam.bin.train.bin:5,/data/agent-corpus-v2/commitpackft-py.bin.train.bin:11,/data/agent-corpus-v2/commitpackft-clj.bin.train.bin:4,/data/agent-corpus-v2/magicoder.bin.train.bin:5,/data/agent-corpus-v2/theorem-qa.bin.train.bin:2

PHASE 13 (14/8/16/21/12/5/24):
/data/aesop-curriculum.bin.train.bin:14,/data/agent-corpus-v2/tinystories.bin.train.bin:8,/data/agent-corpus-v2/cosmopedia.bin.train.bin:16,/data/agent-corpus-v2/fineweb-edu.bin.train.bin:21,/data/tiny-lambda.bin.train.bin:5,/data/tiny-code.bin.train.bin:4,/data/tiny-tool-call.bin.train.bin:3,/data/agent-corpus-v2/xlam.bin.train.bin:5,/data/agent-corpus-v2/commitpackft-py.bin.train.bin:12,/data/agent-corpus-v2/commitpackft-clj.bin.train.bin:5,/data/agent-corpus-v2/magicoder.bin.train.bin:5,/data/agent-corpus-v2/theorem-qa.bin.train.bin:2

PHASE 14 (12/7/15/23/11/5/27):
/data/aesop-curriculum.bin.train.bin:12,/data/agent-corpus-v2/tinystories.bin.train.bin:7,/data/agent-corpus-v2/cosmopedia.bin.train.bin:15,/data/agent-corpus-v2/fineweb-edu.bin.train.bin:23,/data/tiny-lambda.bin.train.bin:4,/data/tiny-code.bin.train.bin:4,/data/tiny-tool-call.bin.train.bin:3,/data/agent-corpus-v2/xlam.bin.train.bin:5,/data/agent-corpus-v2/commitpackft-py.bin.train.bin:14,/data/agent-corpus-v2/commitpackft-clj.bin.train.bin:5,/data/agent-corpus-v2/magicoder.bin.train.bin:5,/data/agent-corpus-v2/theorem-qa.bin.train.bin:3

PHASE 15 (10/7/14/26/10/5/28):
/data/aesop-curriculum.bin.train.bin:10,/data/agent-corpus-v2/tinystories.bin.train.bin:7,/data/agent-corpus-v2/cosmopedia.bin.train.bin:14,/data/agent-corpus-v2/fineweb-edu.bin.train.bin:26,/data/tiny-lambda.bin.train.bin:4,/data/tiny-code.bin.train.bin:3,/data/tiny-tool-call.bin.train.bin:3,/data/agent-corpus-v2/xlam.bin.train.bin:5,/data/agent-corpus-v2/commitpackft-py.bin.train.bin:14,/data/agent-corpus-v2/commitpackft-clj.bin.train.bin:5,/data/agent-corpus-v2/magicoder.bin.train.bin:6,/data/agent-corpus-v2/theorem-qa.bin.train.bin:3

PHASE 16 (8/6/13/28/10/5/30):
/data/aesop-curriculum.bin.train.bin:8,/data/agent-corpus-v2/tinystories.bin.train.bin:6,/data/agent-corpus-v2/cosmopedia.bin.train.bin:13,/data/agent-corpus-v2/fineweb-edu.bin.train.bin:28,/data/tiny-lambda.bin.train.bin:4,/data/tiny-code.bin.train.bin:3,/data/tiny-tool-call.bin.train.bin:3,/data/agent-corpus-v2/xlam.bin.train.bin:5,/data/agent-corpus-v2/commitpackft-py.bin.train.bin:15,/data/agent-corpus-v2/commitpackft-clj.bin.train.bin:6,/data/agent-corpus-v2/magicoder.bin.train.bin:6,/data/agent-corpus-v2/theorem-qa.bin.train.bin:3

PHASE 17 (7/6/13/30/9/4/31):
/data/aesop-curriculum.bin.train.bin:7,/data/agent-corpus-v2/tinystories.bin.train.bin:6,/data/agent-corpus-v2/cosmopedia.bin.train.bin:13,/data/agent-corpus-v2/fineweb-edu.bin.train.bin:30,/data/tiny-lambda.bin.train.bin:3,/data/tiny-code.bin.train.bin:3,/data/tiny-tool-call.bin.train.bin:3,/data/agent-corpus-v2/xlam.bin.train.bin:4,/data/agent-corpus-v2/commitpackft-py.bin.train.bin:15,/data/agent-corpus-v2/commitpackft-clj.bin.train.bin:6,/data/agent-corpus-v2/magicoder.bin.train.bin:7,/data/agent-corpus-v2/theorem-qa.bin.train.bin:3

PHASE 18 (6/5/12/32/8/4/33):
/data/aesop-curriculum.bin.train.bin:6,/data/agent-corpus-v2/tinystories.bin.train.bin:5,/data/agent-corpus-v2/cosmopedia.bin.train.bin:12,/data/agent-corpus-v2/fineweb-edu.bin.train.bin:32,/data/tiny-lambda.bin.train.bin:3,/data/tiny-code.bin.train.bin:3,/data/tiny-tool-call.bin.train.bin:2,/data/agent-corpus-v2/xlam.bin.train.bin:4,/data/agent-corpus-v2/commitpackft-py.bin.train.bin:16,/data/agent-corpus-v2/commitpackft-clj.bin.train.bin:7,/data/agent-corpus-v2/magicoder.bin.train.bin:7,/data/agent-corpus-v2/theorem-qa.bin.train.bin:3

PHASE 19 (5/5/12/33/8/4/33):
/data/aesop-curriculum.bin.train.bin:5,/data/agent-corpus-v2/tinystories.bin.train.bin:5,/data/agent-corpus-v2/cosmopedia.bin.train.bin:12,/data/agent-corpus-v2/fineweb-edu.bin.train.bin:33,/data/tiny-lambda.bin.train.bin:3,/data/tiny-code.bin.train.bin:3,/data/tiny-tool-call.bin.train.bin:2,/data/agent-corpus-v2/xlam.bin.train.bin:4,/data/agent-corpus-v2/commitpackft-py.bin.train.bin:16,/data/agent-corpus-v2/commitpackft-clj.bin.train.bin:7,/data/agent-corpus-v2/magicoder.bin.train.bin:7,/data/agent-corpus-v2/theorem-qa.bin.train.bin:3

PHASE 20 (5/5/12/34/7/4/33):
/data/aesop-curriculum.bin.train.bin:5,/data/agent-corpus-v2/tinystories.bin.train.bin:5,/data/agent-corpus-v2/cosmopedia.bin.train.bin:12,/data/agent-corpus-v2/fineweb-edu.bin.train.bin:34,/data/tiny-lambda.bin.train.bin:3,/data/tiny-code.bin.train.bin:2,/data/tiny-tool-call.bin.train.bin:2,/data/agent-corpus-v2/xlam.bin.train.bin:4,/data/agent-corpus-v2/commitpackft-py.bin.train.bin:16,/data/agent-corpus-v2/commitpackft-clj.bin.train.bin:7,/data/agent-corpus-v2/magicoder.bin.train.bin:7,/data/agent-corpus-v2/theorem-qa.bin.train.bin:3
```

## Decision gates

Three checkpoints where the operator decides whether to proceed,
hold the current mix for another phase, or pivot.

### Gate A — end of Phase 5 (5B)

Read `/data/aesop-v3.bin.eval.jsonl` for the latest entries.
Required:

- `format_validity ≥ 0.5` on at least one of (xLAM, commitpackft-py)
- `tool_name_match ≥ 0.3` on xLAM
- BPC trajectory monotonically declining on Cos / TS / Web

If all three: proceed to Phase 6 (introduce Web).

If `format_validity < 0.3` after 5B: **HOLD** the Phase 5 mix for
another 1B (60→55→50% fables for one more session). The format
anchor needs more saturation before broadening.

If `format_validity < 0.1` after 7B even with hold: structural
failure. Pivot back to a fables-only run for diagnosis or revisit
the chat-template (the v2 findings imply the byte-LM may not be
learning the `<|asst|>\n → {` transition without higher-density
format-anchor signal).

### Gate B — end of Phase 11 (11B)

Required:

- `format_validity ≥ 0.8` on xLAM
- `tool_args_match ≥ 0.3` on xLAM
- `exact_match ≥ 0.1` on commitpackft-py

If all three: proceed to Phase 12 (continue widening).

If only `format_validity` is met: **HOLD** at Phase 11 mix for
another 1B (give tool_args_match more time to climb).

If `format_validity < 0.5`: Phase 5 gate retroactively failed.
Roll back to the latest pre-Gate-A ckpt and re-think.

### Gate C — end of Phase 16 (16B)

Required:

- Bank ablation Δ still climbing (compare ablate-every entries
  in the train log; Δ should not have plateaued)
- BPC on FineWeb-Edu ≤ 1.6
- `exact_match ≥ 0.25` on commitpackft-py

If all three: proceed to Phase 17. Continue gentle wind-down.

If Δ has plateaued: model has saturated current architecture.
Stop at Phase 16 and consider v3.1 with bigger bank
(`sqrt_n=4096 fp16`, ~37 GB) per `parallelization-and-bank-sizing.md`.

## Per-phase tracker

Update this table after each session. `eval-watcher` writes the
metric snapshots; pull them via `progress_report` or read the
last 50 lines of `<base>.eval.jsonl` directly.

| Phase | Status      | Date       | wall-h | $    | step at end | format_validity | tool_args_match | BPC web | BPC cos | ablation Δ | Notes |
|------:|-------------|------------|-------:|-----:|------------:|----------------:|----------------:|--------:|--------:|-----------:|---|
|     1 | pending     |            |        |      |             |                 |                 |         |         |            |   |
|     2 | pending     |            |        |      |             |                 |                 |         |         |            |   |
|     3 | pending     |            |        |      |             |                 |                 |         |         |            |   |
|     4 | pending     |            |        |      |             |                 |                 |         |         |            |   |
|     5 | pending     | (gate A)   |        |      |             |                 |                 |         |         |            |   |
|     6 | pending     |            |        |      |             |                 |                 |         |         |            |   |
|     7 | pending     |            |        |      |             |                 |                 |         |         |            |   |
|     8 | pending     |            |        |      |             |                 |                 |         |         |            |   |
|     9 | pending     |            |        |      |             |                 |                 |         |         |            |   |
|    10 | pending     |            |        |      |             |                 |                 |         |         |            |   |
|    11 | pending     | (gate B)   |        |      |             |                 |                 |         |         |            |   |
|    12 | pending     |            |        |      |             |                 |                 |         |         |            |   |
|    13 | pending     |            |        |      |             |                 |                 |         |         |            |   |
|    14 | pending     |            |        |      |             |                 |                 |         |         |            |   |
|    15 | pending     |            |        |      |             |                 |                 |         |         |            |   |
|    16 | pending     | (gate C)   |        |      |             |                 |                 |         |         |            |   |
|    17 | pending     |            |        |      |             |                 |                 |         |         |            |   |
|    18 | pending     |            |        |      |             |                 |                 |         |         |            |   |
|    19 | pending     |            |        |      |             |                 |                 |         |         |            |   |
|    20 | pending     | (end)      |        |      |             |                 |                 |         |         |            |   |

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
| `tiny-lambda` byte-bin | ☐ TODO | before Phase 5 |
| `tiny-code` byte-bin | ☐ TODO | before Phase 5 |
| `tiny-tool-call` byte-bin | ☐ TODO | before Phase 5 |
| `build_tiny_corpora` Modal function | ☐ TODO | during Phase 4 wallclock |

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
3. **Mini corpora not built in time**: if Phase 5 starts before
   `tiny-*` exists, drop the Mini column to 0% and re-distribute
   to Fables / Mini-aesop-subjects (atom subjects in fables ARE
   tiny-code-equivalent; can substitute).
4. **Bank Δ flatline before Phase 16**: the bank may saturate at
   sqrt_n=2048 with this much data. Gate C handles this — pivot
   to v3.1 with a bigger bank.

## Next action (when ready)

1. Confirm `prepare_for_prod` + `build_aesop_curriculum` have run
   (`modal volume ls mmllm-data /agent-corpus-v2`).
2. Launch Phase 1:
   ```bash
   MIX="$(grep '^PHASE 1' docs/clojure-pedagogy/v3-twenty-billion-plan.md | head -1 | cut -d':' -f2-)"
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
