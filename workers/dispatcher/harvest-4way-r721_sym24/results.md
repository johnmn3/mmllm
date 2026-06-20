# harvest-4way-r721 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R721 ctrl_bpc |
|--------|--------|--------------:|
| V4Y1o | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-190b2d74-V4Y1o | 3.5276 |
| EesRO | fork-joly-os-mmllm-claude-train-sym24-3718657d-EesRO | 3.5311 |
| aX9E7 | origin/claude/train-sym24-5e43dabe-aX9E7 | 3.8299 |
| M7VUV | fork-slaa-us-mmllm-claude-train-sym24-80964fc8-M7VUV | 3.8523 |
| **mean** | | **3.6852** |
| **best** | | **3.5276** |

## Chain progression R720 → R721

Previous harvest: `workers/dispatcher/harvest-1way-r720_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5431         | 3.6852         | +0.1421 |
| ctrl_bpc best  | 3.5431         | 3.5276         | -0.0155 |

## Per-round trajectory (best bird: V4Y1o)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 721 | 6340 | 3.5276 | +0.6702 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r720_sym24`

## Output

`workers/dispatcher/harvest-4way-r721_sym24/round-721/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

