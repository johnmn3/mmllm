# harvest-6way-r1237 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1237 ctrl_bpc |
|--------|--------|--------------:|
| wFoGF | fork-SeniorCareMarket-mmllm-claude-train-sym24-bc31f602-wFoGF | 2.2652 |
| 4sMD5 | fork-joly-os-mmllm-claude-train-sym24-7e1523d9-4sMD5 | 2.2662 |
| L87Hv | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-bc629b14-L87Hv | 2.2672 |
| RRR68 | fork-SeniorCareMarket-mmllm-claude-train-sym24-671bfc54-RRR68 | 2.2690 |
| Ux5CE | fork-slaa-us-mmllm-claude-train-sym24-0d79adbb-Ux5CE | 2.6479 |
| M7Gn2 | fork-slaa-us-mmllm-claude-train-sym24-9ba1666a-M7Gn2 | 2.6644 |
| **mean** | | **2.3967** |
| **best** | | **2.2652** |

## Chain progression R1236 → R1237

Previous harvest: `workers/dispatcher/harvest-6way-r1236_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4293         | 2.3967         | -0.0326 |
| ctrl_bpc best  | 2.2630         | 2.2652         | +0.0022 |

## Per-round trajectory (best bird: wFoGF)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1237 | 4051 | 2.2652 | +0.2413 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1236_sym24`
  - `workers/dispatcher/harvest-6way-r1236_sym24`

## Output

`workers/dispatcher/harvest-6way-r1237_sym24/round-1237/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

