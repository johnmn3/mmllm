# harvest-5way-r1156 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1156 ctrl_bpc |
|--------|--------|--------------:|
| S13a1 | fork-joly-os-mmllm-claude-train-sym24-d2846107-S13a1 | 2.3264 |
| HAhC0 | fork-SeniorCareMarket-mmllm-claude-train-sym24-6d977920-HAhC0 | 2.3290 |
| jao2H | origin/claude/train-sym24-675f6d3b-jao2H | 2.5216 |
| ipwc2 | fork-slaa-us-mmllm-claude-train-sym24-1ef14a3e-ipwc2 | 2.5248 |
| tiXAg | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-608463fc-tiXAg | 2.5283 |
| **mean** | | **2.4460** |
| **best** | | **2.3264** |

## Chain progression R1155 → R1156

Previous harvest: `workers/dispatcher/harvest-9way-r1155_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4764         | 2.4460         | -0.0304 |
| ctrl_bpc best  | 2.3277         | 2.3264         | -0.0013 |

## Per-round trajectory (best bird: S13a1)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1156 | 3574 | 2.3264 | +0.2583 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1155_sym24`

## Output

`workers/dispatcher/harvest-5way-r1156_sym24/round-1156/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

