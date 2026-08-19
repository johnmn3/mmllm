# harvest-11way-r1256 — sparse-delta merge of 11 birds

## Worker endpoints

| handle | branch | R1256 ctrl_bpc |
|--------|--------|--------------:|
| VvhON | fork-slaa-us-mmllm-claude-train-sym24-6c36cf4b-VvhON | 2.2351 |
| xGJW4 | fork-slaa-us-mmllm-claude-train-sym24-4bf7dbc8-xGJW4 | 2.2385 |
| g7SZd | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-666f578c-g7SZd | 2.2508 |
| 8qbMk | fork-joly-os-mmllm-claude-train-sym24-f2929af3-8qbMk | 2.2524 |
| M1qmX | origin/claude/train-sym24-ec9147f5-M1qmX | 2.2540 |
| P29nb | origin/claude/train-sym24-5ce26482-P29nb | 2.2562 |
| fnxF7 | fork-SeniorCareMarket-mmllm-claude-train-sym24-3e4bf227-fnxF7 | 2.2616 |
| 80L3L | origin/claude/train-sym24-f5a5f4b0-80L3L | 2.4308 |
| eRBuB | fork-SeniorCareMarket-mmllm-claude-train-sym24-ace88b56-eRBuB | 2.4339 |
| txpwG | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-4b99d8d3-txpwG | 2.4401 |
| ukOyY | fork-joly-os-mmllm-claude-train-sym24-101e634e-ukOyY | 2.6288 |
| **mean** | | **2.3347** |
| **best** | | **2.2351** |

## Chain progression R1255 → R1256

Previous harvest: `workers/dispatcher/harvest-5way-r1255_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3995         | 2.3347         | -0.0648 |
| ctrl_bpc best  | 2.2357         | 2.2351         | -0.0006 |

## Per-round trajectory (best bird: VvhON)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1256 | 4200 | 2.2351 | +0.2525 |

## Cumulative training contribution

- This harvest: **880 steps** from 11 bird(s)
- Across full ancestry (deduped by bird_id): **1280 steps** from 16 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1255_sym24`
  - `workers/dispatcher/harvest-5way-r1255_sym24`

## Output

`workers/dispatcher/harvest-11way-r1256_sym24/round-1256/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 11 workers)
- `dense.pt` (averaged across 11 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

