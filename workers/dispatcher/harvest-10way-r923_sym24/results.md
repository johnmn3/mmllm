# harvest-10way-r923 — sparse-delta merge of 10 birds

## Worker endpoints

| handle | branch | R923 ctrl_bpc |
|--------|--------|--------------:|
| DEzkB | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-e5418cda-DEzkB | 2.7231 |
| poIa8 | fork-slaa-us-mmllm-claude-train-sym24-f92932cf-poIa8 | 2.7273 |
| iTKnD | origin/claude/train-sym24-813c4c03-iTKnD | 2.7310 |
| A6Bu4 | fork-slaa-us-mmllm-claude-train-sym24-105d9747-A6Bu4 | 2.7337 |
| cpxPL | fork-joly-os-mmllm-claude-train-sym24-f60af7c7-cpxPL | 2.7374 |
| lGYQX | fork-slaa-us-mmllm-claude-train-sym24-2a6f5468-lGYQX | 2.7654 |
| VmKDL | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-14ee569e-VmKDL | 2.9211 |
| llThW | origin/claude/train-sym24-3a5b772a-llThW | 2.9247 |
| SumL7 | fork-SeniorCareMarket-mmllm-claude-train-sym24-5c203306-SumL7 | 2.9330 |
| Ucufk | fork-joly-os-mmllm-claude-train-sym24-859b98c5-Ucufk | 3.1488 |
| **mean** | | **2.8345** |
| **best** | | **2.7231** |

## Chain progression R922 → R923

Previous harvest: `workers/dispatcher/harvest-9way-r922_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8278         | 2.8345         | +0.0067 |
| ctrl_bpc best  | 2.7258         | 2.7231         | -0.0027 |

## Per-round trajectory (best bird: DEzkB)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 923 | 6337 | 2.7231 | +0.1761 |

## Cumulative training contribution

- This harvest: **800 steps** from 10 bird(s)
- Across full ancestry (deduped by bird_id): **1520 steps** from 19 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r922_sym24`
  - `workers/dispatcher/harvest-7way-r922_sym24`
  - `workers/dispatcher/harvest-9way-r922_sym24`

## Output

`workers/dispatcher/harvest-10way-r923_sym24/round-923/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 10 workers)
- `dense.pt` (averaged across 10 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

