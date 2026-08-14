# harvest-7way-r1202 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R1202 ctrl_bpc |
|--------|--------|--------------:|
| iY8Xg | fork-joly-os-mmllm-claude-train-sym24-ea02950c-iY8Xg | 2.2838 |
| ZoNGQ | origin/claude/train-sym24-f3286320-ZoNGQ | 2.3042 |
| ukCld | fork-joly-os-mmllm-claude-train-sym24-68e4e9df-ukCld | 2.4708 |
| BLJt4 | fork-SeniorCareMarket-mmllm-claude-train-sym24-e5d83120-BLJt4 | 2.4878 |
| kdPrH | origin/claude/train-sym24-29995637-kdPrH | 2.6569 |
| 2SKhO | fork-slaa-us-mmllm-claude-train-sym24-1f25f0ad-2SKhO | 2.6662 |
| ZkkXk | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-eb309324-ZkkXk | 2.6704 |
| **mean** | | **2.5057** |
| **best** | | **2.2838** |

## Chain progression R1201 → R1202

Previous harvest: `workers/dispatcher/harvest-5way-r1201_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4151         | 2.5057         | +0.0906 |
| ctrl_bpc best  | 2.2929         | 2.2838         | -0.0091 |

## Per-round trajectory (best bird: iY8Xg)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1202 | 3804 | 2.2838 | +0.2541 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1201_sym24`
  - `workers/dispatcher/harvest-5way-r1201_sym24`

## Output

`workers/dispatcher/harvest-7way-r1202_sym24/round-1202/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

