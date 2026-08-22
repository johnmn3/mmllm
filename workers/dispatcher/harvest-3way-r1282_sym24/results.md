# harvest-3way-r1282 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1282 ctrl_bpc |
|--------|--------|--------------:|
| k8FqI | fork-slaa-us-mmllm-claude-train-sym24-41e179b3-k8FqI | 2.2315 |
| 0mT3P | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-31786fb8-0mT3P | 2.2448 |
| yRsvA | fork-SeniorCareMarket-mmllm-claude-train-sym24-45d3fb60-yRsvA | 2.4166 |
| **mean** | | **2.2976** |
| **best** | | **2.2315** |

## Chain progression R1281 → R1282

Previous harvest: `workers/dispatcher/harvest-6way-r1281_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.2956         | 2.2976         | +0.0020 |
| ctrl_bpc best  | 2.2222         | 2.2315         | +0.0093 |

## Per-round trajectory (best bird: k8FqI)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1282 | 3904 | 2.2315 | +0.2462 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1281_sym24`

## Output

`workers/dispatcher/harvest-3way-r1282_sym24/round-1282/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

