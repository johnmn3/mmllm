# harvest-9way-r723 — sparse-delta merge of 9 birds

## Worker endpoints

| handle | branch | R723 ctrl_bpc |
|--------|--------|--------------:|
| vfj1y | fork-slaa-us-mmllm-claude-train-sym24-c0bd1ab2-vfj1y | 3.5068 |
| 9qZhY | fork-davidwuchn-mmllm-claude-train-sym24-3033060d-9qZhY | 3.5171 |
| 25Vll | origin/claude/train-sym24-6d63e9e2-25Vll | 3.5186 |
| SpqYL | fork-joly-os-mmllm-claude-train-sym24-93eca705-SpqYL | 3.5255 |
| st83c | fork-joly-os-mmllm-claude-train-sym24-403cfcd1-st83c | 3.5260 |
| JLpa3 | fork-davidwuchn-mmllm-claude-train-sym24-d29187df-JLpa3 | 3.5287 |
| 64iFi | fork-slaa-us-mmllm-claude-train-sym24-659ecfa3-64iFi | 3.5295 |
| BN8gd | fork-SeniorCareMarket-mmllm-claude-train-sym24-f778eb72-BN8gd | 3.5350 |
| xiThP | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-68f45cea-xiThP | 3.8380 |
| **mean** | | **3.5584** |
| **best** | | **3.5068** |

## Chain progression R722 → R723

Previous harvest: `workers/dispatcher/harvest-6way-r722_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.6277         | 3.5584         | -0.0693 |
| ctrl_bpc best  | 3.4965         | 3.5068         | +0.0103 |

## Per-round trajectory (best bird: vfj1y)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 723 | 6529 | 3.5068 | +0.5737 |

## Cumulative training contribution

- This harvest: **720 steps** from 9 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r722_sym24`
  - `workers/dispatcher/harvest-6way-r722_sym24`

## Output

`workers/dispatcher/harvest-9way-r723_sym24/round-723/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 9 workers)
- `dense.pt` (averaged across 9 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

