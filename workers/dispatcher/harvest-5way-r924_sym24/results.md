# harvest-5way-r924 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R924 ctrl_bpc |
|--------|--------|--------------:|
| mfFQi | fork-SeniorCareMarket-mmllm-claude-train-sym24-d22da820-mfFQi | 2.7243 |
| pvjRf | fork-joly-os-mmllm-claude-train-sym24-7a30bddc-pvjRf | 2.7245 |
| oHgDJ | origin/claude/train-sym24-43cb21ec-oHgDJ | 2.7344 |
| Dai96 | fork-slaa-us-mmllm-claude-train-sym24-9b37cc57-Dai96 | 2.9114 |
| PtBWd | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-e9209a46-PtBWd | 2.9176 |
| **mean** | | **2.8024** |
| **best** | | **2.7243** |

## Chain progression R923 → R924

Previous harvest: `workers/dispatcher/harvest-10way-r923_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8345         | 2.8024         | -0.0321 |
| ctrl_bpc best  | 2.7231         | 2.7243         | +0.0012 |

## Per-round trajectory (best bird: mfFQi)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 924 | 6411 | 2.7243 | +0.2046 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r923_sym24`
  - `workers/dispatcher/harvest-6way-r923_sym24`

## Output

`workers/dispatcher/harvest-5way-r924_sym24/round-924/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

