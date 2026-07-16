# harvest-3way-r939 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R939 ctrl_bpc |
|--------|--------|--------------:|
| LqEwK | fork-joly-os-mmllm-claude-train-sym24-380234b6-LqEwK | 2.7029 |
| ItzUA | origin/claude/train-sym24-93bbf36e-ItzUA | 2.7120 |
| MtNL5 | fork-SeniorCareMarket-mmllm-claude-train-sym24-533cd722-MtNL5 | 3.1029 |
| **mean** | | **2.8393** |
| **best** | | **2.7029** |

## Chain progression R938 → R939

Previous harvest: `workers/dispatcher/harvest-9way-r938_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7765         | 2.8393         | +0.0628 |
| ctrl_bpc best  | 2.6748         | 2.7029         | +0.0281 |

## Per-round trajectory (best bird: LqEwK)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 939 | 6343 | 2.7029 | +0.1842 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r938_sym24`

## Output

`workers/dispatcher/harvest-3way-r939_sym24/round-939/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

