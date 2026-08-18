# harvest-7way-r1241 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R1241 ctrl_bpc |
|--------|--------|--------------:|
| bvBaR | fork-slaa-us-mmllm-claude-train-sym24-90a31a63-bvBaR | 2.2649 |
| UwToi | fork-SeniorCareMarket-mmllm-claude-train-sym24-9032273a-UwToi | 2.2661 |
| BpiFl | fork-joly-os-mmllm-claude-train-sym24-79af3225-BpiFl | 2.2737 |
| jTrH3 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-3fbbdf04-jTrH3 | 2.4449 |
| UbWuI | origin/claude/train-sym24-291dc17f-UbWuI | 2.4468 |
| Aml3L | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-8f3313dc-Aml3L | 2.6446 |
| rMLal | fork-joly-os-mmllm-claude-train-sym24-1867e725-rMLal | 2.6577 |
| **mean** | | **2.4284** |
| **best** | | **2.2649** |

## Chain progression R1240 → R1241

Previous harvest: `workers/dispatcher/harvest-7way-r1240_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4513         | 2.4284         | -0.0229 |
| ctrl_bpc best  | 2.2508         | 2.2649         | +0.0141 |

## Per-round trajectory (best bird: bvBaR)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1241 | 6634 | 2.2649 | +0.2365 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1240_sym24`
  - `workers/dispatcher/harvest-7way-r1240_sym24`

## Output

`workers/dispatcher/harvest-7way-r1241_sym24/round-1241/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

