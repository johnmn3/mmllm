# harvest-6way-r923 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R923 ctrl_bpc |
|--------|--------|--------------:|
| poIa8 | fork-slaa-us-mmllm-claude-train-sym24-f92932cf-poIa8 | 2.7273 |
| iTKnD | origin/claude/train-sym24-813c4c03-iTKnD | 2.7310 |
| cpxPL | fork-joly-os-mmllm-claude-train-sym24-f60af7c7-cpxPL | 2.7374 |
| lGYQX | fork-slaa-us-mmllm-claude-train-sym24-2a6f5468-lGYQX | 2.7654 |
| VmKDL | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-14ee569e-VmKDL | 2.9211 |
| SumL7 | fork-SeniorCareMarket-mmllm-claude-train-sym24-5c203306-SumL7 | 2.9330 |
| **mean** | | **2.8025** |
| **best** | | **2.7273** |

## Chain progression R922 → R923

Previous harvest: `workers/dispatcher/harvest-9way-r922_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8278         | 2.8025         | -0.0253 |
| ctrl_bpc best  | 2.7258         | 2.7273         | +0.0015 |

## Per-round trajectory (best bird: poIa8)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 923 | 6674 | 2.7273 | +0.2971 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r922_sym24`
  - `workers/dispatcher/harvest-7way-r922_sym24`

## Output

`workers/dispatcher/harvest-6way-r923_sym24/round-923/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

