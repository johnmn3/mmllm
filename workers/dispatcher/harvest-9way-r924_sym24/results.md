# harvest-9way-r924 — sparse-delta merge of 9 birds

## Worker endpoints

| handle | branch | R924 ctrl_bpc |
|--------|--------|--------------:|
| mfFQi | fork-SeniorCareMarket-mmllm-claude-train-sym24-d22da820-mfFQi | 2.7243 |
| pvjRf | fork-joly-os-mmllm-claude-train-sym24-7a30bddc-pvjRf | 2.7245 |
| 85Nio | fork-joly-os-mmllm-claude-train-sym24-340d3c81-85Nio | 2.7249 |
| oHgDJ | origin/claude/train-sym24-43cb21ec-oHgDJ | 2.7344 |
| ykXmM | origin/claude/train-sym24-99dda746-ykXmM | 2.7528 |
| Dai96 | fork-slaa-us-mmllm-claude-train-sym24-9b37cc57-Dai96 | 2.9114 |
| PtBWd | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-e9209a46-PtBWd | 2.9176 |
| cEbqv | fork-SeniorCareMarket-mmllm-claude-train-sym24-7269f4ec-cEbqv | 3.1199 |
| V5sEV | fork-joly-os-mmllm-claude-train-sym24-73b7c373-V5sEV | 3.1216 |
| **mean** | | **2.8590** |
| **best** | | **2.7243** |

## Chain progression R923 → R924

Previous harvest: `workers/dispatcher/harvest-6way-r923_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8025         | 2.8590         | +0.0565 |
| ctrl_bpc best  | 2.7273         | 2.7243         | -0.0030 |

## Per-round trajectory (best bird: mfFQi)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 924 | 6411 | 2.7243 | +0.2046 |

## Cumulative training contribution

- This harvest: **720 steps** from 9 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-10way-r923_sym24`
  - `workers/dispatcher/harvest-4way-r923_sym24`
  - `workers/dispatcher/harvest-6way-r923_sym24`

## Output

`workers/dispatcher/harvest-9way-r924_sym24/round-924/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 9 workers)
- `dense.pt` (averaged across 9 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

