# Contributing compute to mmllm

Train mmllm on your own laptop or workstation (any CPU works, GPU
optional) and have your run merge into a shared community core
checkpoint. No data upload, no central authority — your training
contribution is captured as a small ckpt diff that anyone can verify
and merge.

## Why this works architecturally

mmllm has a triune-brain architecture. The relevant property here is:

- **Local Bank** (cortex) is per-worker, task-specific, never merged.
  Your Local Bank specializes on whatever data you train on.
- **NetBank** (cerebellum, optional) is the shared long-term store.
  Workers contribute mastered patterns; the harvester averages them.
- **Dense trunk** (router) is FedAvg-merged across workers.

So you train on whatever you want, and only your dense-trunk
contribution + your NetBank contributions (if you opt in) merge with
the community. Your personal Local Bank stays yours.

See `docs/triune-brain-architecture.md` for the full mental model.

## Hardware requirements

| Resource | Recommended | Minimum |
|---|---|---|
| RAM | 4 GB | 1 GB |
| Disk | 1 GB | 200 MB |
| CPU | Any modern x86-64 or arm64 (AVX2+ a plus, AMX great) | Any |
| GPU | None required (CUDA optional via `MMLLM_DEVICE=cuda`) | — |
| Time | 30 minutes upward | 10 minutes |

The default CPU config (`default-config-cpu-tiny`) is sized to run on
a 16 GB / 30 GB box with comfortable headroom. Bigger boxes can scale
batch size or use the larger `default-config` if they have GPU.

## Quick start

```bash
git clone https://github.com/johnmn3/mmllm.git
cd mmllm
pip install -e .

# 1. Build the tiny corpus pack (~2 MB, generated locally — no download)
python scripts/build_community_corpus.py /tmp/mmllm-cpu/corpus

# 2. Train ~5000 steps on CPU (~30-60 min on a modern laptop)
mmllm train-cpu /tmp/mmllm-cpu/corpus /tmp/mmllm-cpu/bank 5000 1000 1000

# 3. Your contribution is at /tmp/mmllm-cpu/corpus.ckpts/step-5000/
ls /tmp/mmllm-cpu/corpus.ckpts/
```

`train-cpu` automatically forces `MMLLM_DEVICE=cpu`,
`MMLLM_BANK_ON_GPU=false` (mmap-backed bank V), and a small batch.
Other knobs (focal_gamma, importance_head, carry_enabled, distill_coef,
delim_aux_coef, etc.) are still respected via env var.

**Expected progress on the community corpus:**

| steps | wall (modern CPU) | typical loss | typical val_bpc |
|---|---|---|---|
| 100  | ~30 sec | ~5–8       | ~7   |
| 500  | ~3–5 min | ~4–6       | ~5–7 |
| 5000 | ~30–60 min | ~1–3       | ~1–3 |
| 50000| many hours | <1 (overfit risk on this tiny corpus) | <1 |

Numbers are very rough — depends on CPU. The community corpus is only
~1.5 MB of training data; with B=4 T=128 (~512 tokens/step), 500 steps
sees only ~256k tokens — much less than typical LM training. Don't
expect strong convergence at 500 steps; that's a pipeline-test budget,
not a meaningful training run. Use 5k+ steps for actual contribution.

## Submitting your contribution

The shared community workers directory is at
`https://huggingface.co/datasets/<TBD>/mmllm-workers` (HF Hub allows
free hosting of large blobs). Layout:

```
mmllm-workers/
  <your-handle>/
    step-N/
      dense.pt          ← required: your dense trunk
      bank-net-latest.<i>.bin  ← optional: NetBank V (if you trained with it)
    meta.json           ← {"tokens_trained": N, "steps": N, "label": "..."}
```

Once you've trained, upload **only** `step-N/dense.pt` (~9 MB) plus a
small `meta.json` describing your run. Do **not** upload `opt-*.pt` —
those are per-worker optimizer state, never merged, and would waste
~270 MB of upload bandwidth per contribution.

```bash
# Stage just the upload payload (NOT the whole step-N dir)
mkdir -p /tmp/mmllm-upload/<your-handle>/step-5000
cp /tmp/mmllm-cpu/corpus.ckpts/step-5000/dense.pt \
   /tmp/mmllm-upload/<your-handle>/step-5000/dense.pt
cat > /tmp/mmllm-upload/<your-handle>/meta.json <<EOF
{"tokens_trained": 1280000, "steps": 5000, "label": "<your-handle>"}
EOF

# Upload via HF Hub
pip install huggingface_hub
python -c "
from huggingface_hub import HfApi
api = HfApi()
api.upload_folder(
    folder_path='/tmp/mmllm-upload/<your-handle>',
    path_in_repo='<your-handle>',
    repo_id='<TBD>/mmllm-workers',
    repo_type='dataset',
)
"
```

The `meta.json` should have at least `{"tokens_trained": N, "steps": N,
"label": "<your-handle>"}` so the harvester can weight
your contribution proportionally.

## Running the harvester locally

You don't need permission to run the harvester. Anyone can:

```bash
# Pull the latest community workers directory
huggingface-cli download <TBD>/mmllm-workers --repo-type dataset \
  --local-dir ./workers

# Merge them all into a single core
python -m mmllm.harvester \
  --workers ./workers \
  --output  ./core-merged \
  --weighted-by tokens_trained

# Now ./core-merged/step-N/dense.pt is the merged dense trunk
```

The harvester:
- Loads each worker's `dense.pt`
- Computes a FedAvg weighted average (by `tokens_trained` or
  `steps` from each worker's `meta.json`)
- If any worker carries `bank-net-latest.<i>.bin` files, also
  weighted-averages those (NetBank consolidation)
- Skips Local Bank V (it's personal cortex, never merged)
- Writes the merged result + a `meta.json` listing all sources

If multiple people run the harvester independently with the same set
of workers, they get identical merged results — the merge is
deterministic and order-independent.

## Modal-based harvesting (optional)

The harvester is pure Python with no Modal dependency. It runs on any
CPU box. If you want to run it inside Modal for storage convenience,
wrap `mmllm.harvester.harvest()` in a Modal function:

```python
import modal
from mmllm.harvester import harvest

@modal.function(image=image, volumes={"/data": volume})
def harvest_remote(workers_dir: str, output_dir: str):
    harvest(Path(workers_dir), Path(output_dir),
            weighted_by="tokens_trained")
```

But this is an optimization, not a requirement. Local-only harvesting
works identically.

## How merging is verified

The merged core is just a `list[Tensor]` saved via `torch.save`. Its
integrity is verifiable by anyone:

1. Pull all the source workers
2. Run the harvester yourself
3. `torch.allclose` your output's tensors against any other claim of
   what the merged result should be

This means there's no "trusted authority" — the merge is a function
of the worker contributions, computable by anyone.

## What the merged ckpt is missing

The harvester outputs only `dense.pt` (and optionally
`bank-net-latest.<i>.bin` for NetBank V). Notably absent:

- `opt-dense.pt`, `opt-sparse.pt`: optimizer state. Per worker, never
  merged. When you resume from a merged ckpt, AdamW starts with fresh
  moments. The first ~1k steps will have stronger gradients (no Adam
  smoothing), but training restabilizes quickly.
- `bank-latest.<i>.bin` (Local Bank V): per-worker cortex, never
  merged. When you resume from a merged ckpt, your Local Bank V starts
  at fresh random init. You retrain it on your data.

This is intentional. The triune-brain mapping says Local Bank is
**per-worker** — it specializes to each worker's data and would be
useless to merge naively (averaging different specializations would
destroy them all). The dense trunk + NetBank are the cross-worker
shared substrate.

## Limitations + open questions

- **Topology must match across workers.** All workers must use the
  same `default-config-cpu-tiny` (or whatever the canonical config is
  for the cohort). The harvester checks tensor shapes and refuses to
  merge mismatches.
- **No defense against poisoning.** A worker could submit garbage
  dense.pt and bias the merge. For a research community this is fine;
  for adversarial settings, the harvester would need cryptographic
  signing + reputation weighting (out of scope for v1).
- **Convergence is slow with FedAvg.** Each round of train + merge
  loses some of the local optimization the workers did. Expect
  several rounds to see meaningful improvement.

## Roadmap

- v1 (now): per-worker training + local harvester + dense FedAvg
- v2: cryptographic signing + worker reputation
- v3: distillation pass on a single GPU host that takes K worker ckpts
  and produces a unified core (avoids FedAvg's averaging-loss)
- v4: live "Hivemind"-style bank sync where workers synchronize
  NetBank rows during training rather than only at end-of-run
