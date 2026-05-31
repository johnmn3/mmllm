# Corpus mix v2 — agentic file-editing target

The next training run targets a coherent byte-level model that can
emit JSON tool calls to edit files. Concretely: the model output
schema is

```
{"tool_calls": [{"name": "Edit", "args": {"old_str": "...", "new_str": "..."}}]}
```

and the model needs enough surrounding text/code/instruction-following
ability that the tool calls land on real edits, not just well-formed
syntax.

This document describes the corpus mix, the chat template, and the
eval harness that scores ckpts as they roll out of `train-long`.

## What changed from v1 (the pile-github 5B series)

| | v1 (pile-github 5B-plain) | v2 (agent corpus) |
|---|---|---|
| Source | Pile-Github subset (~95 GB) | HF-curated mix (see below) |
| Corpus shape | Raw code bytes | Chat-template-wrapped SFT + raw text mix |
| Output | Free-form continuation | JSON tool calls |
| Bank query mode | `plain` | `ctx-add` |
| Bank feedback | `plain` (none) | `feedback` |
| Mid-training evals | BPC only | BPC + format-validity + tool-call match |

## Datasets (HuggingFace, public, downloadable today)

Pulled via `mmllm prepare-hf-dataset <key> <out-path>` (or from
Modal: `modal run modal_app.py::prepare_hf_dataset --dataset-key <key>`).
All datasets land on the volume in mmllm's standard byte-bin shape:

```
/data/<key>.bin
/data/<key>.train.bin
/data/<key>.val.bin
/data/<key>.test.bin
```

### SFT-style (chat-template wrapped)

| Key | HF Source | Size | Why |
|---|---|---|---|
| `commitpackft` | `bigcode/commitpackft` | 742k examples / ~3 GB | Real GitHub commits → primary edit signal. Becomes JSON `Edit` tool calls. |
| `xlam` | `Salesforce/xlam-function-calling-60k` | 60k | Native JSON function-call traces; teaches the canonical `{tool_calls: [...]}` shape. |
| `magicoder` | `ise-uiuc/Magicoder-Evol-Instruct-110K` | 110k | Code instruction-following; text-only assistant turns scaffold the format around tool calls. |

### Pretraining-style (raw text, `\n\n` joined)

| Key | HF Source | Size | Why |
|---|---|---|---|
| `cosmopedia` | `HuggingFaceTB/cosmopedia-v2` | 25B tokens | Synthetic textbook-quality from Mixtral. "Distillation flavor without doing the distillation." |
| `fineweb-edu` | `HuggingFaceFW/fineweb-edu` (10B sample) | 10B tokens | Curated educational web text; general world knowledge. |
| `the-stack-v2-py` | `bigcode/the-stack-v2-dedup` (Python config) | TB-scale, capped | Code corpus — Python is the agent's primary working language. |
| `the-stack-v2-md` | `bigcode/the-stack-v2-dedup` (Markdown) | TB-scale, capped | Markdown corpus — the agent edits markdown files. |
| `the-stack-v2-sh` | `bigcode/the-stack-v2-dedup` (Shell) | TB-scale, capped | Shell scripts — CLI/agent commands. |

## Proposed mix proportions (target: ~100 B tokens for v2.0 run)

```
30%  the-stack-v2-py         ~30 B tok    Python code
20%  fineweb-edu             ~20 B tok    Web text (general)
15%  cosmopedia              ~15 B tok    Synthetic textbook
10%  the-stack-v2-md         ~10 B tok    Markdown
 8%  commitpackft (×N epochs) ~8 B tok    File-edit examples
 7%  the-stack-v2-sh          ~7 B tok    Shell scripts
 5%  magicoder (×N)           ~5 B tok    Code instructions
 5%  xlam (×N)                ~5 B tok    Tool-call format
```

CommitPackFT/xLAM/Magicoder are smaller than their share — we'll cycle
them across multiple epochs. That's intentional: they're the
format-defining corpora and the model needs to see the JSON tool-call
shape often enough that it locks in early.

This is a starting point. Adjustable via per-dataset cap args to
`prepare_hf_dataset` and the train-time mixer (mixer is a Phase 0.5
build — for now we'll prep separate `.bin` files and concatenate
them via shell into a single training corpus).

## Chat template (locked!)

The byte-level model learns delimiters from the data, so the template
choice is sticky once the first big run starts. Current default
(in `mmllm.datasets.ChatTemplate`):

```
<|sys|>
{system message}
<|end|>
<|user|>
{user message}
<|end|>
<|asst|>
{assistant message — natural language, possibly with embedded
{"tool_calls": [{"name": "...", "args": {...}}]} JSON}
<|end|>
<|tool|>
{tool result, typically JSON}
<|end|>
```

About 14 bytes overhead per turn marker — small relative to the
content and easy for the LM to learn. Tool calls use a single
canonical JSON shape — no schema variation across datasets, even when
the source data uses a different convention (e.g., xLAM's `arguments`
gets normalized to `args`).

If you re-prep with different delimiters AFTER the first ckpt has
rolled, the eval harness will silently mis-score (boundaries won't
match). Re-prep the eval splits too, or burn the ckpt.

## Eval harness

For each ckpt step, the watcher (`modal run modal_app.py::eval_watcher
--base /data/agent-corpus`) runs:

### BPC evals (perplexity-style; cheap)

For each pretraining-style dataset's `.test.bin`: run the existing
`eval-bpc` over the first ~50k tokens. Lower = better. Comparable
across ckpts.

(Note: `eval-bpc-on-path` CLI verb is still TODO — current battery
logs a placeholder for these. Wire when needed.)

### Agentic evals (generation-driven; the interesting metrics)

For each SFT-style dataset's `.test.bin`: split each transcript at
the last `<|asst|>` boundary, generate from the prompt, score the
generated assistant turn against gold:

| Metric | What it measures |
|---|---|
| `format_validity` | Fraction emitting `{"tool_calls": [...]}` JSON. Earliest signal; should hit 0.5+ within the first few B tokens. |
| `tool_name_match` | Of those that parse, fraction calling the right tool. |
| `tool_args_match` | Of those that parse, fraction with byte-identical args. The hard metric. |
| `exact_match` | Prediction byte-equals gold. The hardest. |

Each eval logs one JSONL row per (ckpt_step, eval_name) to
`<base>.eval.jsonl`, same shape as `train-long`'s `eval` event.

## Runbook

```bash
# 1) Prepare the SFT-style datasets (small, fast).
modal run modal_app.py::prepare_hf_dataset --dataset-key commitpackft
modal run modal_app.py::prepare_hf_dataset --dataset-key xlam
modal run modal_app.py::prepare_hf_dataset --dataset-key magicoder

# 2) Smoke-check the format.
modal run modal_app.py::inspect_dataset_remote --path /data/commitpackft.bin

# 3) Prepare pretraining-style sources (long-running; do these in parallel).
modal run --detach modal_app.py::prepare_hf_dataset \
    --dataset-key cosmopedia --max-bytes 25000000000
modal run --detach modal_app.py::prepare_hf_dataset \
    --dataset-key fineweb-edu --max-bytes 30000000000
modal run --detach modal_app.py::prepare_hf_dataset \
    --dataset-key the-stack-v2-py --max-bytes 30000000000

# 4) (Manual mixer step — concat the prepared bins into a single training
#    corpus. Phase-0.5 mixer is TBD. For now: shell concat with
#    proportions tuned via cap args.)

# 5) Launch training (uses ctx+fb mode; logs to /data/agent-corpus.log.jsonl).
modal run --detach modal_app.py::train_with_bank \
    --total-steps 500000 --eval-every 1000 --ckpt-every 5000 \
    --bank-query-mode ctx-add --bank-feedback-mode feedback \
    --base /data/agent-corpus --bank /data/agent-bank \
    --sqrt-n 2048 --batch 128 --lr 1.4e-3 --lr-warmup 3000

# 6) In parallel: launch the eval watcher (cheap A10G, doesn't
#    interfere with the H100 doing training).
modal run --detach modal_app.py::eval_watcher \
    --base /data/agent-corpus --bank /data/agent-bank
```

## Open items (Phase 0.5)

- **Train-time mixer**: a sampler that draws from N prepared bins with
  configurable proportions per step. Right now we'd shell-concat which
  fixes proportions globally. Mixer would let us anneal the SFT
  proportion higher in the second half.
- **`eval-bpc-on-path` CLI verb**: wire BPC evals against an arbitrary
  `.test.bin` path so the BPC half of the battery actually runs.
- **Custom synthetic markdown-edit data**: deferred (per user). Will
  generate ~10-50k examples via API call when the public-data ceiling
  becomes the bottleneck.
- **Loss masking for SFT**: currently we train on the full transcript
  byte stream (continued-pretraining-style). Real SFT masks loss to
  assistant turns only — a parallel mask byte stream + a small change
  in `train-step`. Defer until format-validity plateaus and we want
  the next quality bump.
