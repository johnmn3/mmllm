# harvest-2way-r1094 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1094 ctrl_bpc |
|--------|--------|--------------:|
| NgZQa | origin/claude/train-sym24-87a68c48-NgZQa | 2.4224 |
| oOYiZ | fork-slaa-us-mmllm-claude-train-sym24-3886c770-oOYiZ | 2.8123 |
| **mean** | | **2.6174** |
| **best** | | **2.4224** |

## Chain progression R1093 → R1094

Previous harvest: `workers/dispatcher/harvest-8way-r1093_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6369         | 2.6174         | -0.0195 |
| ctrl_bpc best  | 2.4075         | 2.4224         | +0.0149 |

## Per-round trajectory (best bird: NgZQa)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1094 | 6505 | 2.4224 | +0.2358 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1093_sym24`
  - `workers/dispatcher/harvest-2way-r1093_sym24`

## Output

`workers/dispatcher/harvest-2way-r1094_sym24/round-1094/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

