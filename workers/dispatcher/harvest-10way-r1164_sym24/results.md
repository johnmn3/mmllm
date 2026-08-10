# harvest-10way-r1164 — sparse-delta merge of 10 birds

## Worker endpoints

| handle | branch | R1164 ctrl_bpc |
|--------|--------|--------------:|
| cdCUj | fork-slaa-us-mmllm-claude-train-sym24-5644727c-cdCUj | 2.3205 |
| iQ7C3 | fork-joly-os-mmllm-claude-train-sym24-bf2931d9-iQ7C3 | 2.3210 |
| eSocv | fork-SeniorCareMarket-mmllm-claude-train-sym24-f3fabbb1-eSocv | 2.3480 |
| HNNmh | fork-slaa-us-mmllm-claude-train-sym24-2eb0de6d-HNNmh | 2.5222 |
| YYkF7 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-73ae0b19-YYkF7 | 2.5228 |
| u5aHB | fork-SeniorCareMarket-mmllm-claude-train-sym24-369ab108-u5aHB | 2.5284 |
| aaqCl | origin/claude/train-sym24-7d3268d4-aaqCl | 2.7086 |
| OoaiN | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-97e42b5a-OoaiN | 2.7199 |
| G6V0o | origin/claude/train-sym24-d6bed8d0-G6V0o | 2.7448 |
| kDmiX | fork-joly-os-mmllm-claude-train-sym24-23b98dc4-kDmiX | 2.7462 |
| **mean** | | **2.5482** |
| **best** | | **2.3205** |

## Chain progression R1163 → R1164

Previous harvest: `workers/dispatcher/harvest-9way-r1163_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4841         | 2.5482         | +0.0641 |
| ctrl_bpc best  | 2.3178         | 2.3205         | +0.0027 |

## Per-round trajectory (best bird: cdCUj)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1164 | 6674 | 2.3205 | +0.2695 |

## Cumulative training contribution

- This harvest: **800 steps** from 10 bird(s)
- Across full ancestry (deduped by bird_id): **1520 steps** from 19 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-11way-r1163_sym24`
  - `workers/dispatcher/harvest-4way-r1163_sym24`
  - `workers/dispatcher/harvest-9way-r1163_sym24`

## Output

`workers/dispatcher/harvest-10way-r1164_sym24/round-1164/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 10 workers)
- `dense.pt` (averaged across 10 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

