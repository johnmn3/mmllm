# harvest-2way-r1126 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1126 ctrl_bpc |
|--------|--------|--------------:|
| jDQ9W | fork-joly-os-mmllm-claude-train-sym24-9c6678a5-jDQ9W | 2.3964 |
| caL6o | origin/claude/train-sym24-b1d3b96f-caL6o | 2.7861 |
| **mean** | | **2.5912** |
| **best** | | **2.3964** |

## Chain progression R1125 → R1126

Previous harvest: `workers/dispatcher/harvest-6way-r1125_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5362         | 2.5912         | +0.0550 |
| ctrl_bpc best  | 2.3826         | 2.3964         | +0.0138 |

## Per-round trajectory (best bird: jDQ9W)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1126 | 4075 | 2.3964 | +0.2291 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1125_sym24`
  - `workers/dispatcher/harvest-3way-r1125_sym24`

## Output

`workers/dispatcher/harvest-2way-r1126_sym24/round-1126/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

