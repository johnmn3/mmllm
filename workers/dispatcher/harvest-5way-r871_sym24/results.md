# harvest-5way-r871 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R871 ctrl_bpc |
|--------|--------|--------------:|
| k7QkZ | origin/claude/train-sym24-df7b7f3e-k7QkZ | 2.8608 |
| tpSBZ | fork-joly-os-mmllm-claude-train-sym24-97233563-tpSBZ | 2.8642 |
| Ku8TB | fork-slaa-us-mmllm-claude-train-sym24-f5e56d47-Ku8TB | 3.0262 |
| qeqyP | fork-SeniorCareMarket-mmllm-claude-train-sym24-4a4867cc-qeqyP | 3.0290 |
| qgLD3 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-609dce9c-qgLD3 | 3.2646 |
| **mean** | | **3.0090** |
| **best** | | **2.8608** |

## Chain progression R870 → R871

Previous harvest: `workers/dispatcher/harvest-3way-r870_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9984         | 3.0090         | +0.0106 |
| ctrl_bpc best  | 2.8703         | 2.8608         | -0.0095 |

## Per-round trajectory (best bird: k7QkZ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 871 | 6658 | 2.8608 | +0.3836 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r870_sym24`

## Output

`workers/dispatcher/harvest-5way-r871_sym24/round-871/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

