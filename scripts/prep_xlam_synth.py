#!/usr/bin/env python3
"""Synthesize a ~xlam-shaped JSON tool-call corpus for FIM training.

xlam (Salesforce/xlam-function-calling-60k) is gated on HF; the CPU-budget
FIM training contribution lives entirely in this repo so it has to be
reproducible without an HF token. This script produces synthetic records
that follow the xLAM schema:

    {"query": <user question>,
     "tools": JSON-string of [{name, description, parameters}, ...],
     "answers": JSON-string of [{name, arguments}, ...]}

After formatting via `mmllm.datasets.fmt_xlam` each record becomes:

    <|sys|>You are a tool-using assistant. Available tools:
    [{...}]<|end|>
    <|user|>{query}<|end|>
    <|asst|>{"tool_calls": [{"name": ..., "args": {...}}]}<|end|>

The FIM training contribution wants ~20k records so the byte budget for
the PSM/SPM corpus is non-trivial after the FIM tax (each FIM record
duplicates the doc bytes once for the prefix-suffix-middle reordering).

Diversity matters — if every record uses get_weather(city=...) the model
memorizes the literal bytes rather than the envelope shape. We use a
catalog of ~30 distinct tools with varied argument shapes (strings, ints,
floats, booleans, lists), and synthesize natural-language queries that
match each tool.

Run:
    python3 scripts/prep_xlam_synth.py /tmp/mmllm-cpu/sources/xlam 20000
"""
from __future__ import annotations

import json
import random
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from mmllm.datasets import fmt_xlam, DEFAULT_TEMPLATE
from mmllm.corpus import split_pile_github


CITIES = ["Tokyo", "Paris", "Mumbai", "Sao Paulo", "Lagos", "Reykjavik",
          "Anchorage", "Auckland", "Cape Town", "Vancouver", "Berlin",
          "Singapore", "Dubai", "Cairo", "Lima", "Helsinki", "Seoul"]
NAMES  = ["Alice", "Bob", "Carlos", "Dmitri", "Elena", "Faisal", "Gita",
          "Hiroshi", "Iliana", "Jamal", "Kenji", "Lina", "Mateo", "Nora",
          "Oluwasegun", "Priya", "Quentin", "Rashida", "Sven", "Tariq"]
CCYS   = ["USD", "EUR", "JPY", "GBP", "CHF", "CAD", "AUD", "INR", "BRL"]
LANGS  = ["python", "javascript", "rust", "go", "clojure", "haskell", "elixir"]


def _tool_get_weather(rng: random.Random) -> tuple[dict, str, dict]:
    tool = {
        "name": "get_weather",
        "description": "Get the current weather for a city.",
        "parameters": {"city": "string", "units": "string"},
    }
    city  = rng.choice(CITIES)
    units = rng.choice(["metric", "imperial"])
    return tool, f"What's the weather like in {city}?", {
        "city": city, "units": units,
    }


def _tool_send_email(rng: random.Random) -> tuple[dict, str, dict]:
    tool = {
        "name": "send_email",
        "description": "Send an email to a recipient.",
        "parameters": {"to": "string", "subject": "string", "body": "string"},
    }
    to = f"{rng.choice(NAMES).lower()}@example.com"
    subj = rng.choice(["Meeting tomorrow", "Project update", "Quick question",
                       "Status report", "Reminder"])
    body = rng.choice(["Please confirm.", "See attached.", "Let me know.",
                       "Thanks!", "Will follow up."])
    return tool, f"Email {to} about {subj.lower()}.", {
        "to": to, "subject": subj, "body": body,
    }


def _tool_currency_convert(rng: random.Random) -> tuple[dict, str, dict]:
    tool = {
        "name": "currency_convert",
        "description": "Convert an amount between two currencies.",
        "parameters": {"amount": "number", "from_ccy": "string",
                       "to_ccy": "string"},
    }
    amt = round(rng.uniform(1.0, 9999.0), 2)
    a, b = rng.sample(CCYS, 2)
    return tool, f"Convert {amt} {a} to {b}.", {
        "amount": amt, "from_ccy": a, "to_ccy": b,
    }


def _tool_create_calendar_event(rng: random.Random) -> tuple[dict, str, dict]:
    tool = {
        "name": "create_calendar_event",
        "description": "Add an event to the calendar.",
        "parameters": {"title": "string", "date": "string",
                       "duration_minutes": "integer"},
    }
    title = rng.choice(["Team standup", "Design review", "1:1",
                        "Customer call", "Quarterly planning"])
    date = f"2026-{rng.randint(1,12):02d}-{rng.randint(1,28):02d}"
    dur = rng.choice([15, 30, 45, 60, 90])
    return tool, f"Put '{title}' on the calendar for {date}.", {
        "title": title, "date": date, "duration_minutes": dur,
    }


def _tool_search_web(rng: random.Random) -> tuple[dict, str, dict]:
    tool = {
        "name": "search_web",
        "description": "Search the web for a query.",
        "parameters": {"query": "string", "max_results": "integer"},
    }
    q = rng.choice(["how to bake bread", "rust vs go performance",
                    "best laptops 2026", "climate change effects",
                    "history of the printing press"])
    k = rng.choice([3, 5, 10])
    return tool, f"Search for: {q}", {"query": q, "max_results": k}


def _tool_run_code(rng: random.Random) -> tuple[dict, str, dict]:
    tool = {
        "name": "run_code",
        "description": "Execute code in a language sandbox.",
        "parameters": {"language": "string", "source": "string"},
    }
    lang = rng.choice(LANGS)
    src  = rng.choice([
        "print('hello')",
        "(println :hi)",
        "fn main(){println!(\"hi\")}",
        "console.log('hi')",
    ])
    return tool, f"Run this {lang} snippet: {src}", {
        "language": lang, "source": src,
    }


def _tool_set_timer(rng: random.Random) -> tuple[dict, str, dict]:
    tool = {
        "name": "set_timer",
        "description": "Start a countdown timer.",
        "parameters": {"seconds": "integer", "label": "string"},
    }
    s = rng.choice([30, 60, 300, 600, 1800, 3600])
    label = rng.choice(["pasta", "pomodoro", "tea", "meeting"])
    return tool, f"Set a {s}-second {label} timer.", {
        "seconds": s, "label": label,
    }


def _tool_book_flight(rng: random.Random) -> tuple[dict, str, dict]:
    tool = {
        "name": "book_flight",
        "description": "Book a one-way or round-trip flight.",
        "parameters": {"origin": "string", "destination": "string",
                       "date": "string", "passengers": "integer",
                       "round_trip": "boolean"},
    }
    o, d = rng.sample(CITIES, 2)
    return tool, f"Book a flight from {o} to {d}.", {
        "origin": o, "destination": d,
        "date": f"2026-{rng.randint(1,12):02d}-{rng.randint(1,28):02d}",
        "passengers": rng.randint(1, 4),
        "round_trip": rng.choice([True, False]),
    }


def _tool_play_music(rng: random.Random) -> tuple[dict, str, dict]:
    tool = {
        "name": "play_music",
        "description": "Play a song or artist.",
        "parameters": {"query": "string", "shuffle": "boolean"},
    }
    q = rng.choice(["Mozart", "Miles Davis", "Beyonce",
                    "Tool", "Radiohead", "Bach"])
    return tool, f"Play {q}.", {"query": q, "shuffle": rng.choice([True, False])}


def _tool_translate(rng: random.Random) -> tuple[dict, str, dict]:
    tool = {
        "name": "translate",
        "description": "Translate text between languages.",
        "parameters": {"text": "string", "source_lang": "string",
                       "target_lang": "string"},
    }
    text = rng.choice(["Hello, world.", "How are you?", "Thank you.",
                       "Where is the train station?",
                       "I would like one coffee, please."])
    src = rng.choice(["en", "es", "fr", "de", "ja"])
    tgt = rng.choice(["en", "es", "fr", "de", "ja", "zh"])
    return tool, f"Translate '{text}' to {tgt}.", {
        "text": text, "source_lang": src, "target_lang": tgt,
    }


def _tool_get_news(rng: random.Random) -> tuple[dict, str, dict]:
    tool = {
        "name": "get_news",
        "description": "Fetch top news in a category.",
        "parameters": {"category": "string", "limit": "integer"},
    }
    cat = rng.choice(["technology", "world", "science", "sports",
                      "business", "health"])
    return tool, f"Show me top {cat} headlines.", {
        "category": cat, "limit": rng.choice([5, 10, 20]),
    }


def _tool_schedule_meeting(rng: random.Random) -> tuple[dict, str, dict]:
    tool = {
        "name": "schedule_meeting",
        "description": "Schedule a meeting with attendees.",
        "parameters": {"attendees": "array", "date": "string",
                       "time": "string", "topic": "string"},
    }
    return tool, "Schedule a sync with the team.", {
        "attendees": rng.sample(NAMES, k=rng.randint(2, 4)),
        "date": f"2026-{rng.randint(1,12):02d}-{rng.randint(1,28):02d}",
        "time": f"{rng.randint(8,17):02d}:{rng.choice(['00','15','30','45'])}",
        "topic": rng.choice(["roadmap", "budget", "retro", "hiring"]),
    }


def _tool_calculate(rng: random.Random) -> tuple[dict, str, dict]:
    tool = {
        "name": "calculate",
        "description": "Evaluate an arithmetic expression.",
        "parameters": {"expression": "string"},
    }
    a, b = rng.randint(1, 999), rng.randint(1, 999)
    op = rng.choice(["+", "-", "*", "/"])
    return tool, f"What is {a} {op} {b}?", {"expression": f"{a}{op}{b}"}


def _tool_set_reminder(rng: random.Random) -> tuple[dict, str, dict]:
    tool = {
        "name": "set_reminder",
        "description": "Create a reminder.",
        "parameters": {"text": "string", "at_time": "string"},
    }
    text = rng.choice(["call mom", "pay rent", "submit report",
                       "buy groceries", "take medication"])
    at = f"2026-{rng.randint(1,12):02d}-{rng.randint(1,28):02d}T{rng.randint(0,23):02d}:00"
    return tool, f"Remind me to {text}.", {"text": text, "at_time": at}


def _tool_get_stock_price(rng: random.Random) -> tuple[dict, str, dict]:
    tool = {
        "name": "get_stock_price",
        "description": "Get current price for a ticker.",
        "parameters": {"ticker": "string"},
    }
    t = rng.choice(["AAPL", "GOOGL", "MSFT", "NVDA", "TSLA", "AMZN", "META"])
    return tool, f"What's {t} trading at?", {"ticker": t}


def _tool_post_message(rng: random.Random) -> tuple[dict, str, dict]:
    tool = {
        "name": "post_message",
        "description": "Post a message to a channel.",
        "parameters": {"channel": "string", "text": "string"},
    }
    chan = rng.choice(["#general", "#random", "#engineering", "#design"])
    txt  = rng.choice(["Heads up: deploy in 10.",
                       "Lunch?", "PR ready for review.",
                       "Anyone seen the cat?"])
    return tool, f"Post in {chan}: {txt}", {"channel": chan, "text": txt}


def _tool_close_ticket(rng: random.Random) -> tuple[dict, str, dict]:
    tool = {
        "name": "close_ticket",
        "description": "Close a support ticket.",
        "parameters": {"ticket_id": "string", "resolution": "string"},
    }
    tid = f"T-{rng.randint(1000, 99999)}"
    return tool, f"Close ticket {tid}.", {
        "ticket_id": tid, "resolution": rng.choice(["fixed", "wontfix",
                                                     "duplicate"]),
    }


def _tool_create_issue(rng: random.Random) -> tuple[dict, str, dict]:
    tool = {
        "name": "create_issue",
        "description": "Open a GitHub issue.",
        "parameters": {"repo": "string", "title": "string", "body": "string",
                       "labels": "array"},
    }
    repo = rng.choice(["mmllm/core", "acme/web", "openai/sdk", "rust-lang/rust"])
    title = rng.choice(["bug in login", "feature: dark mode",
                        "perf regression", "docs typo"])
    return tool, f"File an issue on {repo}: {title}.", {
        "repo": repo, "title": title,
        "body": "Reported by user; needs triage.",
        "labels": rng.sample(["bug", "enhancement", "perf", "docs"],
                              k=rng.randint(1, 2)),
    }


def _tool_get_route(rng: random.Random) -> tuple[dict, str, dict]:
    tool = {
        "name": "get_route",
        "description": "Get directions between two locations.",
        "parameters": {"origin": "string", "destination": "string",
                       "mode": "string"},
    }
    o, d = rng.sample(CITIES, 2)
    return tool, f"How do I get from {o} to {d}?", {
        "origin": o, "destination": d,
        "mode": rng.choice(["driving", "transit", "walking", "cycling"]),
    }


TOOL_FNS = [
    _tool_get_weather, _tool_send_email, _tool_currency_convert,
    _tool_create_calendar_event, _tool_search_web, _tool_run_code,
    _tool_set_timer, _tool_book_flight, _tool_play_music, _tool_translate,
    _tool_get_news, _tool_schedule_meeting, _tool_calculate,
    _tool_set_reminder, _tool_get_stock_price, _tool_post_message,
    _tool_close_ticket, _tool_create_issue, _tool_get_route,
]


# ─────────────────────── diversification ─────────────────────────────────
# A single fixed system prompt makes the corpus highly memorizable — every
# record shares the exact same ~200-byte prefix. The model fits that prefix
# trivially and never learns the structural envelope shape. To prevent
# this we vary (a) the system prompt phrasing, (b) the tool-catalog
# presentation, and (c) the number of tool calls per assistant turn.

SYS_TEMPLATES = [
    "You are a tool-using assistant. Available tools:\n{tools}",
    "You can call these tools to help the user:\n{tools}\nReply with a JSON tool_calls list.",
    "Tools available:\n{tools}",
    "Assistant with tool access. Tools:\n{tools}\nWhen calling, emit a tool_calls JSON object.",
    "You have access to the following tools:\n{tools}\nUse them when relevant.",
    "Tool registry:\n{tools}",
    "{tools}",                                    # bare tools, no preamble
    "You are a helpful assistant. Reply in JSON with the appropriate tool call.",  # tools omitted
    "API tools:\n{tools}\nRespond strictly in the {{\"tool_calls\":[...]}} format.",
    "Toolset:\n{tools}",
]

# How the tool catalog itself is presented.
def _present_tools(tools: list[dict], rng: random.Random) -> str:
    style = rng.choice(["json_array", "json_lines", "bullets", "name_only"])
    if style == "json_array":
        return json.dumps(tools)
    if style == "json_lines":
        return "\n".join(json.dumps(t) for t in tools)
    if style == "bullets":
        return "\n".join(
            f"- {t['name']}({', '.join(t.get('parameters', {}).keys())}): {t.get('description','')}"
            for t in tools)
    if style == "name_only":
        return ", ".join(t["name"] for t in tools)
    return json.dumps(tools)


def gen_record(rng: random.Random) -> dict:
    """Single-call record (kept for backward compat with the old corpus shape).
    The diversified records used in `main` go through `gen_record_diverse`."""
    n_tools_in_catalog = rng.randint(2, 5)
    catalog_fns = rng.sample(TOOL_FNS,
                             k=min(n_tools_in_catalog, len(TOOL_FNS)))
    chosen_fn = rng.choice(catalog_fns)
    chosen_tool, query, args = chosen_fn(rng)
    tools = [fn(rng)[0] for fn in catalog_fns]
    return {
        "query":   query,
        "tools":   json.dumps(tools),
        "answers": json.dumps([{"name":      chosen_tool["name"],
                                "arguments": args}]),
    }


def fmt_diverse(rng: random.Random) -> str:
    """Generate one fully-formatted training record with randomized
    system-prompt template, tool catalog presentation, and 1–3 tool calls.

    Returns the formatted string directly (skips fmt_xlam since we want
    finer control over the envelope shape than the canonical formatter
    provides). Output still parses as the same envelope mmllm.eval-agent
    expects: <|sys|>...<|user|>...<|asst|>{"tool_calls":[...]}<|end|>."""
    from mmllm.datasets import ChatTemplate
    tpl = ChatTemplate()

    # 1) Random catalog (size 2..7)
    catalog_size = rng.randint(2, min(7, len(TOOL_FNS)))
    catalog_fns  = rng.sample(TOOL_FNS, k=catalog_size)
    tools        = [fn(rng)[0] for fn in catalog_fns]

    # 2) 1..3 tool calls in this assistant turn. Each call picks a fn
    #    from the catalog. (Multi-call is rare in xlam but common in
    #    real agent traffic — model needs to see the list envelope.)
    n_calls = rng.choices([1, 2, 3], weights=[6, 3, 1])[0]
    calls = []
    user_intents = []
    for _ in range(n_calls):
        fn = rng.choice(catalog_fns)
        tool, query, args = fn(rng)
        calls.append({"name": tool["name"], "args": args})
        user_intents.append(query)

    # 3) Compose the user query
    if n_calls == 1:
        user_msg = user_intents[0]
    else:
        joiners = [" Also, ", " Then ", " And then ", " Plus, "]
        user_msg = user_intents[0]
        for q in user_intents[1:]:
            # Strip the leading capital so the joiner reads naturally
            q_low = q[:1].lower() + q[1:] if q else q
            user_msg += rng.choice(joiners) + q_low

    # 4) Random system template + catalog presentation
    sys_tpl = rng.choice(SYS_TEMPLATES)
    sys_msg = sys_tpl.format(tools=_present_tools(tools, rng))

    # 5) Sometimes the model is expected to refuse / clarify rather than
    #    emit a tool call. Small fraction (5%) — gives the model a
    #    template for "don't call a tool" envelopes too.
    if rng.random() < 0.05:
        asst_body = rng.choice([
            json.dumps({"tool_calls": []}),
            json.dumps({"tool_calls": [], "reply": "I don't have a tool that can do that."}),
        ])
    else:
        asst_body = json.dumps({"tool_calls": calls})

    return tpl.system(sys_msg) + tpl.user(user_msg) + tpl.assistant(asst_body)


def main() -> None:
    if len(sys.argv) < 2:
        print("usage: prep_xlam_synth.py <out-base> [n-records] [val-bytes] [test-bytes]")
        sys.exit(1)
    out_base   = Path(sys.argv[1])
    n_records  = int(sys.argv[2]) if len(sys.argv) > 2 else 20000
    val_bytes  = int(sys.argv[3]) if len(sys.argv) > 3 else 500_000
    test_bytes = int(sys.argv[4]) if len(sys.argv) > 4 else 500_000

    out_base.parent.mkdir(parents=True, exist_ok=True)
    rng = random.Random(42)

    sep = b"\n\n"
    written = 0
    n_kept  = 0
    print(f"  synthesizing {n_records} DIVERSIFIED xlam-shaped records → {out_base}",
          flush=True)
    print(f"    sys-prompt variants: {len(SYS_TEMPLATES)}  "
          f"catalog-styles: 4  tool catalog: {len(TOOL_FNS)}  "
          f"calls/record: 1..3", flush=True)
    with open(out_base, "wb") as f:
        for i in range(n_records):
            formatted = fmt_diverse(rng)
            if not formatted:
                continue
            buf = formatted.encode("utf-8", errors="replace") + sep
            f.write(buf)
            written += len(buf)
            n_kept += 1
            if n_kept % 5000 == 0:
                print(f"    {n_kept}/{n_records}  ({written/1e6:.1f} MB)",
                      flush=True)

    print(f"  done: {n_kept} records / {written/1e6:.2f} MB", flush=True)

    info = split_pile_github(str(out_base), val_bytes, test_bytes)
    print(f"  train: {info['train']}  ({info['bytes_train']/1e6:.2f} MB)")
    print(f"  val:   {info['val']}    ({info['bytes_val']/1e6:.2f} MB)")
    print(f"  test:  {info['test']}   ({info['bytes_test']/1e6:.2f} MB)")


if __name__ == "__main__":
    main()
