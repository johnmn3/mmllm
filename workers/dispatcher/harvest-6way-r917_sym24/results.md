# harvest-6way-r917 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R917 ctrl_bpc |
|--------|--------|--------------:|
| y0tlJ | origin/claude/train-sym24-6b6d7f39-y0tlJ | 2.7562 |
| sNcdp | fork-joly-os-mmllm-claude-train-sym24-df31c128-sNcdp | 2.9365 |
| C4FVc | fork-SeniorCareMarket-mmllm-claude-train-sym24-cf20b34a-C4FVc | 2.9478 |
| FtscD | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-fa5e57f9-FtscD | 3.1346 |
| BZwy3 | origin/claude/train-sym24-cce05d1b-BZwy3 | 3.1643 |
| nYqKW | fork-slaa-us-mmllm-claude-train-sym24-0d9f32c9-nYqKW | 3.1662 |
| **mean** | | **3.0176** |
| **best** | | **2.7562** |

## Chain progression R916 → R917

Previous harvest: `workers/dispatcher/harvest-4way-r916_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7574         | 3.0176         | +0.2602 |
| ctrl_bpc best  | 2.7383         | 2.7562         | +0.0179 |

## Per-round trajectory (best bird: y0tlJ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 917 | 5318 | 2.7562 | +0.1919 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r916_sym24`
  - `workers/dispatcher/harvest-4way-r916_sym24`

## Output

`workers/dispatcher/harvest-6way-r917_sym24/round-917/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

