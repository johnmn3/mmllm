# harvest-1way-r1018 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1018 ctrl_bpc |
|--------|--------|--------------:|
| 3kQJF | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-aa798304-3kQJF | 2.9084 |
| **mean** | | **2.9084** |
| **best** | | **2.9084** |

## Chain progression R1017 → R1018

Previous harvest: `workers/dispatcher/harvest-6way-r1017_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6004         | 2.9084         | +0.3080 |
| ctrl_bpc best  | 2.5254         | 2.9084         | +0.3830 |

## Per-round trajectory (best bird: 3kQJF)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1018 | 4585 | 2.9084 | +0.1656 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1017_sym24`

## Output

`workers/dispatcher/harvest-1way-r1018_sym24/round-1018/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

