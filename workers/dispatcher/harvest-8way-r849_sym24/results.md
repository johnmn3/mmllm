# harvest-8way-r849 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R849 ctrl_bpc |
|--------|--------|--------------:|
| 2Is12 | fork-SeniorCareMarket-mmllm-claude-train-sym24-378cd903-2Is12 | 2.9266 |
| pPL0t | fork-slaa-us-mmllm-claude-train-sym24-a0182dbe-pPL0t | 2.9404 |
| x7odQ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-17830c67-x7odQ | 2.9503 |
| cJ5Qt | fork-slaa-us-mmllm-claude-train-sym24-c71111ce-cJ5Qt | 2.9634 |
| xgwwI | fork-joly-os-mmllm-claude-train-sym24-4edf48ee-xgwwI | 3.0750 |
| sImh7 | origin/claude/train-sym24-4d1f3788-sImh7 | 3.0885 |
| Mc4xp | fork-joly-os-mmllm-claude-train-sym24-0563ad12-Mc4xp | 3.0957 |
| tRMDH | fork-SeniorCareMarket-mmllm-claude-train-sym24-cd9b819a-tRMDH | 3.3113 |
| **mean** | | **3.0439** |
| **best** | | **2.9266** |

## Chain progression R848 → R849

Previous harvest: `workers/dispatcher/harvest-5way-r848_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0120         | 3.0439         | +0.0319 |
| ctrl_bpc best  | 2.9339         | 2.9266         | -0.0073 |

## Per-round trajectory (best bird: 2Is12)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 849 | 4331 | 2.9266 | +0.3421 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r848_sym24`
  - `workers/dispatcher/harvest-5way-r848_sym24`

## Output

`workers/dispatcher/harvest-8way-r849_sym24/round-849/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

