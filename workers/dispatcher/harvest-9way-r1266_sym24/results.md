# harvest-9way-r1266 — sparse-delta merge of 9 birds

## Worker endpoints

| handle | branch | R1266 ctrl_bpc |
|--------|--------|--------------:|
| 369I8 | fork-slaa-us-mmllm-claude-train-sym24-bc6dab25-369I8 | 2.2289 |
| iAnwW | origin/claude/train-sym24-4f80f33c-iAnwW | 2.2290 |
| HhPyr | fork-slaa-us-mmllm-claude-train-sym24-fc9bf92b-HhPyr | 2.2458 |
| GjHjz | fork-SeniorCareMarket-mmllm-claude-train-sym24-2e47af0e-GjHjz | 2.2511 |
| zzaSe | fork-SeniorCareMarket-mmllm-claude-train-sym24-63f6e0e1-zzaSe | 2.4293 |
| V6XOz | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-fffe9cab-V6XOz | 2.4346 |
| tttPr | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-92c03304-tttPr | 2.4355 |
| MpYYT | fork-joly-os-mmllm-claude-train-sym24-4b108726-MpYYT | 2.6251 |
| oZXAD | origin/claude/train-sym24-1c33915f-oZXAD | 2.6289 |
| **mean** | | **2.3898** |
| **best** | | **2.2289** |

## Chain progression R1265 → R1266

Previous harvest: `workers/dispatcher/harvest-5way-r1265_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3572         | 2.3898         | +0.0326 |
| ctrl_bpc best  | 2.2267         | 2.2289         | +0.0022 |

## Per-round trajectory (best bird: 369I8)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1266 | 4214 | 2.2289 | +0.2478 |

## Cumulative training contribution

- This harvest: **720 steps** from 9 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-12way-r1265_sym24`
  - `workers/dispatcher/harvest-5way-r1265_sym24`

## Output

`workers/dispatcher/harvest-9way-r1266_sym24/round-1266/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 9 workers)
- `dense.pt` (averaged across 9 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

