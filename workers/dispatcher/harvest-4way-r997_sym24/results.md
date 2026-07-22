# harvest-4way-r997 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R997 ctrl_bpc |
|--------|--------|--------------:|
| W0YDV | fork-slaa-us-mmllm-claude-train-sym24-a2d20c52-W0YDV | 2.5719 |
| SY0dB | origin/claude/train-sym24-3082e917-SY0dB | 2.5780 |
| m5dkO | fork-joly-os-mmllm-claude-train-sym24-beda557d-m5dkO | 2.5885 |
| fhcnf | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-430cb3fd-fhcnf | 2.9637 |
| **mean** | | **2.6755** |
| **best** | | **2.5719** |

## Chain progression R996 → R997

Previous harvest: `workers/dispatcher/harvest-7way-r996_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7601         | 2.6755         | -0.0846 |
| ctrl_bpc best  | 2.5694         | 2.5719         | +0.0025 |

## Per-round trajectory (best bird: W0YDV)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 997 | 6476 | 2.5719 | +0.1714 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r996_sym24`

## Output

`workers/dispatcher/harvest-4way-r997_sym24/round-997/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

