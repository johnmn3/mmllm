# harvest-3way-r1050 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1050 ctrl_bpc |
|--------|--------|--------------:|
| LPT3o | origin/claude/train-sym24-99b16257-LPT3o | 2.5156 |
| vyXuq | origin/claude/train-sym24-2f685f87-vyXuq | 2.8527 |
| 62RBc | fork-joly-os-mmllm-claude-train-sym24-06e31b8c-62RBc | 2.8646 |
| **mean** | | **2.7443** |
| **best** | | **2.5156** |

## Chain progression R1049 → R1050

Previous harvest: `workers/dispatcher/harvest-5way-r1049_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6423         | 2.7443         | +0.1020 |
| ctrl_bpc best  | 2.4705         | 2.5156         | +0.0451 |

## Per-round trajectory (best bird: LPT3o)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1050 | 3622 | 2.5156 | +0.2012 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1049_sym24`

## Output

`workers/dispatcher/harvest-3way-r1050_sym24/round-1050/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

