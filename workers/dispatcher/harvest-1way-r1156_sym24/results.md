# harvest-1way-r1156 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1156 ctrl_bpc |
|--------|--------|--------------:|
| S13a1 | fork-joly-os-mmllm-claude-train-sym24-d2846107-S13a1 | 2.3264 |
| **mean** | | **2.3264** |
| **best** | | **2.3264** |

## Chain progression R1155 → R1156

Previous harvest: `workers/dispatcher/harvest-9way-r1155_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4764         | 2.3264         | -0.1500 |
| ctrl_bpc best  | 2.3277         | 2.3264         | -0.0013 |

## Per-round trajectory (best bird: S13a1)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1156 | 3574 | 2.3264 | +0.2583 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1155_sym24`

## Output

`workers/dispatcher/harvest-1way-r1156_sym24/round-1156/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

