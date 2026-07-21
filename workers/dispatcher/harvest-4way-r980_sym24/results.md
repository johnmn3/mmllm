# harvest-4way-r980 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R980 ctrl_bpc |
|--------|--------|--------------:|
| Osrn2 | fork-SeniorCareMarket-mmllm-claude-train-sym24-0e97e364-Osrn2 | 2.5967 |
| yY1v6 | origin/claude/train-sym24-424323a1-yY1v6 | 2.6168 |
| SY2y3 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-ad8fe8d0-SY2y3 | 2.8214 |
| 44qYw | origin/claude/train-sym24-9ddd608f-44qYw | 2.9797 |
| **mean** | | **2.7536** |
| **best** | | **2.5967** |

## Chain progression R979 → R980

Previous harvest: `workers/dispatcher/harvest-5way-r979_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7279         | 2.7536         | +0.0257 |
| ctrl_bpc best  | 2.5999         | 2.5967         | -0.0032 |

## Per-round trajectory (best bird: Osrn2)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 980 | 6630 | 2.5967 | +0.1567 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r979_sym24`
  - `workers/dispatcher/harvest-5way-r979_sym24`

## Output

`workers/dispatcher/harvest-4way-r980_sym24/round-980/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

