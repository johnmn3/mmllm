# harvest-13way-r660 — sparse-delta merge of 13 birds

## Worker endpoints

| handle | branch | R660 ctrl_bpc |
|--------|--------|--------------:|
| gTdO1 | fork-joly-os-mmllm-claude-train-sym24-2e6bfa30-gTdO1 | 3.9990 |
| ZngIN | fork-slaa-us-mmllm-claude-train-sym24-db631b84-ZngIN | 4.0015 |
| Pr7a0 | fork-joly-os-mmllm-claude-train-sym24-c4e04b84-Pr7a0 | 4.0092 |
| glkWV | origin/claude/train-sym24-2e5b0d85-glkWV | 4.0119 |
| pkFKw | fork-davidwuchn-mmllm-claude-train-sym24-c6c7388e-pkFKw | 4.0131 |
| OhOlE | fork-SeniorCareMarket-mmllm-claude-train-sym24-8a12ef21-OhOlE | 4.0328 |
| Nb0jA | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-3de6575d-Nb0jA | 4.0435 |
| 5X1NP | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-95441209-5X1NP | 4.0463 |
| rg3hE | fork-slaa-us-mmllm-claude-train-sym24-a41141be-rg3hE | 4.0530 |
| YMSsH | fork-SeniorCareMarket-mmllm-claude-train-sym24-9b8e8beb-YMSsH | 4.0575 |
| Ek85r | fork-davidwuchn-mmllm-claude-train-sym24-e7c7f212-Ek85r | 4.0767 |
| dGRbK | origin/claude/train-sym24-57f4ccf8-dGRbK | 4.0860 |
| Op4dm | origin/claude/train-sym24-6b0e1114-Op4dm | 4.3933 |
| **mean** | | **4.0634** |
| **best** | | **3.9990** |

## Chain progression R659 → R660

Previous harvest: `workers/dispatcher/harvest-8way-r659_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.1577         | 4.0634         | -0.0943 |
| ctrl_bpc best  | 4.0518         | 3.9990         | -0.0528 |

## Per-round trajectory (best bird: gTdO1)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 660 | 4368 | 3.9990 | +0.1293 |

## Cumulative training contribution

- This harvest: **1040 steps** from 13 bird(s)
- Across full ancestry (deduped by bird_id): **1680 steps** from 21 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r659_sym24`
  - `workers/dispatcher/harvest-8way-r659_sym24`

## Output

`workers/dispatcher/harvest-13way-r660_sym24/round-660/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 13 workers)
- `dense.pt` (averaged across 13 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

