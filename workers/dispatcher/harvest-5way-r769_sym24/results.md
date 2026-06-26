# harvest-5way-r769 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R769 ctrl_bpc |
|--------|--------|--------------:|
| sqFtX | fork-davidwuchn-mmllm-claude-train-sym24-fa1eebe1-sqFtX | 3.2235 |
| uRmhO | fork-davidwuchn-mmllm-claude-train-sym24-a232a1ac-uRmhO | 3.2361 |
| P7Z0j | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-19679c59-P7Z0j | 3.2794 |
| 88X28 | fork-slaa-us-mmllm-claude-train-sym24-5c399b0d-88X28 | 3.3585 |
| SqpnW | fork-joly-os-mmllm-claude-train-sym24-894a980a-SqpnW | 3.6221 |
| **mean** | | **3.3439** |
| **best** | | **3.2235** |

## Chain progression R768 → R769

Previous harvest: `workers/dispatcher/harvest-20way-r768_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3708         | 3.3439         | -0.0269 |
| ctrl_bpc best  | 3.2333         | 3.2235         | -0.0098 |

## Per-round trajectory (best bird: sqFtX)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 769 | 6449 | 3.2235 | +0.5415 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **1440 steps** from 18 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-13way-r768_sym24`
  - `workers/dispatcher/harvest-7way-r768_sym24`

## Output

`workers/dispatcher/harvest-5way-r769_sym24/round-769/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

