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
        "datasets>=2.14",  # streams Pile-uncopyrighted shards (no auth)
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
                    bank_feedback_mode="plain", ablate_every=0):
    """Shared body. All knobs threaded via env vars (MMLLM_DEVICE,
    MMLLM_LR, MMLLM_BATCH, MMLLM_SQRT_N, MMLLM_CPU_OFFLOAD,
    MMLLM_BANK_ON_GPU, MMLLM_SYNC_EVERY, MMLLM_VOLUME_NAME,
    MMLLM_LR_WARMUP, MMLLM_LR_MIN, MMLLM_BANK_QUERY_MODE,
    MMLLM_LONG_TIER_MIX, MMLLM_BANK_FEEDBACK_MODE) so the basilisp
    CLI stays unchanged.

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
           "MMLLM_BATCH":  str(batch),
           "MMLLM_BANK_ON_GPU": "true" if bank_on_gpu else "false",
           "MMLLM_SYNC_EVERY":  str(sync_every),
           "MMLLM_VOLUME_NAME": volume_name,
           "MMLLM_LR_WARMUP":   str(lr_warmup),
           "MMLLM_BANK_QUERY_MODE":    bank_query_mode,
           "MMLLM_LONG_TIER_MIX":      long_tier_mix,
           "MMLLM_BANK_FEEDBACK_MODE": bank_feedback_mode,
           "MMLLM_ABLATE_EVERY":       str(ablate_every)}
    if sqrt_n is not None:
        env["MMLLM_SQRT_N"] = str(sqrt_n)
    if cpu_offload:
        env["MMLLM_CPU_OFFLOAD"] = "true"
    if lr_min is not None:
        env["MMLLM_LR_MIN"] = str(lr_min)
    print(
        f"=== train-long device={device} B={batch} lr={lr} sqrt_n={sqrt_n} "
        f"cpu_offload={cpu_offload} bank_on_gpu={bank_on_gpu} "
        f"sync_every={sync_every} volume={volume_name} "
        f"lr_warmup={lr_warmup} lr_min={lr_min} "
        f"bank_query_mode={bank_query_mode} long_tier_mix={long_tier_mix} "
        f"bank_feedback_mode={bank_feedback_mode} "
        f"ablate_every={ablate_every} "
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
    batch: int = 128,           # per-token throughput plateau zone; smoother gradients
    sqrt_n: int = 0,            # 0 = config default; pass 2048 for ~18.8 GB bank
    cpu_offload: bool = False,  # CPU-offload SparseAdam state → frees ~38 GB GPU VRAM
    lr_warmup: int = 0,         # 0 = constant lr; >0 enables linear warmup + cosine decay
    lr_min: float = 0.0,        # cosine floor (0 = lr/10 by default; only used when lr_warmup > 0)
    bank_query_mode: str = "plain",      # 'plain' | 'ctx-add' — see mmllm.bank_query
    long_tier_mix: str = "sum",          # 'sum' | 'scalar' | 'switch' — see mmllm.gating
    bank_feedback_mode: str = "plain",   # 'plain' | 'feedback' — see mmllm.bank_feedback
    ablate_every: int = 0,               # >0 = log Δ trajectory every N steps; 0 disables
    base: str = "/data/text8",
    bank: str = "/data/bank",
    corpus_base: str = "",               # if set and != base, symlink corpus splits
                                         # so train-long finds them at <base>.{train,val,test}.bin
                                         # while ckpts/log/etc still write under <base>
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
    )


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
    )


@app.local_entrypoint()
def train_multi(n_trainers: int = 4,
                total_steps: int = 25000,
                eval_every: int = 1000,
                ckpt_every: int = 5000,
                lr: float = 1.4e-3,
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
                     bpc_evals, agent_evals, n_samples, gen_len):
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
    env["MMLLM_DEVICE"]      = "cuda"
    env["MMLLM_SQRT_N"]      = str(sqrt_n)
    env["MMLLM_BANK_ON_GPU"] = "true" if bank_on_gpu else "false"
    env["MMLLM_BANK_DTYPE"]  = bank_dtype

    print(f"=== eval battery base={base} ckpt={ckpt_step} log={log_p} ===",
          flush=True)

    # BPC evals (cheap; generation-free) — basilisp `eval-bpc-on-path`
    # verb is a follow-up; for now this loop logs a skip note so the
    # watcher schema stays stable. Agentic evals run below regardless.
    for entry in bpc_evals.split(","):
        entry = entry.strip()
        if not entry:
            continue
        name, _, test_path = entry.partition(":")
        if not os.path.exists(test_path):
            print(f"  skip bpc[{name}]: missing {test_path}", flush=True)
            continue
        print(f"  → bpc[{name}] @ {test_path}  (eval-bpc-on-path verb TBD)",
              flush=True)

    # Agentic evals (generation + scoring).
    for entry in agent_evals.split(","):
        entry = entry.strip()
        if not entry:
            continue
        name, _, test_path = entry.partition(":")
        if not os.path.exists(test_path):
            print(f"  skip agent[{name}]: missing {test_path}", flush=True)
            continue
        print(f"  → agent[{name}] @ {test_path}", flush=True)
        try:
            subprocess.run(
                ["mmllm", "eval-agent",
                 base, str(ckpt_step), bank,
                 test_path, name,
                 str(n_samples), str(gen_len), log_p],
                env=env,
                check=True,
            )
        except subprocess.CalledProcessError as e:
            # One bad eval shouldn't kill the others.
            print(f"    WARN: agent[{name}] eval failed: {e}", flush=True)

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
    bpc_evals:   str  = ("cosmopedia:/data/cosmopedia.test.bin,"
                          "fineweb-edu:/data/fineweb-edu.test.bin,"
                          "the-stack-v2-py:/data/the-stack-v2-py.test.bin"),
    agent_evals: str  = ("commitpackft:/data/commitpackft.test.bin,"
                          "xlam:/data/xlam.test.bin"),
    n_samples:   int  = 50,
    gen_len:     int  = 512,
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
    )


@app.function(
    image=image,
    volumes={"/data": volume},
    timeout=86400 * 7,     # up to a week; long training runs are 1-2 weeks
    gpu="A10G",
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
    bpc_evals:   str  = ("cosmopedia:/data/cosmopedia.test.bin,"
                          "fineweb-edu:/data/fineweb-edu.test.bin,"
                          "the-stack-v2-py:/data/the-stack-v2-py.test.bin"),
    agent_evals: str  = ("commitpackft:/data/commitpackft.test.bin,"
                          "xlam:/data/xlam.test.bin"),
    n_samples:   int  = 50,
    gen_len:     int  = 512,
    max_idle_polls: int = 0,                       # 0 = infinite; else stop after N empty polls
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
