#!/usr/bin/env python3
"""Unpack a prepare-hf-dataset chat-template .bin into per-doc .json files.

Each transcript starts with `<|sys|>\\n` in the chat-template byte stream.
We split on that marker, filter by length, and write each non-empty chunk
to source-root/transcript-NNNNNN.json. The .json extension is what
fim-build-corpus uses to identify the language (json splitter is
json-value-boundary).

Usage:  python3 scripts/unpack_chat_bin_to_json.py <bin-path> <out-dir>
                                                  [min-len] [max-len]
"""
from __future__ import annotations
import os, sys, pathlib

SYS_OPEN = b"<|sys|>\n"

def main() -> None:
    if len(sys.argv) < 3:
        sys.exit("usage: unpack_chat_bin_to_json.py <bin> <out-dir> [min] [max]")
    bin_path = sys.argv[1]
    out_dir  = pathlib.Path(sys.argv[2])
    min_len  = int(sys.argv[3]) if len(sys.argv) > 3 else 100
    max_len  = int(sys.argv[4]) if len(sys.argv) > 4 else 4096
    out_dir.mkdir(parents=True, exist_ok=True)
    data = pathlib.Path(bin_path).read_bytes()
    chunks = data.split(SYS_OPEN)
    written = 0
    skipped_short = 0
    skipped_long  = 0
    for raw in chunks:
        if not raw:
            continue
        body = SYS_OPEN + raw
        n = len(body)
        if n < min_len:
            skipped_short += 1
            continue
        if n > max_len:
            skipped_long += 1
            continue
        out_path = out_dir / f"transcript-{written:06d}.json"
        out_path.write_bytes(body)
        written += 1
    print(f"  unpacked: {written} transcripts to {out_dir}")
    print(f"  filter:   skipped {skipped_short} short (<{min_len}), {skipped_long} long (>{max_len})")
    print(f"  source:   {bin_path}  ({len(data)} bytes)")

if __name__ == "__main__":
    main()
