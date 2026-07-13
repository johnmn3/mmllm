# harvest-3way-r913 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R913 ctrl_bpc |
|--------|--------|--------------:|
| u0Zwc | fork-joly-os-mmllm-claude-train-sym24-1fef7b21-u0Zwc | 2.7482 |
| jbmKP | fork-SeniorCareMarket-mmllm-claude-train-sym24-b0221fda-jbmKP | 3.1305 |
| RuTP1 | origin/claude/train-sym24-dff84b49-RuTP1 | 3.1434 |
| **mean** | | **3.0074** |
| **best** | | **2.7482** |

## Chain progression R912 → R913

Previous harvest: `workers/dispatcher/harvest-6way-r912_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9662         | 3.0074         | +0.0412 |
| ctrl_bpc best  | 2.7564         | 2.7482         | -0.0082 |

## Per-round trajectory (best bird: u0Zwc)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 913 | 6560 | 2.7482 | +0.3322 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r912_sym24`

## Output

`workers/dispatcher/harvest-3way-r913_sym24/round-913/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

