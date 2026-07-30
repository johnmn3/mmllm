# harvest-5way-r1067 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1067 ctrl_bpc |
|--------|--------|--------------:|
| ezWAj | origin/claude/train-sym24-deacc721-ezWAj | 2.4671 |
| nqOUj | origin/claude/train-sym24-84f1b36a-nqOUj | 2.4733 |
| I9slv | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-31474b34-I9slv | 2.6289 |
| XQ5qd | fork-SeniorCareMarket-mmllm-claude-train-sym24-86fea8c4-XQ5qd | 2.6337 |
| MO9w5 | fork-joly-os-mmllm-claude-train-sym24-3b081645-MO9w5 | 2.6375 |
| **mean** | | **2.5681** |
| **best** | | **2.4671** |

## Chain progression R1066 → R1067

Previous harvest: `workers/dispatcher/harvest-6way-r1066_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5977         | 2.5681         | -0.0296 |
| ctrl_bpc best  | 2.4812         | 2.4671         | -0.0141 |

## Per-round trajectory (best bird: ezWAj)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1067 | 6590 | 2.4671 | +0.2201 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1066_sym24`
  - `workers/dispatcher/harvest-4way-r1066_sym24`

## Output

`workers/dispatcher/harvest-5way-r1067_sym24/round-1067/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

