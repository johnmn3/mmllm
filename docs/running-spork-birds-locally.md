# Running spork birds locally (Apple Silicon & beyond)

Train mmllm on **your own machine** and contribute the result back to the shared
chain — exactly like a GitHub-Actions fork bird, just on your hardware (which is
usually far faster than the 7 GB CI runner). A few rounds of local training, then
the script pushes the minimal changeset to your fork and the upstream hourly
**harvest** FedAvg-merges your contribution into the chain.

On Apple Silicon there's an **MLX fast path** (`MMLLM_BACKEND=mlx`) that runs the
whole round on the M-series GPU and is **~13× faster than the default torch-MPS
path** — see [Apple Silicon: the MLX fast path](#apple-silicon-the-mlx-fast-path).

---

## How it works

A "spork bird" is one run of the same pipeline a CI bird uses:

```
scripts/run_local_bird.sh
  └─ scripts/train.sh                    (byte-identical to a fork bird)
       ├─ fetch the current chain head + corpora from upstream Release assets
       ├─ train N rounds × STEPS on your device (extend the chain)
       ├─ encode the round's V_net delta + dense into workers/<handle>/…
       └─ push a  claude/train-sym24-…-<handle>  branch to YOUR fork (origin)
```

Upstream (`johnmn3/mmllm`) runs an hourly harvest that scans forks, FedAvg-merges
new birds into the next `harvest-Nway-r<N>_sym24`, and prunes consumed branches.
Your local bird is **interchangeable with a CI fork bird** — same code path, same
artifacts, same harvest.

---

## One-time setup

1. **Fork** [`github.com/johnmn3/mmllm`](https://github.com/johnmn3/mmllm) and
   clone **your fork**, then `cd` into it:
   ```sh
   git clone git@github.com:<you>/mmllm.git && cd mmllm
   ```
2. **Authenticate the GitHub CLI** (the bird pushes to your fork):
   ```sh
   gh auth login
   ```
3. **Install `uv`** (the Python env auto-bootstraps from it):
   ```sh
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

That's it — no manual venv, corpus download, or checkpoint wrangling. The script
bootstraps the environment and fetches everything it needs from Release assets.

---

## Run it

```sh
bash scripts/run_local_bird.sh [N_ROUNDS]      # default: 5 rounds × 50 steps
```

Examples:
```sh
bash scripts/run_local_bird.sh 10              # 10 rounds (this run's target)
MMLLM_DEVICE=cpu bash scripts/run_local_bird.sh 3   # force CPU, 3 rounds
```

The script auto-detects your device (`mps` on Apple Silicon, else `cuda`, else
`cpu`), bootstraps the venv, preflights `gh`/`origin`, picks a stable per-host
handle, trains, and pushes. When it finishes you'll see a
`claude/train-sym24-…-<handle>` branch on your fork; the next upstream harvest
folds it in.

---

## Apple Silicon: the MLX fast path

The default Apple-Silicon path runs on the GPU via PyTorch-MPS with the bank
resident on-device. There is also an **MLX backend** that runs the entire training
round on the M-series GPU through Apple's MLX framework, which fuses on Metal where
torch-MPS cannot:

```sh
MMLLM_BACKEND=mlx bash scripts/run_local_bird.sh 10
```

- **~13× faster** forward+backward than torch-MPS on the same config (the M-series
  GPU; torch's `torch.compile` is actually *slower* on MPS, so MLX is the real
  accelerator here).
- Produces the **same harvest-compatible artifacts** (`dense.pt` + bank deltas) and
  **consolidates the same way** (V_net carries across rounds; `ctrl_bpc` improves,
  `Δ_net` ≥ 0) — it's a drop-in faster backend, not a different model.
- Falls back to the torch path automatically on any machine without MLX (Linux CI
  birds are unaffected), so the flag is safe to leave set.

Leave `MMLLM_BACKEND` unset to use the proven torch-MPS path.

---

## Useful knobs (all optional)

| env var | default | meaning |
|---|---|---|
| `N_ROUNDS` (positional `$1`) | `5` | rounds this run trains before pushing |
| `MMLLM_STEPS_PER_ROUND` | `50` | training steps per round |
| `MMLLM_DEVICE` | auto | force `mps` / `cuda` / `cpu` |
| `MMLLM_BACKEND` | torch | set `mlx` for the Apple-Silicon fast path |
| `MMLLM_HANDLE` | `L<host-hash>` | your bird's handle in the chain's contributors |
| `MMLLM_CHAIN_PREFIX` | `sym24` | which chain to extend |

The Apple-Silicon path also sets `MMLLM_BANK_ON_GPU=true` and lifts the MPS memory
watermark automatically for full retrieval bandwidth.

---

## What gets pushed, and cleanup

- Each run makes a fresh `claude/train-sym24-…-<handle>` branch on **your fork**
  (never directly on upstream). Upstream's harvest scans forks and merges it.
- The run **self-prunes** consumed bird branches it created, and the lean-repo
  design keeps pushes small (per-round blobs live as Release assets, not in the
  git tree).
- Nothing on upstream's `main` is touched by your run — you contribute via the
  fork + harvest path, exactly like a CI bird.

### Disk hygiene (persistent local clones)

Unlike ephemeral CI runners, a local clone is reused across many bird runs and
its `.git` can bloat. The bird force-pushes its branch every round; left to its
own devices git's **auto-maintenance repacks the whole history into ~16 GB temp
packs**, and any interruption (a killed push, a racing repack) orphans one.
These `tmp_pack_*` files pile up fast — a single bad afternoon orphaned 75 of
them (~659 GB), filling the disk and thrashing swap (symptom: machine lag with
*no* GPU fans, since it's I/O, not compute).

`run_local_bird.sh` now defuses this automatically on every run: it disables
git auto-gc/maintenance in the clone, sweeps orphaned `tmp_pack_*`, **consolidates
accumulated packs with a controlled memory-capped `gc` when they pile up**, and
refuses to start with under 20 GB free; `train.sh` also sweeps on exit. If you
ever see the lag symptom mid-run, the manual fix is:

```bash
rm -f .git/objects/pack/tmp_pack_*     # orphaned temp packs — safe to delete
git config maintenance.auto false      # stop the auto-repack that creates them
git -c pack.windowMemory=256m gc --prune=now   # consolidate accumulated packs
```

**Use a shallow, single-branch clone** for a bird box —
`git clone --depth=1 --single-branch --branch main …`. A bird needs only the
code + the current chain-head manifest (real weights come from Release assets),
not git history or other birds' branches. A fresh shallow clone is ~1 GB of
`.git`; with the controlled `gc` above it stays ~1–2 GB indefinitely. A full
clone needlessly drags a multi-GB history pack around (disabling auto-gc alone
won't shrink it — only a fresh shallow clone or a manual `gc` will).

---

## Verifying it worked

- The run prints per-round `ctrl_bpc` and the ablation `Δ_net` (the consolidation
  signal). A healthy round shows `ctrl_bpc` in range and `Δ_net` ≥ 0.
- After the push, check your fork for the `claude/train-sym24-…` branch, and watch
  the upstream Actions for the next `harvest` run folding it into a new
  `harvest-Nway-r<N>_sym24`.
- Spinning a few of these up over time is exactly how the chain accumulates — any
  Apple-Silicon (or CUDA, or CPU) box can be a first-class bird.
