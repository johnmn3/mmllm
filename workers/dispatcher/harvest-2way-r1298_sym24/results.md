# harvest-2way-r1298 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1298 ctrl_bpc |
|--------|--------|--------------:|
| ZjyS4 | fork-joly-os-mmllm-claude-train-sym24-b137e624-ZjyS4 | 3.7278 |
| mdHoJ | fork-SeniorCareMarket-mmllm-claude-train-sym24-8e9b9f4b-mdHoJ | 3.8379 |
| **mean** | | **3.7828** |
| **best** | | **3.7278** |

## Chain progression R1297 → R1298

Previous harvest: `workers/dispatcher/harvest-6way-r1297_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.1029         | 3.7828         | -0.3201 |
| ctrl_bpc best  | 3.8331         | 3.7278         | -0.1053 |

## Per-round trajectory (best bird: ZjyS4)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1298 | 5366 | 3.7278 | +0.0458 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1297_sym24`

## Output

`workers/dispatcher/harvest-2way-r1298_sym24/round-1298/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

