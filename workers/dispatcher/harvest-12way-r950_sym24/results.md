# harvest-12way-r950 — sparse-delta merge of 12 birds

## Worker endpoints

| handle | branch | R950 ctrl_bpc |
|--------|--------|--------------:|
| 2f7cy | origin/claude/train-sym24-3e52ea41-2f7cy | 2.6494 |
| cxweM | fork-slaa-us-mmllm-claude-train-sym24-2c2ed241-cxweM | 2.6525 |
| mE3G0 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-ed1fba05-mE3G0 | 2.6540 |
| zuNUH | origin/claude/train-sym24-49a7a545-zuNUH | 2.6679 |
| P9b5B | origin/claude/train-sym24-0497a3fc-P9b5B | 2.6855 |
| 7PH1r | fork-slaa-us-mmllm-claude-train-sym24-370cc769-7PH1r | 2.8497 |
| LR2wv | fork-SeniorCareMarket-mmllm-claude-train-sym24-9c609b8d-LR2wv | 2.8566 |
| yBRGO | fork-joly-os-mmllm-claude-train-sym24-608e2785-yBRGO | 2.8577 |
| ebSEb | fork-SeniorCareMarket-mmllm-claude-train-sym24-4db357d1-ebSEb | 3.0545 |
| FkmKu | fork-joly-os-mmllm-claude-train-sym24-2bf11c68-FkmKu | 3.0555 |
| Ku054 | fork-joly-os-mmllm-claude-train-sym24-4f2e2144-Ku054 | 3.0574 |
| 8EerH | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f81bf191-8EerH | 3.0982 |
| **mean** | | **2.8449** |
| **best** | | **2.6494** |

## Chain progression R949 → R950

Previous harvest: `workers/dispatcher/harvest-9way-r949_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8252         | 2.8449         | +0.0197 |
| ctrl_bpc best  | 2.6610         | 2.6494         | -0.0116 |

## Per-round trajectory (best bird: 2f7cy)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 950 | 4356 | 2.6494 | +0.2072 |

## Cumulative training contribution

- This harvest: **960 steps** from 12 bird(s)
- Across full ancestry (deduped by bird_id): **1680 steps** from 21 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r949_sym24`
  - `workers/dispatcher/harvest-7way-r949_sym24`
  - `workers/dispatcher/harvest-9way-r949_sym24`

## Output

`workers/dispatcher/harvest-12way-r950_sym24/round-950/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 12 workers)
- `dense.pt` (averaged across 12 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

