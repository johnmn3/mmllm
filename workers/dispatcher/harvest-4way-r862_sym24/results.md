# harvest-4way-r862 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R862 ctrl_bpc |
|--------|--------|--------------:|
| US50p | origin/claude/train-sym24-2010baaf-US50p | 2.8844 |
| P1rm0 | fork-slaa-us-mmllm-claude-train-sym24-a2ced717-P1rm0 | 2.8925 |
| VgLS3 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-5ff5ffdc-VgLS3 | 3.0628 |
| 3VoB6 | fork-SeniorCareMarket-mmllm-claude-train-sym24-51b7c77a-3VoB6 | 3.0856 |
| **mean** | | **2.9813** |
| **best** | | **2.8844** |

## Chain progression R861 → R862

Previous harvest: `workers/dispatcher/harvest-4way-r861_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8906         | 2.9813         | +0.0907 |
| ctrl_bpc best  | 2.8882         | 2.8844         | -0.0038 |

## Per-round trajectory (best bird: US50p)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 862 | 6524 | 2.8844 | +0.4653 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **1280 steps** from 16 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r861_sym24`

## Output

`workers/dispatcher/harvest-4way-r862_sym24/round-862/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

