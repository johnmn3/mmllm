# harvest-12way-r694 — sparse-delta merge of 12 birds

## Worker endpoints

| handle | branch | R694 ctrl_bpc |
|--------|--------|--------------:|
| X1x6S | fork-joly-os-mmllm-claude-train-sym24-2b9a6b6c-X1x6S | 3.6410 |
| cShzn | fork-slaa-us-mmllm-claude-train-sym24-bf2b8440-cShzn | 3.6597 |
| c6E6Z | fork-SeniorCareMarket-mmllm-claude-train-sym24-d54d25c2-c6E6Z | 3.6923 |
| uPGgl | origin/claude/train-sym24-44ffd86b-uPGgl | 3.7077 |
| YksPK | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-623e23eb-YksPK | 3.7093 |
| ZShzI | fork-slaa-us-mmllm-claude-train-sym24-8ca85a75-ZShzI | 3.7122 |
| 8QqdO | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-dd6c41a0-8QqdO | 3.9887 |
| g3of2 | fork-joly-os-mmllm-claude-train-sym24-61567999-g3of2 | 4.0003 |
| B2P9b | fork-davidwuchn-mmllm-claude-train-sym24-b1f7ace9-B2P9b | 4.0141 |
| 66VDE | origin/claude/train-sym24-4ef49643-66VDE | 4.0146 |
| bZre9 | fork-joly-os-mmllm-claude-train-sym24-8b13ad8c-bZre9 | 4.0220 |
| ZDJFu | fork-davidwuchn-mmllm-claude-train-sym24-7eb8118a-ZDJFu | 4.0336 |
| **mean** | | **3.8496** |
| **best** | | **3.6410** |

## Chain progression R693 → R694

Previous harvest: `workers/dispatcher/harvest-7way-r693_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.8245         | 3.8496         | +0.0251 |
| ctrl_bpc best  | 3.6493         | 3.6410         | -0.0083 |

## Per-round trajectory (best bird: X1x6S)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 694 | 6534 | 3.6410 | +0.4953 |

## Cumulative training contribution

- This harvest: **960 steps** from 12 bird(s)
- Across full ancestry (deduped by bird_id): **1520 steps** from 19 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r693_sym24`
  - `workers/dispatcher/harvest-4way-r693_sym24`
  - `workers/dispatcher/harvest-7way-r693_sym24`

## Output

`workers/dispatcher/harvest-12way-r694_sym24/round-694/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 12 workers)
- `dense.pt` (averaged across 12 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

