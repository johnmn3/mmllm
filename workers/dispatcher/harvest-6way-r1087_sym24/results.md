# harvest-6way-r1087 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1087 ctrl_bpc |
|--------|--------|--------------:|
| emEAE | fork-joly-os-mmllm-claude-train-sym24-1a2a3433-emEAE | 2.4332 |
| 4uDyO | fork-slaa-us-mmllm-claude-train-sym24-310fb220-4uDyO | 2.4601 |
| Z6rMp | fork-SeniorCareMarket-mmllm-claude-train-sym24-e960cf8b-Z6rMp | 2.8096 |
| nzYmw | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-5e3410b8-nzYmw | 2.8127 |
| JpHP9 | origin/claude/train-sym24-7fe6fc40-JpHP9 | 2.8158 |
| wFJUH | origin/claude/train-sym24-c8db0d49-wFJUH | 2.8244 |
| **mean** | | **2.6926** |
| **best** | | **2.4332** |

## Chain progression R1086 → R1087

Previous harvest: `workers/dispatcher/harvest-5way-r1086_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6184         | 2.6926         | +0.0742 |
| ctrl_bpc best  | 2.4134         | 2.4332         | +0.0198 |

## Per-round trajectory (best bird: emEAE)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1087 | 4345 | 2.4332 | +0.2345 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1086_sym24`

## Output

`workers/dispatcher/harvest-6way-r1087_sym24/round-1087/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

