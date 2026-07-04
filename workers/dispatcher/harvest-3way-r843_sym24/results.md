# harvest-3way-r843 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R843 ctrl_bpc |
|--------|--------|--------------:|
| kdHhZ | origin/claude/train-sym24-8bbf904e-kdHhZ | 2.9531 |
| Zox0C | fork-slaa-us-mmllm-claude-train-sym24-07e7cba8-Zox0C | 2.9565 |
| c5kwI | fork-joly-os-mmllm-claude-train-sym24-559ee5fd-c5kwI | 3.0968 |
| **mean** | | **3.0021** |
| **best** | | **2.9531** |

## Chain progression R842 → R843

Previous harvest: `workers/dispatcher/harvest-6way-r842_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0500         | 3.0021         | -0.0479 |
| ctrl_bpc best  | 2.9529         | 2.9531         | +0.0002 |

## Per-round trajectory (best bird: kdHhZ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 843 | 6581 | 2.9531 | +0.3324 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r842_sym24`

## Output

`workers/dispatcher/harvest-3way-r843_sym24/round-843/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

