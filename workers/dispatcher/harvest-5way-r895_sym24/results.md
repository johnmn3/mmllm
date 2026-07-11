# harvest-5way-r895 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R895 ctrl_bpc |
|--------|--------|--------------:|
| bCpwB | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-708e5e3e-bCpwB | 2.8007 |
| hpHnL | fork-slaa-us-mmllm-claude-train-sym24-b4e28985-hpHnL | 2.8090 |
| qrtlP | fork-SeniorCareMarket-mmllm-claude-train-sym24-d9ec5edc-qrtlP | 2.8260 |
| RJFxF | fork-slaa-us-mmllm-claude-train-sym24-7ec813dd-RJFxF | 2.9766 |
| JyQIo | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f83ada77-JyQIo | 3.2007 |
| **mean** | | **2.9226** |
| **best** | | **2.8007** |

## Chain progression R894 → R895

Previous harvest: `workers/dispatcher/harvest-7way-r894_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0263         | 2.9226         | -0.1037 |
| ctrl_bpc best  | 2.8022         | 2.8007         | -0.0015 |

## Per-round trajectory (best bird: bCpwB)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 895 | 4282 | 2.8007 | +0.2416 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r894_sym24`
  - `workers/dispatcher/harvest-3way-r894_sym24`

## Output

`workers/dispatcher/harvest-5way-r895_sym24/round-895/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

