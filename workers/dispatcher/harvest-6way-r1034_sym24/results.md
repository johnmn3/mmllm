# harvest-6way-r1034 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1034 ctrl_bpc |
|--------|--------|--------------:|
| 4egOE | fork-SeniorCareMarket-mmllm-claude-train-sym24-9288e8e5-4egOE | 2.5112 |
| 20ldq | fork-joly-os-mmllm-claude-train-sym24-36c40ccb-20ldq | 2.5172 |
| xpjxU | fork-joly-os-mmllm-claude-train-sym24-69db4860-xpjxU | 2.5241 |
| RSEvb | origin/claude/train-sym24-9f91668b-RSEvb | 2.6873 |
| q54xx | fork-slaa-us-mmllm-claude-train-sym24-58b58da7-q54xx | 2.6989 |
| 8Ltcx | fork-slaa-us-mmllm-claude-train-sym24-0c1b346a-8Ltcx | 2.7070 |
| **mean** | | **2.6076** |
| **best** | | **2.5112** |

## Chain progression R1033 → R1034

Previous harvest: `workers/dispatcher/harvest-8way-r1033_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6084         | 2.6076         | -0.0008 |
| ctrl_bpc best  | 2.4889         | 2.5112         | +0.0223 |

## Per-round trajectory (best bird: 4egOE)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1034 | 4390 | 2.5112 | +0.1939 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1033_sym24`
  - `workers/dispatcher/harvest-8way-r1033_sym24`

## Output

`workers/dispatcher/harvest-6way-r1034_sym24/round-1034/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

