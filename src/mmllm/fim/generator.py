"""FIM corpus generator.

Two entry points:

  make_fim_example(doc, mode, rng, splitter) → bytes | None
    Single-document FIM rearrange.

  build_fim_corpus(input_paths, output_prefix, …)
    Stream-build a train/val/test split corpus from a list of source
    files, writing FIM-formatted byte streams.

Output layout (matches the corp/ module's existing format):
  <output_prefix>.train.bin   uint8 byte stream
  <output_prefix>.val.bin
  <output_prefix>.test.bin

Each stream is a concatenation of FIM examples (and optionally raw
causal examples, mixed at the configured ratio). Documents are
separated by a `\\n\\n` boundary.

The output stream may contain split markers — they're just bytes the
model learns to recognize. No vocab change."""

from __future__ import annotations

import os
import random
from pathlib import Path
from typing import Callable, Iterable, Optional

from mmllm.fim.markers import FIM_PRE, FIM_SUF, FIM_MID, FIM_EOM
from mmllm.fim.splitters import get as get_splitter, Splitter


# ─────────────────────── single-document FIM ───────────────────────


def make_fim_example(doc: bytes, *,
                     mode: str = "psm",
                     rng: random.Random,
                     splitter: Splitter | None = None,
                     ) -> Optional[bytes]:
    """Convert raw doc to FIM-formatted bytes. mode='psm' produces
    `<PRE>prefix<SUF>suffix<MID>middle<EOM>`; mode='spm' uses
    suffix-prefix-middle ordering. `splitter` picks the (i, j) cut
    points; if None, generic random split is used.

    Returns None if the doc is too short or the splitter declines."""
    if splitter is None:
        from mmllm.fim.splitters.generic import split as splitter
    cut = splitter(doc, rng)
    if cut is None:
        return None
    i, j = cut
    if not (0 <= i < j <= len(doc)):
        return None
    prefix = doc[:i]
    middle = doc[i:j]
    suffix = doc[j:]
    if mode == "psm":
        return FIM_PRE + prefix + FIM_SUF + suffix + FIM_MID + middle + FIM_EOM
    elif mode == "spm":
        return FIM_SUF + suffix + FIM_PRE + prefix + FIM_MID + middle + FIM_EOM
    else:
        raise ValueError(f"unknown FIM mode: {mode!r} (expected 'psm' or 'spm')")


# ─────────────────────── source iteration ───────────────────────


def _iter_docs_from_files(paths: Iterable[Path], *,
                         max_doc_bytes: int = 8192) -> Iterable[bytes]:
    """Yield documents from a list of file paths. Files are read whole
    if they fit max_doc_bytes; larger files are split at `\\n\\n` (or
    raw byte chunks) to stay within budget. Binary files are read as-is."""
    for path in paths:
        try:
            data = Path(path).read_bytes()
        except (OSError, IsADirectoryError):
            continue
        if not data:
            continue
        if len(data) <= max_doc_bytes:
            yield data
            continue
        # Big file — split at paragraph boundaries when possible
        chunks = data.split(b"\n\n")
        cur: list[bytes] = []
        cur_len = 0
        for c in chunks:
            need = len(c) + 2
            if cur_len + need > max_doc_bytes and cur:
                yield b"\n\n".join(cur)
                cur = []
                cur_len = 0
            cur.append(c)
            cur_len += need
        if cur:
            yield b"\n\n".join(cur)


# ─────────────────────── corpus builder ───────────────────────


def build_fim_corpus(input_paths: list[Path],
                     output_prefix: Path | str,
                     *,
                     language: str = "generic",
                     fim_ratio: float = 0.5,
                     psm_ratio: float = 0.5,
                     train_frac: float = 0.85,
                     val_frac: float = 0.075,
                     # test_frac = 1 - train - val
                     max_doc_bytes: int = 8192,
                     min_middle: int = 8,
                     max_middle: int = 256,
                     rng_seed: int = 0,
                     verbose: bool = True,
                     ) -> dict:
    """Stream-build a FIM corpus from raw source files.

    Each source document gets converted to:
      - a FIM example with prob `fim_ratio` (PSM with prob `psm_ratio`,
        else SPM); or
      - a raw causal copy with prob 1 - fim_ratio.

    Documents are then concatenated with `\\n\\n` separators into one
    of the train/val/test byte streams chosen by the per-document RNG.

    Returns a dict of stats:
      {"train_bytes": N, "val_bytes": N, "test_bytes": N,
       "n_fim": K, "n_causal": K, "n_skipped": K}"""
    output_prefix = Path(output_prefix)
    output_prefix.parent.mkdir(parents=True, exist_ok=True)
    splitter = get_splitter(language)
    rng = random.Random(rng_seed)

    paths_train = open(f"{output_prefix}.train.bin", "wb")
    paths_val   = open(f"{output_prefix}.val.bin",   "wb")
    paths_test  = open(f"{output_prefix}.test.bin",  "wb")
    streams = (paths_train, paths_val, paths_test)
    weights = (train_frac, val_frac, max(0.0, 1.0 - train_frac - val_frac))

    n_fim = 0
    n_causal = 0
    n_skipped = 0
    total_in = 0

    for doc in _iter_docs_from_files(input_paths, max_doc_bytes=max_doc_bytes):
        total_in += 1
        # Pick output split
        which = rng.choices((0, 1, 2), weights=weights)[0]
        out = streams[which]

        # Decide FIM vs causal
        if rng.random() < fim_ratio:
            mode = "psm" if rng.random() < psm_ratio else "spm"
            blob = make_fim_example(doc, mode=mode, rng=rng,
                                    splitter=splitter)
            if blob is None:
                # Splitter declined — fall back to causal raw doc
                blob = doc
                n_causal += 1
            else:
                n_fim += 1
        else:
            blob = doc
            n_causal += 1

        out.write(blob)
        out.write(b"\n\n")

    for s in streams:
        s.close()

    stats = {
        "train_bytes": Path(f"{output_prefix}.train.bin").stat().st_size,
        "val_bytes":   Path(f"{output_prefix}.val.bin").stat().st_size,
        "test_bytes":  Path(f"{output_prefix}.test.bin").stat().st_size,
        "n_fim":       n_fim,
        "n_causal":    n_causal,
        "n_skipped":   n_skipped,
        "n_input_docs": total_in,
        "language":    language,
    }
    if verbose:
        print(f"  build_fim_corpus({language})  →  {output_prefix}.{{train,val,test}}.bin")
        print(f"     {n_fim} FIM examples + {n_causal} raw-causal docs from {total_in} input docs")
        print(f"     train={stats['train_bytes']:,}B  val={stats['val_bytes']:,}B  test={stats['test_bytes']:,}B")
    return stats


def collect_source_files(source_root: Path | str,
                         *,
                         extensions: tuple[str, ...] = ()) -> list[Path]:
    """Walk source_root and return all file paths matching extensions
    (case-insensitive). Empty `extensions` returns all non-binary-looking
    files."""
    source_root = Path(source_root)
    if not source_root.is_dir():
        return [source_root] if source_root.is_file() else []
    paths = []
    exts_lower = tuple(e.lower() for e in extensions)
    for root, _, files in os.walk(source_root):
        for f in files:
            p = Path(root) / f
            if exts_lower:
                if p.suffix.lower() not in exts_lower:
                    continue
            paths.append(p)
    return paths


# Recommended extensions per language for source-file scraping:
LANGUAGE_EXTENSIONS: dict[str, tuple[str, ...]] = {
    "clojure":  (".clj", ".cljc", ".cljs", ".edn"),
    "python":   (".py",),
    "json":     (".json",),
    "javascript": (".js", ".mjs", ".jsx"),
    "typescript": (".ts", ".tsx"),
    "rust":     (".rs",),
    "go":       (".go",),
    "java":     (".java",),
    "c":        (".c", ".h"),
    "cpp":      (".cpp", ".hpp", ".cc", ".cxx", ".hh"),
    "generic":  (),
}
