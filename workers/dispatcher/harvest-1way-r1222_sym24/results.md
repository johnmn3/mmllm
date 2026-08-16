# harvest-1way-r1222 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1222 ctrl_bpc |
|--------|--------|--------------:|
| 1UVsn | fork-SeniorCareMarket-mmllm-claude-train-sym24-39581564-1UVsn | 2.2797 |
| **mean** | | **2.2797** |
| **best** | | **2.2797** |

## Chain progression R1221 → R1222

Previous harvest: `workers/dispatcher/harvest-6way-r1221_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4061         | 2.2797         | -0.1264 |
| ctrl_bpc best  | 2.2620         | 2.2797         | +0.0177 |

## Per-round trajectory (best bird: 1UVsn)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1222 | 3618 | 2.2797 | +0.2519 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1221_sym24`

## Output

`workers/dispatcher/harvest-1way-r1222_sym24/round-1222/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

