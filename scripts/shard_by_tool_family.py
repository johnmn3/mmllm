"""Tool-family sharder for the synthetic xlam-json corpus.

The hash-by-doc-id sharder used in round-7 produced near-identical
slices because the xlam-synth corpus is uniformly distributed across
tool names (each of the 19 tool names is the primary tool in ~5% of
docs). Workers all saw the same patterns just at different specific
instances — minor divergence at the byte level (5-gram Jaccard ~0.62
between any two hash-shards), no semantic specialization.

This sharder partitions docs by the *family* of their primary tool.
Five families chosen to maximize per-family byte-divergence:

  comm:        send_email, post_message, schedule_meeting,
               create_calendar_event
  search_info: search_web, get_news, get_weather, get_route,
               currency_convert, translate
  productivity: set_timer, set_reminder, calculate, run_code
  media:       play_music, book_flight
  ops:         create_issue, close_ticket, get_stock_price

Each family has ~3000–4500 docs (slightly uneven; the 19 tools are
near-uniform individually so the family sizes track the family
membership counts). Workers training on disjoint families see different
tool names, different argument schemas, different system prompts —
genuine semantic content disjoint, not just doc-id disjoint.

Usage:
  python scripts/shard_by_tool_family.py <json_dir> <output_dir> <family>

Where <family> is one of: comm, search_info, productivity, media, ops.
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path


TOOL_FAMILIES = {
    "comm":         {"send_email", "post_message", "schedule_meeting",
                     "create_calendar_event"},
    "search_info":  {"search_web", "get_news", "get_weather", "get_route",
                     "currency_convert", "translate"},
    "productivity": {"set_timer", "set_reminder", "calculate", "run_code"},
    "media":        {"play_music", "book_flight"},
    "ops":          {"create_issue", "close_ticket", "get_stock_price"},
}

# 0-based shard-index → family mapping (matches the order the run_round8.sh
# default dispatch uses for 5 parallel workers).
SHARD_FAMILIES = ["comm", "search_info", "productivity", "media", "ops"]

# Match the first "name": "tool_name" pair in a doc — this is the primary
# tool call (each doc starts with a system prompt then a single user turn).
PRIMARY_TOOL_RE = re.compile(r'"name":\s*"([^"]+)"')


def primary_tool(doc_bytes: bytes) -> str | None:
    m = PRIMARY_TOOL_RE.search(doc_bytes.decode("utf-8", errors="ignore"))
    return m.group(1) if m else None


def partition(json_dir: Path, family: str) -> list[Path]:
    """Return all doc paths whose primary tool belongs to the given family."""
    if family not in TOOL_FAMILIES:
        raise ValueError(f"unknown family {family!r}; expected one of "
                         f"{sorted(TOOL_FAMILIES)}")
    tools = TOOL_FAMILIES[family]
    out = []
    for d in sorted(json_dir.iterdir()):
        b = d.read_bytes()
        t = primary_tool(b)
        if t in tools:
            out.append(d)
    return out


def main() -> int:
    if len(sys.argv) != 4:
        print(__doc__, file=sys.stderr)
        return 1
    json_dir = Path(sys.argv[1])
    out_dir  = Path(sys.argv[2])
    family   = sys.argv[3]
    out_dir.mkdir(parents=True, exist_ok=True)
    docs = partition(json_dir, family)
    for d in docs:
        target = out_dir / d.name
        if not target.exists():
            os.symlink(d.resolve(), target)
    # Stats — also useful to confirm shard sizes during dispatch
    all_docs = list(json_dir.iterdir())
    pct = 100.0 * len(docs) / max(len(all_docs), 1)
    print(f"  family={family}: {len(docs)} of {len(all_docs)} docs "
          f"({pct:.1f}%) → {out_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
