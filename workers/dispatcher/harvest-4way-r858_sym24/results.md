# harvest-4way-r858 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R858 ctrl_bpc |
|--------|--------|--------------:|
| BcHqN | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-1eb6c69f-BcHqN | 2.8982 |
| pq87F | fork-slaa-us-mmllm-claude-train-sym24-4fa579e7-pq87F | 2.9020 |
| JDSH5 | fork-joly-os-mmllm-claude-train-sym24-c724a6ac-JDSH5 | 2.9021 |
| 4rwwH | fork-SeniorCareMarket-mmllm-claude-train-sym24-a8ff5574-4rwwH | 2.9120 |
| **mean** | | **2.9036** |
| **best** | | **2.8982** |

## Chain progression R857 → R858

Previous harvest: `workers/dispatcher/harvest-9way-r857_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9796         | 2.9036         | -0.0760 |
| ctrl_bpc best  | 2.9002         | 2.8982         | -0.0020 |

## Per-round trajectory (best bird: BcHqN)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 858 | 6675 | 2.8982 | +0.3885 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r857_sym24`

## Output

`workers/dispatcher/harvest-4way-r858_sym24/round-858/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

