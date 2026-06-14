# harvest-10way-r670 — sparse-delta merge of 10 birds

## Worker endpoints

| handle | branch | R670 ctrl_bpc |
|--------|--------|--------------:|
| 6BA3A | fork-davidwuchn-mmllm-claude-train-sym24-3f53616d-6BA3A | 3.8853 |
| nY13X | origin/claude/train-sym24-a3643d97-nY13X | 3.8923 |
| gaiZ5 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-dc1e8d23-gaiZ5 | 3.9174 |
| f9jwQ | fork-slaa-us-mmllm-claude-train-sym24-b35516d5-f9jwQ | 3.9252 |
| QxvpY | fork-SeniorCareMarket-mmllm-claude-train-sym24-74a9c351-QxvpY | 3.9273 |
| 6nQsT | fork-slaa-us-mmllm-claude-train-sym24-b7e0d3da-6nQsT | 3.9321 |
| XsVTH | fork-slaa-us-mmllm-claude-train-sym24-ab6ede10-XsVTH | 3.9333 |
| 9cuSc | fork-joly-os-mmllm-claude-train-sym24-c4a9692c-9cuSc | 3.9529 |
| Xo7cq | fork-davidwuchn-mmllm-claude-train-sym24-a7a417d1-Xo7cq | 4.2065 |
| VCsqs | fork-joly-os-mmllm-claude-train-sym24-630e5c62-VCsqs | 4.2389 |
| **mean** | | **3.9811** |
| **best** | | **3.8853** |

## Chain progression R669 → R670

Previous harvest: `workers/dispatcher/harvest-5way-r669_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.0486         | 3.9811         | -0.0675 |
| ctrl_bpc best  | 3.9320         | 3.8853         | -0.0467 |

## Per-round trajectory (best bird: 6BA3A)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 670 | 6550 | 3.8853 | +0.2671 |

## Cumulative training contribution

- This harvest: **800 steps** from 10 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r669_sym24`
  - `workers/dispatcher/harvest-5way-r669_sym24`

## Output

`workers/dispatcher/harvest-10way-r670_sym24/round-670/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 10 workers)
- `dense.pt` (averaged across 10 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

