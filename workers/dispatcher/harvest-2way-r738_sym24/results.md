# harvest-2way-r738 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R738 ctrl_bpc |
|--------|--------|--------------:|
| uELXF | fork-davidwuchn-mmllm-claude-train-sym24-17c00de7-uELXF | 3.4614 |
| pyMTY | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-54d89eb2-pyMTY | 3.7586 |
| **mean** | | **3.6100** |
| **best** | | **3.4614** |

## Chain progression R737 → R738

Previous harvest: `workers/dispatcher/harvest-1way-r737_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4074         | 3.6100         | +0.2026 |
| ctrl_bpc best  | 3.4074         | 3.4614         | +0.0540 |

## Per-round trajectory (best bird: uELXF)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 738 | 6551 | 3.4614 | +0.6920 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r737_sym24`

## Output

`workers/dispatcher/harvest-2way-r738_sym24/round-738/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

