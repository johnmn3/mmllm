# harvest-5way-r751 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R751 ctrl_bpc |
|--------|--------|--------------:|
| gqMUc | origin/claude/train-sym24-fb7cb5f7-gqMUc | 3.3417 |
| LiMgX | fork-slaa-us-mmllm-claude-train-sym24-fe2a33c9-LiMgX | 3.3440 |
| 1hEDe | fork-davidwuchn-mmllm-claude-train-sym24-441ef237-1hEDe | 3.3721 |
| wX270 | fork-joly-os-mmllm-claude-train-sym24-33bf1c70-wX270 | 3.4013 |
| 836iL | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-87d4b9ff-836iL | 3.6802 |
| **mean** | | **3.4279** |
| **best** | | **3.3417** |

## Chain progression R750 → R751

Previous harvest: `workers/dispatcher/harvest-20way-r750_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4592         | 3.4279         | -0.0313 |
| ctrl_bpc best  | 3.3279         | 3.3417         | +0.0138 |

## Per-round trajectory (best bird: gqMUc)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 751 | 6605 | 3.3417 | +0.6626 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r750_sym24`

## Output

`workers/dispatcher/harvest-5way-r751_sym24/round-751/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

