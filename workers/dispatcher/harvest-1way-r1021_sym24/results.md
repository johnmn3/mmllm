# harvest-1way-r1021 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1021 ctrl_bpc |
|--------|--------|--------------:|
| lrBsX | fork-slaa-us-mmllm-claude-train-sym24-442a2c62-lrBsX | 2.5518 |
| **mean** | | **2.5518** |
| **best** | | **2.5518** |

## Chain progression R1020 → R1021

Previous harvest: `workers/dispatcher/harvest-10way-r1020_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6261         | 2.5518         | -0.0743 |
| ctrl_bpc best  | 2.5179         | 2.5518         | +0.0339 |

## Per-round trajectory (best bird: lrBsX)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1021 | 4018 | 2.5518 | +0.1788 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-7way-r1020_sym24`

## Output

`workers/dispatcher/harvest-1way-r1021_sym24/round-1021/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

