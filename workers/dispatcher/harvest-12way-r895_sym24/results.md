# harvest-12way-r895 — sparse-delta merge of 12 birds

## Worker endpoints

| handle | branch | R895 ctrl_bpc |
|--------|--------|--------------:|
| CkUny | fork-slaa-us-mmllm-claude-train-sym24-2d9b1a59-CkUny | 2.7892 |
| zj2Xw | fork-SeniorCareMarket-mmllm-claude-train-sym24-60059e94-zj2Xw | 2.7954 |
| hIAos | origin/claude/train-sym24-42fb0319-hIAos | 2.7996 |
| bCpwB | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-708e5e3e-bCpwB | 2.8007 |
| GfSwd | fork-joly-os-mmllm-claude-train-sym24-7373c4a0-GfSwd | 2.8069 |
| hpHnL | fork-slaa-us-mmllm-claude-train-sym24-b4e28985-hpHnL | 2.8090 |
| qrtlP | fork-SeniorCareMarket-mmllm-claude-train-sym24-d9ec5edc-qrtlP | 2.8260 |
| RJFxF | fork-slaa-us-mmllm-claude-train-sym24-7ec813dd-RJFxF | 2.9766 |
| XRv9t | origin/claude/train-sym24-0ec67822-XRv9t | 3.1775 |
| FFWXL | origin/claude/train-sym24-d2a55728-FFWXL | 3.1806 |
| JyQIo | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f83ada77-JyQIo | 3.2007 |
| OSZ1r | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-65d88fa7-OSZ1r | 3.2052 |
| **mean** | | **2.9473** |
| **best** | | **2.7892** |

## Chain progression R894 → R895

Previous harvest: `workers/dispatcher/harvest-7way-r894_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0263         | 2.9473         | -0.0790 |
| ctrl_bpc best  | 2.8022         | 2.7892         | -0.0130 |

## Per-round trajectory (best bird: CkUny)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 895 | 6516 | 2.7892 | +0.3051 |

## Cumulative training contribution

- This harvest: **960 steps** from 12 bird(s)
- Across full ancestry (deduped by bird_id): **1520 steps** from 19 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r894_sym24`
  - `workers/dispatcher/harvest-3way-r894_sym24`
  - `workers/dispatcher/harvest-7way-r894_sym24`

## Output

`workers/dispatcher/harvest-12way-r895_sym24/round-895/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 12 workers)
- `dense.pt` (averaged across 12 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

