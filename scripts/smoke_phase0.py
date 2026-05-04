#!/usr/bin/env python3
"""End-to-end smoke for the slow-walk training pipeline.

Exercises every Phase 0 / 0.5 / slow-walk piece against synthetic data
on CPU. Catches integration bugs before any paid Modal session.

What it covers:
    1. ChatTemplate + per-dataset formatters (datasets.py)
    2. `mmllm inspect-dataset` CLI
    3. `mmllm train-long` with:
        - MMLLM_MIX (multi-corpus weighted sampler)
        - MMLLM_MAX_HOURS (session timeout branch)
        - small sqrt_n + small batch (CPU-friendly)
    4. save-checkpoint! writes dense.pt + bank-latest.<i>.bin
    5. session_end JSONL event in log.jsonl
    6. `mmllm eval-bpc-on-path` against held-out test split
    7. `mmllm eval-agent` against synthetic agentic test split
    8. mix sampler picking from multiple corpora during training

What's NOT covered (Modal-only — exercise these on the FIRST paid
session, before scaling up):
    - Modal Volume mount + .commit() (the WARN messages in this smoke
      are expected — we're not in a Modal container; the basilisp
      try/except wrapper gracefully no-ops the .commit() call)
    - publish_ckpt_to_github (needs github-token Secret + gh CLI)
    - eval_watcher polling loop
    - run_eval_battery / progress_report Modal wrappers

Recommended Modal-side validation (cheap calibration session):
    1. modal secret create github-token GITHUB_TOKEN=ghp_xxx
    2. modal run --detach modal_app.py::train_with_bank \\
           --base /data/agent-corpus --bank /data/agent-bank \\
           --max-hours 0.05 --total-steps 10000 \\
           --eval-every 50 --ckpt-every 50 --batch 16 --sqrt-n 256 \\
           --publish-after
       (~3 minutes of H100 = ~$0.15. Validates Volume + ckpt + publish
       end-to-end.)
    3. modal run modal_app.py::progress_report --base /data/agent-corpus
    4. From laptop: MMLLM_ARTIFACTS_URL=...agent-latest mmllm fetch-artifacts ...

Runtime: ~60-90s on a 4-core CPU box.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

# Make `mmllm` importable when run from repo root.
REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

# Required to be set BEFORE importing mmllm (basilisp scans env at import).
os.environ.setdefault("MMLLM_DEVICE",   "cpu")
os.environ.setdefault("MMLLM_SQRT_N",   "32")     # 32² = 1024 entries; ~140 KB/layer × 5
os.environ.setdefault("MMLLM_BATCH",    "2")      # tiny — keep CPU under control
os.environ.setdefault("MMLLM_LR",       "1e-3")

PASS = "\033[92m✓\033[0m"
FAIL = "\033[91m✗\033[0m"
INFO = "\033[94m→\033[0m"


def step(msg: str) -> None:
    print(f"\n{INFO} {msg}", flush=True)


def ok(msg: str) -> None:
    print(f"  {PASS} {msg}", flush=True)


def die(msg: str, exc: Exception | None = None) -> None:
    print(f"  {FAIL} {msg}", flush=True)
    if exc:
        print(f"    {exc}", flush=True)
    sys.exit(1)


# ─────────────────────── synthetic corpus generation ───────────────────────


def make_synthetic_commit_records(n: int = 40) -> list[dict]:
    """Synthetic CommitPackFT-shaped records. Each is a tiny "edit foo.py"
    example with a deterministic old/new diff so the formatter has signal."""
    out = []
    for i in range(n):
        old = f"def hello_{i}():\n    return 'old'\n"
        new = f"def hello_{i}():\n    return 'new_{i}'\n"
        out.append({
            "old_contents": old,
            "new_contents": new,
            "subject":      f"return 'new_{i}' instead of 'old'",
            "lang":         "py",
            "commit":       f"abc{i:04d}",
        })
    return out


def make_synthetic_xlam_records(n: int = 30) -> list[dict]:
    """Synthetic xLAM-shaped records — JSON tool-call format."""
    out = []
    for i in range(n):
        out.append({
            "query":  f"What's the weather in city number {i}?",
            "tools":  json.dumps([{
                "name": "get_weather",
                "description": "Returns the weather forecast for a given city.",
                "parameters": {"city": "string"},
            }]),
            "answers": json.dumps([{
                "name": "get_weather",
                "arguments": {"city": f"city_{i}"},
            }]),
        })
    return out


def write_corpus_bin(records: list[dict], formatter, out_path: Path,
                    val_bytes: int = 2048, test_bytes: int = 2048) -> None:
    """Run records through the formatter, concat with `\\n\\n` separator,
    write to `<out_path>.bin`, then split into train/val/test via the
    same `split_pile_github` the production prep_hf_dataset uses."""
    from mmllm.corpus import split_pile_github

    sep = b"\n\n"
    written = 0
    with open(out_path, "wb") as f:
        for rec in records:
            formatted = formatter(rec)
            if not formatted:
                continue
            buf = formatted.encode("utf-8") + sep
            f.write(buf)
            written += len(buf)

    if written < val_bytes + test_bytes + 256:
        die(f"corpus too small for split: {written} bytes; need >= "
            f"{val_bytes + test_bytes + 256}. Bump record count.")

    split_pile_github(str(out_path), val_bytes, test_bytes)


# ─────────────────────── helpers ───────────────────────


def run_cli(*args: str, env_overrides: dict | None = None,
            check: bool = True, timeout: int = 120) -> subprocess.CompletedProcess:
    """Run `mmllm <args...>` as a subprocess, inheriting env + applying overrides."""
    env = {**os.environ, **(env_overrides or {})}
    cmd = ["mmllm", *args]
    print(f"    $ {' '.join(cmd)}", flush=True)
    r = subprocess.run(cmd, env=env, capture_output=True, text=True, timeout=timeout)
    if r.stdout:
        for line in r.stdout.splitlines()[-20:]:
            print(f"      {line}", flush=True)
    if check and r.returncode != 0:
        print(f"    -- stderr (last 30 lines) --", flush=True)
        for line in (r.stderr or "").splitlines()[-30:]:
            print(f"      {line}", flush=True)
        die(f"command failed (exit {r.returncode}): {' '.join(cmd)}")
    return r


def jsonl_events(path: Path) -> list[dict]:
    if not path.exists():
        return []
    out = []
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            out.append(json.loads(line))
        except json.JSONDecodeError:
            pass
    return out


# ─────────────────────── smoke phases ───────────────────────


def smoke(tmp: Path) -> None:
    # --- Phase 1: formatters + corpus build ----------------------
    step("[1/8] generating synthetic SFT corpora via real formatters")
    from mmllm.datasets import (DEFAULT_TEMPLATE, fmt_commitpackft,
                                fmt_xlam)
    commit_recs = make_synthetic_commit_records(60)
    xlam_recs   = make_synthetic_xlam_records(40)
    write_corpus_bin(commit_recs, fmt_commitpackft, tmp / "commit.bin")
    write_corpus_bin(xlam_recs,   fmt_xlam,         tmp / "xlam.bin")
    for p in (tmp / "commit.bin", tmp / "xlam.bin"):
        size = p.stat().st_size
        if size < 1024:
            die(f"{p}: only {size} bytes — formatter produced nothing useful?")
    ok(f"commit.bin = {(tmp / 'commit.bin').stat().st_size:,} bytes")
    ok(f"xlam.bin   = {(tmp / 'xlam.bin').stat().st_size:,} bytes")
    for split in ("train", "val", "test"):
        for prefix in ("commit", "xlam"):
            p = tmp / f"{prefix}.bin.{split}.bin"
            if not p.exists():
                die(f"split missing: {p}")
    ok("train/val/test splits present for both corpora")

    # --- Phase 2: ChatTemplate round-trip + scorer ---------------
    step("[2/8] ChatTemplate + scorer sanity (no model)")
    from mmllm.evals import (extract_tool_call, score_predictions,
                             split_transcript)

    transcript = (
        DEFAULT_TEMPLATE.system("You are a coding assistant.")
        + DEFAULT_TEMPLATE.user("Edit foo.")
        + DEFAULT_TEMPLATE.assistant_tool_call(
            "Edit", {"old_str": "X", "new_str": "Y"})
    )
    sample = split_transcript(transcript)
    if sample is None:
        die("split_transcript returned None on a valid transcript")
    if "<|asst|>" not in sample.prompt:
        die(f"split_transcript prompt missing asst marker: {sample.prompt!r}")
    if "tool_calls" not in sample.gold:
        die(f"split_transcript gold missing tool_calls: {sample.gold!r}")
    ok("split_transcript partitions at <|asst|> boundary")

    pred = sample.gold  # exact match → all metrics 1.0
    metrics = score_predictions([pred], [sample.gold])
    if metrics["format_validity"] != 1.0 or metrics["exact_match"] != 1.0:
        die(f"score_predictions on exact match misbehaves: {metrics}")
    ok(f"scorer agrees on exact match: {metrics}")

    extracted = extract_tool_call("preface text {\"tool_calls\": [{\"name\": \"X\"}]} suffix")
    if extracted is None:
        die("extract_tool_call failed on preface+JSON+suffix shape")
    ok("extract_tool_call handles natural-language preface")

    # --- Phase 3: inspect-dataset CLI ----------------------------
    step("[3/8] mmllm inspect-dataset CLI")
    r = run_cli("inspect-dataset", str(tmp / "commit.bin"), "500")
    if "<|sys|>" not in r.stdout or "tool_calls" not in r.stdout:
        die("inspect-dataset output missing chat-template markers / JSON")
    ok("inspect-dataset prints expected chat-template + JSON")

    # --- Phase 4: train-long with mix + max-hours ----------------
    step("[4/8] mmllm train-long with --mix + --max-hours (session timeout)")
    base = tmp / "smoke"
    # Symlink the val.bin so train-long can find <base>.val.bin (mix
    # sampler ignores train-path but val-path still drives eval-bpc).
    (base.parent / "smoke.val.bin").symlink_to(tmp / "commit.bin.val.bin")
    (base.parent / "smoke.test.bin").symlink_to(tmp / "commit.bin.test.bin")
    # train-long expects <base>.train.bin to exist even when MMLLM_MIX is
    # set (the arg is bound but not used for sampling). Symlink commit.train.
    (base.parent / "smoke.train.bin").symlink_to(tmp / "commit.bin.train.bin")

    mix = (f"{tmp}/commit.bin.train.bin:60,"
           f"{tmp}/xlam.bin.train.bin:40")
    train_env = {
        "MMLLM_MIX":         mix,
        "MMLLM_MAX_HOURS":   "0.005",   # ~18 sec — forces session-timeout branch
        # Tiny model footprint for CPU: keep sqrt_n=32 from top of file.
    }
    t0 = time.time()
    r = run_cli("train-long", str(base), "", "100000", "9999", "5",
                env_overrides=train_env, timeout=180)
    elapsed = time.time() - t0
    if elapsed > 60:
        die(f"train-long ran for {elapsed:.1f}s — max_hours=0.005 should have "
            f"capped it at ~18s. Timeout branch may not be firing.")
    if "session timeout" not in r.stdout:
        die("train-long stdout missing 'session timeout' marker — "
            "max-hours branch didn't fire?")
    ok(f"train-long exited via session-timeout branch in {elapsed:.1f}s")

    # --- Phase 5: ckpt artifacts on disk -------------------------
    step("[5/8] ckpt artifacts: dense.pt + bank-latest.<i>.bin")
    ckpts_dir = tmp / "smoke.ckpts"
    if not ckpts_dir.is_dir():
        die(f"ckpts dir missing: {ckpts_dir}")
    step_dirs = sorted(d for d in ckpts_dir.iterdir() if d.name.startswith("step-"))
    if not step_dirs:
        die(f"no step-<N> ckpt under {ckpts_dir}")
    last_step_dir = step_dirs[-1]
    ckpt_step = int(last_step_dir.name.split("-")[1])
    dense_pt = last_step_dir / "dense.pt"
    if not dense_pt.exists():
        die(f"dense.pt missing in {last_step_dir}")
    ok(f"dense.pt at step-{ckpt_step} ({dense_pt.stat().st_size:,} bytes)")
    bank_files = sorted(ckpts_dir.glob("bank-latest.*.bin"))
    if not bank_files:
        die(f"bank-latest.<i>.bin missing in {ckpts_dir} — "
            f"save-checkpoint! didn't write the bank V?")
    if len(bank_files) != 5:
        die(f"expected 5 bank-latest files (one per layer), got {len(bank_files)}")
    ok(f"bank-latest.<i>.bin × {len(bank_files)} "
       f"({sum(f.stat().st_size for f in bank_files):,} bytes total)")

    # --- Phase 6: log.jsonl session_end event --------------------
    step("[6/8] log.jsonl session_end event")
    log_path = tmp / "smoke.log.jsonl"
    events = jsonl_events(log_path)
    if not events:
        die(f"log.jsonl empty or missing: {log_path}")
    session_ends = [e for e in events if e.get("event") == "session_end"]
    if not session_ends:
        die("no session_end event in log.jsonl — train-long timeout path "
            "didn't append the budget-tracking row?")
    se = session_ends[-1]
    if se.get("reason") != "max_hours":
        die(f"session_end reason wrong: {se}")
    ok(f"session_end logged at step={se.get('step')} hours={se.get('hours'):.4f}")

    # --- Phase 7: eval-bpc-on-path -------------------------------
    step("[7/8] mmllm eval-bpc-on-path on held-out test split")
    eval_log = tmp / "eval.jsonl"
    r = run_cli("eval-bpc-on-path",
                str(base), str(ckpt_step), "",   # bank=""→ no mmap; in-RAM bank
                str(tmp / "commit.bin.test.bin"),
                "smoke-bpc",
                str(eval_log),
                env_overrides={}, timeout=120)
    if "bpc=" not in r.stdout:
        die("eval-bpc-on-path stdout missing 'bpc=' line")
    bpc_events = [e for e in jsonl_events(eval_log)
                  if e.get("kind") == "bpc"]
    if not bpc_events:
        die(f"eval log missing kind=bpc row: {eval_log}")
    ok(f"eval-bpc-on-path: bpc={bpc_events[-1].get('bpc'):.3f} "
       f"n_tokens={bpc_events[-1].get('n_tokens')}")

    # --- Phase 8: eval-agent -------------------------------------
    step("[8/8] mmllm eval-agent on held-out SFT split (untrained → expect 0.0)")
    r = run_cli("eval-agent",
                str(base), str(ckpt_step), "",   # bank="" → no mmap
                str(tmp / "commit.bin.test.bin"),
                "smoke-agent",
                "5",        # n_samples — tiny for CPU
                "128",      # gen_len
                str(eval_log),
                env_overrides={}, timeout=300)
    if "format=" not in r.stdout:
        die("eval-agent stdout missing 'format=' metric line")
    agent_events = [e for e in jsonl_events(eval_log)
                    if e.get("eval_name") == "smoke-agent"]
    if not agent_events:
        die(f"eval log missing eval_name=smoke-agent row: {eval_log}")
    ev = agent_events[-1]
    # Untrained / barely-trained model is unlikely to emit valid JSON tool
    # calls — we just want the scoring path to RUN, not to score well.
    ok(f"eval-agent ran: format_validity={ev.get('format_validity'):.3f} "
       f"exact_match={ev.get('exact_match'):.3f} "
       f"(0.0 expected — model is untrained)")


def main() -> None:
    print(f"\n{INFO} mmllm slow-walk pipeline smoke")
    print(f"{INFO} python={sys.version.split()[0]}  cwd={Path.cwd()}\n", flush=True)
    t0 = time.time()
    with tempfile.TemporaryDirectory(prefix="mmllm-smoke-") as tmp_str:
        tmp = Path(tmp_str)
        try:
            smoke(tmp)
        except SystemExit:
            raise
        except Exception as e:
            import traceback
            traceback.print_exc()
            die(f"smoke crashed with unexpected exception", e)
    elapsed = time.time() - t0
    print(f"\n{PASS} ALL PHASES PASSED ({elapsed:.1f}s)", flush=True)


if __name__ == "__main__":
    main()
