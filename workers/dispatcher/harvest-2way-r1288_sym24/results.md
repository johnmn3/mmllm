# harvest-2way-r1288 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1288 ctrl_bpc |
|--------|--------|--------------:|
| hdcMf | fork-slaa-us-mmllm-claude-train-sym24-9c0302eb-hdcMf | 2.2089 |
| 5WEsF | fork-SeniorCareMarket-mmllm-claude-train-sym24-8c8f7f71-5WEsF | 2.6385 |
| **mean** | | **2.4237** |
| **best** | | **2.2089** |

## Chain progression R1287 → R1288

Previous harvest: `workers/dispatcher/harvest-11way-r1287_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3329         | 2.4237         | +0.0908 |
| ctrl_bpc best  | 2.2147         | 2.2089         | -0.0058 |

## Per-round trajectory (best bird: hdcMf)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1288 | 4367 | 2.2089 | +0.2489 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1287_sym24`

## Output

`workers/dispatcher/harvest-2way-r1288_sym24/round-1288/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

