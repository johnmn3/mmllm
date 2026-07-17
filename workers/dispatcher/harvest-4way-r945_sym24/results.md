# harvest-4way-r945 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R945 ctrl_bpc |
|--------|--------|--------------:|
| H7D72 | fork-joly-os-mmllm-claude-train-sym24-dc12be9f-H7D72 | 2.6833 |
| nrESY | origin/claude/train-sym24-a5560393-nrESY | 2.8571 |
| KQBBx | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-969e9b11-KQBBx | 2.8616 |
| I9dIp | origin/claude/train-sym24-9edb40a0-I9dIp | 3.0575 |
| **mean** | | **2.8649** |
| **best** | | **2.6833** |

## Chain progression R944 → R945

Previous harvest: `workers/dispatcher/harvest-6way-r944_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7747         | 2.8649         | +0.0902 |
| ctrl_bpc best  | 2.6655         | 2.6833         | +0.0178 |

## Per-round trajectory (best bird: H7D72)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 945 | 6446 | 2.6833 | +0.1579 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r944_sym24`

## Output

`workers/dispatcher/harvest-4way-r945_sym24/round-945/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

