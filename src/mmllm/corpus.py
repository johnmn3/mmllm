"""Build and load corpora for mmllm.

Two families of corpus sources:

  Code corpora (Clojure-flavoured, the eventual product target):
    1. Local source     — walk a dir, gather .clj/.cljc/.cljs/.edn/.vs
                          Default: mmllm source. ~50 MB instantly.
    2. Git-cloned repos — shallow-clone known Clojure-heavy repos
                          (clojure/clojure, babashka, clj-kondo, ...).
                          ~100-300 MB after clone.
    3. HF Stack Clojure — the-stack-v2 Clojure subset via datasets lib
                          (deferred — needs HF auth/setup).

  Standard LM benchmarks (architecture validation):
    4. text8 / enwik8   — Matt Mahoney's compressed Wikipedia bytes.
                          100 MB raw each. Standard byte-level LM
                          benchmarks with published BPC numbers from
                          Transformer-XL, GPT-2, PKM, et al.

Code corpora are concatenated with `\\n\\n` separators. text8/enwik8
arrive as a single flat byte stream and split 90M/5M/5M
(Mikolov et al. 2012 convention) into train/val/test.
"""

from __future__ import annotations

import io
import os
import subprocess
import urllib.request
import zipfile
from pathlib import Path

import numpy as np
import torch

CLOJURE_EXTENSIONS = {".clj", ".cljc", ".cljs", ".edn"}

# Skip these paths even if they contain matching files
SKIP_PARTS = {".git", "node_modules", ".venv", "venv", "__pycache__",
              "target", ".cpcache", "dist", "build"}

# Default Clojure-heavy repos for layer 2 (clone if you want more bytes)
CLOJURE_REPOS = [
    "https://github.com/clojure/clojure",
    "https://github.com/clojure/core.async",
    "https://github.com/clojure/clojurescript",
    "https://github.com/babashka/babashka",
    "https://github.com/clj-kondo/clj-kondo",
    "https://github.com/thheller/shadow-cljs",
]


def _bytes_human(n: float) -> str:
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024:
            return f"{n:.1f} {unit}"
        n /= 1024
    return f"{n:.1f} TB"


def gather_files(root_dir: str | Path) -> list[Path]:
    """Walk dir, return Clojure-source paths excluding skip dirs."""
    root = Path(root_dir)
    out: list[Path] = []
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        if p.suffix not in CLOJURE_EXTENSIONS:
            continue
        if any(part in SKIP_PARTS for part in p.parts):
            continue
        out.append(p)
    return sorted(out)


def build_corpus(out_path: str, source_dirs: list[str]) -> dict:
    """Concatenate matching files from each source dir into out_path.

    Returns a stats dict.
    """
    out = Path(out_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    total_bytes = 0
    file_count = 0
    skipped = 0
    with open(out, "wb") as f:
        for d in source_dirs:
            for p in gather_files(d):
                try:
                    data = p.read_bytes()
                except Exception:
                    skipped += 1
                    continue
                f.write(data)
                f.write(b"\n\n")
                total_bytes += len(data) + 2
                file_count += 1
    return {
        "path":   str(out),
        "files":  file_count,
        "bytes":  total_bytes,
        "human":  _bytes_human(total_bytes),
        "skipped": skipped,
    }


def clone_repos(target_dir: str, urls: list[str] | None = None) -> list[str]:
    """Shallow-clone Clojure repos to target_dir/<repo-name>.

    Returns the list of clone paths. Existing clones are left as-is.
    """
    urls = urls if urls is not None else CLOJURE_REPOS
    target = Path(target_dir)
    target.mkdir(parents=True, exist_ok=True)
    paths: list[str] = []
    for url in urls:
        name = url.rstrip("/").split("/")[-1].removesuffix(".git")
        dest = target / name
        if dest.exists():
            paths.append(str(dest))
            continue
        print(f"  cloning {url} → {dest}")
        try:
            subprocess.run(
                ["git", "clone", "--depth", "1", url, str(dest)],
                check=True, capture_output=True, text=True,
            )
            paths.append(str(dest))
        except subprocess.CalledProcessError as e:
            print(f"  ! failed: {e.stderr.strip().splitlines()[-1] if e.stderr else e}")
    return paths


def load_as_tensor(path: str, use_mmap: bool = False) -> torch.Tensor:
    """Load a corpus binary as a 1-D tensor of byte codepoints.

    `use_mmap=False` (default for small corpora like text8): reads
    the entire file into RAM via np.fromfile and casts to int64 —
    8× memory expansion. Fine at 100 MB, OOMs at 100 GB.

    `use_mmap=True` (REQUIRED for multi-GB corpora): zero-copy
    np.memmap view as uint8. Returns a uint8 torch tensor; callers
    MUST `.long()`-cast per batch (cheap, only batch-sized). Disk
    pages page-fault in on first access and stay in OS cache; the
    working set is bounded by sampled batches, not corpus size.

    At 94 GB train + 64 GB container RAM, the int64 cast path
    would allocate 752 GB — the cause of the 5B run hang.
    """
    if use_mmap:
        arr = np.memmap(path, dtype=np.uint8, mode="r")
        # Zero-copy uint8 view; caller .long()-casts per batch.
        return torch.from_numpy(arr)
    arr = np.fromfile(path, dtype=np.uint8)
    return torch.from_numpy(arr.astype(np.int64))


def stats(path: str) -> str:
    size = os.path.getsize(path)
    return f"  {path}  ({_bytes_human(size)})"


# ─────────────────────── text8 / enwik8 ───────────────────────

MAHONEY_URLS = {
    "text8":  "https://mattmahoney.net/dc/text8.zip",
    "enwik8": "https://mattmahoney.net/dc/enwik8.zip",
}
MAHONEY_EXPECTED = 100_000_000  # both unzip to exactly 100 M bytes


def fetch_mahoney(name: str, out_path: str) -> dict:
    """Fetch text8 or enwik8 from Matt Mahoney's site. Idempotent.

    Both files unzip to exactly 100_000_000 bytes. We cache by
    asserting that exact size, so a partial download is re-fetched.
    """
    if name not in MAHONEY_URLS:
        raise ValueError(f"unknown corpus: {name} (try text8 or enwik8)")
    url = MAHONEY_URLS[name]
    out = Path(out_path)
    if out.exists() and out.stat().st_size == MAHONEY_EXPECTED:
        return {"path": str(out), "bytes": MAHONEY_EXPECTED, "cached": True}
    out.parent.mkdir(parents=True, exist_ok=True)
    print(f"  fetching {url} → {out}")
    req = urllib.request.Request(url, headers={"User-Agent": "mmllm/0.1"})
    with urllib.request.urlopen(req, timeout=180) as r:
        zip_bytes = r.read()
    with zipfile.ZipFile(io.BytesIO(zip_bytes)) as zf:
        with zf.open(name) as src:
            data = src.read()
    if len(data) != MAHONEY_EXPECTED:
        raise RuntimeError(f"unexpected size for {name}: {len(data)}")
    out.write_bytes(data)
    return {"path": str(out), "bytes": len(data), "cached": False}


def split_text8(path: str) -> dict:
    """Standard 90M/5M/5M train/val/test split for text8 / enwik8.

    Writes <path>.train.bin, <path>.val.bin, <path>.test.bin. The
    convention follows Mikolov et al. (2012) and is used by every
    subsequent text8/enwik8 LM paper, so BPC numbers are directly
    comparable.
    """
    base = Path(path)
    raw = base.read_bytes()
    if len(raw) < MAHONEY_EXPECTED:
        raise ValueError(f"corpus < 100M chars at {path}: {len(raw)}")
    train = base.with_name(base.name + ".train.bin")
    val   = base.with_name(base.name + ".val.bin")
    test  = base.with_name(base.name + ".test.bin")
    train.write_bytes(raw[:90_000_000])
    val.write_bytes(raw[90_000_000:95_000_000])
    test.write_bytes(raw[95_000_000:100_000_000])
    return {"train": str(train), "val": str(val), "test": str(test),
            "bytes_train": 90_000_000,
            "bytes_val":   5_000_000,
            "bytes_test":  5_000_000}


# ─────────────────────── Pile-Github (multi-language code) ───────────────────────
#
# The Pile (uncopyrighted version, monology/pile-uncopyrighted) is an
# 800 GB mixed-domain corpus. Its "Github" subset is ~95 GB of
# permissively-licensed multi-language code. We stream the dataset via
# HF datasets (no auth required for monology/pile-uncopyrighted),
# filter `meta.pile_set_name == "Github"`, and concat raw bytes to a
# flat binary. Reference BPC at our scale class:
#   Pythia-160M  ≈ 1.4 BPC on Pile-Github
#   Pythia-410M  ≈ 1.2 BPC
#   Pythia-1.4B  ≈ 1.05 BPC
# (Pythia paper Table 6, byte-level perplexity per Pile subset.)


def fetch_pile_github(out_path: str, max_bytes: int | None = None) -> dict:
    """Stream Pile-uncopyrighted, filter Github subset, concat raw
    UTF-8 bytes to out_path with `\\n\\n` separators between entries.

    `max_bytes` caps output size (useful for smoke tests; pass None
    for full ~95 GB Github subset). HF datasets handles streaming
    + zstandard decompression internally; no auth needed for
    monology/pile-uncopyrighted.
    """
    from datasets import load_dataset

    out = Path(out_path)
    out.parent.mkdir(parents=True, exist_ok=True)

    # Resume case: if file already exists at >= max_bytes, skip
    if max_bytes and out.exists() and out.stat().st_size >= max_bytes:
        return {"path": str(out), "bytes": out.stat().st_size,
                "entries": -1, "scanned": -1, "cached": True}

    print(f"  streaming pile-uncopyrighted, filtering pile_set_name=='Github' ...", flush=True)
    ds = load_dataset(
        "monology/pile-uncopyrighted",
        split="train",
        streaming=True,
    )

    written = 0
    n_kept = 0
    n_total = 0
    with open(out, "wb") as fout:
        for example in ds:
            n_total += 1
            meta = example.get("meta", {}) or {}
            if meta.get("pile_set_name") != "Github":
                continue
            text = example.get("text", "")
            if not text:
                continue
            data = text.encode("utf-8", errors="replace")
            fout.write(data)
            fout.write(b"\n\n")
            written += len(data) + 2
            n_kept += 1
            if n_kept % 5000 == 0:
                print(f"    {written/1e9:.2f} GB, {n_kept} entries kept "
                      f"({n_total} scanned)", flush=True)
            if max_bytes and written >= max_bytes:
                print(f"  done (max_bytes={max_bytes} hit): {written} bytes, "
                      f"{n_kept} entries", flush=True)
                return {"path": str(out), "bytes": written,
                        "entries": n_kept, "scanned": n_total, "cached": False}

    print(f"  done (stream end): {written} bytes, {n_kept} entries", flush=True)
    return {"path": str(out), "bytes": written,
            "entries": n_kept, "scanned": n_total, "cached": False}


def _fetch_pile_shard_to_file(shard_idx: int, tmp_path: str,
                              max_bytes: int | None) -> dict:
    """Worker: download one Pile-uncopyrighted train shard via direct
    HF Hub URL, stream-decompress with zstandard, filter Github, write
    to tmp_path. Used by `fetch_pile_github_parallel`."""
    import json
    import zstandard
    base_url = "https://huggingface.co/datasets/monology/pile-uncopyrighted/resolve/main/train"
    url = f"{base_url}/{shard_idx:02d}.jsonl.zst"
    print(f"  worker shard {shard_idx:02d}: GET {url}", flush=True)
    written = 0
    n_kept = 0
    n_total = 0
    dctx = zstandard.ZstdDecompressor()
    req = urllib.request.Request(url, headers={"User-Agent": "mmllm/0.1"})
    with urllib.request.urlopen(req, timeout=300) as r:
        with dctx.stream_reader(r) as reader:
            buf = io.BufferedReader(reader, buffer_size=4 * 1024 * 1024)
            with open(tmp_path, "wb") as fout:
                while True:
                    line = buf.readline()
                    if not line:
                        break
                    n_total += 1
                    try:
                        obj = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    meta = obj.get("meta", {}) or {}
                    if meta.get("pile_set_name") != "Github":
                        continue
                    text = obj.get("text", "")
                    if not text:
                        continue
                    data = text.encode("utf-8", errors="replace")
                    fout.write(data)
                    fout.write(b"\n\n")
                    written += len(data) + 2
                    n_kept += 1
                    if max_bytes and written >= max_bytes:
                        break
    return {"shard": shard_idx, "bytes": written,
            "entries": n_kept, "scanned": n_total}


def fetch_pile_github_parallel(out_path: str,
                               max_bytes: int | None = None,
                               n_workers: int = 4,
                               max_shards: int = 30) -> dict:
    """Like `fetch_pile_github` but downloads + filters N shards
    concurrently via a ThreadPoolExecutor. Each worker streams one
    shard to a tmp file; tmp files are concatenated to `out_path`
    in shard-index order (capped at `max_bytes`).

    On a 4-CPU container with stock zstandard + json: ~3-4× faster
    than serial streaming, since the bottleneck is single-thread
    zstd decompression + JSON parsing in Python.

    Resumable: if `out_path` already exists at >= max_bytes, returns
    cached without re-fetching.
    """
    import concurrent.futures

    out = Path(out_path)
    out.parent.mkdir(parents=True, exist_ok=True)

    if max_bytes and out.exists() and out.stat().st_size >= max_bytes:
        return {"path": str(out), "bytes": out.stat().st_size,
                "entries": -1, "scanned": -1, "cached": True}

    # Per-shard cap: split max_bytes evenly across workers, with headroom
    if max_bytes:
        per_shard_cap = max_bytes // n_workers + (max_bytes // 4)
    else:
        per_shard_cap = None

    print(f"  fetch_pile_github_parallel: max_bytes={max_bytes} "
          f"n_workers={n_workers} max_shards={max_shards} "
          f"per_shard_cap={per_shard_cap}", flush=True)

    tmp_dir = out.parent / f".{out.name}.parts"
    tmp_dir.mkdir(exist_ok=True)
    tmp_files: list[Path] = []
    futures: dict = {}
    results: list[dict] = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=n_workers) as ex:
        for s in range(max_shards):
            tmp_path = tmp_dir / f"shard_{s:02d}.bin"
            tmp_files.append(tmp_path)
            futures[ex.submit(
                _fetch_pile_shard_to_file, s, str(tmp_path), per_shard_cap,
            )] = s
        for f in concurrent.futures.as_completed(futures):
            try:
                r = f.result()
            except Exception as e:
                s = futures[f]
                print(f"  ! shard {s:02d} failed: {e}", flush=True)
                continue
            results.append(r)
            print(f"  ✓ shard {r['shard']:02d}: "
                  f"{r['bytes']/1e9:.2f} GB, {r['entries']} entries "
                  f"({r['scanned']} scanned)", flush=True)

    # Concat in shard-index order, capped at max_bytes
    total = 0
    BUF = 64 * 1024 * 1024
    with open(out, "wb") as fout:
        for tmp in tmp_files:
            if not tmp.exists():
                continue
            with open(tmp, "rb") as fin:
                while True:
                    if max_bytes and total >= max_bytes:
                        break
                    rem = (max_bytes - total) if max_bytes else BUF
                    chunk = fin.read(min(BUF, rem))
                    if not chunk:
                        break
                    fout.write(chunk)
                    total += len(chunk)
            tmp.unlink(missing_ok=True)
            if max_bytes and total >= max_bytes:
                break
    try:
        tmp_dir.rmdir()
    except OSError:
        pass

    n_kept = sum(r["entries"] for r in results)
    n_total = sum(r["scanned"] for r in results)
    print(f"  done: {total/1e9:.2f} GB written ({n_kept} entries kept, "
          f"{n_total} scanned)", flush=True)
    return {"path": str(out), "bytes": total,
            "entries": n_kept, "scanned": n_total, "cached": False}


def split_pile_github(path: str,
                      val_bytes: int = 100_000_000,
                      test_bytes: int = 100_000_000) -> dict:
    """Split Pile-Github (or any flat byte corpus) into train/val/test
    by raw byte count. Default holds out 100 MB val + 100 MB test
    (overkill for our eval which caps at 100k tokens, but keeps
    splits decoupled from training distribution).

    Writes <path>.train.bin / .val.bin / .test.bin via 64 MB chunked
    copy so we don't load the whole corpus into RAM.
    """
    base = Path(path)
    total = base.stat().st_size
    train_bytes = total - val_bytes - test_bytes
    if train_bytes <= 0:
        raise ValueError(
            f"corpus too small for split: {total} bytes "
            f"(needed val={val_bytes} + test={test_bytes} + train > 0)"
        )
    train = base.with_name(base.name + ".train.bin")
    val   = base.with_name(base.name + ".val.bin")
    test  = base.with_name(base.name + ".test.bin")

    BUF = 64 * 1024 * 1024  # 64 MB chunks

    def _copy_n(src, dst, n):
        remaining = n
        while remaining > 0:
            chunk = src.read(min(BUF, remaining))
            if not chunk:
                break
            dst.write(chunk)
            remaining -= len(chunk)
        return n - remaining

    with open(base, "rb") as src:
        with open(train, "wb") as f:
            _copy_n(src, f, train_bytes)
        with open(val, "wb") as f:
            _copy_n(src, f, val_bytes)
        with open(test, "wb") as f:
            _copy_n(src, f, test_bytes)

    return {"train": str(train), "val": str(val), "test": str(test),
            "bytes_train": train_bytes,
            "bytes_val":   val_bytes,
            "bytes_test":  test_bytes}
