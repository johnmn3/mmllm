"""Eval harness for mmllm — score ckpts against the corpora we trained on.

Two families of evals, mirroring the two families in `datasets.py`:

  Pretraining-style (Cosmopedia, FineWeb-Edu, The Stack v2)
    Metric: bits-per-byte on the held-out `.test.bin` split. Already
    implemented in `core/eval-bpc`. Lower is better. Comparable across
    ckpts and across architectures.

  SFT/agentic-style (CommitPackFT, xLAM, …)
    Metrics:
      • format_validity  — fraction of generated assistant turns that
                           parse as well-formed `{"tool_calls": [...]}` JSON
      • tool_name_match  — fraction whose first tool name matches gold
      • tool_args_match  — fraction whose args dict equals gold's
      • exact_match      — fraction byte-identical to gold assistant turn

    Eval data is the held-out `.test.bin` of the prepared SFT corpus.
    We split each transcript at the LAST `<|asst|>\\n` marker:
        prompt = transcript[: idx + len("<|asst|>\\n")]
        gold   = transcript[idx + len("<|asst|>\\n") : end_marker]
    Generate from prompt up to first `<|end|>`, compare to gold.

The harness is generation-driven (model.sample), not perplexity-driven
— format/tool-match metrics are about what the model *produces*, not
what probability mass it puts on gold tokens.

Threading: the basilisp CLI verb `eval-agent` loads the model + bank,
calls into `score_predictions` here for the metric math. Pure-Python
metric code keeps the basilisp side small and the Python side
unit-testable.
"""
from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable

# Import the chat template so we know exactly which delimiters the
# data was prepared with — if you change `datasets.ChatTemplate`
# you MUST re-prep the eval corpora or the boundaries will be wrong.
from mmllm.datasets import ChatTemplate, DEFAULT_TEMPLATE


# ─────────────────────── transcript splitting ───────────────────────


@dataclass
class EvalSample:
    prompt: str   # prefix to feed to the model
    gold:   str   # gold assistant turn body (no <|end|> marker)


def split_transcript(transcript: str,
                     tpl: ChatTemplate = DEFAULT_TEMPLATE
                     ) -> "EvalSample | None":
    """Split a single transcript at the LAST `<|asst|>` marker.

    Returns None if the transcript doesn't have an assistant turn or
    is malformed (e.g., missing `<|end|>` after the asst marker)."""
    idx = transcript.rfind(tpl.asst_open)
    if idx < 0:
        return None
    body_start = idx + len(tpl.asst_open)
    end_idx    = transcript.find(tpl.end, body_start)
    if end_idx < 0:
        return None
    return EvalSample(
        prompt=transcript[:body_start],
        gold=transcript[body_start:end_idx],
    )


def iter_eval_samples(eval_path: str,
                      tpl: ChatTemplate = DEFAULT_TEMPLATE,
                      max_samples: int = 100,
                      # Default sized for the v2 architecture's max_pos=1024
                      # (see default-config in core.lpy) minus typical
                      # gen_len=128 → ~896-byte ceiling on the prompt the
                      # model can attend over without overflowing the RoPE
                      # cache. 768 leaves headroom. Bump if you ever
                      # increase max_pos.
                      max_prompt_bytes: int = 768,
                      ) -> Iterable[EvalSample]:
    """Read a `.test.bin`, partition into transcripts via the `<|sys|>`
    marker, yield up to `max_samples` (prompt, gold) pairs.

    A naive byte-separator split (e.g., `\\n\\n`) breaks because the
    SAME byte pattern occurs inside transcripts — markdown code blocks
    routinely have blank lines, JSON values can have escaped newlines,
    etc. Structural partitioning on `<|sys|>` is unambiguous because
    every formatter in `mmllm.datasets` starts records with that marker.

    Records longer than max_prompt_bytes (after split) are skipped —
    mmllm has a fixed seq-len cap per forward, and we don't want to
    bench the model on prompts it can't see."""
    if not os.path.exists(eval_path):
        raise FileNotFoundError(eval_path)
    with open(eval_path, "rb") as f:
        # For typical `.test.bin` (≤100 MB) read in full; iterate larger
        # files line-by-line if this becomes a memory issue.
        raw = f.read()
    text = raw.decode("utf-8", errors="replace")

    # Locate every <|sys|> position. Each record is the slice from one
    # marker up to the next (or end of buffer for the last). Bytes
    # before the first marker — possible if test.bin starts mid-record
    # because it's the tail of a larger corpus — are ignored.
    sys_marker = tpl.sys_open
    starts = []
    i = 0
    while True:
        j = text.find(sys_marker, i)
        if j < 0:
            break
        starts.append(j)
        i = j + 1

    n = 0
    for k, s in enumerate(starts):
        if n >= max_samples:
            break
        end = starts[k + 1] if k + 1 < len(starts) else len(text)
        # No rstrip: tpl.end = "\n<|end|>\n" (trailing \n is part of
        # the marker), and split_transcript looks for the literal
        # marker. Stripping the trailing \n breaks the match.
        chunk = text[s:end]
        if not chunk.strip():
            continue
        sample = split_transcript(chunk, tpl)
        if sample is None:
            continue
        if len(sample.prompt) > max_prompt_bytes:
            continue
        yield sample
        n += 1


# ─────────────────────── tool-call parsing ───────────────────────


_TOOL_CALL_RE = re.compile(r"\{[^{}]*\"tool_calls\"\s*:.*?\}\s*\}", re.DOTALL)


def extract_tool_call(text: str) -> "dict | None":
    """Pull the first `{"tool_calls": [...]}` JSON object out of a
    generated assistant turn. The regex is greedy-enough to span the
    whole nested structure; we then `json.loads` to confirm validity.

    Real assistant turns may have natural-language preface before the
    JSON ("Sure, I'll edit the file. {...}") — we scan for the first
    valid JSON object containing a `tool_calls` field."""
    # Fast path: try the whole stripped string first.
    s = text.strip()
    if s.startswith("{"):
        try:
            obj = json.loads(s)
            if isinstance(obj, dict) and "tool_calls" in obj:
                return obj
        except json.JSONDecodeError:
            pass

    # Scan for the first `{` that begins a parseable JSON tool-call obj.
    # Brute-force-but-bounded — scan candidate start points, attempt
    # json.loads with progressively longer windows.
    for i, ch in enumerate(text):
        if ch != "{":
            continue
        # Try expanding window to first matching close + check shape.
        depth = 0
        for j in range(i, len(text)):
            if text[j] == "{":
                depth += 1
            elif text[j] == "}":
                depth -= 1
                if depth == 0:
                    candidate = text[i:j+1]
                    try:
                        obj = json.loads(candidate)
                        if isinstance(obj, dict) and "tool_calls" in obj:
                            return obj
                    except json.JSONDecodeError:
                        pass
                    break
    return None


# ─────────────────────── per-sample scoring ───────────────────────


@dataclass
class SampleScore:
    format_valid:    bool
    tool_name_match: bool
    tool_args_match: bool
    exact_match:     bool
    pred_len:        int
    gold_len:        int


def score_sample(prediction: str, gold: str) -> SampleScore:
    """Score a single (prediction, gold) pair across the agentic metrics."""
    exact = prediction.strip() == gold.strip()
    pred_call = extract_tool_call(prediction)
    gold_call = extract_tool_call(gold)
    fmt_ok = pred_call is not None

    name_ok = False
    args_ok = False
    if pred_call and gold_call:
        pc = pred_call.get("tool_calls", [])
        gc = gold_call.get("tool_calls", [])
        # Defensive: tool_calls might decode as ["foo", "bar"] when the
        # model emits a malformed envelope. Only do dict-key compares
        # when both first entries are actually dicts; otherwise treat
        # name/args as not-match (format_valid still set independently).
        if pc and gc and isinstance(pc[0], dict) and isinstance(gc[0], dict):
            name_ok = (pc[0].get("name") == gc[0].get("name"))
            args_ok = (pc[0].get("args") == gc[0].get("args"))

    return SampleScore(
        format_valid=fmt_ok,
        tool_name_match=name_ok,
        tool_args_match=args_ok,
        exact_match=exact,
        pred_len=len(prediction),
        gold_len=len(gold),
    )


# ─────────────────────── batch scoring ───────────────────────


def score_predictions(predictions: list[str], golds: list[str]) -> dict:
    """Aggregate per-sample scores → metric dict.

    Caller (basilisp side) generates predictions via `mmllm.sample`,
    passes them in alongside golds; we do the metric math here.

    Returns dict with rate metrics + sample counts, ready to JSONL."""
    if len(predictions) != len(golds):
        raise ValueError(
            f"length mismatch: {len(predictions)} preds vs {len(golds)} golds"
        )
    n = len(predictions)
    if n == 0:
        return {
            "n_samples":          0,
            "format_validity":    0.0,
            "tool_name_match":    0.0,
            "tool_args_match":    0.0,
            "exact_match":        0.0,
            "avg_pred_len":       0.0,
            "avg_gold_len":       0.0,
        }

    scores = [score_sample(p, g) for p, g in zip(predictions, golds)]
    return {
        "n_samples":       n,
        "format_validity": sum(s.format_valid    for s in scores) / n,
        "tool_name_match": sum(s.tool_name_match for s in scores) / n,
        "tool_args_match": sum(s.tool_args_match for s in scores) / n,
        "exact_match":     sum(s.exact_match     for s in scores) / n,
        "avg_pred_len":    sum(s.pred_len        for s in scores) / n,
        "avg_gold_len":    sum(s.gold_len        for s in scores) / n,
    }


# ─────────────────────── eval battery configuration ───────────────────────


@dataclass
class EvalSpec:
    """One row in the eval battery — points at a `.test.bin` plus
    metadata about how to score it.

    `kind = "bpc"` → run eval-bpc, no generation needed.
    `kind = "agentic"` → run sample-then-score, format/tool-match metrics.
    """
    name:        str   # short label for logs (e.g., "commitpackft")
    test_path:   str   # path to .test.bin on volume
    kind:        str   # "bpc" | "agentic"
    n_samples:   int = 50    # only used for agentic
    gen_len:     int = 512   # generation cap per sample for agentic
    notes:       str = ""

    def to_dict(self) -> dict:
        return asdict(self)


def default_eval_battery(data_root: str = "/data") -> list[EvalSpec]:
    """Default eval battery — assumes you've prepped the standard
    corpus mix at `<data_root>/<key>.test.bin`.

    Adjust paths / which-evals-run-where in your launch script."""
    root = Path(data_root)
    return [
        # Pretraining-style → BPC only
        EvalSpec(name="cosmopedia",
                 test_path=str(root / "cosmopedia.test.bin"),
                 kind="bpc",
                 notes="synthetic textbook bpc"),
        EvalSpec(name="fineweb-edu",
                 test_path=str(root / "fineweb-edu.test.bin"),
                 kind="bpc",
                 notes="curated web bpc"),
        EvalSpec(name="the-stack-v2-py",
                 test_path=str(root / "the-stack-v2-py.test.bin"),
                 kind="bpc",
                 notes="Python code bpc"),
        # SFT/agentic-style → format/tool-match
        EvalSpec(name="commitpackft",
                 test_path=str(root / "commitpackft.test.bin"),
                 kind="agentic",
                 n_samples=50,
                 gen_len=1024,
                 notes="real GitHub commits → Edit tool calls"),
        EvalSpec(name="xlam",
                 test_path=str(root / "xlam.test.bin"),
                 kind="agentic",
                 n_samples=50,
                 gen_len=512,
                 notes="JSON function-call traces"),
    ]


# ─────────────────────── result aggregation ───────────────────────


def append_eval_log(log_path: str, ckpt_step: int,
                    eval_name: str, results: dict,
                    extra: "dict | None" = None) -> None:
    """One JSONL row per (ckpt_step, eval_name) — same shape as
    train-long's eval-event log so we can plot them on the same
    timeline."""
    row = {
        "step":      ckpt_step,
        "event":     "eval_battery",
        "eval_name": eval_name,
        **results,
    }
    if extra:
        row.update(extra)
    Path(log_path).parent.mkdir(parents=True, exist_ok=True)
    with open(log_path, "a") as f:
        f.write(json.dumps(row) + "\n")
