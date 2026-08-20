# harvest-3way-r1261 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1261 ctrl_bpc |
|--------|--------|--------------:|
| rWMGo | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-fbfdc24b-rWMGo | 2.2571 |
| 0A7Af | fork-joly-os-mmllm-claude-train-sym24-758d53c3-0A7Af | 2.2602 |
| KHzIa | fork-SeniorCareMarket-mmllm-claude-train-sym24-d27d5820-KHzIa | 2.4343 |
| **mean** | | **2.3172** |
| **best** | | **2.2571** |

## Chain progression R1260 → R1261

Previous harvest: `workers/dispatcher/harvest-9way-r1260_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3645         | 2.3172         | -0.0473 |
| ctrl_bpc best  | 2.2477         | 2.2571         | +0.0094 |

## Per-round trajectory (best bird: rWMGo)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1261 | 3761 | 2.2571 | +0.2364 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1260_sym24`

## Output

`workers/dispatcher/harvest-3way-r1261_sym24/round-1261/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

