# harvest-1way-r1007 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1007 ctrl_bpc |
|--------|--------|--------------:|
| fA1Hv | fork-SeniorCareMarket-mmllm-claude-train-sym24-c294e21c-fA1Hv | 2.5946 |
| **mean** | | **2.5946** |
| **best** | | **2.5946** |

## Chain progression R1006 → R1007

Previous harvest: `workers/dispatcher/harvest-6way-r1006_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7171         | 2.5946         | -0.1225 |
| ctrl_bpc best  | 2.5450         | 2.5946         | +0.0496 |

## Per-round trajectory (best bird: fA1Hv)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1007 | 3591 | 2.5946 | +0.1468 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1006_sym24`

## Output

`workers/dispatcher/harvest-1way-r1007_sym24/round-1007/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

