# harvest-10way-r1051 — sparse-delta merge of 10 birds

## Worker endpoints

| handle | branch | R1051 ctrl_bpc |
|--------|--------|--------------:|
| 4zfx4 | fork-SeniorCareMarket-mmllm-claude-train-sym24-37fded23-4zfx4 | 2.4703 |
| AeUGu | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-39ba14a4-AeUGu | 2.4724 |
| iWm9k | fork-slaa-us-mmllm-claude-train-sym24-c61d5520-iWm9k | 2.4950 |
| qxbL3 | fork-slaa-us-mmllm-claude-train-sym24-1b5db6a4-qxbL3 | 2.4990 |
| 56r70 | fork-joly-os-mmllm-claude-train-sym24-bc705ce5-56r70 | 2.4993 |
| FVtPe | origin/claude/train-sym24-c6bd9906-FVtPe | 2.5270 |
| c9BFy | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-4c806ef5-c9BFy | 2.6583 |
| IOxYa | origin/claude/train-sym24-96d55aea-IOxYa | 2.6678 |
| cPf3U | fork-SeniorCareMarket-mmllm-claude-train-sym24-68db53f8-cPf3U | 2.7161 |
| QCD2n | origin/claude/train-sym24-77241469-QCD2n | 2.8577 |
| **mean** | | **2.5863** |
| **best** | | **2.4703** |

## Chain progression R1050 → R1051

Previous harvest: `workers/dispatcher/harvest-9way-r1050_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5764         | 2.5863         | +0.0099 |
| ctrl_bpc best  | 2.4684         | 2.4703         | +0.0019 |

## Per-round trajectory (best bird: 4zfx4)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1051 | 6420 | 2.4703 | +0.2104 |

## Cumulative training contribution

- This harvest: **800 steps** from 10 bird(s)
- Across full ancestry (deduped by bird_id): **1520 steps** from 19 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1050_sym24`
  - `workers/dispatcher/harvest-4way-r1050_sym24`
  - `workers/dispatcher/harvest-9way-r1050_sym24`

## Output

`workers/dispatcher/harvest-10way-r1051_sym24/round-1051/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 10 workers)
- `dense.pt` (averaged across 10 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

