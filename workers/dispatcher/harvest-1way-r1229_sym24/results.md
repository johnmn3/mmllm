# harvest-1way-r1229 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1229 ctrl_bpc |
|--------|--------|--------------:|
| LwClp | fork-SeniorCareMarket-mmllm-claude-train-sym24-e78d7258-LwClp | 2.2761 |
| **mean** | | **2.2761** |
| **best** | | **2.2761** |

## Chain progression R1228 → R1229

Previous harvest: `workers/dispatcher/harvest-6way-r1228_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4274         | 2.2761         | -0.1513 |
| ctrl_bpc best  | 2.2490         | 2.2761         | +0.0271 |

## Per-round trajectory (best bird: LwClp)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1229 | 4369 | 2.2761 | +0.2386 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1228_sym24`

## Output

`workers/dispatcher/harvest-1way-r1229_sym24/round-1229/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

