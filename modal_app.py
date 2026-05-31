"""mmLLM - Memory Mapped LLM training on Modal.

Run from the repo root:

  # One-time: fetch + split text8 into the persistent volume.
  modal run modal_app.py::prepare_data

  # Long-running training. Detach so the local CLI exits while the
  # function keeps running on Modal; tail logs separately. Modal caps
  # each invocation at 24 h — for longer training, re-invoke after
  # the previous run exits; train-long resumes from latest checkpoint.
  modal run --detach modal_app.py::train_with_bank \\
      --total-steps 100000 --eval-every 1000 --ckpt-every 5000

  # Tail logs of the running training task.
  modal app logs mmllm

  # Pull the JSONL log + checkpoints back to local for plotting / restart.
  modal volume get mmllm-data /text8.log.jsonl ./

The persistent volume `mmllm-data` holds:

  /data/text8                  — raw 100 MB byte stream
  /data/text8.{train,val,test}.bin — 90M/5M/5M Mikolov split
  /data/bank.{0..4}.bin        — 1.17 GB mmap'd memory bank V tensors
  /data/text8.ckpts/step-<N>/  — dense + optimizer state checkpoints
  /data/text8.log.jsonl        — append-only training metrics

The bank survives across runs by virtue of the volume; restarts of
train_with_bank resume from the latest /data/text8.ckpts/step-<N>/
because mmllm's `train-long` checks for it on startup.
"""
import modal

app = modal.App("mmllm")

image = (
    modal.Image.debian_slim(python_version="3.11")
    .apt_install("git")
    .pip_install(
        "torch>=2.0",
        "numpy>=1.24",
        "basilisp>=0.3",
        "datasets>=2.14,<4.0",  # streams Pile-uncopyrighted shards (no auth).
                                # Pinned <4.0 because HF deprecated dataset
                                # scripts in 4.x — bigcode/commitpackft (and
                                # several other widely-used datasets) still
                                # ship as scripts. Modern parquet-only
                                # datasets work fine in 3.x too.
        "Pillow>=10.0",         # required by datasets to decode Image-typed
                                # columns (e.g., TheoremQA's `Picture` field).
                                # We don't read the image bytes ourselves but
                                # datasets validates the schema column on
                                # iteration regardless.
        "zstandard>=0.21",  # for Pile shard decompression
        "modal",            # for in-worker Volume.from_name() during bank sync
        "codecarbon>=2.5",  # energy + CO2 instrumentation; pulls pynvml + RAPL
    )
    .add_local_dir(
        ".",
        remote_path="/code",
        copy=True,
        ignore=["__pycache__", "*.pyc", ".basilisp_cache", "*.egg-info", "tests"],
    )
    .run_commands("cd /code && pip install -e .")
)

volume = modal.Volume.from_name(
    # Volume name kept as the pre-rename label until the contents
    # (1B-trained dense ckpts + bank V mmaps + text8/pile-github
    # splits) are migrated. Renaming to "mmllm-data" without
    # migration would silently spin up an empty new volume and
    # strand all the trained artifacts.
    "mmllm-data",
    create_if_missing=True,
)


# Image variant with the GitHub CLI installed — used by
# `publish_ckpt_to_github` to upload release artifacts. The `gh`
# binary handles auth/upload-URL/multipart-asset details we'd
# otherwise have to reinvent in stdlib `urllib`. Kept as a separate
# image layer so training/eval functions don't pay for the apt
# install.
publish_image = (
    image
    # Direct-tarball install of the gh CLI. The apt-repo path
    # (curl GPG keyring → /etc/apt/sources.list.d/ → apt update → apt
    # install) kept flaking on the GPG keyring fetch step ("Connection
    # reset by peer" from cli.github.com), which blew up the whole
    # image build and prevented any function in this app from
    # launching — even functions that don't use publish_image. The
    # tarball path is a single file download from the GitHub releases
    # CDN; falls back across two URLs and retries up to 3× before
    # giving up.
    .run_commands(
        "apt-get update -qq && apt-get install -qq -y curl ca-certificates",
        "set -e; "
        "GH_VERSION=2.62.0; "
        "for url in "
        "  https://github.com/cli/cli/releases/download/v${GH_VERSION}/gh_${GH_VERSION}_linux_amd64.tar.gz "
        "  https://github.com/cli/cli/releases/download/v${GH_VERSION}/gh_${GH_VERSION}_linux_amd64.tar.gz "
        "  https://github.com/cli/cli/releases/download/v${GH_VERSION}/gh_${GH_VERSION}_linux_amd64.tar.gz "
        "; do "
        "  if curl -fsSL --retry 3 --retry-delay 5 -o /tmp/gh.tar.gz \"$url\"; then break; fi; "
        "  echo \"download from $url failed; retrying...\"; "
        "  sleep 5; "
        "done; "
        "tar -xzf /tmp/gh.tar.gz -C /tmp/ && "
        "mv /tmp/gh_${GH_VERSION}_linux_amd64/bin/gh /usr/local/bin/gh && "
        "rm -rf /tmp/gh.tar.gz /tmp/gh_${GH_VERSION}_linux_amd64 && "
        "gh --version",
    )
)


def _maybe_secret(name: str) -> list:
    """Return [Secret.from_name(name)] if the Secret exists in the
    current Modal env, else []. Modal validates Secret references at
    app-init time, so a missing Secret on ANY function decorator
    blocks the WHOLE app from running — even functions that never
    reference that Secret. This helper makes a Secret optional:
    publish-style functions still work (the Secret gets injected as
    env vars at call time IF present), but other functions in the
    same app can run even when the Secret hasn't been created.

    Detection: shell out to `modal secret list` (cheap, cached by the
    Modal CLI). If `name` is in the listing, return a real
    Secret.from_name; otherwise return []. The publish function
    raises a clear error at call time if GITHUB_TOKEN ends up unset
    in env, so users who try to publish without setting up the Secret
    get a meaningful message rather than a silent failure."""
    import subprocess
    try:
        r = subprocess.run(
            ["modal", "secret", "list"],
            capture_output=True, text=True, timeout=10, check=False,
        )
        if r.returncode == 0 and name in (r.stdout or ""):
            return [modal.Secret.from_name(name, required_keys=["GITHUB_TOKEN"])]
    except Exception:
        pass
    return []


# Resolved at module-import time. If the user later creates the
# Secret, they need to re-run their `modal run` command — Modal
# re-imports the file and picks up the new Secret.
_PUBLISH_SECRETS = _maybe_secret("github-token")

# HF token for gated datasets (bigcode/the-stack-v2-dedup,
# Salesforce/xlam-function-calling-60k, etc.). Same conditional
# pattern: if the Secret exists in the Modal env, prepare_hf_dataset
# (and any other function that calls into mmllm.datasets) gets
# HF_TOKEN injected and the gated streams work; if not, gated dataset
# preps fail with a clear "DatasetNotFoundError: gated repo" error
# and the public datasets continue to work.
def _hf_secret():
    """Look up Modal's standard 'huggingface-secret' name first
    (Modal's recommended convention exposes HF_TOKEN), then fall
    back to a user-created 'huggingface-token'. Returns the first
    one that exists, or [] if neither does."""
    import subprocess
    try:
        r = subprocess.run(
            ["modal", "secret", "list"],
            capture_output=True, text=True, timeout=10, check=False,
        )
        out = r.stdout or ""
        for name in ("huggingface-secret", "huggingface-token"):
            if name in out:
                return [modal.Secret.from_name(name, required_keys=["HF_TOKEN"])]
    except Exception:
        pass
    return []


_HF_SECRETS = _hf_secret()


@app.function(
    image=image,
    volumes={"/data": volume},
    timeout=3600,
    cpu=2.0,
    memory=4096,
)
def prepare_data():
    """One-time: fetch Mahoney text8, split 90M/5M/5M into the volume."""
    import subprocess
    print("=== fetch-text8 ===", flush=True)
    subprocess.run(["mmllm", "fetch-text8", "/data/text8"], check=True)
    print("=== split-text8 ===", flush=True)
    subprocess.run(["mmllm", "split-text8", "/data/text8"], check=True)
    volume.commit()
    print("done — volume contents committed", flush=True)


# ── one-shot corpus migration: verbum-bb-data → mmllm-data ──
# Throwaway helper. Mounts both volumes and server-side copies the
# pile-github split files (~95 GB) so a fresh run on `mmllm-data`
# can train without re-fetching from HF. Delete this function and
# the legacy `verbum-bb-data` volume after the in-flight 5B run on
# the legacy volume finishes.
@app.function(
    image=image,
    volumes={
        "/src": modal.Volume.from_name("verbum-bb-data"),
        "/dst": volume,
    },
    timeout=7200,  # 2h ceiling; 95 GB at ~100 MB/s ≈ 16 min, +headroom
    cpu=4.0,
    memory=8192,
)
def migrate_corpus_to_mmllm_data():
    """Copy pile-github.bin.{train,val,test}.bin from verbum-bb-data
    to mmllm-data. Idempotent: skips files that already exist at the
    expected size on the destination."""
    import os
    import shutil
    import time

    files = [
        "pile-github.bin.train.bin",
        "pile-github.bin.val.bin",
        "pile-github.bin.test.bin",
    ]
    BUF = 64 * 1024 * 1024  # 64 MB
    total = 0
    t0 = time.time()
    for name in files:
        src = f"/src/{name}"
        dst = f"/dst/{name}"
        if not os.path.exists(src):
            print(f"  ! missing source: {src} — skipping", flush=True)
            continue
        src_size = os.path.getsize(src)
        if os.path.exists(dst) and os.path.getsize(dst) == src_size:
            print(f"  = already present: {name} ({src_size/1e9:.2f} GB)", flush=True)
            continue
        print(f"  → copying {name} ({src_size/1e9:.2f} GB)…", flush=True)
        t1 = time.time()
        with open(src, "rb") as fin, open(dst, "wb") as fout:
            written = 0
            while True:
                chunk = fin.read(BUF)
                if not chunk:
                    break
                fout.write(chunk)
                written += len(chunk)
        dt = time.time() - t1
        rate = (written / 1e9) / max(dt, 1e-6)
        print(f"  ✓ {name}: {written/1e9:.2f} GB in {dt:.1f}s "
              f"({rate:.2f} GB/s)", flush=True)
        total += written
    volume.commit()
    print(f"done — copied {total/1e9:.2f} GB in {time.time()-t0:.1f}s; "
          f"committed to mmllm-data", flush=True)


# ── one-shot artifact migration: trained bank + log → mmllm-data ──
# Companion to migrate_corpus_to_mmllm_data. Run after the 5B-on-legacy
# completes, before deleting verbum-bb-data. The trained bank is the
# warm-start substrate for any future run that wants to inherit the
# 5B's learned semantic content rather than start from scratch.
@app.function(
    image=image,
    volumes={
        "/src": modal.Volume.from_name("verbum-bb-data"),
        "/dst": volume,
    },
    timeout=3600,
    cpu=4.0,
    memory=8192,
)
def migrate_artifacts_to_mmllm_data(bank_prefix: str = "pile-bank-3tier",
                                    log_name: str = "pile-github.bin.log.jsonl",
                                    dense_ckpt: str = "pile-github.bin.ckpts/step-305000/dense.pt",
                                    n_layers: int = 5):
    """Copy the trained bank V mmap files + training log + final dense
    ckpt from verbum-bb-data to mmllm-data. Idempotent: skips files
    that already exist at the expected size on the destination.

    Files copied:
      - /src/<bank_prefix>.{0..n_layers-1}.bin → /dst/<same path>
      - /src/<log_name> → /dst/<same path>
      - /src/<dense_ckpt> → /dst/<same path>  (final trained dense
        weights paired with the bank; opt-state intentionally NOT
        copied since we won't resume this particular run)
    """
    import os
    import time

    files = (
        [f"{bank_prefix}.{i}.bin" for i in range(n_layers)]
        + [log_name, dense_ckpt]
    )
    BUF = 64 * 1024 * 1024  # 64 MB
    total = 0
    t0 = time.time()
    for name in files:
        src = f"/src/{name}"
        dst = f"/dst/{name}"
        if not os.path.exists(src):
            print(f"  ! missing source: {src} — skipping", flush=True)
            continue
        src_size = os.path.getsize(src)
        if os.path.exists(dst) and os.path.getsize(dst) == src_size:
            print(f"  = already present: {name} ({src_size/1e9:.2f} GB)", flush=True)
            continue
        # dense_ckpt has an intermediate ckpts/step-N/ path; ensure dir exists
        os.makedirs(os.path.dirname(dst) or ".", exist_ok=True)
        print(f"  → copying {name} ({src_size/1e9:.2f} GB)…", flush=True)
        t1 = time.time()
        with open(src, "rb") as fin, open(dst, "wb") as fout:
            written = 0
            while True:
                chunk = fin.read(BUF)
                if not chunk:
                    break
                fout.write(chunk)
                written += len(chunk)
        dt = time.time() - t1
        rate = (written / 1e9) / max(dt, 1e-6)
        print(f"  ✓ {name}: {written/1e9:.2f} GB in {dt:.1f}s "
              f"({rate:.2f} GB/s)", flush=True)
        total += written
    volume.commit()
    print(f"done — copied {total/1e9:.2f} GB in {time.time()-t0:.1f}s; "
          f"committed to mmllm-data", flush=True)


@app.function(
    image=image,
    volumes={"/data": volume},
    timeout=43200,  # up to 12 h for full ~95 GB Github subset
    cpu=4.0,
    memory=16384,
)
def prepare_pile_github(max_bytes: int = 5_000_000_000,
                        val_bytes: int = 100_000_000,
                        test_bytes: int = 100_000_000):
    """Stream Pile-uncopyrighted, filter Github subset, split.

    Defaults: 5 GB Github content + 100 MB val + 100 MB test.
    Pass max_bytes=30_000_000_000 for ~30 GB (matches 20 GB bank).
    Resumable: if /data/pile-github.bin already exists at >= max_bytes,
    fetch is skipped (split is re-run).
    """
    import subprocess
    print(f"=== fetch-pile-github max_bytes={max_bytes} (parallel, 4 workers) ===",
          flush=True)
    subprocess.run(
        ["mmllm", "fetch-pile-github",
         "/data/pile-github.bin", str(max_bytes), "4"],  # 4 parallel workers
        check=True,
    )
    print(f"=== split-pile-github val={val_bytes} test={test_bytes} ===",
          flush=True)
    subprocess.run(
        ["mmllm", "split-pile-github", "/data/pile-github.bin",
         str(val_bytes), str(test_bytes)],
        check=True,
    )
    volume.commit()
    print("done — pile-github prepared on volume", flush=True)


@app.function(
    image=image,
    volumes={"/data": volume},
    timeout=21600,   # up to 6 h — generation is single-process, ~few-K rec/s
    cpu=4.0,
    memory=16384,
)
def build_aesop_curriculum(out_path:      str = "/data/aesop-curriculum.bin",
                           n_per_example: int = 200,
                           seed:          int = 0,
                           val_bytes:     int = 50_000_000,
                           test_bytes:    int = 50_000_000):
    """Generate the K-12 Clojure curriculum byte-bin on Modal.

    Walks every (fable, grade, subject, example) across the 5
    Phase-C-complete fables and writes `n_per_example` records per
    example. Default n=200 → ~1.2M records / ~600 MB byte-bin —
    sized to fill the 60% fable share of a 1B-token training run.

    Output layout matches all other corpora on the volume:
      <out_path>           flat byte stream
      <out_path>.train.bin
      <out_path>.val.bin
      <out_path>.test.bin

    Each record is rendered through DEFAULT_TEMPLATE (sys + user +
    asst, with `\\n<|end|>\\n` closers) — same shape as every
    other formatter in mmllm.datasets, so the byte-bin is a
    drop-in for `--mix`.
    """
    import subprocess
    from pathlib import Path
    print(f"=== build-aesop-curriculum n_per_example={n_per_example} "
          f"seed={seed} → {out_path} ===", flush=True)
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["python", "-m", "mmllm.aesop.generate",
         "--curriculum",
         "--out", out_path,
         "--n", str(n_per_example),
         "--seed", str(seed),
         "--val-bytes", str(val_bytes),
         "--test-bytes", str(test_bytes)],
        check=True,
    )
    volume.commit()
    final_size = Path(out_path).stat().st_size
    print(f"done — aesop-curriculum prepared on volume "
          f"({final_size/1e9:.2f} GB)", flush=True)


@app.function(
    image=image,
    volumes={"/data": volume},
    timeout=3600,
    cpu=4.0,
    memory=16384,
)
def topup_pile_github(
    base: str = "/data/pile-github.bin",
    val_bytes: int = 200_000_000,
    test_bytes: int = 200_000_000,
):
    """Append surviving shard-tmp files from a previous prepare_pile_github
    that hit its max_bytes cap, then re-run the split.

    `fetch_pile_github_parallel` writes each shard's Github content to
    `<base>.parts/shard_NN.bin` then concats them into <base>, capped at
    max_bytes. When the cap fires mid-concat, tmps for unread shards
    stay on the volume — this function reads those leftover tmps in
    shard-index order, appends to <base>, deletes them as it consumes,
    then re-runs split-pile-github so train/val/test reflect the new
    bigger corpus.

    Idempotent on a clean volume — does nothing if the parts dir is
    missing or empty.
    """
    import os
    import subprocess
    from pathlib import Path

    base_path = Path(base)
    parts_dir = base_path.parent / f".{base_path.name}.parts"

    if not parts_dir.exists():
        print(f"  no parts dir at {parts_dir} — nothing to top up", flush=True)
        return

    tmp_files = sorted(parts_dir.glob("shard_*.bin"))
    if not tmp_files:
        print(f"  parts dir {parts_dir} is empty — nothing to top up", flush=True)
        try:
            parts_dir.rmdir()
        except OSError:
            pass
        return

    initial_size = base_path.stat().st_size if base_path.exists() else 0
    leftover_total = sum(t.stat().st_size for t in tmp_files)
    print(
        f"=== topup_pile_github: appending {len(tmp_files)} leftover shards "
        f"({leftover_total/1e9:.2f} GB) to existing {initial_size/1e9:.2f} GB "
        f"{base} ===",
        flush=True,
    )

    BUF = 64 * 1024 * 1024
    total_appended = 0
    with open(base_path, "ab") as fout:  # append mode — preserves first 30 GB
        for tmp in tmp_files:
            tmp_size = tmp.stat().st_size
            with open(tmp, "rb") as fin:
                while True:
                    chunk = fin.read(BUF)
                    if not chunk:
                        break
                    fout.write(chunk)
                    total_appended += len(chunk)
            tmp.unlink()
            print(
                f"  ✓ {tmp.name}: appended {tmp_size/1e9:.2f} GB "
                f"(running total appended: {total_appended/1e9:.2f} GB)",
                flush=True,
            )

    # Cleanup parts dir — should be empty now since we unlinked every tmp.
    try:
        parts_dir.rmdir()
    except OSError as e:
        print(f"  warn: {parts_dir} not empty after cleanup: {e}", flush=True)

    final_size = base_path.stat().st_size
    print(
        f"  {base}: {initial_size/1e9:.2f} GB → {final_size/1e9:.2f} GB",
        flush=True,
    )

    # Re-split: existing train/val/test become stale at the new size.
    print(f"=== re-split val={val_bytes} test={test_bytes} ===", flush=True)
    subprocess.run(
        [
            "mmllm", "split-pile-github", base,
            str(val_bytes), str(test_bytes),
        ],
        check=True,
    )
    volume.commit()
    print(f"done — final {base} = {final_size/1e9:.2f} GB", flush=True)


def _run_train_long(total_steps, eval_every, ckpt_every, device, lr,
                    batch=4, base="/data/text8", bank="/data/bank",
                    sqrt_n=None, cpu_offload=False, bank_on_gpu=True,
                    sync_every=0, volume_name="mmllm-data",
                    lr_warmup=0, lr_min=None,
                    bank_query_mode="plain", long_tier_mix="sum",
                    bank_feedback_mode="plain", ablate_every=0,
                    max_hours=0.0, mix="",
                    lr_dense_mult=1.0, lr_bank_mult=1.0,
                    z_loss_coef=0.0, mtp_coef=0.0,
                    slot_log_every=0, dead_slot_reinit=False,
                    netbank_enabled=False, netbank_path=None,
                    netbank_sqrt_n=8192, netbank_c_net=64,
                    netbank_top_k=64, netbank_sub_top_k=64,
                    netbank_delay_ms_min=1.0, netbank_delay_ms_max=10.0,
                    netbank_on_gpu=False,
                    lr_net_mult=1.0,
                    lr_dense_mult_end=None,
                    lr_bank_mult_end=None,
                    lr_net_mult_end=None,
                    focal_gamma=0.0,
                    importance_head=False,
                    importance_aux=1.0,
                    carry_enabled=False,
                    carry_n_clocks=4,
                    grad_clip=0.0,
                    nan_guard=False,
                    log_param_norms=False,
                    distill_coef=0.0,
                    distill_direction_only=False,
                    alpha_net=False,
                    replay_every=0,
                    replay_buffer_size=256,
                    replay_threshold=0.5,
                    # 9-spike upgrade plan (#1-#9)
                    lr_kab_mult=None,            # #3 — K_a/K_b separate LR
                    lr_kab_mult_end=None,
                    delim_aux_coef=0.0,          # #4 — JSON-delimiter aux head
                    schema_mask_weight=1.0,      # #5 — schema-mask CE weight
                    pause_bytes=0,               # #9 — pause-byte prefix
                    pause_prob=0.5,
                    pause_byte_val=0,
                    bank_repeat_n=1,             # #7+#8 — Local Bank iter refinement
                    bank_repeat_alpha=0.1,
                    bank_cold_boost=0.0,         # #1 — cold-row gradient boost
                    bank_cold_boost_eps=1.0,
                    phase_label=""):
    """Shared body. All knobs threaded via env vars (MMLLM_DEVICE,
    MMLLM_LR, MMLLM_BATCH, MMLLM_SQRT_N, MMLLM_CPU_OFFLOAD,
    MMLLM_BANK_ON_GPU, MMLLM_SYNC_EVERY, MMLLM_VOLUME_NAME,
    MMLLM_LR_WARMUP, MMLLM_LR_MIN, MMLLM_LR_DENSE_MULT,
    MMLLM_LR_BANK_MULT, MMLLM_BANK_QUERY_MODE, MMLLM_LONG_TIER_MIX,
    MMLLM_BANK_FEEDBACK_MODE) so the basilisp CLI stays unchanged.

    `lr_dense_mult` / `lr_bank_mult` decouple the AdamW (dense /
    router) and SparseAdam (bank / experts) lrs from the unified
    peak `lr`. Default 1.0 / 1.0 = legacy behaviour. See
    docs/router-bank-lr-decoupling.md for the differential-decay
    schedule (cool dense after ~9-12B tokens; cool bank later).

    `bank_on_gpu=False` switches to the CPUPinnedEmbedding path —
    bank V lives in the mmap'd file, cross-device gather happens
    per query. Required for multi-trainer setups (only mmap-shared
    banks can be safely written by N concurrent processes).

    `sync_every>0` enables cross-worker bank sync via Modal Volume
    commit/reload + mmap remap (PagedMmapStorage). For multi-trainer
    Hogwild this is mandatory — without it, workers train on private
    copies of the bank and never see each other's writes. Recommended
    50-500 steps; 100 is a balanced default. Set 0 for single-worker.

    `lr_warmup>0` enables linear warmup + cosine decay schedule:
    0 → lr → lr_min over (warmup, total_steps - warmup) steps.
    `lr_min` defaults to lr/10 if not set. lr_warmup=0 (default)
    means constant lr — backward compat.

    `bank_query_mode` selects the bank-query shaper (mmllm.bank_query):
    'plain' (default; q_long_flat unchanged) or 'ctx-add' (additive
    W_ctx · x with zero-init, identical to plain at step 0).

    `long_tier_mix` selects how the long-tier SDPA and bank-V outputs
    combine (mmllm.gating): 'sum' (default), 'scalar' (per-head α/β),
    'switch' (sigmoid-gated convex mix).

    `bank_feedback_mode` selects whether the bank's output feeds back
    into x before q-proj (mmllm.bank_feedback): 'plain' (default; no
    feedback) or 'feedback' (probe → bank → W_back · result added to
    x; W_back zero-init, identical to plain at step 0; one extra PKM
    lookup per layer per forward).
    """
    import os
    import subprocess
    env = {**os.environ,
           "MMLLM_DEVICE": device,
           "MMLLM_LR":     str(lr),
           "MMLLM_LR_DENSE_MULT": str(lr_dense_mult),
           "MMLLM_LR_BANK_MULT":  str(lr_bank_mult),
           "MMLLM_BATCH":  str(batch),
           "MMLLM_BANK_ON_GPU": "true" if bank_on_gpu else "false",
           "MMLLM_SYNC_EVERY":  str(sync_every),
           "MMLLM_VOLUME_NAME": volume_name,
           "MMLLM_LR_WARMUP":   str(lr_warmup),
           "MMLLM_BANK_QUERY_MODE":    bank_query_mode,
           "MMLLM_LONG_TIER_MIX":      long_tier_mix,
           "MMLLM_BANK_FEEDBACK_MODE": bank_feedback_mode,
           "MMLLM_ABLATE_EVERY":       str(ablate_every),
           "MMLLM_Z_LOSS_COEF":        str(z_loss_coef),
           "MMLLM_MTP_COEF":           str(mtp_coef),
           "MMLLM_SLOT_LOG_EVERY":     str(slot_log_every),
           "MMLLM_DEAD_SLOT_REINIT":   "true" if dead_slot_reinit else "false",
           "MMLLM_NETBANK_ENABLED":    "true" if netbank_enabled else "false",
           "MMLLM_NET_SQRT_N":         str(netbank_sqrt_n),
           "MMLLM_NET_C_NET":          str(netbank_c_net),
           "MMLLM_NET_TOP_K":          str(netbank_top_k),
           "MMLLM_NET_SUB_TOP_K":      str(netbank_sub_top_k),
           "MMLLM_NET_DELAY_MS_MIN":   str(netbank_delay_ms_min),
           "MMLLM_NET_DELAY_MS_MAX":   str(netbank_delay_ms_max),
           "MMLLM_NET_BANK_ON_GPU":    "true" if netbank_on_gpu else "false",
           "MMLLM_LR_NET_MULT":        str(lr_net_mult),
           # Per-multiplier END values for cosine schedules. None → use
           # the start value (constant; backward-compat). When set, lr
           # mult cosine-interpolates from start → end across (warmup,
           # total_steps]. T1 plan: bank 10→1, net 5→10 to drive
           # consolidation: Local cools as Net ramps up.
           "MMLLM_LR_DENSE_MULT_END":  str(lr_dense_mult_end if lr_dense_mult_end is not None else lr_dense_mult),
           "MMLLM_LR_BANK_MULT_END":   str(lr_bank_mult_end  if lr_bank_mult_end  is not None else lr_bank_mult),
           "MMLLM_LR_NET_MULT_END":    str(lr_net_mult_end   if lr_net_mult_end   is not None else lr_net_mult),
           # Router-smarts (focal CE + importance head + multi-timescale
           # carry). Defaults are no-op (focal_gamma=0 → plain CE,
           # importance_head=false, carry_enabled=false). Each is opt-in
           # via env var so old runs / ckpts stay parameter-identical.
           "MMLLM_FOCAL_GAMMA":        str(focal_gamma),
           "MMLLM_IMPORTANCE_HEAD":    "true" if importance_head else "false",
           "MMLLM_IMPORTANCE_AUX":     str(importance_aux),
           "MMLLM_CARRY_ENABLED":      "true" if carry_enabled else "false",
           "MMLLM_CARRY_N_CLOCKS":     str(carry_n_clocks),
           "MMLLM_GRAD_CLIP":          str(grad_clip),
           "MMLLM_NAN_GUARD":          "true" if nan_guard else "false",
           "MMLLM_LOG_PARAM_NORMS":    "true" if log_param_norms else "false",
           "MMLLM_DISTILL_COEF":       str(distill_coef),
           "MMLLM_DISTILL_DIRECTION_ONLY": "true" if distill_direction_only else "false",
           "MMLLM_ALPHA_NET":          "true" if alpha_net else "false",
           "MMLLM_REPLAY_EVERY":       str(replay_every),
           "MMLLM_REPLAY_BUFFER_SIZE": str(replay_buffer_size),
           "MMLLM_REPLAY_THRESHOLD":   str(replay_threshold),
           # 9-spike upgrade plan env knobs
           "MMLLM_LR_KAB_MULT":        str(lr_kab_mult)     if lr_kab_mult     is not None else str(lr_dense_mult),
           "MMLLM_LR_KAB_MULT_END":    str(lr_kab_mult_end) if lr_kab_mult_end is not None else (str(lr_kab_mult) if lr_kab_mult is not None else str(lr_dense_mult)),
           "MMLLM_DELIM_AUX_COEF":     str(delim_aux_coef),
           "MMLLM_SCHEMA_MASK_WEIGHT": str(schema_mask_weight),
           "MMLLM_PAUSE_BYTES":        str(pause_bytes),
           "MMLLM_PAUSE_PROB":         str(pause_prob),
           "MMLLM_PAUSE_BYTE_VAL":     str(pause_byte_val),
           "MMLLM_BANK_REPEAT_N":      str(bank_repeat_n),
           "MMLLM_BANK_REPEAT_ALPHA":  str(bank_repeat_alpha),
           "MMLLM_BANK_COLD_BOOST":    str(bank_cold_boost),
           "MMLLM_BANK_COLD_BOOST_EPS":str(bank_cold_boost_eps),
           "MMLLM_PHASE_LABEL":        phase_label,
           # Expandable allocator avoids the fragmentation pattern that
           # OOM'd Phase 4 at the first ablation: the allocator was holding
           # ~17 GB of cached-but-unallocated memory it couldn't reuse for
           # a 4 GB request. expandable_segments lets PyTorch grow segments
           # rather than allocate fixed-size chunks.
           "PYTORCH_CUDA_ALLOC_CONF":  "expandable_segments:True"}
    if netbank_path is not None:
        env["MMLLM_NET_BANK_PATH"] = netbank_path
    if sqrt_n is not None:
        env["MMLLM_SQRT_N"] = str(sqrt_n)
    if cpu_offload:
        env["MMLLM_CPU_OFFLOAD"] = "true"
    if lr_min is not None:
        env["MMLLM_LR_MIN"] = str(lr_min)
    if max_hours and max_hours > 0:
        env["MMLLM_MAX_HOURS"] = str(max_hours)
    if mix:
        env["MMLLM_MIX"] = mix
    phase_label = os.environ.get("MMLLM_PHASE_LABEL", "(no phase label)")
    print(f"=== PHASE LABEL: {phase_label} ===", flush=True)
    print(
        f"=== train-long device={device} B={batch} lr={lr} "
        f"lr_dense_mult={lr_dense_mult} lr_bank_mult={lr_bank_mult} sqrt_n={sqrt_n} "
        f"cpu_offload={cpu_offload} bank_on_gpu={bank_on_gpu} "
        f"sync_every={sync_every} volume={volume_name} "
        f"lr_warmup={lr_warmup} lr_min={lr_min} "
        f"bank_query_mode={bank_query_mode} long_tier_mix={long_tier_mix} "
        f"bank_feedback_mode={bank_feedback_mode} "
        f"ablate_every={ablate_every} max_hours={max_hours} "
        f"mix={'(set)' if mix else '(none)'} "
        f"focal_gamma={focal_gamma} importance_head={importance_head} "
        f"carry_enabled={carry_enabled} carry_n_clocks={carry_n_clocks} "
        f"grad_clip={grad_clip} "
        f"total={total_steps} eval-every={eval_every} "
        f"ckpt-every={ckpt_every} base={base} ===",
        flush=True,
    )
    subprocess.run(
        [
            "mmllm", "train-long",
            base, bank,
            str(total_steps), str(eval_every), str(ckpt_every),
        ],
        check=True,
        env=env,
    )
    volume.commit()
    print(f"done — base={base} bank={bank} committed", flush=True)


@app.function(
    image=image,
    volumes={"/data": volume},
    timeout=86400,    # Modal caps at 24 h per invocation; resume across runs.
    gpu="H100",       # 80 GB VRAM (same headroom as A100-80GB) but ~1.5-2× compute
    memory=65536,     # 64 GB host RAM (CPU-offload SparseAdam state needs ~38 GB at sqrt_n=2048)
)
def train_with_bank(
    total_steps: int = 100000,
    eval_every: int = 1000,
    ckpt_every: int = 5000,
    lr: float = 1.4e-3,         # peak lr — sqrt(128/64)-scaled from prior B=64/lr=1e-3 best
    lr_dense_mult: float = 1.0, # multiplier on AdamW (dense / router) lr — see docs/router-bank-lr-decoupling.md
    lr_bank_mult: float = 1.0,  # multiplier on SparseAdam (bank / experts) lr
    batch: int = 128,           # per-token throughput plateau zone; smoother gradients
    sqrt_n: int = 0,            # 0 = config default; pass 2048 for ~18.8 GB bank
    cpu_offload: bool = False,  # CPU-offload SparseAdam state → frees ~38 GB GPU VRAM
    lr_warmup: int = 0,         # 0 = constant lr; >0 enables linear warmup + cosine decay
    lr_min: float = 0.0,        # cosine floor (0 = lr/10 by default; only used when lr_warmup > 0)
    bank_query_mode: str = "plain",      # 'plain' | 'ctx-add' — see mmllm.bank_query
    long_tier_mix: str = "sum",          # 'sum' | 'scalar' | 'switch' — see mmllm.gating
    bank_feedback_mode: str = "plain",   # 'plain' | 'feedback' — see mmllm.bank_feedback
    ablate_every: int = 0,               # >0 = log Δ trajectory every N steps; 0 disables
    z_loss_coef: float = 0.0,            # ST-MoE-style query z-loss on K_a/K_b (1e-5 typical)
    mtp_coef: float = 0.0,               # multi-byte-prediction t+2 aux head coefficient (0.25 typical)
    slot_log_every: int = 0,             # log per-layer PKM slot-utilization entropy every N steps
    dead_slot_reinit: bool = False,      # at slot-log events, reinit dead K_a/K_b rows + their V slice
    netbank_enabled: bool = False,       # enable the off-machine "long-term memory" tier (NetBank)
    netbank_path: str = "",              # mmap path prefix; defaults to <bank>+'-net' if unset
    netbank_sqrt_n: int = 8192,          # NetBank side length (entries = sqrt_n²); 8192 → 67M entries
    netbank_c_net: int = 64,             # NetBank V bottleneck dim (rows stored as c_net latents)
    netbank_top_k: int = 64,             # rows retrieved per NetBank query (larger payload)
    netbank_sub_top_k: int = 64,         # sub-keys retained per K_a/K_b half before re-rank
    netbank_delay_ms_min: float = 1.0,   # min simulated WAN delay per NetBank forward (ms)
    netbank_delay_ms_max: float = 10.0,  # max simulated WAN delay (uniform random in [min, max])
    netbank_on_gpu: bool = False,        # NetBank V on GPU VRAM (training-fast) vs CPU mmap (production-realism)
    lr_net_mult: float = 1.0,            # multiplier on NetBank's SparseAdam lr
    lr_dense_mult_end: float = -1.0,     # cosine-schedule end for AdamW lr mult; -1 = use start (constant)
    lr_bank_mult_end:  float = -1.0,     # cosine-schedule end for SparseAdam lr mult; T1 default = 1.0
    lr_net_mult_end:   float = -1.0,     # cosine-schedule end for NetBank SparseAdam lr mult; T1 default = 10.0
    # ── router-smarts (mid-brain enrichments) ──
    focal_gamma: float = 0.0,            # focal CE exponent: 0 = plain CE, 2 = up-weight hard bytes
    importance_head: bool = False,       # learned per-position difficulty predictor (decoupled from main loss; mean-1 multiplier)
    importance_aux: float = 1.0,         # coefficient on IH self-supervised aux MSE; 0 = freeze IH at init
    carry_enabled: bool = False,         # per-block MultiTimescaleCarry (4 EMAs, log-spaced decays)
    carry_n_clocks: int = 4,             # number of EMAs per carry block
    grad_clip: float = 0.0,              # max global L2 norm for AdamW gradient clipping (0 = disabled, 1.0 standard)
    nan_guard: bool = False,             # forward-pass NaN check at each block + logits — aborts with layer-id on first NaN
    log_param_norms: bool = False,       # at each slot_log_every event, write per-param L∞/L2 norms to log.jsonl
    distill_coef: float = 0.0,           # P2': aux MSE coef driving Net to mimic Local's attention output (0 = disabled)
    distill_direction_only: bool = False,# normalize Net & Local to unit-norm before MSE (Net learns Local's direction, not magnitude)
    alpha_net: bool = False,             # per-head learnable scale on Net's path in SwitchGate (compensates for Net's smaller magnitude)
    replay_every: int = 0,               # P3: every N main steps run a frozen-Local replay step on a buffered mastered batch (0 = disabled)
    replay_buffer_size: int = 256,       # P3: max (x, y) batches kept in replay buffer (CPU)
    replay_threshold: float = 0.5,       # P3: plain-CE below which a batch is pushed to the buffer (mastered-position selector)
    # — 9-spike upgrade plan knobs (default off / no-op) —
    lr_kab_mult: float = -1.0,           # #3: K_a/K_b separate LR mult; -1 = use lr_dense_mult (single group)
    lr_kab_mult_end: float = -1.0,       # #3: cosine end for kab; -1 = use lr_kab_mult (constant)
    delim_aux_coef: float = 0.0,         # #4: JSON-delimiter aux head's BCE coef (0 = disabled)
    schema_mask_weight: float = 1.0,     # #5: per-position CE weight on positions after a JSON delimiter (1.0 = disabled)
    pause_bytes: int = 0,                # #9: number of pause bytes to prepend to training batches (0 = disabled)
    pause_prob: float = 0.5,             # #9: per-batch probability of pause prefix injection
    pause_byte_val: int = 0,             # #9: byte value for pause filler (0 = NUL)
    bank_repeat_n: int = 1,              # #7+8: Local Bank iterative refinement passes per forward (1 = no iter, legacy)
    bank_repeat_alpha: float = 0.1,      # #7+8: scale on prev mem_out fed back into bank_q
    bank_cold_boost: float = 0.0,        # #1: cold-row gradient boost on Local V (0 = disabled)
    bank_cold_boost_eps: float = 1.0,    # #1: smoothing in `1 + boost / (eps + count)`
    phase_label: str = "",               # human-readable tag for this run (printed at startup, recorded in manifest)
    base: str = "/data/text8",
    bank: str = "/data/bank",
    corpus_base: str = "",               # if set and != base, symlink corpus splits
                                         # so train-long finds them at <base>.{train,val,test}.bin
                                         # while ckpts/log/etc still write under <base>
    max_hours: float = 0.0,              # 0 = no cap. >0 = clean shutdown after N hours
                                         # (slow-walk budget bounding). Resumes next session
                                         # from latest ckpt.
    mix: str = "",                       # MMLLM_MIX passthrough — multi-corpus weighted
                                         # sampler. Format: 'p1:w1,p2:w2,...'. When set,
                                         # `base` arg is ignored for sampling — only
                                         # base.val.bin still drives eval-bpc.
    publish_after: bool = False,         # if True, after the session ends successfully,
                                         # auto-spawn publish_ckpt_to_github with the resolved
                                         # latest ckpt step. Requires `github-token` Modal
                                         # Secret set. See publish_ckpt_to_github docstring.
    gh_repo: str = "johnmn3/mmllm",      # GH repo for publish_after target.
    tag_prefix: str = "agent",           # tag namespace for publish_after.
):
    """Long-running training on A100-80GB + GPU-resident bank.

    Dense modules (q/k/v/o/FFN/RMSNorm/embeddings/K_a/K_b) live on
    cuda; the bank V is wrapped in CPUPinnedEmbedding so .to('cuda')
    skips it — it stays page-faulted from /data/bank.<i>.bin. Per
    forward, top-K indices are computed on GPU, copied to CPU,
    V rows gathered on CPU, result copied back to GPU. Sparse-grad
    backward flows GPU→CPU through .to() and lands on V on CPU;
    SparseAdam writes touched rows back through the mmap.

    Defaults (B=64, lr=1e-3) reflect the lr_sweep result + the
    sqrt(B) heuristic for scaling lr alongside batch. Above
    B≈64 per-token throughput plateaus on the bank gather +
    PCIe transfer.

    Resumable: latest <base>.ckpts/step-<N>/ wins. Bank mmap files
    survive across runs via the persistent volume (when bank
    storage uses mmap; with MMLLM_BANK_ON_GPU=true the bank
    lives in VRAM and is reset each container restart).

    sqrt_n=0 uses default-config (currently 512 → 1.17 GB bank).
    Pass sqrt_n=2048 for 18.8 GB bank (~20 GB target). Above
    sqrt_n≈1024 the bank V + SparseAdam state exceeds A100 40GB
    VRAM, so we pin to A100-80GB.

    `corpus_base`: when set and different from `base`, symlinks
    <corpus_base>.{train,val,test}.bin → <base>.{train,val,test}.bin
    so train-long finds the data at <base> while ckpts/log/bank
    write under <base>'s namespace. Useful for running multiple
    architectural variants against the same corpus without
    duplicating the data and without colliding outputs.
    """
    if corpus_base and corpus_base != base:
        import os
        for split in ("train", "val", "test"):
            link = f"{base}.{split}.bin"
            target = f"{corpus_base}.{split}.bin"
            if not os.path.lexists(link):
                os.symlink(target, link)
                print(f"  symlinked {link} → {target}", flush=True)
    _run_train_long(
        total_steps, eval_every, ckpt_every, "cuda", lr,
        batch=batch, base=base, bank=bank,
        sqrt_n=(sqrt_n if sqrt_n > 0 else None),
        cpu_offload=cpu_offload,
        lr_warmup=lr_warmup,
        lr_min=(lr_min if lr_min > 0 else None),
        bank_query_mode=bank_query_mode,
        long_tier_mix=long_tier_mix,
        bank_feedback_mode=bank_feedback_mode,
        ablate_every=ablate_every,
        max_hours=max_hours,
        mix=mix,
        lr_dense_mult=lr_dense_mult,
        lr_bank_mult=lr_bank_mult,
        z_loss_coef=z_loss_coef,
        mtp_coef=mtp_coef,
        slot_log_every=slot_log_every,
        dead_slot_reinit=dead_slot_reinit,
        netbank_enabled=netbank_enabled,
        netbank_path=(netbank_path or None),
        netbank_sqrt_n=netbank_sqrt_n,
        netbank_c_net=netbank_c_net,
        netbank_top_k=netbank_top_k,
        netbank_sub_top_k=netbank_sub_top_k,
        netbank_delay_ms_min=netbank_delay_ms_min,
        netbank_delay_ms_max=netbank_delay_ms_max,
        netbank_on_gpu=netbank_on_gpu,
        lr_net_mult=lr_net_mult,
        lr_dense_mult_end=(None if lr_dense_mult_end < 0 else lr_dense_mult_end),
        lr_bank_mult_end =(None if lr_bank_mult_end  < 0 else lr_bank_mult_end),
        lr_net_mult_end  =(None if lr_net_mult_end   < 0 else lr_net_mult_end),
        focal_gamma=focal_gamma,
        importance_head=importance_head,
        importance_aux=importance_aux,
        carry_enabled=carry_enabled,
        carry_n_clocks=carry_n_clocks,
        grad_clip=grad_clip,
        nan_guard=nan_guard,
        log_param_norms=log_param_norms,
        distill_coef=distill_coef,
        distill_direction_only=distill_direction_only,
        alpha_net=alpha_net,
        replay_every=replay_every,
        replay_buffer_size=replay_buffer_size,
        replay_threshold=replay_threshold,
        # 9-spike knobs (-1 sentinels mean "use default")
        lr_kab_mult     =(None if lr_kab_mult     < 0 else lr_kab_mult),
        lr_kab_mult_end =(None if lr_kab_mult_end < 0 else lr_kab_mult_end),
        delim_aux_coef  =delim_aux_coef,
        schema_mask_weight=schema_mask_weight,
        pause_bytes     =pause_bytes,
        pause_prob      =pause_prob,
        pause_byte_val  =pause_byte_val,
        bank_repeat_n   =bank_repeat_n,
        bank_repeat_alpha=bank_repeat_alpha,
        bank_cold_boost =bank_cold_boost,
        bank_cold_boost_eps=bank_cold_boost_eps,
        phase_label    =phase_label,
    )
    if publish_after:
        # Spawn publish on its own container (uses publish_image w/ gh CLI).
        # .remote() blocks; the user gets one final "published" log line
        # when the upload completes. Wrapped so a publish failure doesn't
        # mask a successful training session in the operator's eye.
        try:
            print(f"  → publishing latest ckpt to {gh_repo} ({tag_prefix}-step-N + "
                  f"{tag_prefix}-latest)", flush=True)
            result = publish_ckpt_to_github.remote(
                base=base, ckpt_step=0,
                gh_repo=gh_repo, tag_prefix=tag_prefix,
            )
            print(f"  ✓ published: {result.get('release_url') if result else '(no result)'}",
                  flush=True)
        except Exception as e:
            print(f"  ✗ publish_after failed: {e}\n"
                  f"    Training session succeeded; ckpt is on volume at "
                  f"{base}.ckpts/. Re-publish manually with:\n"
                  f"    modal run modal_app.py::publish_ckpt_to_github "
                  f"--base {base} --gh-repo {gh_repo} --tag-prefix {tag_prefix}",
                  flush=True)


@app.function(
    image=image,
    volumes={"/data": volume},
    timeout=14400,  # 4 h cap — sweep is short
    gpu="T4",       # T4 is fine for short sweeps; A10G reserved for prod
    memory=16384,
)
def lr_sweep(
    lrs: str = "3e-3,1e-3,3e-4,1e-4",
    steps_per: int = 2500,
    eval_every: int = 500,
):
    """Sequentially run train-long at each lr, fresh bank+ckpts each
    time, and tag the JSONL log so we can compare them. Each run
    writes to a separate base prefix on the volume:

      /data/sweep-lr-<tag>.{train,val,test}.bin   (symlinked from text8.*.bin)
      /data/sweep-bank-<tag>.<i>.bin              (fresh per lr)
      /data/sweep-lr-<tag>.ckpts/                 (fresh per lr)
      /data/sweep-lr-<tag>.log.jsonl              (fresh per lr)

    After all runs, prints a summary BPC table.

    `lrs` is comma-separated (Modal CLI can't pass list[float]).
    """
    import os
    import subprocess
    import json

    lrs_parsed = [float(s.strip()) for s in lrs.split(",") if s.strip()]
    print(f"=== lr_sweep {lrs_parsed} steps_per={steps_per} ===", flush=True)
    summaries = []
    for lr in lrs_parsed:
        tag = f"{lr:.0e}".replace("-0", "-")  # 3e-3, 1e-3, 3e-4, 1e-4
        base = f"/data/sweep-lr-{tag}"
        bank = f"/data/sweep-bank-{tag}"

        # Fresh bank + ckpts + log per sweep entry
        for f in [
            f"{bank}.0.bin", f"{bank}.1.bin", f"{bank}.2.bin",
            f"{bank}.3.bin", f"{bank}.4.bin",
            f"{base}.log.jsonl",
        ]:
            try: os.remove(f)
            except FileNotFoundError: pass
        ckpt_dir = f"{base}.ckpts"
        if os.path.isdir(ckpt_dir):
            import shutil
            shutil.rmtree(ckpt_dir)

        # Symlink the data files (text8 corpus already on volume)
        for split in ["train", "val", "test"]:
            link = f"{base}.{split}.bin"
            target = f"/data/text8.{split}.bin"
            try: os.remove(link)
            except FileNotFoundError: pass
            os.symlink(target, link)

        print(f"\n=== sweep entry lr={lr} tag={tag} ===", flush=True)
        _run_train_long(steps_per, eval_every, steps_per,  # ckpt only at end
                        "cuda", lr, base=base, bank=bank)

        # Read final eval line from log
        log_path = f"{base}.log.jsonl"
        try:
            with open(log_path) as f:
                lines = [json.loads(l) for l in f if l.strip()]
            final = next((r for r in reversed(lines) if r.get("event") == "final"), None)
            summaries.append({"lr": lr, "tag": tag, "final": final})
        except Exception as e:
            summaries.append({"lr": lr, "tag": tag, "error": str(e)})

    print("\n═══════════════ lr_sweep summary ═══════════════", flush=True)
    print(f"{'lr':>10}  {'val_bpc':>8}  {'val_ppl':>8}  {'wall_s':>8}", flush=True)
    for s in summaries:
        f = s.get("final")
        if f:
            print(f"{s['lr']:>10.0e}  {f['val_bpc']:>8.4f}  {f['val_ppl']:>8.2f}  {f['wall_s']:>8.1f}",
                  flush=True)
        else:
            print(f"{s['lr']:>10.0e}  ERROR: {s.get('error', 'no final')}", flush=True)
    volume.commit()


@app.function(
    image=image,
    volumes={"/data": volume},
    timeout=3600,
    cpu=4.0,
    memory=16384,
)
def quantize_bank(
    in_prefix: str = "/data/pile-bank-3tier",
    out_prefix: str = "/data/pile-bank-3tier-int8",
    n_layers: int = 5,
    q_dim: int = 224,         # default-config: 7 long heads × 32 head_dim
):
    """Convert a trained fp32 bank V (per-layer raw arrays) into the
    int8 quantized format. Phase 3 of the inference optimization plan.

    Reads /data/<in_prefix>.<i>.bin (fp32 bank from train-long
    `bank_saved` event). Writes /data/<out_prefix>.<i>.int8.bin
    (header + fp16 scales + int8 rows; ~4× smaller).

    Quantization is per-row symmetric int8 with fp16-stored scale.
    See mmllm.memory.quantize_fp32_bank_to_int8_shaped for the math.
    """
    import subprocess
    print(
        f"=== quantize_bank in={in_prefix}.<i>.bin → out={out_prefix}.<i>.int8.bin "
        f"n_layers={n_layers} q_dim={q_dim} ===",
        flush=True,
    )
    subprocess.run(
        ["mmllm", "bank-quantize", in_prefix, out_prefix, str(n_layers)],
        check=True,
    )
    volume.commit()
    print(f"done — int8 bank committed to {out_prefix}.<i>.int8.bin", flush=True)


# ─────────────────────── publish ckpt → GitHub Release ───────────────────────
#
# Auto-publish the latest slow-walk ckpt (dense.pt + int8-quantized bank V)
# to a GitHub Release. Per-step tag is immutable; a moving "<prefix>-latest"
# tag is force-replaced each call so the laptop pull command can always
# point at the same URL.
#
# Constraint inherited from save-checkpoint!: bank-latest.<i>.bin is
# overwritten on every save, so this function publishes whatever bank
# state is CURRENTLY on volume — paired with the resolved ckpt_step's
# dense.pt. If you ckpt at step 30k, train another session to step 32.5k,
# then call publish for ckpt_step=30000, the bank would be the step-32500
# state — mismatched. Guard: we only support ckpt_step=0 (auto-resolves to
# latest) or ckpt_step=<latest step on disk>; any older value errors.


@app.function(
    image=publish_image,
    volumes={"/data": volume},
    # Conditional Secret reference — see `_maybe_secret` above. If the
    # 'github-token' Secret is missing the app still loads, but calling
    # this function will raise a clear "GITHUB_TOKEN not set" error at
    # the os.environ.get() check in the body.
    secrets=_PUBLISH_SECRETS,
    timeout=3600,         # 1 h cap — quantize + upload of 5+1 GB total
    cpu=4.0,
    memory=16384,
)
def publish_ckpt_to_github(
    base:          str  = "/data/agent-corpus",
    ckpt_step:     int  = 0,                # 0 = auto-resolve to latest on disk
    gh_repo:       str  = "johnmn3/mmllm",
    tag_prefix:    str  = "agent",
    n_layers:      int  = 5,
    q_dim:         int  = 224,
    update_latest: bool = True,
    notes:         str  = "",                # optional addendum to the release body
):
    """Quantize bank V → int8, upload (dense.pt + 5 × bank.int8.bin) to
    a GitHub Release.

    Per-step release: <tag_prefix>-step-<N>     (immutable; idempotent
                                                  re-publish skips if
                                                  already present)
    Latest release:   <tag_prefix>-latest        (force-replaced each call
                                                  if update_latest=True)

    Requires a Modal Secret named `github-token` with GITHUB_TOKEN set
    to a PAT that has `repo` + `write:packages` scope on `gh_repo`.
    Set up once via:

        modal secret create github-token GITHUB_TOKEN=ghp_xxx
    """
    import os
    import re
    import subprocess
    from pathlib import Path

    ckpts_dir = f"{base}.ckpts"
    if not os.path.isdir(ckpts_dir):
        raise FileNotFoundError(f"no ckpts dir at {ckpts_dir}")

    # Resolve latest step on disk.
    on_disk = []
    for d in os.listdir(ckpts_dir):
        m = re.match(r"step-(\d+)$", d)
        if m:
            on_disk.append(int(m.group(1)))
    if not on_disk:
        raise FileNotFoundError(f"no step-<N> dirs under {ckpts_dir}")
    latest_step = max(on_disk)

    if ckpt_step <= 0:
        ckpt_step = latest_step
        print(f"  resolved ckpt_step=latest → {ckpt_step}", flush=True)
    elif ckpt_step != latest_step:
        # bank-latest.<i>.bin reflects the most-recent save-checkpoint!
        # call. Pairing it with an older dense.pt would publish
        # mismatched state.
        raise ValueError(
            f"ckpt_step={ckpt_step} != latest_on_disk={latest_step}; "
            f"bank-latest.<i>.bin was overwritten at step {latest_step}, "
            f"so publishing step {ckpt_step}'s dense with the current "
            f"bank state would be incoherent. Use ckpt_step=0 (auto-latest) "
            f"or republish step {latest_step}.",
        )

    dense_pt = f"{ckpts_dir}/step-{ckpt_step}/dense.pt"
    if not os.path.exists(dense_pt):
        raise FileNotFoundError(dense_pt)
    bank_files_fp32 = [f"{ckpts_dir}/bank-latest.{i}.bin"
                       for i in range(n_layers)]
    for bf in bank_files_fp32:
        if not os.path.exists(bf):
            raise FileNotFoundError(bf)

    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise RuntimeError(
            "GITHUB_TOKEN not in env — Modal Secret 'github-token' missing or "
            "doesn't expose GITHUB_TOKEN. Run "
            "`modal secret create github-token GITHUB_TOKEN=<your_pat>`.",
        )
    env = {**os.environ, "GH_TOKEN": token}

    # Quantize bank → int8. Output goes alongside the fp32 bank-latest
    # files so we don't have to manage another path. Cleanup at the end.
    int8_prefix = f"{ckpts_dir}/bank-publish-int8"
    print(f"  quantize: {ckpts_dir}/bank-latest.<i>.bin → "
          f"{int8_prefix}.<i>.int8.bin", flush=True)
    subprocess.run(
        ["mmllm", "bank-quantize",
         f"{ckpts_dir}/bank-latest", int8_prefix, str(n_layers)],
        check=True,
    )
    int8_files = [f"{int8_prefix}.{i}.int8.bin" for i in range(n_layers)]
    for bf in int8_files:
        if not os.path.exists(bf):
            raise FileNotFoundError(f"quantize did not produce {bf}")

    step_tag = f"{tag_prefix}-step-{ckpt_step}"
    latest_tag = f"{tag_prefix}-latest"

    # Per-step release body.
    body = (
        f"mmllm slow-walk ckpt at step {ckpt_step}\n\n"
        f"Bundle:\n"
        f"- `dense.pt` — trained dense weights\n"
        f"- `bank-publish-int8.{{0..{n_layers-1}}}.int8.bin` — int8 quantized "
        f"bank V (per-row symmetric, fp16 scale; "
        f"~4× compression vs fp32)\n\n"
        f"Pull on a laptop / non-Modal box:\n"
        f"```\n"
        f"MMLLM_ARTIFACTS_URL=https://github.com/{gh_repo}/releases/download/"
        f"{step_tag} \\\n"
        f"  mmllm fetch-artifacts /tmp/agent-bench\n"
        f"```\n"
    )
    if notes:
        body += f"\n---\n\n{notes}\n"

    # Per-step tag — idempotent (skip if exists). We never force-replace
    # a step tag (immutable per-ckpt artifact).
    existing = subprocess.run(
        ["gh", "release", "view", step_tag, "--repo", gh_repo],
        env=env, capture_output=True,
    )
    if existing.returncode == 0:
        print(f"  release {step_tag} already exists — skipping per-step "
              f"upload (use a different tag-prefix to re-publish)",
              flush=True)
    else:
        print(f"  → publishing {step_tag} ({1 + n_layers} files, "
              f"~{0.2 + n_layers * 0.94:.1f} GB)", flush=True)
        subprocess.run(
            ["gh", "release", "create", step_tag,
             "--repo", gh_repo,
             "--title", f"mmllm agent ckpt step-{ckpt_step}",
             "--notes", body,
             dense_pt, *int8_files],
            env=env,
            check=True,
        )

    # Latest tag — force-replace each call so a fixed URL points at
    # current state.
    if update_latest:
        # Delete the old latest release (and tag — --cleanup-tag on gh
        # 2.32+). Ignore failure if it didn't exist.
        del_result = subprocess.run(
            ["gh", "release", "delete", latest_tag, "--yes",
             "--cleanup-tag", "--repo", gh_repo],
            env=env, capture_output=True,
        )
        if del_result.returncode == 0:
            print(f"  removed previous {latest_tag}", flush=True)

        latest_body = (
            f"Latest mmllm slow-walk ckpt — currently step {ckpt_step} "
            f"(immutable mirror at {step_tag}).\n\n"
            f"This tag is force-replaced after each training session. "
            f"Pin to a specific step via `{step_tag}` for reproducibility.\n\n"
            + body
        )
        print(f"  → force-replacing {latest_tag} → step {ckpt_step}", flush=True)
        subprocess.run(
            ["gh", "release", "create", latest_tag,
             "--repo", gh_repo,
             "--title", f"mmllm agent latest (step-{ckpt_step})",
             "--notes", latest_body,
             dense_pt, *int8_files],
            env=env,
            check=True,
        )

    # Cleanup the temp int8 files. Saves ~5 GB on volume between sessions.
    for f in int8_files:
        try:
            os.unlink(f)
        except OSError:
            pass
    volume.commit()

    print(f"  done — published step {ckpt_step} to {gh_repo}", flush=True)
    return {
        "step":          ckpt_step,
        "step_tag":      step_tag,
        "latest_tag":    latest_tag if update_latest else None,
        "gh_repo":       gh_repo,
        "release_url":   f"https://github.com/{gh_repo}/releases/tag/{step_tag}",
    }


@app.function(
    image=image,
    volumes={"/data": volume},
    timeout=1800,
    gpu="H100",
    memory=131072,    # 128 GB — at sqrt_n=2048 fp32, bank in VRAM is 18.8 GB,
                       # plus per-sequence KV caches scale with B (~21 MB/seq)
)
def bench_inference_batch(
    base: str = "/data/pile-github.bin",
    ckpt_step: int = 305000,
    bank: str = "/data/pile-bank-3tier",
    n_warm: int = 10,
    n_time: int = 50,
    sqrt_n: int = 2048,
    bank_on_gpu: bool = True,
    bank_dtype: str = "fp32",        # fp32 (use the .bin bank) or int8 (.int8.bin)
    batch: int = 32,                 # synchronized batch size
    bank_query_mode: str = "plain",
    long_tier_mix:   str = "sum",
    bank_feedback_mode: str = "plain",
):
    """Phase-2 continuous-batching bench on H100 (single GPU).

    Decodes n_time tokens in parallel for B sequences and reports
    aggregate throughput. Same architectural premise as the local
    CPU bench (mmllm bench-batch) but on a much higher-throughput
    matmul backend.

    For multi-GPU aggregate throughput: each H100 in a DGX runs an
    independent server process serving its own B sequences with its
    own dense weights; the bank can be shared via a node-level
    networked filesystem with mmap, or each GPU loads its own copy
    in VRAM. Linear scaling with GPU count once interconnect cost
    is amortized over the batch.
    """
    import os, subprocess
    env = {**os.environ,
           "MMLLM_DEVICE":            "cuda",
           "MMLLM_SQRT_N":            str(sqrt_n),
           "MMLLM_BANK_ON_GPU":       "true" if bank_on_gpu else "false",
           "MMLLM_BANK_DTYPE":        bank_dtype,
           "MMLLM_BANK_QUERY_MODE":   bank_query_mode,
           "MMLLM_LONG_TIER_MIX":     long_tier_mix,
           "MMLLM_BANK_FEEDBACK_MODE": bank_feedback_mode}
    bank_arg = (bank if bank_dtype != "int8"
                else bank.replace("/data/pile-bank-3tier",
                                  "/data/pile-bank-3tier-int8"))
    print(
        f"=== bench_inference_batch base={base} ckpt={ckpt_step} bank={bank_arg} "
        f"sqrt_n={sqrt_n} bank_on_gpu={bank_on_gpu} bank_dtype={bank_dtype} "
        f"batch={batch} n_warm={n_warm} n_time={n_time} ===",
        flush=True,
    )
    subprocess.run(
        ["mmllm", "bench-batch", base, str(ckpt_step), bank_arg,
         str(n_warm), str(n_time), str(batch)],
        check=True, env=env,
    )


@app.function(
    image=image,
    volumes={"/data": volume},
    timeout=1800,
    gpu="H100",
    memory=65536,
)
def bench_inference(
    base: str = "/data/pile-github.bin",
    ckpt_step: int = 305000,
    bank: str = "/data/pile-bank-3tier",
    n_warm: int = 50,
    n_time: int = 500,
    sqrt_n: int = 2048,
    bank_on_gpu: bool = True,
    compile_forward: bool = False,   # MMLLM_COMPILE — Phase-1a
    dense_dtype: str = "",           # 'bf16' enables Phase-1 step C1 cast
    num_threads: int = 0,            # 0 = container cpu_count; sets MMLLM_NUM_THREADS
    max_t: int = 0,                  # 0 = config default (4096); sets MMLLM_MAX_T
    bank_query_mode: str = "plain",  # MUST match the trained ckpt's mode
    long_tier_mix:   str = "sum",    # MUST match the trained ckpt's mode
    bank_feedback_mode: str = "plain",  # MUST match the trained ckpt's mode
):
    """Benchmark per-token inference speed on a trained checkpoint.

    bank_on_gpu=True   : bank V loaded into cuda VRAM. Single-instance,
                         fastest path. Bank is per-process (no sharing
                         across parallel inference instances).
    bank_on_gpu=False  : bank V is mmap'd from disk; per-token cross-
                         device gather of top-K rows CPU→GPU. Slower
                         per token but allows N parallel inference
                         instances to share one bank via mmap pages.

    Phase-1 toggles:
      compile_forward=True → MMLLM_COMPILE=true (torch.compile of
        the per-token forward; ~30-50% gain expected with static
        shapes from pre-alloc KV).
      dense_dtype='bf16'   → MMLLM_DENSE_DTYPE=bf16 (cast dense Linear
        weights to bf16 before bench; halves dense memory bandwidth).

    Architectural mode flags MUST match what the checkpoint was trained
    with — bench-inference loads dense.pt by parameter order, so a
    feedback-trained ckpt loaded into a plain-built model will fail
    on parameter-count mismatch (extra W_probe/W_back tensors).

    Reports tok/sec and ms/tok at batch=1. Both modes use the same
    trained dense weights from <base>.ckpts/step-<ckpt_step>/dense.pt
    and the same bank V at <bank>.<i>.bin.
    """
    import os, subprocess
    env = {**os.environ,
           "MMLLM_DEVICE":            "cuda",
           "MMLLM_SQRT_N":            str(sqrt_n),
           "MMLLM_BANK_ON_GPU":       "true" if bank_on_gpu else "false",
           "MMLLM_COMPILE":           "true" if compile_forward else "false",
           "MMLLM_BANK_QUERY_MODE":   bank_query_mode,
           "MMLLM_LONG_TIER_MIX":     long_tier_mix,
           "MMLLM_BANK_FEEDBACK_MODE": bank_feedback_mode}
    if dense_dtype:
        env["MMLLM_DENSE_DTYPE"] = dense_dtype
    if num_threads > 0:
        env["MMLLM_NUM_THREADS"] = str(num_threads)
    if max_t > 0:
        env["MMLLM_MAX_T"] = str(max_t)
    print(
        f"=== bench_inference base={base} ckpt={ckpt_step} bank={bank} "
        f"sqrt_n={sqrt_n} bank_on_gpu={bank_on_gpu} "
        f"compile_forward={compile_forward} dense_dtype={dense_dtype or 'fp32'} "
        f"num_threads={num_threads or 'default'} max_t={max_t or 'default'} "
        f"bq={bank_query_mode} ltm={long_tier_mix} fb={bank_feedback_mode} "
        f"n_warm={n_warm} n_time={n_time} ===",
        flush=True,
    )
    subprocess.run(
        ["mmllm", "bench", base, str(ckpt_step), bank,
         str(n_warm), str(n_time)],
        check=True, env=env,
    )


@app.function(
    image=image,
    volumes={"/data": volume},
    timeout=1800,
    cpu=8.0,
    memory=32768,    # bank V at sqrt_n=2048 is 18.8 GB; need RAM headroom
)
def bench_inference_cpu(
    base: str = "/data/pile-github.bin",
    ckpt_step: int = 305000,
    bank: str = "/data/pile-bank-3tier",
    n_warm: int = 50,
    n_time: int = 200,
    sqrt_n: int = 2048,
    compile_forward: bool = False,   # MMLLM_COMPILE — Phase-1a
    dense_dtype: str = "",           # 'bf16' for Phase-1 step C1
    num_threads: int = 0,            # 0 = container cpu_count
    max_t: int = 0,                  # 0 = config default (4096)
    bank_query_mode: str = "plain",  # MUST match the trained ckpt's mode
    long_tier_mix:   str = "sum",    # MUST match the trained ckpt's mode
    bank_feedback_mode: str = "plain",  # MUST match the trained ckpt's mode
):
    """CPU-only inference benchmark on a trained checkpoint. Many
    end-users will run this CPU-bound (no GPU available, edge deploy,
    laptop, etc.) — measure that path explicitly.

    The bank is mmap'd from disk on CPU; the cross-device gather is a
    no-op (everything stays on CPU). At batch=1 this measures the
    single-conversation latency a CPU user would see.

    sqrt_n=2048 means 18.8 GB bank V; container needs >=24 GB RAM.

    Architectural mode flags MUST match what the checkpoint was trained
    with — see bench_inference docstring.
    """
    import os, subprocess
    env = {**os.environ,
           "MMLLM_DEVICE":            "cpu",
           "MMLLM_SQRT_N":            str(sqrt_n),
           "MMLLM_BANK_ON_GPU":       "false",     # no GPU; bank stays mmap'd
           "MMLLM_COMPILE":           "true" if compile_forward else "false",
           "MMLLM_BANK_QUERY_MODE":   bank_query_mode,
           "MMLLM_LONG_TIER_MIX":     long_tier_mix,
           "MMLLM_BANK_FEEDBACK_MODE": bank_feedback_mode}
    if dense_dtype:
        env["MMLLM_DENSE_DTYPE"] = dense_dtype
    if num_threads > 0:
        env["MMLLM_NUM_THREADS"] = str(num_threads)
    if max_t > 0:
        env["MMLLM_MAX_T"] = str(max_t)
    print(
        f"=== bench_inference_cpu base={base} ckpt={ckpt_step} bank={bank} "
        f"sqrt_n={sqrt_n} compile_forward={compile_forward} "
        f"dense_dtype={dense_dtype or 'fp32'} "
        f"num_threads={num_threads or 'default'} max_t={max_t or 'default'} "
        f"bq={bank_query_mode} ltm={long_tier_mix} fb={bank_feedback_mode} "
        f"n_warm={n_warm} n_time={n_time} ===",
        flush=True,
    )
    subprocess.run(
        ["mmllm", "bench", base, str(ckpt_step), bank,
         str(n_warm), str(n_time)],
        check=True, env=env,
    )


@app.function(
    image=image,
    volumes={"/data": volume},
    timeout=86400,
    cpu=4.0,
    memory=8192,
)
def train_with_bank_cpu(
    total_steps: int = 100000,
    eval_every: int = 1000,
    ckpt_every: int = 5000,
    lr: float = 3e-3,
    batch: int = 4,
):
    """CPU-only fallback (slower; useful for debugging or as a control
    against the GPU run). Same volume layout, same checkpoint format."""
    _run_train_long(total_steps, eval_every, ckpt_every, "cpu", lr, batch=batch)


@app.function(
    image=image,
    volumes={"/data": volume},
    timeout=3600,
    cpu=4.0,
    memory=8192,
)
def spike_bank_query(
    steps: int = 200,
    eval_every: int = 100,
    sqrt_n: int = 128,
    batch: int = 4,
):
    """Spike: compare bank-query='plain' vs 'ctx-add' on a 200-step
    text8 smoke. Both runs use long-tier-mix='sum' to isolate the
    bank-query change. Reports control bpc + bank-zero Δ for each.

    Pass criteria:
      - both runs complete without error
      - both show loss descent
      - ctx-add starts identical to plain at step 0 (W_ctx zero-init);
        any difference in final bpc reflects what the dense weights
        learned to add to the bank query
    """
    import os, subprocess, shutil, json
    summary = {}
    for bq in ("plain", "ctx-add"):
        base = f"/data/spike-bq-{bq}"
        bank = f"/data/spike-bq-{bq}-bank"
        for f in (
            f"{base}.train.bin", f"{base}.val.bin", f"{base}.test.bin",
            f"{base}.log.jsonl",
            *[f"{bank}.{i}.bin" for i in range(5)],
        ):
            try: os.remove(f)
            except FileNotFoundError: pass
        if os.path.isdir(f"{base}.ckpts"):
            shutil.rmtree(f"{base}.ckpts")
        for split in ("train", "val", "test"):
            os.symlink(f"/data/text8.{split}.bin", f"{base}.{split}.bin")

        env = {**os.environ,
               "MMLLM_DEVICE": "cpu",
               "MMLLM_BATCH":  str(batch),
               "MMLLM_LR":     "3e-3",
               "MMLLM_SQRT_N": str(sqrt_n),
               "MMLLM_LONG_TIER_MIX": "sum",
               "MMLLM_BANK_QUERY_MODE": bq}
        print(f"=== spike_bank_query: bank-query={bq} steps={steps} ===", flush=True)
        subprocess.run(
            ["mmllm", "train-long", base, bank,
             str(steps), str(eval_every), str(steps + 1)],
            check=True, env=env,
        )
        try:
            lines = open(f"{base}.log.jsonl").read().strip().splitlines()
            ablations = [json.loads(l) for l in lines
                         if json.loads(l).get("event") == "ablation"]
            if ablations:
                a = ablations[-1]
                summary[bq] = {
                    "control_bpc": a["control_bpc"],
                    "ablated_bpc": a["ablated_bpc"],
                    "delta_bpc":   a["delta_bpc"],
                }
        except Exception as e:
            print(f"  WARN: could not parse log for {bq}: {e}", flush=True)

    print("\n=== spike_bank_query summary ===", flush=True)
    print(f"  {'bq':10} {'control':>10} {'ablated':>10} {'Δ':>10}", flush=True)
    for bq, r in summary.items():
        print(f"  {bq:10} {r['control_bpc']:10.4f} {r['ablated_bpc']:10.4f} {r['delta_bpc']:+10.4f}",
              flush=True)
    print("=== spike_bank_query: done ===", flush=True)


@app.function(
    image=image,
    volumes={"/data": volume},
    timeout=3600,
    cpu=4.0,
    memory=8192,
)
def spike_bank_feedback(
    steps: int = 200,
    eval_every: int = 100,
    sqrt_n: int = 128,
    batch: int = 4,
):
    """Spike: 4-way A/B of bank-query × bank-feedback combos at 200
    steps, sqrt_n=128 on text8. Validates whether bidirectional
    retrieval-augmented attention earns its keep beyond either
    direction alone.

    Combos:
      - plain   + plain     (baseline; matches spike_bank_query's plain)
      - ctx-add + plain     (current best per spike_bank_query)
      - plain   + feedback  (pure bank → dense feedback)
      - ctx-add + feedback  (both directions wired up)

    Pass criteria:
      - all four runs complete without error
      - all four show loss descent
      - directional signal: (ctx-add, feedback) shows non-trivial bpc
        improvement over (ctx-add, plain). If (plain, feedback) alone
        also improves over (plain, plain), feedback is independently
        useful; if it doesn't, the feedback path needs ctx-add to
        meaningfully exploit the bank.
    """
    import os, subprocess, shutil, json
    summary = {}
    combos = [
        ("plain",   "plain"),
        ("ctx-add", "plain"),
        ("plain",   "feedback"),
        ("ctx-add", "feedback"),
    ]
    for bq, fb in combos:
        tag = f"bq-{bq}_fb-{fb}"
        base = f"/data/spike-fb-{tag}"
        bank = f"/data/spike-fb-{tag}-bank"
        for f in (
            f"{base}.train.bin", f"{base}.val.bin", f"{base}.test.bin",
            f"{base}.log.jsonl",
            *[f"{bank}.{i}.bin" for i in range(5)],
        ):
            try: os.remove(f)
            except FileNotFoundError: pass
        if os.path.isdir(f"{base}.ckpts"):
            shutil.rmtree(f"{base}.ckpts")
        for split in ("train", "val", "test"):
            os.symlink(f"/data/text8.{split}.bin", f"{base}.{split}.bin")

        env = {**os.environ,
               "MMLLM_DEVICE": "cpu",
               "MMLLM_BATCH":  str(batch),
               "MMLLM_LR":     "3e-3",
               "MMLLM_SQRT_N": str(sqrt_n),
               "MMLLM_LONG_TIER_MIX":      "sum",
               "MMLLM_BANK_QUERY_MODE":    bq,
               "MMLLM_BANK_FEEDBACK_MODE": fb}
        print(f"=== spike_bank_feedback: bq={bq} fb={fb} steps={steps} ===",
              flush=True)
        subprocess.run(
            ["mmllm", "train-long", base, bank,
             str(steps), str(eval_every), str(steps + 1)],
            check=True, env=env,
        )
        try:
            lines = open(f"{base}.log.jsonl").read().strip().splitlines()
            ablations = [json.loads(l) for l in lines
                         if json.loads(l).get("event") == "ablation"]
            if ablations:
                a = ablations[-1]
                summary[tag] = {
                    "control_bpc": a["control_bpc"],
                    "ablated_bpc": a["ablated_bpc"],
                    "delta_bpc":   a["delta_bpc"],
                }
        except Exception as e:
            print(f"  WARN: could not parse log for {tag}: {e}", flush=True)

    print("\n=== spike_bank_feedback summary ===", flush=True)
    print(f"  {'combo':22} {'control':>10} {'ablated':>10} {'Δ':>10}", flush=True)
    for tag, r in summary.items():
        print(f"  {tag:22} {r['control_bpc']:10.4f} {r['ablated_bpc']:10.4f} {r['delta_bpc']:+10.4f}",
              flush=True)
    print("=== spike_bank_feedback: done ===", flush=True)


@app.function(
    image=image,
    volumes={"/data": volume},
    timeout=3600,
    cpu=4.0,
    memory=8192,
)
def spike_long_gates(
    steps: int = 200,
    eval_every: int = 100,
    sqrt_n: int = 128,
    batch: int = 4,
    short_window: int = 0,   # 0 = unbounded
    long_window: int = 0,
):
    """Spike: compare 'sum' / 'scalar' / 'switch' long-tier path-mixing
    on a 200-step text8 smoke. Reports control bpc + bank-zero Δ for each.
    Each run is a fresh model, fresh bank, same data; only the gate kind
    differs. Runs sequentially on CPU; ~3-5 min total.

    Pass criteria:
      - all three runs complete without error
      - all three show loss descent (final < initial)
      - either scalar or switch should produce a different control_bpc
        than sum (proves the gate is actually doing something)
    """
    import os, subprocess, shutil, json
    summary = {}
    for kind in ("sum", "scalar", "switch"):
        base = f"/data/spike-{kind}"
        bank = f"/data/spike-{kind}-bank"
        for f in (
            f"{base}.train.bin", f"{base}.val.bin", f"{base}.test.bin",
            f"{base}.log.jsonl",
            *[f"{bank}.{i}.bin" for i in range(5)],
        ):
            try: os.remove(f)
            except FileNotFoundError: pass
        if os.path.isdir(f"{base}.ckpts"):
            shutil.rmtree(f"{base}.ckpts")
        for split in ("train", "val", "test"):
            os.symlink(f"/data/text8.{split}.bin", f"{base}.{split}.bin")

        env = {**os.environ,
               "MMLLM_DEVICE": "cpu",
               "MMLLM_BATCH":  str(batch),
               "MMLLM_LR":     "3e-3",
               "MMLLM_SQRT_N": str(sqrt_n),
               "MMLLM_LONG_TIER_MIX": kind}
        if short_window > 0:
            env["MMLLM_SHORT_WINDOW"] = str(short_window)
        if long_window > 0:
            env["MMLLM_LONG_WINDOW"] = str(long_window)
        print(f"=== spike_long_gates: kind={kind} steps={steps} ===", flush=True)
        subprocess.run(
            ["mmllm", "train-long", base, bank,
             str(steps), str(eval_every), str(steps + 1)],
            check=True, env=env,
        )
        # Pull final ablation summary from the log
        try:
            lines = open(f"{base}.log.jsonl").read().strip().splitlines()
            ablations = [json.loads(l) for l in lines
                         if json.loads(l).get("event") == "ablation"]
            if ablations:
                a = ablations[-1]
                summary[kind] = {
                    "control_bpc": a["control_bpc"],
                    "ablated_bpc": a["ablated_bpc"],
                    "delta_bpc":   a["delta_bpc"],
                }
        except Exception as e:
            print(f"  WARN: could not parse log for {kind}: {e}", flush=True)

    print("\n=== spike_long_gates summary ===", flush=True)
    print(f"  {'kind':10} {'control':>10} {'ablated':>10} {'Δ':>10}", flush=True)
    for kind, r in summary.items():
        print(f"  {kind:10} {r['control_bpc']:10.4f} {r['ablated_bpc']:10.4f} {r['delta_bpc']:+10.4f}",
              flush=True)
    print("=== spike_long_gates: done ===", flush=True)


@app.function(
    image=image,
    volumes={"/data": volume},
    timeout=1800,
    cpu=4.0,
    memory=8192,
)
def smoke_3tier(
    total_steps: int = 100,
    eval_every: int = 50,
    ckpt_every: int = 100,
    sqrt_n: int = 128,    # tiny bank: 16384 entries × 224 dim ≈ 14 MB/layer
    batch: int = 4,
    lr: float = 3e-3,
):
    """Smoke test for the three-tier architecture (short / long-KV / bank).
    Fresh base + bank under /data/smoke-3tier* so it doesn't collide with
    any prior run state. Validates: forward shapes, backward, BPC eval,
    bank ablation, save_to_mmap. Should complete in 1-3 min on 4 CPUs.

    Pass criteria (printed at end of run):
      - loss decreases (any steady downward trend over 100 steps)
      - eval-bpc returns finite numbers
      - control bpc < ablated bpc (Δ > 0; bank carries some signal)
      - bank V mmap files exist on the volume
    """
    import os, subprocess, shutil
    base = "/data/smoke-3tier"
    bank = "/data/smoke-3tier-bank"

    print("=== smoke_3tier: clean prior smoke artifacts ===", flush=True)
    for f in (
        f"{base}.train.bin", f"{base}.val.bin", f"{base}.test.bin",
        f"{base}.log.jsonl",
        f"{bank}.0.bin", f"{bank}.1.bin", f"{bank}.2.bin",
        f"{bank}.3.bin", f"{bank}.4.bin",
    ):
        try: os.remove(f)
        except FileNotFoundError: pass
    if os.path.isdir(f"{base}.ckpts"):
        shutil.rmtree(f"{base}.ckpts")

    print("=== smoke_3tier: symlink text8 splits ===", flush=True)
    for split in ("train", "val", "test"):
        os.symlink(f"/data/text8.{split}.bin", f"{base}.{split}.bin")

    print(f"=== smoke_3tier: train sqrt_n={sqrt_n} steps={total_steps} ===", flush=True)
    _run_train_long(
        total_steps, eval_every, ckpt_every, "cpu", lr,
        batch=batch, base=base, bank=bank, sqrt_n=sqrt_n,
    )

    print("=== smoke_3tier: verify bank mmap files ===", flush=True)
    for i in range(5):
        path = f"{bank}.{i}.bin"
        if os.path.exists(path):
            size_mb = os.path.getsize(path) / (1024 * 1024)
            print(f"  {path}: {size_mb:.1f} MB", flush=True)
        else:
            print(f"  MISSING: {path}", flush=True)
    print("=== smoke_3tier: done ===", flush=True)


# ─────────────────────── multi-trainer (Hogwild-style) ───────────────────────


@app.function(
    image=image,
    volumes={"/data": volume},
    timeout=3600,
    cpu=4.0,
    memory=16384,
)
def prepare_bank(bank_path: str = "/data/shared-bank",
                 sqrt_n: int = 2048,
                 q_dim: int = 224,
                 n_layers: int = 5):
    """Pre-create + initialize bank V mmap files for multi-trainer.

    Idempotent: existing files at the right size are kept. Otherwise
    each <bank_path>.<i>.bin is created at sqrt_n²·q_dim·4 bytes and
    Gaussian-initialized. Run once before train_multi to ensure the
    N concurrent trainers all open existing files in mode='r+' and
    don't race on first-write init.
    """
    import sys
    sys.path.insert(0, "/code/src")
    from mmllm.memory import prepare_bank_files
    print(
        f"=== prepare_bank {bank_path} sqrt_n={sqrt_n} q_dim={q_dim} "
        f"n_layers={n_layers} ===",
        flush=True,
    )
    result = prepare_bank_files(bank_path, n_layers, sqrt_n, q_dim)
    for p in result["paths"]:
        cached = "cached" if p["cached"] else "created"
        print(f"  {p['path']}  ({p['bytes']/1e9:.2f} GB, {cached})", flush=True)
    volume.commit()
    print(
        f"done — total bank size {result['total_bytes']/1e9:.2f} GB", flush=True
    )


@app.function(
    image=image,
    volumes={"/data": volume},
    timeout=7200,                  # NetBank can be 80+GB; init takes longer
    cpu=8.0,
    memory=32768,
)
def prepare_netbank(bank_path: str = "/data/aesop-v3-bank-net",
                    sqrt_n: int = 8192,
                    c_net: int = 64,
                    n_layers: int = 5,
                    dtype: str = "fp32"):
    """Pre-create + initialize NetBank V mmap files (one per layer).
    Idempotent: existing correctly-sized files are kept.

    At sqrt_n=8192 + c_net=64 + fp32 = 17.2 GB per layer × 5 = 85.9 GB.
    Run once before the first NetBank-enabled training launch so the
    first session doesn't burn 10-20 min on Gaussian init.
    """
    import sys
    sys.path.insert(0, "/code/src")
    from mmllm.netbank import prepare_netbank_files
    print(
        f"=== prepare_netbank {bank_path} sqrt_n={sqrt_n} c_net={c_net} "
        f"dtype={dtype} n_layers={n_layers} ===",
        flush=True,
    )
    result = prepare_netbank_files(bank_path, n_layers, sqrt_n, c_net, dtype)
    for p in result["paths"]:
        cached = "cached" if p["cached"] else "created"
        print(f"  {p['path']}  ({p['bytes']/1e9:.2f} GB, {cached})", flush=True)
    volume.commit()
    print(
        f"done — total netbank size {result['total_bytes']/1e9:.2f} GB", flush=True
    )
    return result


@app.function(
    image=image,
    volumes={"/data": volume},
    timeout=86400,
    gpu="A100-80GB",
    memory=65536,
)
def train_with_bank_worker(
    trainer_id: int = 0,
    total_steps: int = 25000,
    eval_every: int = 1000,
    ckpt_every: int = 5000,
    lr: float = 1.4e-3,
    lr_dense_mult: float = 1.0,
    lr_bank_mult: float = 1.0,
    batch: int = 128,
    sqrt_n: int = 2048,
    bank: str = "/data/shared-bank",
    base: str = "/data/pile-github.bin",
    sync_every: int = 100,
    volume_name: str = "mmllm-data",
    bank_query_mode: str = "plain",
    long_tier_mix: str = "sum",
    bank_feedback_mode: str = "plain",
):
    """One worker in a Hogwild-style multi-trainer pool.

    Crucially uses bank_on_gpu=False — bank V lives in the mmap'd
    file shared across all workers. Each worker owns its own dense
    weights, AdamW state, SparseAdam state (m, v moments) on its
    own GPU/host RAM.

    Cross-worker bank sharing happens via PagedMmapStorage: every
    `sync_every` training steps each worker commits its bank pages
    to the named Modal Volume, then reloads to pull other workers'
    commits and re-mmaps so V.weight sees the freshest content.
    Modal commits are last-writer-wins per file; row-level
    interleaving across pages is accepted as Hogwild noise.

    Per-worker outputs derive from `trainer_id`:
      - log:  <base>.t<id>.log.jsonl
      - ckpt: <base>.t<id>.ckpts/
    Bank is shared at <bank>.<i>.bin across all workers.
    """
    import os
    import subprocess
    # Per-worker output paths so logs/ckpts don't collide
    worker_base = f"{base}.t{trainer_id}"
    # Symlink the corpus splits so train-long sees the right names
    for split in ("train", "val", "test"):
        link = f"{worker_base}.{split}.bin"
        target = f"{base}.{split}.bin"
        if not os.path.lexists(link):
            os.symlink(target, link)
    print(f"=== worker {trainer_id} base={worker_base} bank={bank} "
          f"sync_every={sync_every} ===", flush=True)
    _run_train_long(
        total_steps, eval_every, ckpt_every, "cuda", lr,
        batch=batch, base=worker_base, bank=bank,
        sqrt_n=sqrt_n,
        cpu_offload=True,
        bank_on_gpu=False,  # ← shared mmap bank, not per-trainer GPU copy
        sync_every=sync_every,
        volume_name=volume_name,
        bank_query_mode=bank_query_mode,
        long_tier_mix=long_tier_mix,
        bank_feedback_mode=bank_feedback_mode,
        lr_dense_mult=lr_dense_mult,
        lr_bank_mult=lr_bank_mult,
    )


@app.local_entrypoint()
def train_multi(n_trainers: int = 4,
                total_steps: int = 25000,
                eval_every: int = 1000,
                ckpt_every: int = 5000,
                lr: float = 1.4e-3,
                lr_dense_mult: float = 1.0,
                lr_bank_mult: float = 1.0,
                batch: int = 128,
                sqrt_n: int = 2048,
                bank: str = "/data/shared-bank",
                base: str = "/data/pile-github.bin",
                sync_every: int = 100,
                volume_name: str = "mmllm-data",
                bank_query_mode: str = "plain",
                long_tier_mix: str = "sum"):
    """Orchestrator: pre-init bank, fan out N parallel
    train_with_bank_worker calls all sharing the same bank file.

    Pattern A (data-parallel): all workers point at the same `base`.
        Each samples random sub-batches with its own RNG; effective
        batch is N×batch on the same data distribution.

    Pattern B (multi-task): pass different `base` per worker. Not
        directly supported by this entrypoint yet — extend by
        looping over a list of (corpus_path, dense_ckpt_path) pairs
        instead of a single base.
    """
    print(f"=== train_multi: n_trainers={n_trainers} steps={total_steps} "
          f"sqrt_n={sqrt_n} bank={bank} base={base} "
          f"bank_query_mode={bank_query_mode} long_tier_mix={long_tier_mix} ===",
          flush=True)
    # 1. Make sure bank files exist at the right size so workers can
    #    safely open r+ (no first-write race).
    print("preparing shared bank…", flush=True)
    prepare_bank.remote(bank_path=bank, sqrt_n=sqrt_n, n_layers=5)
    # 2. Spawn N workers.
    print(f"spawning {n_trainers} workers…", flush=True)
    handles = []
    for i in range(n_trainers):
        h = train_with_bank_worker.spawn(
            trainer_id=i,
            total_steps=total_steps,
            eval_every=eval_every,
            ckpt_every=ckpt_every,
            lr=lr,
            lr_dense_mult=lr_dense_mult,
            lr_bank_mult=lr_bank_mult,
            batch=batch,
            sqrt_n=sqrt_n,
            bank=bank,
            base=base,
            sync_every=sync_every,
            volume_name=volume_name,
            bank_query_mode=bank_query_mode,
            long_tier_mix=long_tier_mix,
        )
        handles.append((i, h))
        print(f"  worker {i} spawned: {h.object_id}", flush=True)
    # 3. Join — each worker exits independently when its ckpt+ablation done.
    print(f"waiting for {n_trainers} workers to finish…", flush=True)
    for i, h in handles:
        try:
            h.get()
            print(f"  ✓ worker {i} done", flush=True)
        except Exception as e:
            print(f"  ✗ worker {i} failed: {e}", flush=True)
    print("all workers complete.", flush=True)


@app.local_entrypoint()
def train_multi_b(bases: str = "/data/text8,/data/pile-github.bin",
                  total_steps: int = 25000,
                  eval_every: int = 1000,
                  ckpt_every: int = 5000,
                  lr: float = 1.4e-3,
                  lr_dense_mult: float = 1.0,
                  lr_bank_mult: float = 1.0,
                  batch: int = 128,
                  sqrt_n: int = 2048,
                  bank: str = "/data/shared-bank-b",
                  sync_every: int = 100,
                  volume_name: str = "mmllm-data",
                  bank_query_mode: str = "plain",
                  long_tier_mix: str = "sum"):
    """Pattern B (multi-task): N workers, EACH on its own corpus, sharing one bank.

    `bases` is a comma-separated list of base paths (one per worker).
    `n_trainers` is derived from `len(bases)`. Each worker keeps its
    own ckpts/logs under `<base>.t<id>.{ckpts,log.jsonl}`; all workers
    share the bank at `<bank>.<i>.bin`.

    Tests "bank as cross-corpus substrate": diverse training
    distributions converge into one shared retrieval surface.

    Smoke example (sqrt_n=512, 500 steps, ~3-5 min wall):
      modal run --detach mmllm/modal_app.py::train_multi_b \\
          --bases /data/text8,/data/pile-github.bin \\
          --total-steps 500 --eval-every 500 --ckpt-every 500 \\
          --sqrt-n 512 --bank /data/shared-bank-smoke-b
    """
    bases_list = [b.strip() for b in bases.split(",") if b.strip()]
    n_trainers = len(bases_list)
    print(f"=== train_multi_b: n_trainers={n_trainers} bases={bases_list} "
          f"sqrt_n={sqrt_n} bank={bank} ===", flush=True)
    # 1. Pre-init shared bank (idempotent on file size).
    print("preparing shared bank…", flush=True)
    prepare_bank.remote(bank_path=bank, sqrt_n=sqrt_n, n_layers=5)
    # 2. Spawn one worker per base.
    print(f"spawning {n_trainers} workers (one per corpus)…", flush=True)
    handles = []
    for i, base_i in enumerate(bases_list):
        h = train_with_bank_worker.spawn(
            trainer_id=i,
            total_steps=total_steps,
            eval_every=eval_every,
            ckpt_every=ckpt_every,
            lr=lr,
            lr_dense_mult=lr_dense_mult,
            lr_bank_mult=lr_bank_mult,
            batch=batch,
            sqrt_n=sqrt_n,
            bank=bank,
            base=base_i,
            sync_every=sync_every,
            volume_name=volume_name,
            bank_query_mode=bank_query_mode,
            long_tier_mix=long_tier_mix,
        )
        handles.append((i, base_i, h))
        print(f"  worker {i} ({base_i}) spawned: {h.object_id}", flush=True)
    # 3. Join — workers exit independently when their ckpt+ablation done.
    print(f"waiting for {n_trainers} workers to finish…", flush=True)
    for i, base_i, h in handles:
        try:
            h.get()
            print(f"  ✓ worker {i} ({base_i}) done", flush=True)
        except Exception as e:
            print(f"  ✗ worker {i} ({base_i}) failed: {e}", flush=True)
    print("all workers complete.", flush=True)


# ─────────────────────── HF dataset prep (Phase 0) ───────────────────────
#
# Stages a HuggingFace dataset onto the volume in mmllm's standard byte-bin
# shape (uint8 stream + train/val/test split). The basilisp side
# (`mmllm prepare-hf-dataset`) does the actual work; this wrapper just
# threads Modal arguments through and commits the volume.


@app.function(
    image=image,
    volumes={"/data": volume},
    secrets=_HF_SECRETS,   # injects HF_TOKEN if 'huggingface-secret' or
                           # 'huggingface-token' Modal Secret exists; gated
                           # datasets (the-stack-v2-*, xlam, ...) need this
    timeout=86400,         # 24 h — large pretraining-style sources stream slow
    cpu=4.0,
    memory=32768,          # 32 GB — formatter buffers + records held in flight
)
def prepare_hf_dataset(
    dataset_key: str,
    out_path:    str       = "",      # default: /data/<key>.bin
    max_bytes:   int       = 5_000_000_000,
    val_bytes:   int       = 50_000_000,
    test_bytes:  int       = 50_000_000,
):
    """Stream a HuggingFace dataset → uint8 byte stream on the volume.

    Output layout (mirrors `prepare_pile_github`):
      <out_path>            flat bytes
      <out_path>.train.bin
      <out_path>.val.bin
      <out_path>.test.bin

    Pass `out_path=""` to default to `/data/<dataset_key>.bin`.
    `dataset_key` selects from `mmllm.datasets.DATASET_REGISTRY` —
    currently:
      commitpackft | xlam | magicoder      (SFT-style, chat-template wrapped)
      cosmopedia | fineweb-edu             (pretraining-style, raw text)
      the-stack-v2-{py,md,sh}              (code subsets)

    SFT-style datasets are tiny (<5 GB at full size) so default cap
    is fine; pretraining-style sources need a much higher cap (e.g.,
    50 GB cosmopedia, 100 GB fineweb-edu sample).
    """
    import subprocess
    final_out = out_path or f"/data/{dataset_key}.bin"
    print(f"=== prepare_hf_dataset key={dataset_key} → {final_out} "
          f"max={max_bytes/1e9:.1f} GB ===", flush=True)
    subprocess.run(
        ["mmllm", "prepare-hf-dataset",
         dataset_key, final_out,
         str(max_bytes), str(val_bytes), str(test_bytes)],
        check=True,
    )
    volume.commit()
    print(f"done — staged on volume: {final_out}", flush=True)


@app.function(
    image=image,
    volumes={"/data": volume},
    timeout=600,
    cpu=1.0,
    memory=2048,
)
def inspect_dataset_remote(path: str, n_chars: int = 4000):
    """Print first n_chars bytes of a prepared `.bin` from the volume.
    Useful smoke check after a prepare_hf_dataset run before launching
    a multi-day training job on a malformed corpus."""
    import subprocess
    subprocess.run(["mmllm", "inspect-dataset", path, str(n_chars)],
                   check=True)


# ─────────────────────── prepare-for-prod (parallel staging) ───────────────────────
#
# One-shot orchestrator that spawns parallel HF prep jobs for every
# public dataset in DATASET_REGISTRY at production caps. Each prep
# runs in its own Modal container; this function blocks until they
# all return and then sets up the base.{train,val,test}.bin symlinks
# train-long expects.
#
# Cost: ~$1-3 of CPU container time across ~11 parallel preps + the
# orchestrator's wait time (~$0.01).  Runtime: 30-90 min wall clock
# (longest leg = open-web-math / fineweb-edu streaming at HF
# unauthenticated rate limits).


# Per-dataset (max_bytes, val_bytes, test_bytes) for production.
# val/test are sized per-dataset because some sources are tiny:
#   - theorem-qa is ~232 KB total (just the test split from
#     TIGER-Lab/TheoremQA — no train/val splits exist publicly).
#     val + test must sum to less than that, hence 50K/50K.
#   - algebraic-stack now points at hoskinson-center/proof-pile
#     (parquet-based, no zstd shards). 2 GB cap covers a healthy
#     mix of formal proofs + arXiv math + math.SE.
# Categorization:
#   SFT-style    — small datasets, near-full coverage at these caps
#   Pretraining  — large datasets, 5 GB cap (stream + stop)
#   Specialty    — smaller datasets, full or near-full coverage
#
# Total ~24 GB on volume after all preps complete.
PROD_CAPS = {
    # key                   max_bytes        val_bytes   test_bytes
    "commitpackft-py":   (2_000_000_000,    20_000_000, 20_000_000),
    "commitpackft-md":   (1_000_000_000,    20_000_000, 20_000_000),
    "commitpackft-sh":   (1_000_000_000,    20_000_000, 20_000_000),
    "commitpackft-js":   (1_000_000_000,    20_000_000, 20_000_000),
    "commitpackft-clj":  ( 500_000_000,       500_000,    500_000),  # Clojure: only ~6.5 MB raw on HF
    "magicoder":          ( 500_000_000,    10_000_000, 10_000_000),
    "cosmopedia":         (5_000_000_000,    20_000_000, 20_000_000),
    "fineweb-edu":        (5_000_000_000,    20_000_000, 20_000_000),
    "open-web-math":      (5_000_000_000,    20_000_000, 20_000_000),
    "algebraic-stack":    (2_000_000_000,    20_000_000, 20_000_000),  # via hoskinson-center/proof-pile
    "code-contests":      (1_000_000_000,    20_000_000, 20_000_000),
    "theorem-qa":         ( 100_000_000,        50_000,     50_000),  # ~232 KB total
    # Eval-only — MultiPL-E HumanEval-Clojure (~175 KB / 161 problems).
    # PROD_CAPS includes it just to stage train/val/test files; operator
    # does NOT include in --mix (it's a benchmark). eval_watcher routes
    # it via agent_evals to measure Clojure code-gen ability per ckpt.
    "humaneval-clj":      (    200_000,         50_000,     50_000),  # ~175 KB total
    # Gated (HF token required + per-dataset license click-through).
    # prepare_for_prod attempts them and fails gracefully (per-dataset
    # error capture) if the token is missing or license unaccepted.
    "xlam":               ( 200_000_000,    10_000_000, 10_000_000),  # GATED — Salesforce/xlam-function-calling-60k
    "the-stack-clj":      (2_000_000_000,    20_000_000, 20_000_000),  # GATED — bigcode/the-stack-dedup (v1) clojure
    # Tool-call diversity additions (per docs/router-bank-lr-decoupling
    # follow-up: byte-level format anchor needs more API-schema variety
    # than xLAM alone provides).
    "glaive-funcall":     ( 500_000_000,    20_000_000, 20_000_000),  # ~251MB raw HF → ~500MB after templating
    "hermes-funcall":     ( 200_000_000,     2_000_000,  2_000_000),  # smaller, ~10-100k records — small val/test
    "toolace":            ( 100_000_000,     1_000_000,  1_000_000),  # 11.3k records, ~26k API pool — small splits
    # Format-only warmup: same source as xlam, args masked. Used for
    # short pre-mix saturation phases; no HF redownload, just retemplate.
    "format-anchor":      ( 100_000_000,     1_000_000,  1_000_000),  # SAME src as xlam, ~13MB after value-masking
}


@app.function(
    image=image,
    volumes={"/data": volume},
    timeout=14400,    # 4h cap — orchestrator just waits, longest leg is HF stream
    cpu=1.0,
    memory=2048,
)
def prepare_for_prod(
    out_dir:         str  = "/data/agent-corpus-v2",
    base_for_eval:   str  = "/data/agent-corpus-v2.bin",
    primary:         str  = "fineweb-edu",   # source for base.{train,val,test}.bin symlinks
    skip_existing:   bool = True,
):
    """Spawn parallel HF prep for every entry in PROD_CAPS, wait for all,
    then set up the symlinks train-long needs.

    Output layout per dataset:
      <out_dir>/<key>.bin
      <out_dir>/<key>.bin.train.bin
      <out_dir>/<key>.bin.val.bin
      <out_dir>/<key>.bin.test.bin

    Symlinks set up after preps complete:
      <base_for_eval>.train.bin → <out_dir>/<primary>.bin.train.bin
      <base_for_eval>.val.bin   → <out_dir>/<primary>.bin.val.bin
      <base_for_eval>.test.bin  → <out_dir>/<primary>.bin.test.bin

    train-long uses base.val.bin to drive in-training eval-bpc; the
    train.bin symlink is a no-op when MMLLM_MIX is set (which it will
    be for prod) but still needs to exist for the no-mix code path's
    initial open() call.

    `primary` picks which dataset's val/test become the in-training
    eval-bpc set. Default fineweb-edu — generic web text, decent
    proxy for "is the model still general?" Can be changed later by
    re-running this function with a different `primary`.

    Per-dataset failures are reported in the summary; the orchestrator
    doesn't block training launch, but the operator should `inspect_dataset_remote`
    any that come back empty before kicking off a real session.

    Idempotent if skip_existing=True (default): existing .train.bin
    files trigger a skip. Useful when re-running after a partial
    failure or after adding new dataset keys to PROD_CAPS.
    """
    import os
    import time
    from pathlib import Path

    Path(out_dir).mkdir(parents=True, exist_ok=True)
    print(f"=== prepare_for_prod: out_dir={out_dir} primary={primary} ===",
          flush=True)
    print(f"  caps: " + ", ".join(f"{k}={v[0]/1e9:.1f}GB"
                                   for k, v in PROD_CAPS.items()),
          flush=True)

    handles = []
    skipped = []
    for key, (max_bytes, val_bytes, test_bytes) in PROD_CAPS.items():
        out_path = f"{out_dir}/{key}.bin"
        train_p = Path(f"{out_path}.train.bin")
        if skip_existing and train_p.exists() and train_p.stat().st_size > 0:
            sz = sum(Path(f"{out_path}.{s}.bin").stat().st_size
                     for s in ("train", "val", "test")
                     if Path(f"{out_path}.{s}.bin").exists())
            print(f"  = [{key}] cached on volume ({sz/1e9:.2f} GB) — skipping",
                  flush=True)
            skipped.append(key)
            continue
        h = prepare_hf_dataset.spawn(
            dataset_key=key,
            out_path=out_path,
            max_bytes=max_bytes,
            val_bytes=val_bytes,
            test_bytes=test_bytes,
        )
        handles.append((key, h, max_bytes))
        print(f"  → [{key}] spawned (max={max_bytes/1e9:.1f} GB, "
              f"val+test={(val_bytes + test_bytes)/1e6:.1f} MB)",
              flush=True)

    if handles:
        print(f"\nwaiting for {len(handles)} parallel preps to finish "
              f"({len(skipped)} cached) ...\n", flush=True)
    successes = list(skipped)
    failures  = []
    t0 = time.time()
    for key, h, cap in handles:
        try:
            h.get()
            successes.append(key)
            print(f"  ✓ [{key}]  ({(time.time() - t0)/60:.1f} min into wait)",
                  flush=True)
        except Exception as e:
            failures.append((key, f"{type(e).__name__}: {e}"))
            print(f"  ✗ [{key}]: {type(e).__name__}: {e}", flush=True)

    # Pull the spawned containers' volume writes back into our orchestrator's
    # view. Without this, `target.exists()` below returns False even for
    # files that ARE on the volume — same eventual-consistency lesson as
    # the smoke pipeline (see commit a4332ed).
    volume.reload()

    # Set up base.{train,val,test}.bin symlinks for train-long.
    if primary in successes:
        primary_path = f"{out_dir}/{primary}.bin"
        for split in ("train", "val", "test"):
            link   = Path(f"{base_for_eval}.{split}.bin")
            target = Path(f"{primary_path}.{split}.bin")
            if not target.exists():
                print(f"  ! cannot symlink {link} — target missing: {target}",
                      flush=True)
                continue
            if link.exists() or link.is_symlink():
                link.unlink()
            link.symlink_to(target)
            print(f"  → symlinked {link} → {target}", flush=True)
    else:
        print(f"  ! primary={primary} did not prep successfully — "
              f"can't set up symlinks. Fix the failure and re-run, or pass "
              f"--primary <other-key>.",
              flush=True)

    volume.commit()
    print(f"\n=== prep summary ===", flush=True)
    print(f"  ok ({len(successes)}): {successes}", flush=True)
    if failures:
        print(f"  failed ({len(failures)}):", flush=True)
        for k, e in failures:
            print(f"    [{k}] {e}", flush=True)
    print(f"  base for training: {base_for_eval}", flush=True)
    print(f"  total wall time: {(time.time() - t0)/60:.1f} min", flush=True)
    return {
        "ok":     successes,
        "failed": failures,
        "base":   base_for_eval,
        "out_dir": out_dir,
    }


# ─────────────────────── Clojure-specific corpora ───────────────────────
#
# Two non-HF prep paths for Clojure substrate beyond commitpackft-clj:
#
#   prepare_coal_mine
#     mfikes/coal-mine — 4Clojure submissions from top-1000 users.
#     368k LOC, 50k tests, 195k assertions, MANY user-submitted
#     solutions per problem. The polynomial-hierarchy "many-ways-to-
#     solve" signal in dense Clojure form. EPL-1.0.
#
#   prepare_clojars_permissive
#     Clojars feed walk → license filter → source-jar extract.
#     Multi-GB of permissively-licensed real-world Clojure libraries.
#     The bulk Clojure substrate.
#
# Both write to /data/agent-corpus-v2/<name>.bin in the standard
# byte-stream + train/val/test split shape, so train-long's mix
# sampler can include them like any other corpus.


@app.function(
    image=image,
    volumes={"/data": volume},
    timeout=3600,         # 1 h cap — git clone + file walk is fast
    cpu=2.0,
    memory=4096,
)
def prepare_coal_mine(
    out_path:    str = "/data/agent-corpus-v2/coal-mine.bin",
    val_bytes:   int = 5_000_000,
    test_bytes:  int = 5_000_000,
):
    """Clone mfikes/coal-mine, walk src/coal_mine/problem_*.cljc, concat
    each into a flat byte stream.

    Each problem file is a Clojure namespace containing many
    `(defcheck solution-XXXX (fn [...] ...))` blocks — multiple user-
    submitted solutions to the same 4Clojure problem. Emitting them
    as raw bytes (with a `;;; problem N` header per file) preserves
    the multi-solution-per-problem signal without needing chat-template
    wrapping; the model sees consecutive blocks of "different solutions
    to the same implicit problem" — the polynomial-hierarchy
    softness/hardness boundary in Clojure form.

    Output: ~100 MB raw, split per the val_bytes / test_bytes args.
    """
    import glob
    import os
    import subprocess
    from pathlib import Path
    from mmllm.corpus import split_pile_github

    repo_dir = "/tmp/coal-mine"
    if not os.path.isdir(repo_dir):
        print(f"  cloning mfikes/coal-mine → {repo_dir}", flush=True)
        subprocess.run(
            ["git", "clone", "--depth", "1",
             "https://github.com/mfikes/coal-mine.git", repo_dir],
            check=True, capture_output=True,
        )

    problems = sorted(glob.glob(f"{repo_dir}/src/coal_mine/problem_*.cljc"))
    print(f"  found {len(problems)} problem files", flush=True)

    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    written = 0
    n_files = 0
    with open(out_path, "wb") as fout:
        for path in problems:
            with open(path, "rb") as src:
                content = src.read()
            num = (os.path.basename(path)
                   .replace("problem_", "").replace(".cljc", ""))
            header = f";;; coal-mine: problem {num}\n".encode("utf-8")
            fout.write(header)
            fout.write(content)
            fout.write(b"\n\n")
            written += len(header) + len(content) + 2
            n_files += 1
            if n_files % 25 == 0:
                print(f"    {n_files} problems  {written/1e6:.1f} MB written",
                      flush=True)

    print(f"  done: {n_files} problems / {written/1e6:.1f} MB total",
          flush=True)

    print(f"  splitting into train/val/test (val={val_bytes/1e6:.1f} MB, "
          f"test={test_bytes/1e6:.1f} MB)", flush=True)
    split_pile_github(out_path, val_bytes, test_bytes)
    volume.commit()
    return {"path": out_path, "bytes": written, "n_problems": n_files}


# Permissive licenses we accept from Clojars. Match is substring on the
# lowercased POM <license><name>...</name> field, so e.g. "Eclipse Public
# License - v 1.0" matches "eclipse public license".
_PERMISSIVE_LICENSE_PATTERNS = (
    "eclipse public license",
    "epl-1.0", "epl-2.0", "epl 1.0", "epl 2.0", "epl",
    "mit license", "the mit license", "mit",
    "bsd-2-clause", "bsd-3-clause", "bsd 2-clause", "bsd 3-clause",
    "bsd",
    "apache license, version 2",
    "apache license 2", "apache 2.0", "apache-2.0",
    "isc license", "isc",
    "creative commons",  # CC0 / CC-BY are arguably permissive enough
    "cc0", "unlicense", "wtfpl",
)


@app.function(
    image=image,
    volumes={"/data": volume},
    timeout=3600,         # generation is CPU-bound, ~10k rec/s; 200k = ~20 s
    cpu=4.0,
    memory=8192,
)
def prepare_aesop_capstone(
    out_path:    str = "/data/agent-corpus-v3/aesop-capstone.bin",
    n_records:   int = 200_000,
    seed:        int = 0,
    val_bytes:   int = 5_000_000,
    test_bytes:  int = 5_000_000,
):
    """Generate the aesop-capstone synthetic corpus on the volume.

    Calls into mmllm.aesop.generate.generate_corpus, which procedurally
    builds (story → Clojure code → tool-call) triples across 10 fables
    × 31 chapter variants. Every record's math is verified by evaluating
    the underlying Expr tree — no hallucinated arithmetic in the corpus.

    Output layout matches all other prepared corpora:
      <out_path>            flat byte stream
      <out_path>.train.bin
      <out_path>.val.bin
      <out_path>.test.bin

    Throughput: ~10k records/s on CPU. 200k records ≈ 130-150 MB total
    + ~20s wall.
    """
    from pathlib import Path
    from mmllm.aesop.generate import generate_corpus

    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    print(f"  prepare_aesop_capstone → {out_path}  "
          f"(n={n_records}, seed={seed})", flush=True)
    stats = generate_corpus(
        out_path=out_path,
        n_records=n_records,
        seed=seed,
        val_bytes=val_bytes,
        test_bytes=test_bytes,
        do_split=True,
        verbose=True,
    )
    volume.commit()
    print(f"  committed: {stats['n_records']} records / "
          f"{stats['bytes']/1e6:.1f} MB", flush=True)
    return stats


@app.function(
    image=image,
    volumes={"/data": volume},
    timeout=14400,        # 4 h cap — fetch jars from Clojars
    cpu=4.0,
    memory=8192,
)
def prepare_clojars_permissive(
    out_path:       str = "/data/agent-corpus-v2/clojars-permissive.bin",
    max_bytes:      int = 2_000_000_000,
    val_bytes:      int = 20_000_000,
    test_bytes:     int = 20_000_000,
    max_artifacts:  int = 5000,
    max_file_bytes: int = 65536,    # skip giant generated files
):
    """Walk Clojars' feed.clj.gz, filter to permissively-licensed
    artifacts, download source/main jars, extract .clj/.cljs/.cljc/.edn,
    concat into a byte stream.

    Yields multi-GB of permissively-licensed real-world Clojure source
    — the bulk Clojure substrate that complements coal-mine's curated
    problem-solving and commitpackft's file-edit signal.

    Filter chain per artifact:
      1. Latest version only (skip historical versions)
      2. POM <license><name>...</name> matches a permissive pattern
      3. Source jar exists (fallback: main jar)
      4. Each extracted file ≤ max_file_bytes (skips auto-generated bloat)

    Cost: ~$0.20-0.50 of CPU container time depending on cap settings.
    Wall time: minutes-to-hour depending on Clojars CDN throughput.
    """
    import gzip
    import io
    import os
    import re
    import time
    import urllib.error
    import urllib.request
    import xml.etree.ElementTree as ET
    import zipfile
    from pathlib import Path
    from mmllm.corpus import split_pile_github

    Path(out_path).parent.mkdir(parents=True, exist_ok=True)

    def _http_get(url: str, timeout: int = 60) -> "bytes | None":
        """GET url; return body or None on any error."""
        try:
            req = urllib.request.Request(
                url, headers={"User-Agent": "mmllm/0.1 clojars-prep"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except (urllib.error.URLError, TimeoutError, ConnectionError):
            return None

    def _is_permissive(license_text: str) -> bool:
        s = (license_text or "").lower().strip()
        return any(pat in s for pat in _PERMISSIVE_LICENSE_PATTERNS)

    def _parse_pom_license(pom_bytes: bytes) -> "str | None":
        try:
            root = ET.fromstring(pom_bytes)
        except ET.ParseError:
            return None
        # POMs use the Maven 4.0.0 namespace. We look for any <license>
        # element regardless of namespace.
        for el in root.iter():
            tag = el.tag.split("}", 1)[-1] if "}" in el.tag else el.tag
            if tag != "license":
                continue
            for child in el.iter():
                ctag = (child.tag.split("}", 1)[-1]
                        if "}" in child.tag else child.tag)
                if ctag == "name" and child.text:
                    return child.text
        return None

    print(f"  fetching Clojars feed.clj.gz ...", flush=True)
    feed_compressed = _http_get(
        "https://clojars.org/repo/feed.clj.gz", timeout=120)
    if feed_compressed is None:
        raise RuntimeError("failed to fetch Clojars feed.clj.gz")
    feed_text = gzip.decompress(feed_compressed).decode("utf-8",
                                                          errors="replace")

    # Each entry looks like:
    #   {:group-id "g" :artifact-id "a" :description "d" :scm "s" :versions ["v1" "v2"]}
    # The order of keys / presence of optional keys varies; use a tolerant
    # regex that captures group-id + artifact-id + the FIRST quoted version
    # in the :versions vector (taken to mean the latest).
    artifact_re = re.compile(
        r':group-id\s+"([^"]+)".*?'
        r':artifact-id\s+"([^"]+)".*?'
        r':versions\s+\[\s*"([^"]+)"',
        re.DOTALL,
    )
    artifacts = []
    for m in artifact_re.finditer(feed_text):
        group, artifact, latest_version = m.groups()
        artifacts.append((group, artifact, latest_version))
    print(f"  feed parsed: {len(artifacts)} unique artifacts", flush=True)

    written       = 0
    n_processed   = 0
    n_permissive  = 0
    n_files       = 0
    t0 = time.time()
    seen_paths = set()        # dedupe identical (group/artifact, internal-path) pairs

    with open(out_path, "wb") as fout:
        for group, artifact, version in artifacts:
            if written >= max_bytes:
                break
            if n_processed >= max_artifacts:
                break
            n_processed += 1

            group_path = group.replace(".", "/")
            base_url = (f"https://repo.clojars.org/{group_path}/"
                        f"{artifact}/{version}/{artifact}-{version}")
            pom_bytes = _http_get(base_url + ".pom", timeout=30)
            if pom_bytes is None:
                continue
            license_text = _parse_pom_license(pom_bytes)
            if not _is_permissive(license_text or ""):
                continue
            n_permissive += 1

            # Try sources jar first; fall back to main jar.
            jar_bytes = _http_get(base_url + "-sources.jar", timeout=120)
            if jar_bytes is None:
                jar_bytes = _http_get(base_url + ".jar", timeout=120)
            if jar_bytes is None:
                continue

            try:
                zf = zipfile.ZipFile(io.BytesIO(jar_bytes))
            except zipfile.BadZipFile:
                continue

            try:
                for name in zf.namelist():
                    if not name.endswith((".clj", ".cljs", ".cljc", ".edn")):
                        continue
                    info = zf.getinfo(name)
                    if info.file_size > max_file_bytes:
                        continue
                    dedupe_key = (artifact, name)
                    if dedupe_key in seen_paths:
                        continue
                    seen_paths.add(dedupe_key)
                    try:
                        content = zf.read(name)
                    except (KeyError, RuntimeError):
                        continue
                    header = (f";;; clojars: {group}/{artifact}-"
                              f"{version} :: {name}\n").encode("utf-8")
                    fout.write(header)
                    fout.write(content)
                    fout.write(b"\n\n")
                    written += len(header) + len(content) + 2
                    n_files += 1
                    if written >= max_bytes:
                        break
            finally:
                zf.close()

            if n_processed % 100 == 0:
                dt = time.time() - t0
                print(f"    [{n_processed:>4}/{max_artifacts}] "
                      f"permissive={n_permissive} files={n_files} "
                      f"{written/1e6:.1f} MB / {dt:.0f}s "
                      f"(license: {(license_text or 'unknown')[:50]})",
                      flush=True)

    print(f"  done: processed={n_processed} permissive={n_permissive} "
          f"files={n_files} bytes={written/1e6:.1f} MB",
          flush=True)
    if written == 0:
        print(f"  ! no files extracted — Clojars feed parse may have"
              f" failed; check the regex against current feed format",
              flush=True)
        raise RuntimeError("clojars prep wrote 0 bytes")

    print(f"  splitting into train/val/test (val={val_bytes/1e6:.1f} MB, "
          f"test={test_bytes/1e6:.1f} MB)", flush=True)
    split_pile_github(out_path, val_bytes, test_bytes)
    volume.commit()
    return {
        "path":          out_path,
        "bytes":         written,
        "n_processed":   n_processed,
        "n_permissive":  n_permissive,
        "n_files":       n_files,
    }


# ─────────────────────── eval battery (Phase 0) ───────────────────────
#
# Run the full eval battery against a single ckpt step. Combines
# eval-bpc on pretraining-style test splits with eval-agent on
# SFT-style test splits. Writes one JSONL log per (ckpt_step, eval_name).
# `eval_watcher` polls the volume for new step-N dirs and runs this
# automatically as training produces ckpts.


def _run_eval_agent(base, ckpt_step, bank, test_path, name,
                    n_samples, gen_len, log_path):
    """Subprocess wrapper for the basilisp eval-agent CLI verb.
    Threaded via subprocess so a single Python failure in basilisp
    doesn't kill the whole Modal worker — the watcher catches and
    keeps going."""
    import subprocess
    subprocess.run(
        ["mmllm", "eval-agent",
         base, str(ckpt_step) if ckpt_step is not None else "",
         bank, test_path, name,
         str(n_samples), str(gen_len), log_path],
        check=True,
    )


def _do_eval_battery(base, ckpt_step, bank, log_path,
                     sqrt_n, bank_on_gpu, bank_dtype,
                     bpc_evals, agent_evals, n_samples, gen_len,
                     bank_query_mode="plain",
                     bank_feedback_mode="plain",
                     long_tier_mix="sum",
                     focal_gamma=0.0,
                     importance_head=False,
                     carry_enabled=False,
                     carry_n_clocks=4):
    """Body of the eval battery — factored so eval_watcher can call it
    directly (no nested-Modal-function dispatch). Returns the resolved
    ckpt_step (since callers may pass 0 = latest)."""
    import os
    import re
    import subprocess

    log_p = log_path or f"{base}.eval.jsonl"

    # Resolve ckpt_step=0 → latest step-N under <base>.ckpts/
    if ckpt_step <= 0:
        ckpts_dir = f"{base}.ckpts"
        if not os.path.isdir(ckpts_dir):
            print(f"  no ckpts dir at {ckpts_dir} — nothing to eval", flush=True)
            return ckpt_step
        steps = []
        for d in os.listdir(ckpts_dir):
            m = re.match(r"step-(\d+)$", d)
            if m:
                steps.append(int(m.group(1)))
        if not steps:
            print(f"  no step-<N> dirs in {ckpts_dir}", flush=True)
            return ckpt_step
        ckpt_step = max(steps)
        print(f"  resolved ckpt_step=latest → {ckpt_step}", flush=True)

    env = os.environ.copy()
    env["MMLLM_DEVICE"]             = "cuda"
    env["MMLLM_SQRT_N"]             = str(sqrt_n)
    env["MMLLM_BANK_ON_GPU"]        = "true" if bank_on_gpu else "false"
    env["MMLLM_BANK_DTYPE"]         = bank_dtype
    # The training-time architectural knobs MUST match at eval time —
    # ctx-add adds W_ctx per block, feedback adds W_back. If the eval
    # container builds a model with the wrong knobs, the dense ckpt
    # load hits a tensor-shape mismatch (82 trained tensors don't fit
    # into 67 model params, etc).
    env["MMLLM_BANK_QUERY_MODE"]    = bank_query_mode
    env["MMLLM_BANK_FEEDBACK_MODE"] = bank_feedback_mode
    env["MMLLM_LONG_TIER_MIX"]      = long_tier_mix
    # Router-smarts arch knobs MUST match training. If trainer used
    # --carry-enabled and the eval container builds without it, the
    # carry params in the ckpt are silently dropped by tolerant load
    # and the model runs without its multi-timescale residual — eval
    # bpc reads way higher than train val_bpc. Same for --importance-
    # head (loads but is unused if not constructed) and --focal-gamma
    # (eval doesn't use focal at inference, but threading the env var
    # keeps the model definition symmetric).
    env["MMLLM_FOCAL_GAMMA"]        = str(focal_gamma)
    env["MMLLM_IMPORTANCE_HEAD"]    = "true" if importance_head else "false"
    env["MMLLM_CARRY_ENABLED"]      = "true" if carry_enabled else "false"
    env["MMLLM_CARRY_N_CLOCKS"]     = str(carry_n_clocks)
    env["PYTORCH_CUDA_ALLOC_CONF"]  = "expandable_segments:True"

    print(f"=== eval battery base={base} ckpt={ckpt_step} log={log_p} ===",
          flush=True)

    # Filter the spec strings to only entries whose test_path actually
    # exists on volume — `eval-battery-on-ckpt` (basilisp side) doesn't
    # check, so we pre-filter here. Skipped entries get a print line
    # for visibility.
    def _existing(entries_str, label):
        kept = []
        for entry in (entries_str or "").split(","):
            entry = entry.strip()
            if not entry:
                continue
            name, _, test_path = entry.partition(":")
            if not os.path.exists(test_path):
                print(f"  skip {label}[{name}]: missing {test_path}",
                      flush=True)
                continue
            kept.append(entry)
        return ",".join(kept)

    bpc_kept   = _existing(bpc_evals,   "bpc")
    agent_kept = _existing(agent_evals, "agent")

    # ONE basilisp invocation: builds model + loads dense + bank V
    # ONCE, then iterates all eval targets in-process. Replaces the
    # prior pattern of N+M independent subprocess calls (each of which
    # redundantly reloaded the 17.5 GB bank V from disk — ~10-20 min
    # of wasted I/O per ckpt at sqrt_n=2048 fp32).
    try:
        subprocess.run(
            ["mmllm", "eval-battery-on-ckpt",
             base, str(ckpt_step), bank,
             bpc_kept, agent_kept,
             str(n_samples), str(gen_len), log_p],
            env=env,
            check=True,
        )
    except subprocess.CalledProcessError as e:
        # If the whole battery dies, log + continue — the watcher will
        # mark this ckpt as seen anyway and move on.
        print(f"    WARN: eval-battery-on-ckpt at step {ckpt_step} failed: {e}",
              flush=True)

    volume.commit()
    print(f"done — eval battery for ckpt {ckpt_step} → {log_p}", flush=True)
    return ckpt_step


@app.function(
    image=image,
    volumes={"/data": volume},
    timeout=7200,          # 2 h cap per battery run
    gpu="A10G",            # cheap GPU for eval; bigger GPUs reserved for training
    memory=32768,
)
def run_eval_battery(
    base:        str  = "/data/agent-corpus",
    ckpt_step:   int  = 0,                         # 0 = use latest under <base>.ckpts/
    bank:        str  = "/data/agent-bank",
    log_path:    str  = "",                        # default: <base>.eval.jsonl
    sqrt_n:      int  = 2048,
    bank_on_gpu: bool = True,
    bank_dtype:  str  = "fp32",
    # Architectural knobs MUST match what training used — see
    # _do_eval_battery's MMLLM_BANK_QUERY_MODE / MMLLM_BANK_FEEDBACK_MODE
    # comment for why. Defaults match the recommended v2 setup
    # (ctx-add + feedback). Override to 'plain' for v1-style baselines.
    bank_query_mode:    str = "ctx-add",
    bank_feedback_mode: str = "feedback",
    long_tier_mix:      str = "sum",
    bpc_evals:   str  = ("cosmopedia:/data/cosmopedia.test.bin,"
                          "fineweb-edu:/data/fineweb-edu.test.bin,"
                          "the-stack-v2-py:/data/the-stack-v2-py.test.bin"),
    agent_evals: str  = ("commitpackft-py:/data/commitpackft-py.test.bin,"
                          "magicoder:/data/magicoder.test.bin"),
    n_samples:   int  = 50,
    gen_len:     int  = 256,    # default 256 fits max_pos=1024 + max_prompt_bytes=768 with margin
):
    """Run the full eval battery against a single ckpt.

    Skips evals whose test_path doesn't exist (so the battery pays
    off the moment any one corpus is staged). Writes one JSONL row
    per eval to log_path (default `<base>.eval.jsonl`). Same shape
    as train-long's eval events so plots align on the step axis.
    """
    _do_eval_battery(
        base, ckpt_step, bank, log_path,
        sqrt_n, bank_on_gpu, bank_dtype,
        bpc_evals, agent_evals, n_samples, gen_len,
        bank_query_mode=bank_query_mode,
        bank_feedback_mode=bank_feedback_mode,
        long_tier_mix=long_tier_mix,
    )


@app.function(
    image=image,
    volumes={"/data": volume},
    timeout=86400,         # Modal caps at 24 h per invocation; the watcher's
                           # outer loop is idempotent (`<log_path>.seen.txt`)
                           # so just relaunch it daily for multi-day runs.
    gpu="L4",              # 24GB VRAM (fits sqrt_n=2048 fp32 bank at 18.8GB);
                           # cheaper + better available than A10G. Bank fits
                           # on-GPU; with bank_on_gpu=False the watcher would
                           # work on T4/16GB at the cost of PCIe-per-query.
    memory=32768,
)
def eval_watcher(
    base:        str  = "/data/agent-corpus",
    bank:        str  = "/data/agent-bank",
    log_path:    str  = "",
    poll_seconds: int = 300,                       # 5 min between scans
    sqrt_n:      int  = 2048,
    bank_on_gpu: bool = True,
    bank_dtype:  str  = "fp32",
    bank_query_mode:    str = "ctx-add",
    bank_feedback_mode: str = "feedback",
    long_tier_mix:      str = "sum",
    bpc_evals:   str  = ("cosmopedia:/data/cosmopedia.test.bin,"
                          "fineweb-edu:/data/fineweb-edu.test.bin,"
                          "the-stack-v2-py:/data/the-stack-v2-py.test.bin"),
    agent_evals: str  = ("commitpackft-py:/data/commitpackft-py.test.bin,"
                          "magicoder:/data/magicoder.test.bin"),
    n_samples:   int  = 50,
    gen_len:     int  = 256,    # default 256 fits max_pos=1024 + max_prompt_bytes=768 with margin
    max_idle_polls: int = 0,                       # 0 = infinite; else stop after N empty polls
    focal_gamma:    float = 0.0,
    importance_head: bool = False,
    carry_enabled:   bool = False,
    carry_n_clocks:  int  = 4,
):
    """Poll <base>.ckpts/ for new step-<N> dirs and eval each one.

    Idempotent — keeps a `<log_path>.seen.txt` set of already-evaluated
    ckpt_steps so a watcher restart doesn't re-eval everything.

    Run alongside `train_with_bank` to get continuous quality-by-step
    metrics in the same JSONL the training run writes to. The watcher
    runs on cheap A10G (eval workload is small), so the H100 keeps
    burning training tokens uninterrupted.
    """
    import os
    import re
    import time

    log_p   = log_path or f"{base}.eval.jsonl"
    seen_p  = f"{log_p}.seen.txt"
    seen    = set()
    if os.path.exists(seen_p):
        with open(seen_p) as f:
            for line in f:
                line = line.strip()
                if line:
                    seen.add(int(line))
        print(f"  watcher: resumed with {len(seen)} already-evaled steps",
              flush=True)

    ckpts_dir = f"{base}.ckpts"
    idle_count = 0

    print(f"=== eval_watcher base={base} every={poll_seconds}s ===",
          flush=True)

    while True:
        volume.reload()  # pick up new ckpt dirs the trainer wrote
        if not os.path.isdir(ckpts_dir):
            print(f"  watcher: no ckpts dir yet at {ckpts_dir}", flush=True)
            time.sleep(poll_seconds)
            continue

        # Find ckpt steps not yet evaluated.
        steps = []
        for d in os.listdir(ckpts_dir):
            m = re.match(r"step-(\d+)$", d)
            if m:
                s = int(m.group(1))
                if s not in seen:
                    steps.append(s)
        steps.sort()

        if not steps:
            idle_count += 1
            if max_idle_polls and idle_count >= max_idle_polls:
                print(f"  watcher: {max_idle_polls} idle polls — exiting",
                      flush=True)
                return
            time.sleep(poll_seconds)
            continue

        idle_count = 0
        for s in steps:
            print(f"  watcher: → eval ckpt step {s}", flush=True)
            try:
                _do_eval_battery(
                    base, s, bank, log_p,
                    sqrt_n, bank_on_gpu, bank_dtype,
                    bpc_evals, agent_evals, n_samples, gen_len,
                    bank_query_mode=bank_query_mode,
                    bank_feedback_mode=bank_feedback_mode,
                    long_tier_mix=long_tier_mix,
                    focal_gamma=focal_gamma,
                    importance_head=importance_head,
                    carry_enabled=carry_enabled,
                    carry_n_clocks=carry_n_clocks,
                )
            except Exception as e:
                print(f"    WARN: ckpt {s} eval errored: {e} — skipping",
                      flush=True)
            # Mark seen either way so we don't infinite-loop on a broken
            # ckpt. The trainer will produce the next one shortly.
            seen.add(s)
            with open(seen_p, "a") as f:
                f.write(f"{s}\n")
            volume.commit()


# ─────────────────────── slow-walk progress report ───────────────────────


@app.function(
    image=image,
    volumes={"/data": volume},
    timeout=120,
    cpu=1.0,
    memory=2048,
)
def progress_report(base: str = "/data/agent-corpus",
                    h100_dollars_per_hour: float = 3.00):
    """Aggregate a run's training_energy + session_end events to show:
       total wall hours, est $ spent, latest step, ckpt history.

    Lightweight — reads <base>.log.jsonl + lists <base>.ckpts/.
    No GPU. Cheap to call between sessions to see "where we are."
    """
    import json
    import os
    import re

    log_path = f"{base}.log.jsonl"
    ckpts_dir = f"{base}.ckpts"

    print(f"=== progress_report base={base} ===", flush=True)

    # Walk the log for training_energy + session_end events.
    total_wall_s = 0.0
    n_sessions   = 0
    last_step    = 0
    last_loss    = None
    last_eval    = None
    if os.path.exists(log_path):
        with open(log_path) as f:
            for line in f:
                try:
                    row = json.loads(line)
                except json.JSONDecodeError:
                    continue
                ev = row.get("event", "")
                if ev == "training_energy":
                    total_wall_s += float(row.get("wall_s", 0))
                    n_sessions   += 1
                elif ev == "session_end":
                    pass  # already captured by training_energy
                elif ev == "eval":
                    last_step = max(last_step, int(row.get("step", 0)))
                    last_eval = row
                elif ev == "ablation_intermediate":
                    last_eval = row
                if "step" in row:
                    last_step = max(last_step, int(row.get("step", 0)))
                if "loss" in row:
                    last_loss = row.get("loss")
    else:
        print(f"  no log at {log_path} — has training started?", flush=True)

    total_h    = total_wall_s / 3600.0
    est_cost   = total_h * h100_dollars_per_hour

    # List ckpts on disk.
    ckpt_steps = []
    if os.path.isdir(ckpts_dir):
        for d in os.listdir(ckpts_dir):
            m = re.match(r"step-(\d+)$", d)
            if m:
                ckpt_steps.append(int(m.group(1)))
    ckpt_steps.sort()

    print(f"  sessions completed:   {n_sessions}", flush=True)
    print(f"  total wall time:      {total_h:.2f} h", flush=True)
    print(f"  est cost (@${h100_dollars_per_hour}/h):  ${est_cost:.2f}", flush=True)
    print(f"  latest training step: {last_step:,}", flush=True)
    if last_loss is not None:
        print(f"  latest training loss: {last_loss:.3f}", flush=True)
    if last_eval:
        bpc = last_eval.get("val_bpc")
        if bpc:
            print(f"  latest val bpc:       {bpc:.4f}", flush=True)
    print(f"  ckpts on volume ({len(ckpt_steps)}):", flush=True)
    for s in ckpt_steps[-10:]:
        print(f"    step-{s}", flush=True)
    if len(ckpt_steps) > 10:
        print(f"    ... ({len(ckpt_steps) - 10} earlier)", flush=True)


# ─────────────────────── Modal-side pipeline smoke ───────────────────────
#
# End-to-end Modal smoke: preps a small slice of every registered
# dataset, optionally trains for ~3 min on H100, optionally runs the
# eval battery, optionally publishes to GitHub Release. Each phase is
# behind an --include-* flag so the operator controls cost.
#
# Cost budget (single H100 ≈ $3/hr, A10G ≈ $1.10/hr, CPU ≈ $0.05/hr):
#
#   default (prep + inspect only):                     ~$0.05-0.15
#   + --include-train (3 min H100):                    + ~$0.15
#   + --include-eval (5 min A10G):                     + ~$0.10
#   + --include-publish (CPU upload to GH Release):    + ~$0.02
#
# Total at "everything enabled": ~$0.30-0.45.
#
# Auth requirements (degrade gracefully if absent):
#   - HF_TOKEN env (Modal Secret 'huggingface-token' if you want the
#     gated bigcode/the-stack-v2-dedup datasets — pass --include-gated).
#     Smoke currently doesn't auto-load it; set up via:
#       modal secret create huggingface-token HF_TOKEN=hf_xxx
#     then add `secrets=[Secret.from_name("huggingface-token")]` to
#     this function's decorator. Without it, gated datasets fail with
#     a clear WARN and the smoke continues with the public ones.
#   - GITHUB_TOKEN — needed only for --include-publish. Set up via the
#     existing 'github-token' Modal Secret (see publish_ckpt_to_github).


@app.function(
    image=publish_image,        # has gh CLI for the optional publish phase
    volumes={"/data": volume},
    secrets=_HF_SECRETS,        # for --include-gated dataset preps; harmless if absent
    timeout=14400,              # 4 h cap (worst case: 8 datasets × HF stream)
    cpu=4.0,
    memory=32768,
)
def smoke_pipeline_modal(
    smoke_base:        str  = "/data/_smoke",
    cap_bytes:         int  = 50_000_000,    # 50 MB per dataset
    val_bytes:         int  = 500_000,
    test_bytes:        int  = 500_000,
    skip_existing:     bool = True,          # idempotent re-runs
    include_gated:     bool = False,         # try bigcode/the-stack-v2-dedup
    include_train:     bool = False,         # spawn ~3-min H100 session (~$0.15)
    include_eval:      bool = False,         # spawn eval battery on A10G (~$0.10)
    include_publish:   bool = False,         # publish ckpt to GH Release (~$0.02)
    publish_tag_prefix: str = "agent-smoke", # keep separate from real run tags
    publish_gh_repo:    str = "johnmn3/mmllm",
    cleanup_after:      bool = False,        # remove /data/_smoke* on success
):
    """End-to-end Modal pipeline smoke against small slices of every
    registered dataset.

    Phases (all gated behind --include-* flags except prep+inspect):

      1. prep + inspect          — for each dataset key in DATASET_REGISTRY
                                    (skips gated ones unless --include-gated)
      2. training (--include-train) — 3-min H100 session over a small mix
                                       of whatever just prepped successfully
      3. eval battery (--include-eval) — bpc + agentic against held-out splits
      4. publish (--include-publish) — int8-quantize bank + upload to a
                                        <tag-prefix>-step-<N> GH Release

    Smoke artifacts land at <smoke_base>/<dataset-key>.bin (+ .train/.val/.test).
    Pass --cleanup-after to remove them on success.

    Per-dataset failures are captured + reported in the final summary
    rather than aborting the whole smoke (so a single flaky HF dataset
    or a missing Secret doesn't poison the rest).
    """
    import os
    import re
    import shutil
    import time
    import traceback
    from pathlib import Path

    from mmllm.datasets import (DATASET_REGISTRY, inspect_dataset,
                                prepare_hf_dataset)

    # Datasets that require HF auth (license click-through or explicit
    # access grant). Smoke skips these by default; pass --include-gated
    # to attempt them (also requires HF_TOKEN env / Modal Secret).
    #   - bigcode/the-stack-v2-dedup: license + auth
    #   - Salesforce/xlam-function-calling-60k: gated (Salesforce-style
    #     "click to accept terms" gate; needs HF auth even for public
    #     read)
    GATED = {"the-stack-v2-py", "the-stack-v2-md", "the-stack-v2-sh",
             "the-stack-clj", "xlam"}

    Path(smoke_base).mkdir(parents=True, exist_ok=True)

    keys = sorted(DATASET_REGISTRY.keys())
    if not include_gated:
        keys = [k for k in keys if k not in GATED]

    # ── phase 1: prep + inspect ──
    print(f"=== smoke phase 1: prep + inspect {len(keys)} datasets ===",
          flush=True)
    print(f"  cap={cap_bytes/1e6:.0f} MB per dataset, base={smoke_base}",
          flush=True)
    if not include_gated:
        print(f"  (skipping gated: {sorted(GATED)} — pass --include-gated + "
              f"set up huggingface-token Secret to enable)",
              flush=True)
    successes_sft  = []
    successes_ptr  = []   # pretraining-style
    failures       = []
    for key in keys:
        spec = DATASET_REGISTRY[key]
        out_path = f"{smoke_base}/{key}.bin"
        train_p = Path(f"{out_path}.train.bin")

        if skip_existing and train_p.exists() and train_p.stat().st_size > 0:
            sz = sum(Path(f"{out_path}.{s}.bin").stat().st_size
                     for s in ("train", "val", "test")
                     if Path(f"{out_path}.{s}.bin").exists())
            print(f"  ✓ [{key}] cached on volume ({sz/1e6:.1f} MB total) — skipping",
                  flush=True)
            (successes_sft if spec["kind"] == "sft" else successes_ptr).append(key)
            continue

        print(f"  → [{key}] preparing ({spec['hf_name']}, "
              f"{'sft' if spec['kind'] == 'sft' else 'pretrain'})",
              flush=True)
        try:
            t0 = time.time()
            stats = prepare_hf_dataset(
                key, out_path,
                max_bytes=cap_bytes,
                val_bytes=val_bytes, test_bytes=test_bytes,
            )
            head = inspect_dataset(out_path, 400)
            dt = time.time() - t0
            print(f"  ✓ [{key}] {stats['n_records']} records / "
                  f"{stats['bytes']/1e6:.1f} MB in {dt:.1f}s",
                  flush=True)
            head_oneline = head[:200].replace("\n", " ⏎ ")
            print(f"    head: {head_oneline}…", flush=True)
            (successes_sft if spec["kind"] == "sft" else successes_ptr).append(key)
        except Exception as e:
            print(f"  ✗ [{key}] failed: {type(e).__name__}: {e}", flush=True)
            failures.append((key, f"{type(e).__name__}: {e}"))
    volume.commit()
    successes = successes_sft + successes_ptr
    print(f"  → phase 1 done: {len(successes)} ok, {len(failures)} failed",
          flush=True)

    train_step = None
    train_base = f"{smoke_base}/_train"
    train_bank = f"{smoke_base}/_bank"

    # ── phase 2: training (optional) ──
    if include_train:
        print(f"\n=== smoke phase 2: ~3-min training session ===", flush=True)
        if not successes:
            print(f"  no datasets prepared — skipping training", flush=True)
        else:
            mix_parts = [f"{smoke_base}/{k}.bin.train.bin:1" for k in successes]
            mix = ",".join(mix_parts)

            # train-long needs <base>.{train,val,test}.bin to exist. Symlink
            # them to the first successful prep so val drives eval-bpc; the
            # train link is unused when MMLLM_MIX is set but train-long still
            # opens it on the no-mix path before checking the env var.
            first = successes[0]
            for split in ("train", "val", "test"):
                link = Path(f"{train_base}.{split}.bin")
                target = Path(f"{smoke_base}/{first}.bin.{split}.bin")
                if link.exists() or link.is_symlink():
                    link.unlink()
                link.symlink_to(target.resolve())
            # Modal Volumes are eventually consistent across containers —
            # train_with_bank.remote() spawns a new container that mounts
            # the same volume, so we have to commit() the symlinks here
            # or the new container will hit FileNotFoundError on
            # <train_base>.val.bin.
            volume.commit()

            print(f"  mix: {len(successes)} corpora "
                  f"(uniform 1/{len(successes)} weight each)", flush=True)
            print(f"  H100 cap: 3 min (max_hours=0.05) → ~$0.15", flush=True)
            try:
                train_with_bank.remote(
                    base=train_base, bank=train_bank,
                    total_steps=100000,        # well above what we'd hit in 3 min
                    eval_every=200,
                    ckpt_every=100,
                    max_hours=0.05,            # ~3 min cap
                    batch=4,
                    sqrt_n=64,                 # tiny bank for fast iter
                    lr=1e-3,
                    bank_query_mode="ctx-add",
                    bank_feedback_mode="feedback",
                    ablate_every=0,            # skip ablation in smoke
                    mix=mix,
                    publish_after=False,       # phase 4 below handles publish
                )
                # Pull in any volume writes the training container made
                # (ckpts, log, bank-latest). Without this, listdir() on
                # ckpts_dir returns the smoke container's stale view —
                # we'd see no step-<N> dirs even though the training
                # container wrote several.
                volume.reload()
                ckpts_dir = Path(f"{train_base}.ckpts")
                if ckpts_dir.is_dir():
                    steps = [int(m.group(1))
                             for m in (re.match(r"step-(\d+)$", d.name)
                                       for d in ckpts_dir.iterdir())
                             if m]
                    if steps:
                        train_step = max(steps)
                        print(f"  ✓ training: latest ckpt at step-{train_step}",
                              flush=True)
                if train_step is None:
                    print(f"  ✗ training completed but no ckpt found at "
                          f"{ckpts_dir} — session may have aborted before "
                          f"first ckpt-every boundary",
                          flush=True)
            except Exception as e:
                print(f"  ✗ training failed: {type(e).__name__}: {e}", flush=True)
                traceback.print_exc()

    # ── phase 3: eval battery (optional) ──
    if include_eval:
        print(f"\n=== smoke phase 3: eval battery ===", flush=True)
        if train_step is None:
            print(f"  no ckpt available — skipping eval battery (need "
                  f"--include-train to produce one)",
                  flush=True)
        else:
            agent_evals = ",".join(
                f"{k}:{smoke_base}/{k}.bin.test.bin" for k in successes_sft)
            bpc_evals = ",".join(
                f"{k}:{smoke_base}/{k}.bin.test.bin" for k in successes_ptr)
            print(f"  bpc evals: {len(successes_ptr)}  agent evals: "
                  f"{len(successes_sft)}",
                  flush=True)
            try:
                run_eval_battery.remote(
                    base=train_base,
                    ckpt_step=train_step,
                    bank=train_bank,
                    log_path=f"{train_base}.eval.jsonl",
                    sqrt_n=64,
                    bank_on_gpu=True,
                    # Mirror the architectural knobs the smoke training
                    # used (see phase-2 train_with_bank.remote call) — the
                    # eval container must build a model with matching
                    # shape or dense ckpt load fails.
                    bank_query_mode="ctx-add",
                    bank_feedback_mode="feedback",
                    bpc_evals=bpc_evals,
                    agent_evals=agent_evals,
                    n_samples=3,
                    gen_len=128,
                )
                print(f"  ✓ eval battery completed", flush=True)
            except Exception as e:
                print(f"  ✗ eval failed: {type(e).__name__}: {e}", flush=True)

    # ── phase 4: publish (optional) ──
    if include_publish:
        print(f"\n=== smoke phase 4: publish ckpt to GH Release ===", flush=True)
        if train_step is None:
            print(f"  no ckpt available — skipping publish "
                  f"(need --include-train)",
                  flush=True)
        else:
            try:
                publish_result = publish_ckpt_to_github.remote(
                    base=train_base, ckpt_step=0,
                    gh_repo=publish_gh_repo,
                    tag_prefix=publish_tag_prefix,
                    n_layers=5, q_dim=224,
                    update_latest=True,
                    notes=f"Smoke run ({publish_tag_prefix}). DELETE after validation.",
                )
                print(f"  ✓ published: {publish_result.get('release_url')}",
                      flush=True)
            except Exception as e:
                print(f"  ✗ publish failed: {type(e).__name__}: {e}\n"
                      f"    (most likely cause: 'github-token' Modal Secret "
                      f"missing or PAT lacks repo:write scope)",
                      flush=True)

    # ── cleanup ──
    if cleanup_after:
        print(f"\n=== cleanup: removing {smoke_base}* ===", flush=True)
        try:
            for p in Path("/data").glob("_smoke*"):
                if p.is_dir():
                    shutil.rmtree(p)
                else:
                    p.unlink()
            volume.commit()
            print(f"  ✓ cleaned", flush=True)
        except Exception as e:
            print(f"  ✗ cleanup failed: {e}", flush=True)

    # ── summary ──
    print(f"\n=== smoke summary ===", flush=True)
    print(f"  prep ok ({len(successes)}): {successes}", flush=True)
    if failures:
        print(f"  prep failed ({len(failures)}):", flush=True)
        for k, e in failures:
            print(f"    [{k}] {e}", flush=True)
    if include_train:
        print(f"  training: {'step ' + str(train_step) if train_step else 'no ckpt'}",
              flush=True)
    print(f"  artifacts: {smoke_base}/<key>.bin (+ .train/.val/.test) "
          f"{'(cleaned)' if cleanup_after else '(retained — pass --cleanup-after to clear)'}",
          flush=True)

    return {
        "prep_ok":     successes,
        "prep_fail":   failures,
        "train_step":  train_step,
        "smoke_base":  smoke_base,
    }


@app.local_entrypoint()
def main(
    steps: int = 100000,
    eval_every: int = 1000,
    ckpt_every: int = 5000,
):
    """Prepare data then start training. Use --detach for true long runs."""
    print("preparing data on Modal volume…", flush=True)
    prepare_data.remote()
    print(f"starting training (steps={steps})…", flush=True)
    train_with_bank.remote(
        total_steps=steps,
        eval_every=eval_every,
        ckpt_every=ckpt_every,
    )
    print("submitted.", flush=True)
