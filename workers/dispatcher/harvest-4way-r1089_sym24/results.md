# harvest-4way-r1089 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1089 ctrl_bpc |
|--------|--------|--------------:|
| 03XTM | fork-slaa-us-mmllm-claude-train-sym24-66e82bc0-03XTM | 2.4040 |
| nooPR | fork-SeniorCareMarket-mmllm-claude-train-sym24-0d7593a3-nooPR | 2.4177 |
| 16FTE | fork-joly-os-mmllm-claude-train-sym24-5105c8d4-16FTE | 2.4261 |
| i495Y | origin/claude/train-sym24-c775c671-i495Y | 2.4381 |
| **mean** | | **2.4215** |
| **best** | | **2.4040** |

## Chain progression R1088 → R1089

Previous harvest: `workers/dispatcher/harvest-11way-r1088_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4762         | 2.4215         | -0.0547 |
| ctrl_bpc best  | 2.4082         | 2.4040         | -0.0042 |

## Per-round trajectory (best bird: 03XTM)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1089 | 4272 | 2.4040 | +0.2435 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-11way-r1088_sym24`
  - `workers/dispatcher/harvest-5way-r1088_sym24`

## Output

`workers/dispatcher/harvest-4way-r1089_sym24/round-1089/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

