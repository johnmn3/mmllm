#!/usr/bin/env bash
# build_clojure_fim_corpus.sh — real FIM-marker corpus for clojure.
#
# Pipeline:
#   1. Pull loubnabnl/clojure_checks via the datasets library, filter
#      records flagged with credential entities (KEY/PASSWORD/etc),
#      write each `content` field as a separate .clj file under
#      /tmp/mmllm-cpu/sources/clojure/.
#   2. Run `mmllm fim-build-corpus clojure` to apply the clojure
#      splitter (sexpr-aware) and wrap each example with
#      <|fim_pre|>prefix<|fim_suf|>suffix<|fim_mid|>middle<|fim_eom|>
#      → /tmp/mmllm-cpu/battery/clojure-fim.{train,val,test}.bin.
#
# Idempotent: skips step (1) if the source dir is non-empty; skips
# step (2) if the output bin exists.

set -e
ROOT=$(git rev-parse --show-toplevel); cd "$ROOT"

SOURCES_DIR=/tmp/mmllm-cpu/sources/clojure
OUT_PREFIX=/tmp/mmllm-cpu/battery/clojure-fim
N_FILES_TARGET="${MMLLM_CLOJURE_N_FILES:-4000}"

mkdir -p "$SOURCES_DIR"
mkdir -p /tmp/mmllm-cpu/battery

# ── Step 1: dump .clj source files (skip if already populated) ──────
EXISTING=$(find "$SOURCES_DIR" -maxdepth 1 -name '*.clj' 2>/dev/null | head -1)
if [ -n "$EXISTING" ]; then
  echo "  [1/2] $SOURCES_DIR populated — skipping HF pull"
else
  echo "  [1/2] pulling loubnabnl/clojure_checks → $SOURCES_DIR (target $N_FILES_TARGET files)…"
  python3 - "$SOURCES_DIR" "$N_FILES_TARGET" <<'PYEOF'
import sys, os, pathlib
from datasets import load_dataset
sys.path.insert(0, 'src')
from mmllm.datasets import _clojure_record_has_secrets

out_dir = pathlib.Path(sys.argv[1])
target  = int(sys.argv[2])
out_dir.mkdir(parents=True, exist_ok=True)

ds = load_dataset('loubnabnl/clojure_checks', split='train', streaming=True)
n_written, n_skipped = 0, 0
for r in ds:
    if _clojure_record_has_secrets(r):
        n_skipped += 1
        continue
    content = r.get('content')
    if not content or len(content) < 100 or len(content) > 32768:
        n_skipped += 1
        continue
    # Use the record id (or fallback to running counter) as filename
    fid = r.get('id') or f"rec{n_written:06d}"
    (out_dir / f"clj-{fid}.clj").write_text(content, encoding='utf-8')
    n_written += 1
    if n_written % 500 == 0:
        print(f"    {n_written} files written, {n_skipped} skipped (creds/length)")
    if n_written >= target:
        break
print(f"  done: {n_written} .clj files written, {n_skipped} skipped")
PYEOF
fi

# ── Step 2: fim-build-corpus clojure ────────────────────────────────
if [ -s "${OUT_PREFIX}.train.bin" ] && [ -s "${OUT_PREFIX}.val.bin" ]; then
  # Check if the bin has FIM markers (file size > 0, contains <|fim_)
  if head -c 1048576 "${OUT_PREFIX}.train.bin" 2>/dev/null | grep -q '<|fim_'; then
    echo "  [2/2] FIM-marker corpus exists at $OUT_PREFIX.*.bin — skipping"
    exit 0
  fi
  echo "  [2/2] existing bins lack FIM markers — rebuilding"
fi

echo "  [2/2] running mmllm fim-build-corpus clojure…"
mmllm fim-build-corpus clojure "$SOURCES_DIR" "$OUT_PREFIX" 0.7 0.5 2>&1 \
  | grep -vE "^Downloading|^$|^Fatal Python|^Thread |^  <no Python|^Python runtime|^Extension modules|^Warning" \
  | tail -10

echo ""
echo "  ready:"
ls -lh "${OUT_PREFIX}".*.bin
