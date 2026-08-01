# harvest-6way-r1085 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1085 ctrl_bpc |
|--------|--------|--------------:|
| RBXfb | fork-slaa-us-mmllm-claude-train-sym24-2f423174-RBXfb | 2.4499 |
| TKac7 | fork-joly-os-mmllm-claude-train-sym24-dffa3260-TKac7 | 2.4578 |
| yPshI | origin/claude/train-sym24-06572bec-yPshI | 2.6208 |
| R7KNs | origin/claude/train-sym24-82351cd6-R7KNs | 2.8132 |
| PBdtQ | fork-SeniorCareMarket-mmllm-claude-train-sym24-58b1c679-PBdtQ | 2.8162 |
| IgCjf | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-8e66fd47-IgCjf | 2.8182 |
| **mean** | | **2.6627** |
| **best** | | **2.4499** |

## Chain progression R1084 → R1085

Previous harvest: `workers/dispatcher/harvest-8way-r1084_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5556         | 2.6627         | +0.1071 |
| ctrl_bpc best  | 2.4305         | 2.4499         | +0.0194 |

## Per-round trajectory (best bird: RBXfb)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1085 | 6486 | 2.4499 | +0.2219 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-6way-r1084_sym24`
  - `workers/dispatcher/harvest-8way-r1084_sym24`

## Output

`workers/dispatcher/harvest-6way-r1085_sym24/round-1085/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

