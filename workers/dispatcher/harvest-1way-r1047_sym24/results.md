# harvest-1way-r1047 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1047 ctrl_bpc |
|--------|--------|--------------:|
| KPUEH | fork-SeniorCareMarket-mmllm-claude-train-sym24-55c26339-KPUEH | 2.5172 |
| **mean** | | **2.5172** |
| **best** | | **2.5172** |

## Chain progression R1046 → R1047

Previous harvest: `workers/dispatcher/harvest-2way-r1046_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6960         | 2.5172         | -0.1788 |
| ctrl_bpc best  | 2.5146         | 2.5172         | +0.0026 |

## Per-round trajectory (best bird: KPUEH)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1047 | 3747 | 2.5172 | +0.1938 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1046_sym24`

## Output

`workers/dispatcher/harvest-1way-r1047_sym24/round-1047/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

