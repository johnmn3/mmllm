# harvest-4way-r622 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R622 ctrl_bpc |
|--------|--------|--------------:|
| uzTxn | fork-slaa-us-mmllm-claude-train-sym24-11c27350-uzTxn | 2.1214 |
| hp4EQ | fork-joly-os-mmllm-claude-train-sym24-1ac0ca4f-hp4EQ | 2.1270 |
| LsbDP | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-64048445-LsbDP | 2.5873 |
| nIDLO | fork-davidwuchn-mmllm-claude-train-sym24-239e4933-nIDLO | 2.5911 |
| **mean** | | **2.3567** |
| **best** | | **2.1214** |

## Chain progression R621 → R622

Previous harvest: `workers/dispatcher/harvest-1way-r621_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5851         | 2.3567         | -0.2284 |
| ctrl_bpc best  | 2.5851         | 2.1214         | -0.4637 |

## Per-round trajectory (best bird: uzTxn)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 622 | 5474 | 2.1214 | +0.0405 |

## Cumulative training contribution

- This harvest: **200 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **750 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r621_sym24`

## Output

`workers/dispatcher/harvest-4way-r622_sym24/round-622/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

