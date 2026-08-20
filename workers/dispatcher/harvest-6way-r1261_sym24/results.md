# harvest-6way-r1261 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1261 ctrl_bpc |
|--------|--------|--------------:|
| P2IAb | fork-SeniorCareMarket-mmllm-claude-train-sym24-bafd5317-P2IAb | 2.2392 |
| rWMGo | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-fbfdc24b-rWMGo | 2.2571 |
| 0A7Af | fork-joly-os-mmllm-claude-train-sym24-758d53c3-0A7Af | 2.2602 |
| KHzIa | fork-SeniorCareMarket-mmllm-claude-train-sym24-d27d5820-KHzIa | 2.4343 |
| Vw0P0 | origin/claude/train-sym24-12385e6a-Vw0P0 | 2.6233 |
| Qz21U | fork-slaa-us-mmllm-claude-train-sym24-d3b49508-Qz21U | 2.6392 |
| **mean** | | **2.4089** |
| **best** | | **2.2392** |

## Chain progression R1260 → R1261

Previous harvest: `workers/dispatcher/harvest-9way-r1260_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3645         | 2.4089         | +0.0444 |
| ctrl_bpc best  | 2.2477         | 2.2392         | -0.0085 |

## Per-round trajectory (best bird: P2IAb)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1261 | 3800 | 2.2392 | +0.2408 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1260_sym24`
  - `workers/dispatcher/harvest-9way-r1260_sym24`

## Output

`workers/dispatcher/harvest-6way-r1261_sym24/round-1261/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

