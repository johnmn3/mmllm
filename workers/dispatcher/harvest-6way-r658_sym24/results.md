# harvest-6way-r658 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R658 ctrl_bpc |
|--------|--------|--------------:|
| Jfr6C | origin/claude/train-sym24-3a7ac82a-Jfr6C | 4.0878 |
| 38BXx | fork-joly-os-mmllm-claude-train-sym24-3006e4ed-38BXx | 4.0894 |
| uwRZp | fork-slaa-us-mmllm-claude-train-sym24-10649ade-uwRZp | 4.0905 |
| AbVRW | fork-davidwuchn-mmllm-claude-train-sym24-9019c500-AbVRW | 4.0922 |
| lFTfg | fork-SeniorCareMarket-mmllm-claude-train-sym24-b75a0e67-lFTfg | 4.0965 |
| 9I1nE | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-cfad1e80-9I1nE | 4.4404 |
| **mean** | | **4.1495** |
| **best** | | **4.0878** |

## Chain progression R657 → R658

Previous harvest: `workers/dispatcher/harvest-8way-r657_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.2529         | 4.1495         | -0.1034 |
| ctrl_bpc best  | 4.1004         | 4.0878         | -0.0126 |

## Per-round trajectory (best bird: Jfr6C)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 658 | 4379 | 4.0878 | +0.0649 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r657_sym24`

## Output

`workers/dispatcher/harvest-6way-r658_sym24/round-658/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

