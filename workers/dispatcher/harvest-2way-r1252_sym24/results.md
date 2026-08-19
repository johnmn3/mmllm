# harvest-2way-r1252 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1252 ctrl_bpc |
|--------|--------|--------------:|
| ayiLv | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-8e4a175b-ayiLv | 2.2402 |
| 13elt | fork-SeniorCareMarket-mmllm-claude-train-sym24-d1c83778-13elt | 2.2562 |
| **mean** | | **2.2482** |
| **best** | | **2.2402** |

## Chain progression R1251 → R1252

Previous harvest: `workers/dispatcher/harvest-11way-r1251_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4963         | 2.2482         | -0.2481 |
| ctrl_bpc best  | 2.2391         | 2.2402         | +0.0011 |

## Per-round trajectory (best bird: ayiLv)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1252 | 4351 | 2.2402 | +0.2452 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-6way-r1251_sym24`

## Output

`workers/dispatcher/harvest-2way-r1252_sym24/round-1252/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

