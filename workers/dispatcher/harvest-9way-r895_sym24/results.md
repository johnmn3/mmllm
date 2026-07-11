# harvest-9way-r895 — sparse-delta merge of 9 birds

## Worker endpoints

| handle | branch | R895 ctrl_bpc |
|--------|--------|--------------:|
| zj2Xw | fork-SeniorCareMarket-mmllm-claude-train-sym24-60059e94-zj2Xw | 2.7954 |
| hIAos | origin/claude/train-sym24-42fb0319-hIAos | 2.7996 |
| bCpwB | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-708e5e3e-bCpwB | 2.8007 |
| GfSwd | fork-joly-os-mmllm-claude-train-sym24-7373c4a0-GfSwd | 2.8069 |
| hpHnL | fork-slaa-us-mmllm-claude-train-sym24-b4e28985-hpHnL | 2.8090 |
| qrtlP | fork-SeniorCareMarket-mmllm-claude-train-sym24-d9ec5edc-qrtlP | 2.8260 |
| RJFxF | fork-slaa-us-mmllm-claude-train-sym24-7ec813dd-RJFxF | 2.9766 |
| FFWXL | origin/claude/train-sym24-d2a55728-FFWXL | 3.1806 |
| JyQIo | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f83ada77-JyQIo | 3.2007 |
| **mean** | | **2.9106** |
| **best** | | **2.7954** |

## Chain progression R894 → R895

Previous harvest: `workers/dispatcher/harvest-7way-r894_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0263         | 2.9106         | -0.1157 |
| ctrl_bpc best  | 2.8022         | 2.7954         | -0.0068 |

## Per-round trajectory (best bird: zj2Xw)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 895 | 6594 | 2.7954 | +0.2475 |

## Cumulative training contribution

- This harvest: **720 steps** from 9 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r894_sym24`
  - `workers/dispatcher/harvest-3way-r894_sym24`

## Output

`workers/dispatcher/harvest-9way-r895_sym24/round-895/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 9 workers)
- `dense.pt` (averaged across 9 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

