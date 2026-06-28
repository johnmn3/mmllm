# harvest-8way-r793 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R793 ctrl_bpc |
|--------|--------|--------------:|
| dh8Lg | fork-joly-os-mmllm-claude-train-sym24-29124fc4-dh8Lg | 3.1185 |
| Kfidk | origin/claude/train-sym24-b2ed085e-Kfidk | 3.1424 |
| E8bEO | fork-davidwuchn-mmllm-claude-train-sym24-f9c70ab1-E8bEO | 3.2640 |
| gdXtb | fork-SeniorCareMarket-mmllm-claude-train-sym24-8b3b428e-gdXtb | 3.2665 |
| G69Yl | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-565f626b-G69Yl | 3.2686 |
| w9jvu | origin/claude/train-sym24-02c0fe3a-w9jvu | 3.5196 |
| ZyPIK | fork-joly-os-mmllm-claude-train-sym24-b629f517-ZyPIK | 3.5198 |
| prtFg | fork-slaa-us-mmllm-claude-train-sym24-b5914a8c-prtFg | 3.5235 |
| **mean** | | **3.3279** |
| **best** | | **3.1185** |

## Chain progression R792 → R793

Previous harvest: `workers/dispatcher/harvest-8way-r792_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2426         | 3.3279         | +0.0853 |
| ctrl_bpc best  | 3.1350         | 3.1185         | -0.0165 |

## Per-round trajectory (best bird: dh8Lg)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 793 | 6455 | 3.1185 | +0.4350 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **1280 steps** from 16 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r792_sym24`
  - `workers/dispatcher/harvest-8way-r792_sym24`

## Output

`workers/dispatcher/harvest-8way-r793_sym24/round-793/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

