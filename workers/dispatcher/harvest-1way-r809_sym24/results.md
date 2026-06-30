# harvest-1way-r809 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R809 ctrl_bpc |
|--------|--------|--------------:|
| ZNPjS | fork-SeniorCareMarket-mmllm-claude-train-sym24-70c352b3-ZNPjS | 3.4295 |
| **mean** | | **3.4295** |
| **best** | | **3.4295** |

## Chain progression R808 → R809

Previous harvest: `workers/dispatcher/harvest-11way-r808_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2456         | 3.4295         | +0.1839 |
| ctrl_bpc best  | 3.0685         | 3.4295         | +0.3610 |

## Per-round trajectory (best bird: ZNPjS)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 809 | 3664 | 3.4295 | +0.5092 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-6way-r808_sym24`

## Output

`workers/dispatcher/harvest-1way-r809_sym24/round-809/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

