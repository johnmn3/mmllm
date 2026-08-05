# harvest-8way-r1120 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R1120 ctrl_bpc |
|--------|--------|--------------:|
| AvrnV | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-c890c963-AvrnV | 2.3612 |
| 4wwll | origin/claude/train-sym24-89482fe2-4wwll | 2.3655 |
| HY8Hf | fork-joly-os-mmllm-claude-train-sym24-6a318c60-HY8Hf | 2.3704 |
| gUl8U | origin/claude/train-sym24-316881fa-gUl8U | 2.3795 |
| yQ5lc | fork-slaa-us-mmllm-claude-train-sym24-328f6969-yQ5lc | 2.3890 |
| VLuU2 | origin/claude/train-sym24-d693a509-VLuU2 | 2.5780 |
| q31ct | fork-SeniorCareMarket-mmllm-claude-train-sym24-4d825625-q31ct | 2.7609 |
| aQCUd | fork-joly-os-mmllm-claude-train-sym24-f8b8a21c-aQCUd | 2.7671 |
| **mean** | | **2.4964** |
| **best** | | **2.3612** |

## Chain progression R1119 → R1120

Previous harvest: `workers/dispatcher/harvest-6way-r1119_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5387         | 2.4964         | -0.0423 |
| ctrl_bpc best  | 2.3615         | 2.3612         | -0.0003 |

## Per-round trajectory (best bird: AvrnV)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1120 | 6411 | 2.3612 | +0.2467 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1119_sym24`
  - `workers/dispatcher/harvest-5way-r1119_sym24`
  - `workers/dispatcher/harvest-6way-r1119_sym24`

## Output

`workers/dispatcher/harvest-8way-r1120_sym24/round-1120/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

