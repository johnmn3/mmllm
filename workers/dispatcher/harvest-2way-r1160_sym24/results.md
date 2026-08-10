# harvest-2way-r1160 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1160 ctrl_bpc |
|--------|--------|--------------:|
| qRR7W | fork-joly-os-mmllm-claude-train-sym24-c1c9f348-qRR7W | 2.3301 |
| O0cqt | origin/claude/train-sym24-8f3b1fbd-O0cqt | 2.3558 |
| **mean** | | **2.3430** |
| **best** | | **2.3301** |

## Chain progression R1159 → R1160

Previous harvest: `workers/dispatcher/harvest-5way-r1159_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5272         | 2.3430         | -0.1843 |
| ctrl_bpc best  | 2.3548         | 2.3301         | -0.0247 |

## Per-round trajectory (best bird: qRR7W)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1160 | 6708 | 2.3301 | +0.2598 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1159_sym24`

## Output

`workers/dispatcher/harvest-2way-r1160_sym24/round-1160/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

