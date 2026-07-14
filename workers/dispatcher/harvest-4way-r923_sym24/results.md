# harvest-4way-r923 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R923 ctrl_bpc |
|--------|--------|--------------:|
| poIa8 | fork-slaa-us-mmllm-claude-train-sym24-f92932cf-poIa8 | 2.7273 |
| iTKnD | origin/claude/train-sym24-813c4c03-iTKnD | 2.7310 |
| cpxPL | fork-joly-os-mmllm-claude-train-sym24-f60af7c7-cpxPL | 2.7374 |
| VmKDL | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-14ee569e-VmKDL | 2.9211 |
| **mean** | | **2.7792** |
| **best** | | **2.7273** |

## Chain progression R922 → R923

Previous harvest: `workers/dispatcher/harvest-9way-r922_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8278         | 2.7792         | -0.0486 |
| ctrl_bpc best  | 2.7258         | 2.7273         | +0.0015 |

## Per-round trajectory (best bird: poIa8)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 923 | 6674 | 2.7273 | +0.2971 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r922_sym24`

## Output

`workers/dispatcher/harvest-4way-r923_sym24/round-923/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

