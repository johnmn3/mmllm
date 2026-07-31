# harvest-9way-r1075 — sparse-delta merge of 9 birds

## Worker endpoints

| handle | branch | R1075 ctrl_bpc |
|--------|--------|--------------:|
| C8a4F | origin/claude/train-sym24-6e00d056-C8a4F | 2.4375 |
| Qkvlt | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-affe6237-Qkvlt | 2.4447 |
| MnalW | fork-slaa-us-mmllm-claude-train-sym24-ed31f53c-MnalW | 2.4499 |
| r34Ir | origin/claude/train-sym24-2e9b9087-r34Ir | 2.4622 |
| MP04r | fork-joly-os-mmllm-claude-train-sym24-3dcedfc7-MP04r | 2.6133 |
| d2mW3 | fork-joly-os-mmllm-claude-train-sym24-a14c9ed5-d2mW3 | 2.6236 |
| ae5RQ | fork-SeniorCareMarket-mmllm-claude-train-sym24-502958d3-ae5RQ | 2.6254 |
| 0nAc7 | origin/claude/train-sym24-c2bdaa3d-0nAc7 | 2.8289 |
| kpX94 | origin/claude/train-sym24-c4031c4f-kpX94 | 2.8291 |
| **mean** | | **2.5905** |
| **best** | | **2.4375** |

## Chain progression R1074 → R1075

Previous harvest: `workers/dispatcher/harvest-5way-r1074_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6498         | 2.5905         | -0.0593 |
| ctrl_bpc best  | 2.4634         | 2.4375         | -0.0259 |

## Per-round trajectory (best bird: C8a4F)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1075 | 6382 | 2.4375 | +0.2217 |

## Cumulative training contribution

- This harvest: **720 steps** from 9 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1074_sym24`
  - `workers/dispatcher/harvest-4way-r1074_sym24`
  - `workers/dispatcher/harvest-5way-r1074_sym24`

## Output

`workers/dispatcher/harvest-9way-r1075_sym24/round-1075/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 9 workers)
- `dense.pt` (averaged across 9 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

