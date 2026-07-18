# harvest-2way-r952 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R952 ctrl_bpc |
|--------|--------|--------------:|
| Tz1pO | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-77404379-Tz1pO | 2.6406 |
| NNd3B | fork-slaa-us-mmllm-claude-train-sym24-67b9f1a0-NNd3B | 3.0654 |
| **mean** | | **2.8530** |
| **best** | | **2.6406** |

## Chain progression R951 → R952

Previous harvest: `workers/dispatcher/harvest-9way-r951_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8179         | 2.8530         | +0.0351 |
| ctrl_bpc best  | 2.6556         | 2.6406         | -0.0150 |

## Per-round trajectory (best bird: Tz1pO)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 952 | 4345 | 2.6406 | +0.2128 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r951_sym24`

## Output

`workers/dispatcher/harvest-2way-r952_sym24/round-952/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

