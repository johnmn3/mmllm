# harvest-4way-r873 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R873 ctrl_bpc |
|--------|--------|--------------:|
| 0fm4c | fork-SeniorCareMarket-mmllm-claude-train-sym24-5683ae8b-0fm4c | 2.8543 |
| aTfFl | fork-slaa-us-mmllm-claude-train-sym24-63049111-aTfFl | 2.8652 |
| YvyZm | origin/claude/train-sym24-6215feae-YvyZm | 2.8706 |
| r9O1J | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-633bf0c0-r9O1J | 3.2574 |
| **mean** | | **2.9619** |
| **best** | | **2.8543** |

## Chain progression R872 → R873

Previous harvest: `workers/dispatcher/harvest-10way-r872_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9612         | 2.9619         | +0.0007 |
| ctrl_bpc best  | 2.8667         | 2.8543         | -0.0124 |

## Per-round trajectory (best bird: 0fm4c)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 873 | 6608 | 2.8543 | +0.4190 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r872_sym24`
  - `workers/dispatcher/harvest-7way-r872_sym24`

## Output

`workers/dispatcher/harvest-4way-r873_sym24/round-873/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

