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
                    lr_warmup=0, lr_min=None):
    """Shared body. All knobs threaded via env vars (MMLLM_DEVICE,
    MMLLM_LR, MMLLM_BATCH, MMLLM_SQRT_N, MMLLM_CPU_OFFLOAD,
    MMLLM_BANK_ON_GPU, MMLLM_SYNC_EVERY, MMLLM_VOLUME_NAME,
    MMLLM_LR_WARMUP, MMLLM_LR_MIN) so the basilisp CLI stays unchanged.

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
           "MMLLM_LR_WARMUP":   str(lr_warmup)}
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
    base: str = "/data/text8",
    bank: str = "/data/bank",
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
    """
    _run_train_long(
        total_steps, eval_every, ckpt_every, "cuda", lr,
        batch=batch, base=base, bank=bank,
        sqrt_n=(sqrt_n if sqrt_n > 0 else None),
        cpu_offload=cpu_offload,
        lr_warmup=lr_warmup,
        lr_min=(lr_min if lr_min > 0 else None),
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
                volume_name: str = "mmllm-data"):
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
          f"sqrt_n={sqrt_n} bank={bank} base={base} ===", flush=True)
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
                  volume_name: str = "mmllm-data"):
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
