# harvest-10way-r1138 — sparse-delta merge of 10 birds

## Worker endpoints

| handle | branch | R1138 ctrl_bpc |
|--------|--------|--------------:|
| ZMLM3 | origin/claude/train-sym24-f4e634c0-ZMLM3 | 2.3490 |
| 2RNto | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-78128f38-2RNto | 2.3612 |
| 8xeYj | fork-SeniorCareMarket-mmllm-claude-train-sym24-d75e38af-8xeYj | 2.3730 |
| 7fx1P | fork-slaa-us-mmllm-claude-train-sym24-4433f21d-7fx1P | 2.5430 |
| APlg2 | fork-joly-os-mmllm-claude-train-sym24-f0699e30-APlg2 | 2.5438 |
| AOTxY | fork-slaa-us-mmllm-claude-train-sym24-7abc044b-AOTxY | 2.5460 |
| qIxgz | fork-SeniorCareMarket-mmllm-claude-train-sym24-511f8e8b-qIxgz | 2.5478 |
| SGFpb | fork-slaa-us-mmllm-claude-train-sym24-9fc5a23e-SGFpb | 2.7417 |
| wl40s | fork-joly-os-mmllm-claude-train-sym24-51a5a8c2-wl40s | 2.7433 |
| wadj8 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f3bf050c-wadj8 | 2.7502 |
| **mean** | | **2.5499** |
| **best** | | **2.3490** |

## Chain progression R1137 → R1138

Previous harvest: `workers/dispatcher/harvest-9way-r1137_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4663         | 2.5499         | +0.0836 |
| ctrl_bpc best  | 2.3423         | 2.3490         | +0.0067 |

## Per-round trajectory (best bird: ZMLM3)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1138 | 3854 | 2.3490 | +0.2406 |

## Cumulative training contribution

- This harvest: **800 steps** from 10 bird(s)
- Across full ancestry (deduped by bird_id): **1520 steps** from 19 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-13way-r1137_sym24`
  - `workers/dispatcher/harvest-3way-r1137_sym24`
  - `workers/dispatcher/harvest-9way-r1137_sym24`

## Output

`workers/dispatcher/harvest-10way-r1138_sym24/round-1138/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 10 workers)
- `dense.pt` (averaged across 10 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

