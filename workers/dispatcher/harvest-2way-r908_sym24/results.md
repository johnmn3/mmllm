# harvest-2way-r908 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R908 ctrl_bpc |
|--------|--------|--------------:|
| OvUVZ | fork-slaa-us-mmllm-claude-train-sym24-ea707f3c-OvUVZ | 2.7763 |
| a1fhl | origin/claude/train-sym24-e6398891-a1fhl | 2.9747 |
| **mean** | | **2.8755** |
| **best** | | **2.7763** |

## Chain progression R907 → R908

Previous harvest: `workers/dispatcher/harvest-11way-r907_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8609         | 2.8755         | +0.0146 |
| ctrl_bpc best  | 2.7690         | 2.7763         | +0.0073 |

## Per-round trajectory (best bird: OvUVZ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 908 | 6442 | 2.7763 | +0.2535 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-6way-r907_sym24`

## Output

`workers/dispatcher/harvest-2way-r908_sym24/round-908/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

