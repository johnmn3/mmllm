# harvest-4way-r939 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R939 ctrl_bpc |
|--------|--------|--------------:|
| qaR9W | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-c7f7de14-qaR9W | 2.6913 |
| LqEwK | fork-joly-os-mmllm-claude-train-sym24-380234b6-LqEwK | 2.7029 |
| ItzUA | origin/claude/train-sym24-93bbf36e-ItzUA | 2.7120 |
| MtNL5 | fork-SeniorCareMarket-mmllm-claude-train-sym24-533cd722-MtNL5 | 3.1029 |
| **mean** | | **2.8023** |
| **best** | | **2.6913** |

## Chain progression R938 → R939

Previous harvest: `workers/dispatcher/harvest-9way-r938_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7765         | 2.8023         | +0.0258 |
| ctrl_bpc best  | 2.6748         | 2.6913         | +0.0165 |

## Per-round trajectory (best bird: qaR9W)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 939 | 6377 | 2.6913 | +0.1863 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r938_sym24`

## Output

`workers/dispatcher/harvest-4way-r939_sym24/round-939/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

