# harvest-5way-r1153 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1153 ctrl_bpc |
|--------|--------|--------------:|
| CozX3 | fork-joly-os-mmllm-claude-train-sym24-fcb69779-CozX3 | 2.3313 |
| h4oOR | fork-SeniorCareMarket-mmllm-claude-train-sym24-a97e6dd0-h4oOR | 2.5273 |
| Eje5S | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-43527236-Eje5S | 2.7156 |
| dHSwY | fork-slaa-us-mmllm-claude-train-sym24-294eb607-dHSwY | 2.7193 |
| yL92m | origin/claude/train-sym24-f2df0d99-yL92m | 2.7295 |
| **mean** | | **2.6046** |
| **best** | | **2.3313** |

## Chain progression R1152 → R1153

Previous harvest: `workers/dispatcher/harvest-6way-r1152_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4494         | 2.6046         | +0.1552 |
| ctrl_bpc best  | 2.3367         | 2.3313         | -0.0054 |

## Per-round trajectory (best bird: CozX3)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1153 | 6376 | 2.3313 | +0.2484 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1152_sym24`

## Output

`workers/dispatcher/harvest-5way-r1153_sym24/round-1153/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

