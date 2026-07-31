# harvest-4way-r1078 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1078 ctrl_bpc |
|--------|--------|--------------:|
| YX30N | fork-SeniorCareMarket-mmllm-claude-train-sym24-1e73a576-YX30N | 2.6122 |
| FKJcl | fork-slaa-us-mmllm-claude-train-sym24-4788ebc6-FKJcl | 2.6189 |
| dnRAf | fork-joly-os-mmllm-claude-train-sym24-6478ea25-dnRAf | 2.6262 |
| 7KtTR | origin/claude/train-sym24-c35c83fd-7KtTR | 2.8321 |
| **mean** | | **2.6723** |
| **best** | | **2.6122** |

## Chain progression R1077 → R1078

Previous harvest: `workers/dispatcher/harvest-9way-r1077_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5124         | 2.6723         | +0.1599 |
| ctrl_bpc best  | 2.4339         | 2.6122         | +0.1783 |

## Per-round trajectory (best bird: YX30N)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1078 | 6528 | 2.6122 | +0.2100 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1077_sym24`
  - `workers/dispatcher/harvest-7way-r1077_sym24`

## Output

`workers/dispatcher/harvest-4way-r1078_sym24/round-1078/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

