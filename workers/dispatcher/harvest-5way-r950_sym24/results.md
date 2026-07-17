# harvest-5way-r950 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R950 ctrl_bpc |
|--------|--------|--------------:|
| 2f7cy | origin/claude/train-sym24-3e52ea41-2f7cy | 2.6494 |
| cxweM | fork-slaa-us-mmllm-claude-train-sym24-2c2ed241-cxweM | 2.6525 |
| LR2wv | fork-SeniorCareMarket-mmllm-claude-train-sym24-9c609b8d-LR2wv | 2.8566 |
| yBRGO | fork-joly-os-mmllm-claude-train-sym24-608e2785-yBRGO | 2.8577 |
| 8EerH | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f81bf191-8EerH | 3.0982 |
| **mean** | | **2.8229** |
| **best** | | **2.6494** |

## Chain progression R949 → R950

Previous harvest: `workers/dispatcher/harvest-9way-r949_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8252         | 2.8229         | -0.0023 |
| ctrl_bpc best  | 2.6610         | 2.6494         | -0.0116 |

## Per-round trajectory (best bird: 2f7cy)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 950 | 4356 | 2.6494 | +0.2072 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r949_sym24`
  - `workers/dispatcher/harvest-7way-r949_sym24`

## Output

`workers/dispatcher/harvest-5way-r950_sym24/round-950/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

