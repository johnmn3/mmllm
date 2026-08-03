# harvest-1way-r1103 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1103 ctrl_bpc |
|--------|--------|--------------:|
| vQwFk | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-12448e22-vQwFk | 2.7931 |
| **mean** | | **2.7931** |
| **best** | | **2.7931** |

## Chain progression R1102 → R1103

Previous harvest: `workers/dispatcher/harvest-6way-r1102_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5368         | 2.7931         | +0.2563 |
| ctrl_bpc best  | 2.3890         | 2.7931         | +0.4041 |

## Per-round trajectory (best bird: vQwFk)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1103 | 6282 | 2.7931 | +0.2124 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1102_sym24`

## Output

`workers/dispatcher/harvest-1way-r1103_sym24/round-1103/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

