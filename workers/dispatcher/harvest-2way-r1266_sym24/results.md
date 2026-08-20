# harvest-2way-r1266 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1266 ctrl_bpc |
|--------|--------|--------------:|
| 369I8 | fork-slaa-us-mmllm-claude-train-sym24-bc6dab25-369I8 | 2.2289 |
| V6XOz | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-fffe9cab-V6XOz | 2.4346 |
| **mean** | | **2.3317** |
| **best** | | **2.2289** |

## Chain progression R1265 → R1266

Previous harvest: `workers/dispatcher/harvest-12way-r1265_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4017         | 2.3317         | -0.0699 |
| ctrl_bpc best  | 2.2267         | 2.2289         | +0.0022 |

## Per-round trajectory (best bird: 369I8)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1266 | 4214 | 2.2289 | +0.2478 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r1265_sym24`

## Output

`workers/dispatcher/harvest-2way-r1266_sym24/round-1266/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

