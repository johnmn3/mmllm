# harvest-4way-r918 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R918 ctrl_bpc |
|--------|--------|--------------:|
| 68fni | fork-slaa-us-mmllm-claude-train-sym24-550aeda1-68fni | 2.7535 |
| 2oant | fork-SeniorCareMarket-mmllm-claude-train-sym24-ac3a49ac-2oant | 2.7870 |
| SPjd0 | fork-joly-os-mmllm-claude-train-sym24-8ec168cf-SPjd0 | 2.9265 |
| XjOMi | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-6907ecdf-XjOMi | 2.9369 |
| **mean** | | **2.8510** |
| **best** | | **2.7535** |

## Chain progression R610 → R918

Previous harvest: `workers/dispatcher/harvest-2way-merge-r610_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.1372         | 2.8510         | +0.7138 |
| ctrl_bpc best  | 2.1268         | 2.7535         | +0.6267 |

## Per-round trajectory (best bird: 68fni)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 918 | 6659 | 2.7535 | +0.2083 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r917_sym24`
  - `workers/dispatcher/harvest-3way-r917_sym24`
  - `workers/dispatcher/harvest-6way-r917_sym24`

## Output

`workers/dispatcher/harvest-4way-r918_sym24/round-918/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

