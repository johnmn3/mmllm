# harvest-6way-r1078 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1078 ctrl_bpc |
|--------|--------|--------------:|
| KIymq | fork-SeniorCareMarket-mmllm-claude-train-sym24-8225e5fe-KIymq | 2.4339 |
| YX30N | fork-SeniorCareMarket-mmllm-claude-train-sym24-1e73a576-YX30N | 2.6122 |
| FKJcl | fork-slaa-us-mmllm-claude-train-sym24-4788ebc6-FKJcl | 2.6189 |
| 5VK6O | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-17bf4bd6-5VK6O | 2.6229 |
| dnRAf | fork-joly-os-mmllm-claude-train-sym24-6478ea25-dnRAf | 2.6262 |
| 7KtTR | origin/claude/train-sym24-c35c83fd-7KtTR | 2.8321 |
| **mean** | | **2.6244** |
| **best** | | **2.4339** |

## Chain progression R1077 → R1078

Previous harvest: `workers/dispatcher/harvest-9way-r1077_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5124         | 2.6244         | +0.1120 |
| ctrl_bpc best  | 2.4339         | 2.4339         | +0.0000 |

## Per-round trajectory (best bird: KIymq)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1078 | 5416 | 2.4339 | +0.2259 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1077_sym24`
  - `workers/dispatcher/harvest-7way-r1077_sym24`

## Output

`workers/dispatcher/harvest-6way-r1078_sym24/round-1078/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

