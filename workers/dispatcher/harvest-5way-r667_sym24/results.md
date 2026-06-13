# harvest-5way-r667 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R667 ctrl_bpc |
|--------|--------|--------------:|
| YPVdo | fork-SeniorCareMarket-mmllm-claude-train-sym24-c5a41e1d-YPVdo | 3.8934 |
| 8z1fK | fork-slaa-us-mmllm-claude-train-sym24-c0016dcf-8z1fK | 3.9171 |
| K8Xxg | fork-davidwuchn-mmllm-claude-train-sym24-46b34628-K8Xxg | 3.9189 |
| X1pev | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-1418df83-X1pev | 3.9730 |
| 7AJ6a | fork-joly-os-mmllm-claude-train-sym24-eb63477a-7AJ6a | 4.0110 |
| **mean** | | **3.9427** |
| **best** | | **3.8934** |

## Chain progression R666 → R667

Previous harvest: `workers/dispatcher/harvest-15way-r666_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.0267         | 3.9427         | -0.0840 |
| ctrl_bpc best  | 3.9071         | 3.8934         | -0.0137 |

## Per-round trajectory (best bird: YPVdo)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 667 | 6569 | 3.8934 | +0.2429 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r666_sym24`

## Output

`workers/dispatcher/harvest-5way-r667_sym24/round-667/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

