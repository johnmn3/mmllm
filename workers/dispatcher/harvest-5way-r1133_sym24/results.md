# harvest-5way-r1133 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1133 ctrl_bpc |
|--------|--------|--------------:|
| uS7yD | origin/claude/train-sym24-768e1d7c-uS7yD | 2.3563 |
| pe8Nx | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-0081bd39-pe8Nx | 2.5582 |
| Frd0D | fork-SeniorCareMarket-mmllm-claude-train-sym24-7faec279-Frd0D | 2.5609 |
| aInoD | fork-slaa-us-mmllm-claude-train-sym24-66bb3fc2-aInoD | 2.5631 |
| 4sYjv | fork-slaa-us-mmllm-claude-train-sym24-7d5e3043-4sYjv | 2.7519 |
| **mean** | | **2.5581** |
| **best** | | **2.3563** |

## Chain progression R1132 → R1133

Previous harvest: `workers/dispatcher/harvest-6way-r1132_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5259         | 2.5581         | +0.0322 |
| ctrl_bpc best  | 2.3471         | 2.3563         | +0.0092 |

## Per-round trajectory (best bird: uS7yD)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1133 | 6586 | 2.3563 | +0.2385 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1132_sym24`
  - `workers/dispatcher/harvest-4way-r1132_sym24`

## Output

`workers/dispatcher/harvest-5way-r1133_sym24/round-1133/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

