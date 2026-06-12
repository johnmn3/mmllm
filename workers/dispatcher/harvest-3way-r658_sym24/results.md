# harvest-3way-r658 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R658 ctrl_bpc |
|--------|--------|--------------:|
| Jfr6C | origin/claude/train-sym24-3a7ac82a-Jfr6C | 4.0878 |
| AbVRW | fork-davidwuchn-mmllm-claude-train-sym24-9019c500-AbVRW | 4.0922 |
| lFTfg | fork-SeniorCareMarket-mmllm-claude-train-sym24-b75a0e67-lFTfg | 4.0965 |
| **mean** | | **4.0922** |
| **best** | | **4.0878** |

## Chain progression R657 → R658

Previous harvest: `workers/dispatcher/harvest-8way-r657_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.2529         | 4.0922         | -0.1607 |
| ctrl_bpc best  | 4.1004         | 4.0878         | -0.0126 |

## Per-round trajectory (best bird: Jfr6C)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 658 | 4379 | 4.0878 | +0.0649 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r657_sym24`

## Output

`workers/dispatcher/harvest-3way-r658_sym24/round-658/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

