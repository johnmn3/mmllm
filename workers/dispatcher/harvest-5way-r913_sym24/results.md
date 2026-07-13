# harvest-5way-r913 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R913 ctrl_bpc |
|--------|--------|--------------:|
| u0Zwc | fork-joly-os-mmllm-claude-train-sym24-1fef7b21-u0Zwc | 2.7482 |
| VcPbU | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-794986a5-VcPbU | 2.9487 |
| jbmKP | fork-SeniorCareMarket-mmllm-claude-train-sym24-b0221fda-jbmKP | 3.1305 |
| RuTP1 | origin/claude/train-sym24-dff84b49-RuTP1 | 3.1434 |
| AuJV0 | fork-slaa-us-mmllm-claude-train-sym24-f76e86b4-AuJV0 | 3.1580 |
| **mean** | | **3.0258** |
| **best** | | **2.7482** |

## Chain progression R912 → R913

Previous harvest: `workers/dispatcher/harvest-6way-r912_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9662         | 3.0258         | +0.0596 |
| ctrl_bpc best  | 2.7564         | 2.7482         | -0.0082 |

## Per-round trajectory (best bird: u0Zwc)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 913 | 6560 | 2.7482 | +0.3322 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r912_sym24`

## Output

`workers/dispatcher/harvest-5way-r913_sym24/round-913/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

