# harvest-6way-r670 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R670 ctrl_bpc |
|--------|--------|--------------:|
| 6BA3A | fork-davidwuchn-mmllm-claude-train-sym24-3f53616d-6BA3A | 3.8853 |
| nY13X | origin/claude/train-sym24-a3643d97-nY13X | 3.8923 |
| gaiZ5 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-dc1e8d23-gaiZ5 | 3.9174 |
| f9jwQ | fork-slaa-us-mmllm-claude-train-sym24-b35516d5-f9jwQ | 3.9252 |
| 6nQsT | fork-slaa-us-mmllm-claude-train-sym24-b7e0d3da-6nQsT | 3.9321 |
| 9cuSc | fork-joly-os-mmllm-claude-train-sym24-c4a9692c-9cuSc | 3.9529 |
| **mean** | | **3.9175** |
| **best** | | **3.8853** |

## Chain progression R669 → R670

Previous harvest: `workers/dispatcher/harvest-5way-r669_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.0486         | 3.9175         | -0.1311 |
| ctrl_bpc best  | 3.9320         | 3.8853         | -0.0467 |

## Per-round trajectory (best bird: 6BA3A)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 670 | 6550 | 3.8853 | +0.2671 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r669_sym24`
  - `workers/dispatcher/harvest-5way-r669_sym24`

## Output

`workers/dispatcher/harvest-6way-r670_sym24/round-670/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

