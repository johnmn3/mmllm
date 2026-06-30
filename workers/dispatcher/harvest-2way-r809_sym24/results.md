# harvest-2way-r809 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R809 ctrl_bpc |
|--------|--------|--------------:|
| Qmcn2 | fork-slaa-us-mmllm-claude-train-sym24-3d3810f9-Qmcn2 | 3.1896 |
| ZNPjS | fork-SeniorCareMarket-mmllm-claude-train-sym24-70c352b3-ZNPjS | 3.4295 |
| **mean** | | **3.3095** |
| **best** | | **3.1896** |

## Chain progression R808 → R809

Previous harvest: `workers/dispatcher/harvest-11way-r808_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2456         | 3.3095         | +0.0639 |
| ctrl_bpc best  | 3.0685         | 3.1896         | +0.1211 |

## Per-round trajectory (best bird: Qmcn2)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 809 | 4195 | 3.1896 | +0.4574 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-6way-r808_sym24`

## Output

`workers/dispatcher/harvest-2way-r809_sym24/round-809/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

