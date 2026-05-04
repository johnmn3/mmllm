"""HuggingFace dataset → byte-stream prep for mmllm.

Existing pile-github / text8 / enwik8 prep all converge on the same
on-disk shape:

    /data/<base>.bin            flat uint8 byte stream
    /data/<base>.train.bin      90% (rest = val + test)
    /data/<base>.val.bin        held-out
    /data/<base>.test.bin       held-out

`mmllm train-long` reads `<base>.{train,val,test}.bin` via mmap, so
any new corpus that lands in this shape Just Works with the existing
training loop. This module wraps HF dataset → bytes for that shape.

Two flavors of source:

  Pretraining-style (FineWeb-Edu, Cosmopedia, The Stack v2, …)
    Plain text records. We concatenate with `\\n\\n` separators —
    same convention as the local Clojure scrape in `corpus.py`.

  SFT/agentic-style (CommitPackFT, xLAM, Glaive, Magicoder, …)
    Structured records (instruction + response + tool calls). We
    apply a chat template (see `ChatTemplate`) that produces a
    consistent role-marked byte stream the byte-level LM can learn:

        <|sys|>
        {system msg}
        <|end|>
        <|user|>
        {user msg}
        <|end|>
        <|asst|>
        {assistant msg with embedded JSON tool calls}
        <|end|>
        <|tool|>
        {tool result}
        <|end|>

    Tool calls in assistant turns use a single canonical JSON shape:

        {"tool_calls": [{"name": "<tool>", "args": {...}}]}

    Mixed (text + tool call) assistant turns put text first:

        Sure, I'll edit the file.
        {"tool_calls": [...]}

    Byte-level model learns the delimiters AND the JSON shape from
    the data. No tokenizer hacks — the bytes are the format.

NOTE: All formatters here produce raw text. Loss-masking (i.e.,
"only train on assistant turns") is NOT applied — this is continued-
pretraining-style, where the model sees the full transcript and
learns the format end-to-end. True SFT with loss masking is a Phase 1
addition (would require a parallel mask byte stream the train loop
applies pre-loss).
"""
from __future__ import annotations

import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterable, Iterator

# ─────────────────────── chat template ───────────────────────

@dataclass
class ChatTemplate:
    """ChatML-flavored role markers, but with shorter role names so
    byte-level overhead per turn is ~14 bytes instead of ~24.

    The exact delimiters here are a swappable knob — changing them
    means re-prepping all SFT-style corpora. Lock in early."""
    sys_open:    str = "<|sys|>\n"
    user_open:   str = "<|user|>\n"
    asst_open:   str = "<|asst|>\n"
    tool_open:   str = "<|tool|>\n"
    end:         str = "\n<|end|>\n"

    def system(self, content: str) -> str:
        return f"{self.sys_open}{content}{self.end}"

    def user(self, content: str) -> str:
        return f"{self.user_open}{content}{self.end}"

    def assistant(self, content: str) -> str:
        return f"{self.asst_open}{content}{self.end}"

    def tool(self, content: str) -> str:
        return f"{self.tool_open}{content}{self.end}"

    def assistant_tool_call(self, name: str, args: dict,
                            preface: str = "") -> str:
        """Assistant turn whose payload is a JSON tool call. `preface`
        is optional natural-language text before the JSON (mirrors how
        real agents frequently say "Sure, I'll …" before emitting the
        call).  Single canonical JSON shape so the LM learns one
        format."""
        call = {"tool_calls": [{"name": name, "args": args}]}
        body = (preface + "\n" if preface else "") + json.dumps(call)
        return self.assistant(body)


DEFAULT_TEMPLATE = ChatTemplate()


# ─────────────────────── per-dataset formatters ───────────────────────
#
# A formatter is a callable: record → str (or None to skip).
# Records are dicts straight from `datasets.load_dataset`.
# The string is the formatted bytes for that record.

FormatterFn = Callable[[dict], "str | None"]


def fmt_commitpackft(rec: dict, tpl: ChatTemplate = DEFAULT_TEMPLATE,
                     max_file_bytes: int = 16384) -> "str | None":
    """CommitPackFT (bigcode/commitpackft) → file-edit SFT example.

    Schema:
      old_contents (str), new_contents (str), subject (commit msg),
      lang (file extension), commit (hash).

    Skip rules:
      - Either side > max_file_bytes — keeps long-tail files from
        dominating sequence-length budget.
      - Identical old/new — defensively, no signal.
      - Missing fields.

    Output schema is a JSON tool call to a hypothetical `Edit` tool
    that takes (path, old_str, new_str) — matches Anthropic-style
    file-edit tools."""
    old_c = rec.get("old_contents") or rec.get("old_file")
    new_c = rec.get("new_contents") or rec.get("new_file")
    msg   = rec.get("subject") or rec.get("message") or ""
    lang  = rec.get("lang") or rec.get("language") or "txt"
    if not old_c or not new_c or old_c == new_c:
        return None
    if len(old_c) > max_file_bytes or len(new_c) > max_file_bytes:
        return None

    sys_msg  = ("You are a coding assistant. Apply the requested edit "
                "to the file by emitting an Edit tool call.")
    user_msg = (f"Apply this change: {msg}\n\n"
                f"```{lang}\n{old_c}\n```")
    return (
        tpl.system(sys_msg)
        + tpl.user(user_msg)
        + tpl.assistant_tool_call(
            "Edit",
            {"old_str": old_c, "new_str": new_c},
        )
    )


def fmt_xlam(rec: dict, tpl: ChatTemplate = DEFAULT_TEMPLATE) -> "str | None":
    """xLAM-function-calling-60k (Salesforce/xlam-function-calling-60k).

    Schema:
      query (str user question),
      tools (JSON-string list of available tool schemas),
      answers (JSON-string list of {name, arguments} dicts).

    The `answers` field already IS the canonical tool-call format —
    we just lift it into our wrapper and let the model learn it."""
    query   = rec.get("query")
    tools_s = rec.get("tools")
    ans_s   = rec.get("answers")
    if not query or not ans_s:
        return None
    try:
        answers = json.loads(ans_s) if isinstance(ans_s, str) else ans_s
    except json.JSONDecodeError:
        return None
    if not answers:
        return None

    # Optional: include the tool catalog in the system prompt so the
    # model sees what's available. Truncate aggressively if huge.
    if tools_s and isinstance(tools_s, str) and len(tools_s) < 4000:
        sys_msg = ("You are a tool-using assistant. Available tools:\n"
                   + tools_s)
    else:
        sys_msg = "You are a tool-using assistant."

    # Normalize answer keys: xLAM uses 'arguments', we use 'args'.
    norm_calls = []
    for a in answers:
        if not isinstance(a, dict):
            continue
        norm_calls.append({
            "name": a.get("name") or a.get("tool", ""),
            "args": a.get("arguments") or a.get("args", {}),
        })
    if not norm_calls:
        return None

    asst_body = json.dumps({"tool_calls": norm_calls})
    return (
        tpl.system(sys_msg)
        + tpl.user(query)
        + tpl.assistant(asst_body)
    )


def fmt_magicoder(rec: dict, tpl: ChatTemplate = DEFAULT_TEMPLATE) -> "str | None":
    """Magicoder-Evol-Instruct-110K (ise-uiuc/Magicoder-Evol-Instruct-110K).

    Schema: instruction (str), response (str). Pure text SFT — no
    tool calls. Useful for instruction-following format scaffolding."""
    inst = rec.get("instruction")
    resp = rec.get("response") or rec.get("output")
    if not inst or not resp:
        return None
    sys_msg = "You are a helpful coding assistant."
    return (
        tpl.system(sys_msg)
        + tpl.user(inst)
        + tpl.assistant(resp)
    )


def fmt_cosmopedia(rec: dict) -> "str | None":
    """Cosmopedia-v2 (HuggingFaceTB/cosmopedia-v2).

    Pretraining-style synthetic textbook content. No chat wrapping —
    just the raw text, separated by blank lines downstream. Field
    name varies across configs; try common ones."""
    txt = rec.get("text") or rec.get("content") or rec.get("article")
    if not txt:
        return None
    return txt


def fmt_fineweb_edu(rec: dict) -> "str | None":
    """FineWeb-Edu (HuggingFaceFW/fineweb-edu).

    Pretraining-style web text, educational filter. Plain `text` field."""
    txt = rec.get("text")
    if not txt:
        return None
    return txt


def fmt_the_stack_v2(rec: dict, max_file_bytes: int = 32768) -> "str | None":
    """The Stack v2 (bigcode/the-stack-v2-dedup).

    Pretraining-style code. Field is `content`. Cap at max_file_bytes
    — long files (auto-generated, vendored libs) eat the corpus
    budget without much signal."""
    content = rec.get("content") or rec.get("text")
    if not content:
        return None
    if len(content) > max_file_bytes:
        return None
    return content


def fmt_open_web_math(rec: dict) -> "str | None":
    """OpenWebMath (open-web-math/open-web-math).

    14.7B-token corpus of mathematical text scraped from the web —
    proofs, derivations, math.SE answers, lecture notes. Pretraining-
    style: just the `text` field. Carries the formal-reasoning signal
    we want present throughout training, not just at the end."""
    txt = rec.get("text")
    if not txt:
        return None
    return txt


def fmt_algebraic_stack(rec: dict) -> "str | None":
    """AlgebraicStack — math+code from arXiv (Lean, Coq, Isabelle proofs +
    algorithmic implementations). Available as a config of
    `EleutherAI/proof-pile-2`. Pretraining-style; just emit `text`.

    Why we want this: the formal-proof traces (Lean tactic scripts,
    Coq tactics, Isabelle Isar proofs) expose the model to the
    'softness vs hardness' boundary you can see when a tactic
    succeeds vs gets stuck. Different signal shape from raw code."""
    txt = rec.get("text")
    if not txt:
        return None
    return txt


def fmt_theorem_qa(rec: dict, tpl: ChatTemplate = DEFAULT_TEMPLATE
                   ) -> "str | None":
    """TheoremQA (TIGER-Lab/TheoremQA).

    Theorem statements + answers (numerical or formula). Chat-template
    wrap as Q → A so the model sees the structure. Subject field
    (Calculus, Topology, Number Theory, …) goes in the system message
    so it acts as a topic prior."""
    q = rec.get("Question") or rec.get("question")
    a = rec.get("Answer")  or rec.get("answer")
    if not q or a is None:
        return None
    subject = rec.get("Subject") or rec.get("subject") or ""
    sys_msg = "You are a mathematics assistant."
    if subject:
        sys_msg += f" Topic: {subject}."
    return (
        tpl.system(sys_msg)
        + tpl.user(str(q))
        + tpl.assistant(str(a))
    )


# DeepMind's code_contests language code → human-readable name. Schema
# stores `solutions.language` as a parallel int array; UNKNOWN_LANGUAGE
# is 0 in their proto.
_CC_LANG_NAMES = {0: "Unknown", 1: "Python2", 2: "C++", 3: "Python", 4: "Java"}


def fmt_code_contests(rec: dict, tpl: ChatTemplate = DEFAULT_TEMPLATE,
                      n_accepted: int = 2, n_rejected: int = 2,
                      max_code_bytes: int = 8000) -> "str | None":
    """DeepMind code_contests (deepmind/code_contests).

    Competitive-programming problems with BOTH accepted and rejected
    solutions. The rejected ones are the interesting bit — the model
    sees the boundary between code that works and code that doesn't,
    paired with the same problem statement.

    Returns a string of up to (n_accepted + n_rejected) chat-wrapped
    records concatenated; iter_eval_samples partitions on `<|sys|>`
    so each (problem, solution, verdict) triple is one record.

    Schema (DeepMind's parquet export):
      name, description, cf_rating (int), difficulty (int),
      solutions = {language: [int,...], solution: [str,...]}     (accepted)
      incorrect_solutions = same shape                            (rejected)

    Each emitted record is:

      <|sys|>You are solving a competitive programming problem.
             [Codeforces rating: N.]
      <|user|># {name}\\n\\n{description}
      <|asst|>{code}
      <|tool|>{"verdict": "Accepted"|"Rejected", "language": "Python"|...}

    Python solutions are preferred (lang_id=3) to align with our
    coding-agent target language. Falls back to other languages if
    no Python solution exists."""
    desc = rec.get("description")
    if not desc:
        return None
    name = rec.get("name") or "Unnamed problem"
    cf_rating = rec.get("cf_rating") or 0

    sys_msg = "You are solving a competitive programming problem."
    if cf_rating:
        sys_msg += f" Codeforces rating: {cf_rating}."
    user_msg = f"# {name}\n\n{desc}"

    def _pairs(field):
        """Return list of (lang_id, code) tuples from either the
        dict-of-lists or list-of-dicts representation."""
        if isinstance(field, dict):
            langs = field.get("language", []) or []
            sols  = field.get("solution", []) or []
            return list(zip(langs, sols))
        if isinstance(field, list):
            return [(x.get("language"), x.get("solution"))
                    for x in field if isinstance(x, dict)]
        return []

    def _records(pairs, verdict, cap):
        # Prefer Python (lang_id=3); fall back to others.
        py    = [(l, s) for (l, s) in pairs if l == 3]
        other = [(l, s) for (l, s) in pairs if l != 3]
        out = []
        for lang, code in (py + other)[:cap]:
            if not code or len(code) > max_code_bytes:
                continue
            lang_name = _CC_LANG_NAMES.get(lang, "Unknown")
            tool_payload = json.dumps({"verdict": verdict,
                                        "language": lang_name})
            out.append(
                tpl.system(sys_msg)
                + tpl.user(user_msg)
                + tpl.assistant(code)
                + tpl.tool(tool_payload)
            )
        return out

    accepted = _records(_pairs(rec.get("solutions")),          "Accepted",  n_accepted)
    rejected = _records(_pairs(rec.get("incorrect_solutions")), "Rejected", n_rejected)
    if not accepted and not rejected:
        return None
    return "\n".join(accepted + rejected)


# Registry: dataset key → (HF name, config, split, formatter)
# Add more here as we expand the mix.
DATASET_REGISTRY = {
    # SFT-style (chat-template wrapped)
    #
    # CommitPackFT ships as a per-language dataset script — `load_dataset
    # ("bigcode/commitpackft")` without a config raises "Config name is
    # missing" with the full 277-language list. We expose just a few
    # high-value-for-coding-agent slices (python, markdown, shell,
    # javascript). Add more by appending entries with the same shape;
    # see the language list in the error message or
    # https://huggingface.co/datasets/bigcode/commitpackft.
    "commitpackft-py": {
        "hf_name":   "bigcode/commitpackft",
        "hf_config": "python",
        "split":     "train",
        "formatter": fmt_commitpackft,
        "kind":      "sft",
        "notes":     "Python-language file-edit commits → JSON Edit tool calls",
    },
    "commitpackft-md": {
        "hf_name":   "bigcode/commitpackft",
        "hf_config": "markdown",
        "split":     "train",
        "formatter": fmt_commitpackft,
        "kind":      "sft",
        "notes":     "Markdown-language file-edit commits → JSON Edit tool calls",
    },
    "commitpackft-sh": {
        "hf_name":   "bigcode/commitpackft",
        "hf_config": "shell",
        "split":     "train",
        "formatter": fmt_commitpackft,
        "kind":      "sft",
        "notes":     "Shell-language file-edit commits → JSON Edit tool calls",
    },
    "commitpackft-js": {
        "hf_name":   "bigcode/commitpackft",
        "hf_config": "javascript",
        "split":     "train",
        "formatter": fmt_commitpackft,
        "kind":      "sft",
        "notes":     "JavaScript-language file-edit commits → JSON Edit tool calls",
    },
    "xlam": {
        "hf_name":   "Salesforce/xlam-function-calling-60k",
        "hf_config": None,
        "split":     "train",
        "formatter": fmt_xlam,
        "kind":      "sft",
        "notes":     "60k JSON tool-call traces, single + parallel calls",
    },
    "magicoder": {
        "hf_name":   "ise-uiuc/Magicoder-Evol-Instruct-110K",
        "hf_config": None,
        "split":     "train",
        "formatter": fmt_magicoder,
        "kind":      "sft",
        "notes":     "110k code instruction-following (text only, no tools)",
    },
    # Pretraining-style (raw text, \\n\\n joined)
    "cosmopedia": {
        # The HF repo `HuggingFaceTB/cosmopedia-v2` ships with multiple
        # configs (cosmopedia-v2, fineweb-edu-dedup, python-edu) — the
        # bare dataset name without an explicit config raises
        # "ValueError: Config name is missing". Pick cosmopedia-v2
        # (the synthetic-textbook one) explicitly.
        "hf_name":   "HuggingFaceTB/cosmopedia-v2",
        "hf_config": "cosmopedia-v2",
        "split":     "train",
        "formatter": fmt_cosmopedia,
        "kind":      "pretrain",
        "notes":     "25B tokens of synthetic textbook-quality text",
    },
    "fineweb-edu": {
        "hf_name":   "HuggingFaceFW/fineweb-edu",
        "hf_config": "sample-10BT",
        "split":     "train",
        "formatter": fmt_fineweb_edu,
        "kind":      "pretrain",
        "notes":     "1.3T tokens curated web text; default cfg = 10B sample",
    },
    "the-stack-v2-py": {
        "hf_name":   "bigcode/the-stack-v2-dedup",
        "hf_config": "Python",
        "split":     "train",
        "formatter": fmt_the_stack_v2,
        "kind":      "pretrain",
        "notes":     "Python subset of The Stack v2 dedup",
    },
    "the-stack-v2-md": {
        "hf_name":   "bigcode/the-stack-v2-dedup",
        "hf_config": "Markdown",
        "split":     "train",
        "formatter": fmt_the_stack_v2,
        "kind":      "pretrain",
        "notes":     "Markdown subset of The Stack v2 dedup",
    },
    "the-stack-v2-sh": {
        "hf_name":   "bigcode/the-stack-v2-dedup",
        "hf_config": "Shell",
        "split":     "train",
        "formatter": fmt_the_stack_v2,
        "kind":      "pretrain",
        "notes":     "Shell subset of The Stack v2 dedup",
    },
    # Math + formal reasoning. These don't teach JSON tool calls, but
    # they teach the polynomial-hierarchy-softness/hardness intuition
    # the v2 thesis bets on (formal proofs that succeed vs proofs that
    # don't go through, programs that run vs programs that TLE).
    # Mixed in throughout slow-walk training — not phased.
    "open-web-math": {
        "hf_name":   "open-web-math/open-web-math",
        "hf_config": None,
        "split":     "train",
        "formatter": fmt_open_web_math,
        "kind":      "pretrain",
        "notes":     "14.7B tokens of mathematical web text (proofs, derivations, math.SE)",
    },
    "algebraic-stack": {
        "hf_name":   "EleutherAI/proof-pile-2",
        "hf_config": "algebraic-stack",
        "split":     "train",
        "formatter": fmt_algebraic_stack,
        "kind":      "pretrain",
        "notes":     "Math+code from arXiv: Lean, Coq, Isabelle proofs + algorithmic impls",
    },
    "code-contests": {
        "hf_name":   "deepmind/code_contests",
        "hf_config": None,
        "split":     "train",
        "formatter": fmt_code_contests,
        # 'pretrain' for eval-routing: agentic eval expects JSON tool
        # calls in the assistant turn but code-contests assistant turns
        # are *code*, so format-validity would always be 0.0. BPC eval
        # over the held-out split is the meaningful metric. Training
        # still benefits from chat-template wrapping (problem→solution
        # structure) regardless of eval routing.
        "kind":      "pretrain",
        "notes":     "Competitive-programming problems with accepted + rejected solutions (verdict-tagged)",
    },
    "theorem-qa": {
        "hf_name":   "TIGER-Lab/TheoremQA",
        "hf_config": None,
        "split":     "test",   # TheoremQA only ships a 'test' split publicly
        "formatter": fmt_theorem_qa,
        "kind":      "pretrain",
        "notes":     "Theorem statements + answers across math subjects (Calc, Topology, NT, ...)",
    },
}


# ─────────────────────── prep entry point ───────────────────────


def _human_bytes(n: float) -> str:
    for u in ("B", "KB", "MB", "GB", "TB"):
        if n < 1024:
            return f"{n:.1f} {u}"
        n /= 1024
    return f"{n:.1f} PB"


def _iter_hf(hf_name: str, hf_config: "str | None", split: str
             ) -> Iterator[dict]:
    """Stream records from HF without materializing the whole dataset.

    We use streaming=True so a 25B-token corpus doesn't get materialized
    locally — `prepare_hf_dataset` consumes records lazily and stops
    when it hits the byte cap."""
    from datasets import load_dataset
    if hf_config:
        ds = load_dataset(hf_name, hf_config, split=split, streaming=True)
    else:
        ds = load_dataset(hf_name, split=split, streaming=True)
    yield from ds


def prepare_hf_dataset(
    dataset_key: str,
    out_path:    str,
    max_bytes:   int = 5_000_000_000,
    val_bytes:   int = 50_000_000,
    test_bytes:  int = 50_000_000,
    formatter:   "FormatterFn | None" = None,
) -> dict:
    """Stream a HF dataset, format records, write uint8 byte stream.

    Output layout (mirrors prepare_pile_github):
      <out_path>            .bin flat byte stream
      <out_path>.train.bin
      <out_path>.val.bin
      <out_path>.test.bin

    `dataset_key` looks up DATASET_REGISTRY for HF source + formatter.
    Pass `formatter` to override (useful for testing custom formatters
    against the same HF source).

    Returns a stats dict for logging."""
    if dataset_key not in DATASET_REGISTRY:
        raise ValueError(
            f"unknown dataset key: {dataset_key} "
            f"(known: {sorted(DATASET_REGISTRY)})"
        )
    spec = DATASET_REGISTRY[dataset_key]
    fmt: FormatterFn = formatter or spec["formatter"]

    out = Path(out_path)
    out.parent.mkdir(parents=True, exist_ok=True)

    sep = b"\n\n"  # record separator — same as local Clojure scrape
    written = 0
    n_records = 0
    n_skipped = 0
    print(f"  prepare_hf_dataset[{dataset_key}] → {out_path}",
          flush=True)
    print(f"    hf={spec['hf_name']} config={spec['hf_config']} "
          f"split={spec['split']} cap={_human_bytes(max_bytes)}",
          flush=True)

    with open(out, "wb") as fout:
        for rec in _iter_hf(spec["hf_name"], spec["hf_config"], spec["split"]):
            try:
                formatted = fmt(rec)
            except Exception as e:
                # Per-record formatter errors shouldn't halt a TB run.
                # Count and continue.
                n_skipped += 1
                if n_skipped < 10:
                    print(f"    skip (formatter err): {e}", flush=True)
                continue
            if not formatted:
                n_skipped += 1
                continue
            buf = formatted.encode("utf-8", errors="replace") + sep
            fout.write(buf)
            written += len(buf)
            n_records += 1
            if n_records % 10000 == 0:
                print(f"    {n_records} records  "
                      f"{_human_bytes(written)} written  "
                      f"({n_skipped} skipped)",
                      flush=True)
            if written >= max_bytes:
                print(f"    cap hit at {_human_bytes(written)}", flush=True)
                break

    print(f"  done: {n_records} records / {_human_bytes(written)} "
          f"({n_skipped} skipped)",
          flush=True)

    # Splits via existing corpus.split_pile_github (same shape on disk).
    from mmllm.corpus import split_pile_github
    split_info = split_pile_github(str(out), val_bytes, test_bytes)

    return {
        "dataset_key": dataset_key,
        "out_path":    str(out),
        "bytes":       written,
        "n_records":   n_records,
        "n_skipped":   n_skipped,
        "splits":      split_info,
    }


def inspect_dataset(path: str, n_chars: int = 4000) -> str:
    """Read first n_chars bytes of a prepared `.bin` and decode as UTF-8.

    Useful smoke check after a `prepare_hf_dataset` run — eyeball the
    chat template, JSON shape, etc., before launching a multi-day
    training run on a malformed corpus."""
    if not os.path.exists(path):
        raise FileNotFoundError(path)
    with open(path, "rb") as f:
        buf = f.read(n_chars)
    return buf.decode("utf-8", errors="replace")
