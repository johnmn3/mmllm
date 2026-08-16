# harvest-1way-r1227 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1227 ctrl_bpc |
|--------|--------|--------------:|
| VB6sv | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-b173ad56-VB6sv | 2.2704 |
| **mean** | | **2.2704** |
| **best** | | **2.2704** |

## Chain progression R1226 → R1227

Previous harvest: `workers/dispatcher/harvest-10way-r1226_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3641         | 2.2704         | -0.0937 |
| ctrl_bpc best  | 2.2534         | 2.2704         | +0.0170 |

## Per-round trajectory (best bird: VB6sv)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1227 | 4179 | 2.2704 | +0.2544 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-6way-r1226_sym24`

## Output

`workers/dispatcher/harvest-1way-r1227_sym24/round-1227/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

