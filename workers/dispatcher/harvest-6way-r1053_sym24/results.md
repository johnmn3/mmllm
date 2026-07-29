# harvest-6way-r1053 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1053 ctrl_bpc |
|--------|--------|--------------:|
| 0gMQE | fork-slaa-us-mmllm-claude-train-sym24-9ff2066a-0gMQE | 2.4584 |
| wwkDg | origin/claude/train-sym24-86d5efe4-wwkDg | 2.4830 |
| cuiCG | fork-SeniorCareMarket-mmllm-claude-train-sym24-cf38f4d2-cuiCG | 2.4878 |
| OJ7hW | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-684b191f-OJ7hW | 2.5161 |
| QvMoI | origin/claude/train-sym24-1ef95df8-QvMoI | 2.8597 |
| ANppI | fork-joly-os-mmllm-claude-train-sym24-fbd9d332-ANppI | 2.8618 |
| **mean** | | **2.6111** |
| **best** | | **2.4584** |

## Chain progression R1052 → R1053

Previous harvest: `workers/dispatcher/harvest-6way-r1052_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6833         | 2.6111         | -0.0722 |
| ctrl_bpc best  | 2.4646         | 2.4584         | -0.0062 |

## Per-round trajectory (best bird: 0gMQE)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1053 | 6398 | 2.4584 | +0.2155 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1052_sym24`

## Output

`workers/dispatcher/harvest-6way-r1053_sym24/round-1053/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

