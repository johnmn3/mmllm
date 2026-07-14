# harvest-2way-r918 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R918 ctrl_bpc |
|--------|--------|--------------:|
| 2oant | fork-SeniorCareMarket-mmllm-claude-train-sym24-ac3a49ac-2oant | 2.7870 |
| SPjd0 | fork-joly-os-mmllm-claude-train-sym24-8ec168cf-SPjd0 | 2.9265 |
| **mean** | | **2.8567** |
| **best** | | **2.7870** |

## Chain progression R917 → R918

Previous harvest: `workers/dispatcher/harvest-6way-r917_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0176         | 2.8567         | -0.1608 |
| ctrl_bpc best  | 2.7562         | 2.7870         | +0.0308 |

## Per-round trajectory (best bird: 2oant)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 918 | 5375 | 2.7870 | +0.2601 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r917_sym24`
  - `workers/dispatcher/harvest-3way-r917_sym24`

## Output

`workers/dispatcher/harvest-2way-r918_sym24/round-918/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

