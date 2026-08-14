# harvest-1way-r1207 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1207 ctrl_bpc |
|--------|--------|--------------:|
| qNAT8 | fork-SeniorCareMarket-mmllm-claude-train-sym24-a3b93331-qNAT8 | 2.4690 |
| **mean** | | **2.4690** |
| **best** | | **2.4690** |

## Chain progression R1206 → R1207

Previous harvest: `workers/dispatcher/harvest-10way-r1206_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4804         | 2.4690         | -0.0114 |
| ctrl_bpc best  | 2.2812         | 2.4690         | +0.1878 |

## Per-round trajectory (best bird: qNAT8)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1207 | 4265 | 2.4690 | +0.2264 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1206_sym24`

## Output

`workers/dispatcher/harvest-1way-r1207_sym24/round-1207/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

