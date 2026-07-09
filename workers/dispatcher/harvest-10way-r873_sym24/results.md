# harvest-10way-r873 — sparse-delta merge of 10 birds

## Worker endpoints

| handle | branch | R873 ctrl_bpc |
|--------|--------|--------------:|
| 0fm4c | fork-SeniorCareMarket-mmllm-claude-train-sym24-5683ae8b-0fm4c | 2.8543 |
| aTfFl | fork-slaa-us-mmllm-claude-train-sym24-63049111-aTfFl | 2.8652 |
| a3TiL | fork-joly-os-mmllm-claude-train-sym24-79ef53de-a3TiL | 2.8656 |
| mOGBv | origin/claude/train-sym24-08cbfc8a-mOGBv | 2.8663 |
| YvyZm | origin/claude/train-sym24-6215feae-YvyZm | 2.8706 |
| rpCrT | fork-joly-os-mmllm-claude-train-sym24-3eebb3d6-rpCrT | 2.8993 |
| Ulg82 | fork-SeniorCareMarket-mmllm-claude-train-sym24-1b6d3980-Ulg82 | 3.0322 |
| kgbrD | origin/claude/train-sym24-9cc6cb70-kgbrD | 3.2277 |
| r9O1J | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-633bf0c0-r9O1J | 3.2574 |
| 9k499 | fork-slaa-us-mmllm-claude-train-sym24-f16c7b42-9k499 | 3.2627 |
| **mean** | | **3.0001** |
| **best** | | **2.8543** |

## Chain progression R872 → R873

Previous harvest: `workers/dispatcher/harvest-7way-r872_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9267         | 3.0001         | +0.0734 |
| ctrl_bpc best  | 2.8674         | 2.8543         | -0.0131 |

## Per-round trajectory (best bird: 0fm4c)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 873 | 6608 | 2.8543 | +0.4190 |

## Cumulative training contribution

- This harvest: **800 steps** from 10 bird(s)
- Across full ancestry (deduped by bird_id): **1360 steps** from 17 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-10way-r872_sym24`
  - `workers/dispatcher/harvest-4way-r872_sym24`
  - `workers/dispatcher/harvest-7way-r872_sym24`

## Output

`workers/dispatcher/harvest-10way-r873_sym24/round-873/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 10 workers)
- `dense.pt` (averaged across 10 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

