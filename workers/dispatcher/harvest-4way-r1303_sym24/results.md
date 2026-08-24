# harvest-4way-r1303 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1303 ctrl_bpc |
|--------|--------|--------------:|
| 22SQH | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-e02e84f4-22SQH | 3.5844 |
| 6oCvL | fork-joly-os-mmllm-claude-train-sym24-7c5880e0-6oCvL | 3.5957 |
| O44DS | origin/claude/train-sym24-13af2c6f-O44DS | 3.6036 |
| 2ptfy | fork-joly-os-mmllm-claude-train-sym24-1f3b19bc-2ptfy | 3.6245 |
| **mean** | | **3.6021** |
| **best** | | **3.5844** |

## Chain progression R1302 → R1303

Previous harvest: `workers/dispatcher/harvest-5way-r1302_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.7319         | 3.6021         | -0.1298 |
| ctrl_bpc best  | 3.5489         | 3.5844         | +0.0355 |

## Per-round trajectory (best bird: 22SQH)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1303 | 6600 | 3.5844 | +0.0775 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1302_sym24`
  - `workers/dispatcher/harvest-5way-r1302_sym24`

## Output

`workers/dispatcher/harvest-4way-r1303_sym24/round-1303/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

