# harvest-7way-r660 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R660 ctrl_bpc |
|--------|--------|--------------:|
| gTdO1 | fork-joly-os-mmllm-claude-train-sym24-2e6bfa30-gTdO1 | 3.9990 |
| glkWV | origin/claude/train-sym24-2e5b0d85-glkWV | 4.0119 |
| pkFKw | fork-davidwuchn-mmllm-claude-train-sym24-c6c7388e-pkFKw | 4.0131 |
| OhOlE | fork-SeniorCareMarket-mmllm-claude-train-sym24-8a12ef21-OhOlE | 4.0328 |
| Nb0jA | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-3de6575d-Nb0jA | 4.0435 |
| rg3hE | fork-slaa-us-mmllm-claude-train-sym24-a41141be-rg3hE | 4.0530 |
| Op4dm | origin/claude/train-sym24-6b0e1114-Op4dm | 4.3933 |
| **mean** | | **4.0781** |
| **best** | | **3.9990** |

## Chain progression R659 → R660

Previous harvest: `workers/dispatcher/harvest-13way-r659_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.1152         | 4.0781         | -0.0371 |
| ctrl_bpc best  | 4.0164         | 3.9990         | -0.0174 |

## Per-round trajectory (best bird: gTdO1)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 660 | 4368 | 3.9990 | +0.1293 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r659_sym24`

## Output

`workers/dispatcher/harvest-7way-r660_sym24/round-660/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

