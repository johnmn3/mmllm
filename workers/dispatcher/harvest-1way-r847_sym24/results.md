# harvest-1way-r847 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R847 ctrl_bpc |
|--------|--------|--------------:|
| HJ2SO | fork-SeniorCareMarket-mmllm-claude-train-sym24-092632f7-HJ2SO | 3.3164 |
| **mean** | | **3.3164** |
| **best** | | **3.3164** |

## Chain progression R846 → R847

Previous harvest: `workers/dispatcher/harvest-5way-r846_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0529         | 3.3164         | +0.2635 |
| ctrl_bpc best  | 2.9391         | 3.3164         | +0.3773 |

## Per-round trajectory (best bird: HJ2SO)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 847 | 6668 | 3.3164 | +0.3259 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r846_sym24`

## Output

`workers/dispatcher/harvest-1way-r847_sym24/round-847/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

