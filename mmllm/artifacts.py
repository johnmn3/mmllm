"""Download trained-artifact bundles from a public HTTPS source.

By default targets a GitHub Release on the mmllm repo, but the URL
template is overridable so you can self-host (S3, R2, HuggingFace,
local file server, whatever).

Why this exists: laptops doing `mmllm bench-batch` need a trained
checkpoint + bank but don't have Modal access. GitHub Releases gives
a 2-GB-per-file public-bandwidth-free fetch path that the
`requests`-equivalent stdlib pulls cleanly. One `mmllm fetch-artifacts`
gets the whole int8 inference bundle.

Default release expects this layout:

    <RELEASE_BASE>/dense.pt
    <RELEASE_BASE>/pile-bank-3tier-int8.0.int8.bin
    <RELEASE_BASE>/pile-bank-3tier-int8.1.int8.bin
    ...

with `<RELEASE_BASE>` typically
    https://github.com/<owner>/<repo>/releases/download/<tag>

Override via MMLLM_ARTIFACTS_URL env var or the cli arg.
"""
from __future__ import annotations

import os
import urllib.request
from pathlib import Path

DEFAULT_RELEASE_BASE = (
    "https://github.com/johnmn3/mmllm/releases/download/v0.1-bench"
)

# Files that make up the inference bundle (5B-plain ckpt + int8 bank).
# Listed once here so updates only edit one place.
DEFAULT_BUNDLE = [
    # (release-side filename, local-side path under out_dir)
    ("dense.pt",                          "pile-github.bin.ckpts/step-305000/dense.pt"),
    ("pile-bank-3tier-int8.0.int8.bin",   "pile-bank-3tier-int8.0.int8.bin"),
    ("pile-bank-3tier-int8.1.int8.bin",   "pile-bank-3tier-int8.1.int8.bin"),
    ("pile-bank-3tier-int8.2.int8.bin",   "pile-bank-3tier-int8.2.int8.bin"),
    ("pile-bank-3tier-int8.3.int8.bin",   "pile-bank-3tier-int8.3.int8.bin"),
    ("pile-bank-3tier-int8.4.int8.bin",   "pile-bank-3tier-int8.4.int8.bin"),
]


def _human_bytes(n: float) -> str:
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if n < 1024:
            return f"{n:.1f} {unit}"
        n /= 1024
    return f"{n:.1f} PB"


def _download_one(url: str, dst: Path, chunk: int = 64 * 1024 * 1024) -> int:
    """Stream `url` to `dst` in 64 MB chunks. Returns total bytes
    written. No SHA verification (relies on TLS + GitHub-side
    integrity); add that later if needed."""
    dst.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": "mmllm/0.1"})
    written = 0
    with urllib.request.urlopen(req, timeout=300) as r:
        size_hdr = r.headers.get("content-length")
        total = int(size_hdr) if size_hdr else 0
        with open(dst, "wb") as fout:
            while True:
                buf = r.read(chunk)
                if not buf:
                    break
                fout.write(buf)
                written += len(buf)
                if total > 0:
                    pct = 100.0 * written / total
                    print(f"\r    {dst.name}: {pct:5.1f}%  "
                          f"({_human_bytes(written)} / {_human_bytes(total)})",
                          end="", flush=True)
            print()
    return written


def fetch_artifacts(
    out_dir: str | Path,
    release_base: str | None = None,
    bundle: list | None = None,
) -> dict:
    """Download the inference artifact bundle to `out_dir`.

    Idempotent: skips files that exist at any non-zero size (use
    --force or delete the file to re-fetch). Returns stats dict.

    out_dir/
      pile-github.bin.ckpts/step-305000/dense.pt
      pile-bank-3tier-int8.0.int8.bin
      ...

    After fetch, run:
      MMLLM_BANK_DTYPE=int8 MMLLM_BANK_ON_GPU=false MMLLM_SQRT_N=2048 \\
      mmllm bench /path/to/out_dir/pile-github.bin 305000 \\
                  /path/to/out_dir/pile-bank-3tier-int8 50 200
    """
    out_path = Path(out_dir)
    base = release_base or os.environ.get(
        "MMLLM_ARTIFACTS_URL", DEFAULT_RELEASE_BASE,
    )
    files = bundle or DEFAULT_BUNDLE
    print(f"  fetching artifacts from {base} → {out_path}", flush=True)
    total = 0
    skipped = 0
    fetched = 0
    for remote_name, local_rel in files:
        url = f"{base}/{remote_name}"
        dst = out_path / local_rel
        if dst.exists() and dst.stat().st_size > 0:
            print(f"  ✓ cached: {dst} ({_human_bytes(dst.stat().st_size)})",
                  flush=True)
            skipped += 1
            continue
        print(f"  → {url}", flush=True)
        n = _download_one(url, dst)
        total += n
        fetched += 1
    return {
        "out_dir":      str(out_path),
        "release_base": base,
        "n_fetched":    fetched,
        "n_cached":     skipped,
        "total_bytes":  total,
        "total_human":  _human_bytes(total),
    }
