# harvest-4way-r694 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R694 ctrl_bpc |
|--------|--------|--------------:|
| X1x6S | fork-joly-os-mmllm-claude-train-sym24-2b9a6b6c-X1x6S | 3.6410 |
| c6E6Z | fork-SeniorCareMarket-mmllm-claude-train-sym24-d54d25c2-c6E6Z | 3.6923 |
| YksPK | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-623e23eb-YksPK | 3.7093 |
| B2P9b | fork-davidwuchn-mmllm-claude-train-sym24-b1f7ace9-B2P9b | 4.0141 |
| **mean** | | **3.7642** |
| **best** | | **3.6410** |

## Chain progression R693 → R694

Previous harvest: `workers/dispatcher/harvest-7way-r693_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.8245         | 3.7642         | -0.0603 |
| ctrl_bpc best  | 3.6493         | 3.6410         | -0.0083 |

## Per-round trajectory (best bird: X1x6S)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 694 | 6534 | 3.6410 | +0.4953 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r693_sym24`

## Output

`workers/dispatcher/harvest-4way-r694_sym24/round-694/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

