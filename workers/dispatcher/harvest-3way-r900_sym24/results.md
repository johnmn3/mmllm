# harvest-3way-r900 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R900 ctrl_bpc |
|--------|--------|--------------:|
| Vod1o | fork-SeniorCareMarket-mmllm-claude-train-sym24-959d848c-Vod1o | 2.8119 |
| o8mCT | origin/claude/train-sym24-92238159-o8mCT | 2.9574 |
| vCs26 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-5e38d9af-vCs26 | 2.9615 |
| **mean** | | **2.9103** |
| **best** | | **2.8119** |

## Chain progression R899 → R900

Previous harvest: `workers/dispatcher/harvest-3way-r899_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9153         | 2.9103         | -0.0050 |
| ctrl_bpc best  | 2.8029         | 2.8119         | +0.0090 |

## Per-round trajectory (best bird: Vod1o)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 900 | 4274 | 2.8119 | +0.2043 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r899_sym24`

## Output

`workers/dispatcher/harvest-3way-r900_sym24/round-900/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

