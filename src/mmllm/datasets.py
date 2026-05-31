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
import re
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


_GLAIVE_FUNCALL_RE = re.compile(
    r"<functioncall>\s*(\{.*?\})\s*</functioncall>", re.DOTALL
)
_HERMES_TOOLCALL_RE = re.compile(
    r"<tool_call>\s*(\{.*?\})\s*</tool_call>", re.DOTALL
)


def _normalize_tool_call_dict(d: dict) -> "dict | None":
    """Coerce a vendor-specific tool-call dict into our canonical
    {name, args} shape. Returns None if not parseable.

    Inputs we see in the wild:
      Glaive:   {"name": "X", "arguments": "{json-string}"}
      Hermes:   {"name": "X", "arguments": {parsed-json}}
      OpenAI:   {"name": "X", "arguments": "{json-string}"}
      ToolACE:  {"name": "X", "arguments": {...}}  (sometimes "args")
    """
    if not isinstance(d, dict):
        return None
    name = d.get("name") or d.get("tool")
    if not name:
        return None
    args = d.get("arguments")
    if args is None:
        args = d.get("args")
    if args is None:
        args = {}
    # Glaive's "arguments" is often a JSON-encoded STRING; parse it.
    if isinstance(args, str):
        try:
            args = json.loads(args)
        except json.JSONDecodeError:
            # Some entries have malformed JSON in arguments; keep the
            # string as-is so the model still sees the structure.
            args = {"_raw": args}
    if not isinstance(args, dict):
        args = {"value": args}
    return {"name": name, "args": args}


def fmt_glaive(rec: dict, tpl: ChatTemplate = DEFAULT_TEMPLATE) -> "str | None":
    """Glaive-function-calling-v2 (glaiveai/glaive-function-calling-v2).

    Schema: chat is a single big string with role-prefixed turns,
    plus a `system` field containing the tool catalog.

    The assistant turn embeds tool calls inside <functioncall>{json}</functioncall>
    XML wrappers. We MUST strip the wrappers before emitting — leaving
    them in would teach the byte-LM the wrong anchor (our anchor is
    `<|asst|>\\n` immediately followed by raw JSON, no XML).

    Output: standard system + (multi) user/asst/tool turns. For asst
    turns whose body contains a <functioncall>, replace the wrapper +
    inner JSON with our canonical {"tool_calls":[{...}]}; everything
    outside the wrapper is dropped to keep the anchor adjacency clean.
    """
    chat = rec.get("chat")
    sys_field = rec.get("system")
    if not isinstance(chat, str) or not chat.strip():
        return None
    sys_msg = sys_field.strip() if isinstance(sys_field, str) and sys_field.strip() else \
              "You are a tool-using assistant."

    # Glaive's chat string uses literal "USER:", "ASSISTANT:", "FUNCTION RESPONSE:"
    # role prefixes. Split on them.
    role_re = re.compile(r"\b(USER|ASSISTANT|FUNCTION RESPONSE):\s*")
    parts = role_re.split(chat)
    # split returns ['', 'USER', '<text>', 'ASSISTANT', '<text>', ...]
    if len(parts) < 3:
        return None

    out = [tpl.system(sys_msg)]
    i = 1
    saw_asst = False
    while i + 1 < len(parts):
        role = parts[i].strip()
        body = parts[i + 1].strip()
        i += 2
        if not body:
            continue
        if role == "USER":
            out.append(tpl.user(body))
        elif role == "ASSISTANT":
            m = _GLAIVE_FUNCALL_RE.search(body)
            if m:
                try:
                    inner = json.loads(m.group(1))
                except json.JSONDecodeError:
                    continue
                norm = _normalize_tool_call_dict(inner)
                if norm is None:
                    continue
                # Emit ONLY the canonical JSON in the asst turn — drop the
                # natural-language preface and anything outside the
                # <functioncall> wrapper. Keeps `<|asst|>\n` adjacent to `{`.
                out.append(tpl.assistant(json.dumps({"tool_calls": [norm]})))
                saw_asst = True
            else:
                # Plain assistant text turn (no tool call)
                out.append(tpl.assistant(body))
                saw_asst = True
        elif role == "FUNCTION RESPONSE":
            out.append(tpl.tool(body))
    if not saw_asst:
        return None
    return "".join(out)


def fmt_hermes_funcall(rec: dict, tpl: ChatTemplate = DEFAULT_TEMPLATE) -> "str | None":
    """NousResearch/hermes-function-calling-v1 (any subset).

    Schema (typical): conversations = [{"from": "system"/"human"/"gpt"/"tool",
                                         "value": "<text>"}].

    The assistant turns ('gpt') wrap tool calls in <tool_call>{json}</tool_call>
    XML. Same problem and same fix as Glaive — strip the wrapper, emit
    raw canonical JSON adjacent to <|asst|>\\n.
    """
    convs = rec.get("conversations") or rec.get("messages")
    if not isinstance(convs, list) or not convs:
        return None

    out = []
    saw_asst = False
    for turn in convs:
        if not isinstance(turn, dict):
            continue
        role = (turn.get("from") or turn.get("role") or "").lower()
        body = turn.get("value") or turn.get("content")
        if not isinstance(body, str) or not body.strip():
            continue
        body = body.strip()
        if role in ("system",):
            out.append(tpl.system(body))
        elif role in ("human", "user"):
            out.append(tpl.user(body))
        elif role in ("gpt", "assistant"):
            m = _HERMES_TOOLCALL_RE.search(body)
            if m:
                try:
                    inner = json.loads(m.group(1))
                except json.JSONDecodeError:
                    continue
                norm = _normalize_tool_call_dict(inner)
                if norm is None:
                    continue
                out.append(tpl.assistant(json.dumps({"tool_calls": [norm]})))
                saw_asst = True
            else:
                out.append(tpl.assistant(body))
                saw_asst = True
        elif role in ("tool", "function"):
            out.append(tpl.tool(body))
    if not saw_asst:
        return None
    return "".join(out)


def fmt_toolace(rec: dict, tpl: ChatTemplate = DEFAULT_TEMPLATE) -> "str | None":
    """Team-ACE/ToolACE.

    Schema: conversations = [{"from": "system"/"user"/"assistant"/"tool",
                              "value": "<text>"}]. Some splits use
    `messages` with `role` instead of `from`.

    Assistant tool-call turns: body is a JSON-encoded LIST of calls
    (no XML wrapper, but the whole body is the JSON list, not our
    {"tool_calls": [...]} object). We detect a leading `[` and convert.

    Plain assistant text turns are emitted verbatim. ToolACE has very
    diverse API schemas (~26k pool) — that's the diversity benefit.
    """
    convs = rec.get("conversations") or rec.get("messages")
    if not isinstance(convs, list) or not convs:
        return None

    out = []
    saw_asst = False
    for turn in convs:
        if not isinstance(turn, dict):
            continue
        role = (turn.get("from") or turn.get("role") or "").lower()
        body = turn.get("value") or turn.get("content")
        if not isinstance(body, str) or not body.strip():
            continue
        body = body.strip()
        if role == "system":
            out.append(tpl.system(body))
        elif role in ("user", "human"):
            out.append(tpl.user(body))
        elif role in ("assistant", "gpt"):
            # ToolACE's assistant tool-call turns are a JSON list of dicts.
            if body.startswith("[") and "name" in body[:200]:
                try:
                    parsed = json.loads(body)
                except json.JSONDecodeError:
                    out.append(tpl.assistant(body))
                    saw_asst = True
                    continue
                if isinstance(parsed, list):
                    norms = [
                        n for n in (_normalize_tool_call_dict(c) for c in parsed)
                        if n is not None
                    ]
                    if norms:
                        out.append(
                            tpl.assistant(json.dumps({"tool_calls": norms}))
                        )
                        saw_asst = True
                        continue
            # Fallback: plain text assistant turn
            out.append(tpl.assistant(body))
            saw_asst = True
        elif role in ("tool", "function"):
            out.append(tpl.tool(body))
    if not saw_asst:
        return None
    return "".join(out)


def fmt_format_anchor(rec: dict, tpl: ChatTemplate = DEFAULT_TEMPLATE) -> "str | None":
    """Format-only warmup variant.

    Takes any tool-call record (xLAM/Glaive/ToolACE) and replaces the
    argument VALUES with placeholders while keeping argument NAMES
    and the JSON skeleton intact. The model sees the same structural
    pattern over and over with different surface content stripped:

        {"tool_calls":[{"name":"<TOOL>","args":{"a":"X","b":0,"c":[]}}]}

    Goal (Schema-RL / SLOT 2025): hammer the schema skeleton into the
    byte distribution before content learning, so format_validity can
    crawl off zero. Trains on `xlam` records (preferred — most uniform).
    """
    query   = rec.get("query") or rec.get("instruction") or "What's the answer?"
    ans_s   = rec.get("answers")
    if not ans_s:
        return None
    try:
        answers = json.loads(ans_s) if isinstance(ans_s, str) else ans_s
    except json.JSONDecodeError:
        return None
    if not isinstance(answers, list) or not answers:
        return None

    norm_calls = []
    for a in answers:
        if not isinstance(a, dict):
            continue
        name = a.get("name") or a.get("tool")
        if not name:
            continue
        args = a.get("arguments") or a.get("args") or {}
        if isinstance(args, str):
            try:
                args = json.loads(args)
            except json.JSONDecodeError:
                args = {}
        if not isinstance(args, dict):
            args = {}
        # Replace each value with a placeholder of matching type
        masked = {}
        for k, v in args.items():
            if isinstance(v, bool):
                masked[k] = False
            elif isinstance(v, (int, float)):
                masked[k] = 0
            elif isinstance(v, list):
                masked[k] = []
            elif isinstance(v, dict):
                masked[k] = {}
            else:
                masked[k] = "X"
        # Keep the tool name (low cardinality, helps anchor) but drop
        # the user query content
        norm_calls.append({"name": name, "args": masked})
    if not norm_calls:
        return None

    asst_body = json.dumps({"tool_calls": norm_calls})
    return (
        tpl.system("You are a tool-using assistant.")
        + tpl.user("Q.")
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


def fmt_cosmopedia(rec: dict, tpl: ChatTemplate = DEFAULT_TEMPLATE) -> "str | None":
    """Cosmopedia-v2 (HuggingFaceTB/cosmopedia-v2).

    Pretraining-style synthetic textbook content. Wrapped in ChatTemplate
    as a single assistant turn with a routing-hint system message so the
    byte distribution at training time matches the other (SFT/agentic)
    corpora — the model sees `<|sys|>...<|asst|>...<|end|>` envelopes
    everywhere, never bare text. The system message lets the model
    route on "this is textbook-style content" vs other domains."""
    txt = rec.get("text") or rec.get("content") or rec.get("article")
    if not txt:
        return None
    return tpl.system("You are a textbook author. Produce clear, accurate prose.") + tpl.assistant(txt)


def fmt_fineweb_edu(rec: dict, tpl: ChatTemplate = DEFAULT_TEMPLATE) -> "str | None":
    """FineWeb-Edu (HuggingFaceFW/fineweb-edu).

    Pretraining-style web text, educational filter. Wrapped in
    ChatTemplate envelope to match the rest of the corpus mix — see
    fmt_cosmopedia comment for the rationale."""
    txt = rec.get("text")
    if not txt:
        return None
    return tpl.system("You are a writer producing educational web content.") + tpl.assistant(txt)


def fmt_tiny_stories(rec: dict) -> "str | None":
    """TinyStories (roneneldan/TinyStories).

    ~2.1M short stories with constrained vocab (~2k words, 3-year-old
    reading level), generated by GPT-3.5/4. The Eldan & Li 2023 result:
    1M-33M parameter models can produce coherent grammatical English when
    trained on this corpus. We use it as the basic-English-grammar
    foundation in the post-pivot two-corpus mix (paired with the
    aesop-capstone synthetic corpus for joint code/structure/narrative
    grounding).

    Schema: just `text` field with the story body. Wrapped in
    ChatTemplate envelope to match the rest of the corpus mix — see
    fmt_cosmopedia comment for the rationale."""
    txt = rec.get("text")
    if not txt:
        return None
    return DEFAULT_TEMPLATE.system("You are telling a short children's story.") + DEFAULT_TEMPLATE.assistant(txt)


def fmt_the_stack_v2(rec: dict, max_file_bytes: int = 32768,
                     tpl: ChatTemplate = DEFAULT_TEMPLATE) -> "str | None":
    """The Stack v2 (bigcode/the-stack-v2-dedup).

    Pretraining-style code. Field is `content`. Cap at max_file_bytes —
    long files (auto-generated, vendored libs) eat the corpus budget
    without much signal. Wrapped in ChatTemplate envelope to match the
    rest of the corpus mix — see fmt_cosmopedia comment for rationale.

    The lang_or_path metadata (when present) goes in the system message
    so the model can route on language/path context — useful since
    Python looks very different from Markdown looks very different from
    shell scripts."""
    content = rec.get("content") or rec.get("text")
    if not content:
        return None
    if len(content) > max_file_bytes:
        return None
    lang = rec.get("lang") or rec.get("language") or rec.get("path") or ""
    sys_msg = f"You are a code author. Source file ({lang})." if lang else "You are a code author."
    return tpl.system(sys_msg) + tpl.assistant(content)


def fmt_open_web_math(rec: dict, tpl: ChatTemplate = DEFAULT_TEMPLATE) -> "str | None":
    """OpenWebMath (open-web-math/open-web-math).

    14.7B-token corpus of mathematical text scraped from the web —
    proofs, derivations, math.SE answers, lecture notes. Wrapped in
    ChatTemplate envelope to match the rest of the corpus mix — see
    fmt_cosmopedia comment for the rationale."""
    txt = rec.get("text")
    if not txt:
        return None
    return tpl.system("You are a math tutor working through a problem step by step.") + tpl.assistant(txt)


_CLOJURE_CRED_TAGS = frozenset({
    "KEY", "PASSWORD", "TOKEN", "AUTH", "SECRET", "API_KEY",
    "ACCESS_TOKEN", "PRIVATE_KEY",
})


def _clojure_record_has_secrets(rec: dict) -> bool:
    """loubnabnl/clojure_checks pre-flags PII/credential entities in
    `entities` field (tags: NAME, USERNAME, EMAIL, PASSWORD, KEY,
    IP_ADDRESS, etc.). GitHub push-protection blocks pushes containing
    credential-shaped strings (long random hex/b64).

    We skip records where any flagged entity is in the credential-leak
    set (KEY, PASSWORD, TOKEN, etc.). Records with only PII tags
    (NAME, USERNAME, EMAIL, IP_ADDRESS) are kept — those are common in
    repo metadata (contributor lists, header comments) and don't
    typically trip secret-scanning."""
    import ast
    ents = rec.get("entities")
    if not ents:
        return False
    # entities ships as either list-of-dicts or a stringified Python list
    if isinstance(ents, str):
        try:
            ents = ast.literal_eval(ents)
        except Exception:
            # If parse fails, be conservative: assume credential present
            return True
    if not isinstance(ents, (list, tuple)):
        return True
    for e in ents:
        if not isinstance(e, dict):
            continue
        tag = (e.get("tag") or "").upper()
        if tag in _CLOJURE_CRED_TAGS:
            return True
    return False


def fmt_clojure_content(rec: dict, max_file_bytes: int = 32768,
                        tpl: ChatTemplate = DEFAULT_TEMPLATE) -> "str | None":
    """loubnabnl/clojure_checks → raw Clojure source emit.

    Schema: `content` (original .clj file), `new_content` (post-edit),
    `max_stars_repo_name`, `max_stars_repo_path`, `entities` (PII/cred
    detections). For 'clojure-general' we emit the original content
    chat-wrapped with repo path tag (same envelope as fmt_the_stack_v2).

    Records with non-empty `entities` are skipped — those carry detected
    credentials/usernames/etc. that GitHub push-protection blocks."""
    if _clojure_record_has_secrets(rec):
        return None
    content = rec.get("content")
    if not content or len(content) > max_file_bytes:
        return None
    path = rec.get("max_stars_repo_path") or ""
    sys_msg = f"You are a Clojure author. Source file ({path})." if path \
              else "You are a Clojure author."
    return tpl.system(sys_msg) + tpl.assistant(content)


def fmt_clojure_edit(rec: dict, max_file_bytes: int = 16384,
                     tpl: ChatTemplate = DEFAULT_TEMPLATE) -> "str | None":
    """loubnabnl/clojure_checks → edit-style FIM example.

    Uses `content` (old) → `new_content` (new) as a code-edit pair,
    formatted as a JSON Edit tool call (matches fmt_commitpackft's
    envelope). FIM loss mask trains on the edit payload only.

    Records with non-empty `entities` are skipped (cred leaks)."""
    if _clojure_record_has_secrets(rec):
        return None
    old_c = rec.get("content")
    new_c = rec.get("new_content")
    if not old_c or not new_c or old_c == new_c:
        return None
    if len(old_c) > max_file_bytes or len(new_c) > max_file_bytes:
        return None
    path = rec.get("max_stars_repo_path") or "file.clj"
    sys_msg  = ("You are a Clojure coding assistant. Apply the requested "
                "edit to the file by emitting an Edit tool call.")
    user_msg = (f"Edit {path}:\n\n```clojure\n{old_c}\n```")
    return (
        tpl.system(sys_msg)
        + tpl.user(user_msg)
        + tpl.assistant_tool_call(
            "Edit",
            {"path": path, "old_str": old_c, "new_str": new_c},
        )
    )


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


def fmt_humaneval_clj(rec: dict, tpl: ChatTemplate = DEFAULT_TEMPLATE
                      ) -> "str | None":
    """MultiPL-E humaneval-clj (nuprl/MultiPL-E config='humaneval-clj').

    HumanEval ported to Clojure — 161 problems with prompts + tests.
    Schema: prompt, tests, name, doctests, language ('clj'),
    stop_tokens, prompt_terminology, original.

    Used as eval-only (kind='pretrain' so the eval battery routes
    BPC-style; agentic eval against this would also work but the
    'pass-the-tests' variant requires a Clojure runtime which we
    don't have wired). For training, the prompt+tests text is on-
    target Clojure code so harmless if cycled in — but at 175 KB
    total it's too small to materially shift training and is more
    useful held out for measuring Clojure code-gen ability."""
    prompt = rec.get("prompt")
    tests  = rec.get("tests") or ""
    name   = rec.get("name")  or ""
    if not prompt:
        return None
    # Emit prompt + tests joined; the prompt typically ends with a
    # function signature ready for completion, and the tests are the
    # canonical spec.
    body = prompt
    if tests:
        body += "\n\n;; Tests:\n" + tests
    return body


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
    "commitpackft-clj": {
        # Clojure file-edit commits — public, no HF auth needed (just
        # like the other commitpackft slices). Cap is small because
        # Clojure has way less GitHub volume than Python; expect
        # ~50-200 MB raw, even less after the formatter's 16KB
        # max_file_bytes filter. This is the fast path to Clojure-
        # specific edit signal for the eventual product target.
        "hf_name":   "bigcode/commitpackft",
        "hf_config": "clojure",
        "split":     "train",
        "formatter": fmt_commitpackft,
        "kind":      "sft",
        "notes":     "Clojure file-edit commits → JSON Edit tool calls",
    },
    "xlam": {
        "hf_name":   "Salesforce/xlam-function-calling-60k",
        "hf_config": None,
        "split":     "train",
        "formatter": fmt_xlam,
        "kind":      "sft",
        "notes":     "60k JSON tool-call traces, single + parallel calls",
    },
    "glaive-funcall": {
        "hf_name":   "glaiveai/glaive-function-calling-v2",
        "hf_config": None,
        "split":     "train",
        "formatter": fmt_glaive,
        "kind":      "sft",
        "notes":     "113k function-call dialogues; <functioncall> XML "
                     "wrappers stripped to canonical {tool_calls:[...]}",
    },
    "hermes-funcall": {
        "hf_name":   "NousResearch/hermes-function-calling-v1",
        "hf_config": None,
        "split":     "train",
        "formatter": fmt_hermes_funcall,
        "kind":      "sft",
        "notes":     "Hermes function-call corpus; <tool_call> XML "
                     "wrappers stripped to canonical {tool_calls:[...]}",
    },
    "toolace": {
        "hf_name":   "Team-ACE/ToolACE",
        "hf_config": None,
        "split":     "train",
        "formatter": fmt_toolace,
        "kind":      "sft",
        "notes":     "11.3k synth tool-call dialogues, ~26k API pool — "
                     "highest schema diversity",
    },
    "format-anchor": {
        # Format-only warmup: re-uses xLAM records but masks argument
        # values. Schema-RL / SLOT 2025: hammer the JSON skeleton into
        # the byte distribution before content learning. Same HF source
        # as `xlam`; only the formatter differs.
        "hf_name":   "Salesforce/xlam-function-calling-60k",
        "hf_config": None,
        "split":     "train",
        "formatter": fmt_format_anchor,
        "kind":      "sft",
        "notes":     "Schema-skeleton warmup (xLAM records, args masked)",
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
    "the-stack-clj": {
        # Originally tried bigcode/the-stack-v2-dedup but that dataset
        # is metadata-only by design — records have blob_id but no
        # `content` field; actual code lives on Software Heritage S3.
        # Switched to v1 (bigcode/the-stack-dedup) which has content
        # baked in. Gated; needs HF license click-through at
        # https://huggingface.co/datasets/bigcode/the-stack-dedup .
        #
        # v1 ships as a single 'default' config; per-language slices
        # are addressed via `data_dir="data/<language>"` rather than
        # an HF config name. Hence hf_config=None + hf_data_dir set.
        "hf_name":     "bigcode/the-stack-dedup",
        "hf_config":   None,
        "hf_data_dir": "data/clojure",
        "split":       "train",
        "formatter":   fmt_the_stack_v2,  # same content-field formatter works
        "kind":        "pretrain",
        "notes":       "Clojure subset of The Stack v1 dedup (gated; has content)",
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
        # Originally pointed at EleutherAI/proof-pile-2 algebraic-stack
        # config but that dataset's compressed shards trip a
        # `zstandard.ZstdError: Unknown frame descriptor` somewhere
        # mid-stream — a zstandard library / shard format mismatch
        # we couldn't quickly resolve.
        #
        # Switched to the predecessor `hoskinson-center/proof-pile`
        # — parquet-based, no loading script, no zstd shards. Same
        # role: formal-proof + math signal for the polynomial-
        # hierarchy thesis. Schema is `{text, meta}` — formatter
        # reads the bare text field, content includes:
        #   - arXiv math papers (LaTeX source)
        #   - Lean/Coq/Isabelle/HOL proof scripts (the "formal"
        #     subset; meta.config="formal")
        #   - math StackExchange Q&A
        #   - math textbooks + mathoverflow + math wiki
        # — all on-thesis for "softness/hardness boundary" exposure.
        "hf_name":   "hoskinson-center/proof-pile",
        "hf_config": None,
        "split":     "train",
        "formatter": fmt_algebraic_stack,
        "kind":      "pretrain",
        "notes":     "Formal proofs (Lean/Coq/Isabelle/HOL) + arXiv math + math.SE",
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
    "humaneval-clj": {
        # MultiPL-E (nuprl/MultiPL-E) HumanEval ported to Clojure —
        # 161 problems × ~1 KB each = ~175 KB total. Eval-only by
        # convention: it's a benchmark, including in training would
        # corrupt the eval. PROD_CAPS sizes it tiny; operator does
        # NOT include in --mix; eval_watcher includes it in agent_evals
        # to measure the model's Clojure code-gen ability per ckpt.
        "hf_name":   "nuprl/MultiPL-E",
        "hf_config": "humaneval-clj",
        "split":     "test",      # MultiPL-E ships only a test split
        "formatter": fmt_humaneval_clj,
        "kind":      "pretrain",  # routes to BPC eval; agentic-test variant TBD
        "notes":     "HumanEval-Clojure (eval-only, 161 problems / ~175 KB)",
    },
    "clojure-checks-content": {
        # loubnabnl/clojure_checks — ungated, parquet-based, ~14k records
        # / 152 MB raw. `content` holds the original Clojure file; we
        # emit it chat-wrapped as a code-author pretraining example.
        "hf_name":   "loubnabnl/clojure_checks",
        "hf_config": None,
        "split":     "train",
        "formatter": fmt_clojure_content,
        "kind":      "pretrain",
        "notes":     "Clojure source code from loubnabnl/clojure_checks (ungated)",
    },
    "clojure-checks-edit": {
        # Same dataset, edit-style envelope: (content → new_content) as a
        # JSON tool call. FIM loss mask trains on the edit payload only.
        "hf_name":   "loubnabnl/clojure_checks",
        "hf_config": None,
        "split":     "train",
        "formatter": fmt_clojure_edit,
        "kind":      "sft",
        "notes":     "Clojure file edits from loubnabnl/clojure_checks (ungated, FIM)",
    },
    "tiny-stories": {
        # roneneldan/TinyStories — Eldan & Li 2023's curated synthetic
        # children's stories (~2k word vocab). At our scale this is the
        # English grammatical-coherence foundation, paired with the
        # aesop-capstone for joint code+structure grounding (post-pivot
        # two-corpus mix). 2.1M stories, ~500 MB total.
        "hf_name":   "roneneldan/TinyStories",
        "hf_config": None,
        "split":     "train",
        "formatter": fmt_tiny_stories,
        "kind":      "pretrain",
        "notes":     "TinyStories — basic English grammar foundation (~500 MB, 2.1M stories)",
    },
}


# ─────────────────────── prep entry point ───────────────────────


def _human_bytes(n: float) -> str:
    for u in ("B", "KB", "MB", "GB", "TB"):
        if n < 1024:
            return f"{n:.1f} {u}"
        n /= 1024
    return f"{n:.1f} PB"


def _iter_hf(hf_name: str, hf_config: "str | None", split: str,
             hf_data_dir: "str | None" = None) -> Iterator[dict]:
    """Stream records from HF without materializing the whole dataset.

    We use streaming=True so a 25B-token corpus doesn't get materialized
    locally — `prepare_hf_dataset` consumes records lazily and stops
    when it hits the byte cap.

    `trust_remote_code=True` is required for datasets that ship a
    Python loading script (e.g., `bigcode/commitpackft` per-language
    configs, `EleutherAI/proof-pile-2` algebraic-stack, others).
    Modern parquet-only datasets ignore it. We pass True
    unconditionally — the security implication is "this dataset's
    loader runs in our container," which on a sandboxed Modal CPU
    container is acceptable for the public datasets we use.

    `hf_data_dir` (optional) — for datasets that ship a single
    'default' config but partition language slices by directory
    (e.g., bigcode/the-stack-dedup uses data_dir='data/clojure').
    """
    from datasets import load_dataset
    kwargs = dict(split=split, streaming=True, trust_remote_code=True)
    if hf_data_dir:
        kwargs["data_dir"] = hf_data_dir
    if hf_config:
        ds = load_dataset(hf_name, hf_config, **kwargs)
    else:
        ds = load_dataset(hf_name, **kwargs)
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
        for rec in _iter_hf(spec["hf_name"], spec["hf_config"],
                             spec["split"],
                             hf_data_dir=spec.get("hf_data_dir")):
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
