# harvest-2way-r1127 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1127 ctrl_bpc |
|--------|--------|--------------:|
| p3nmr | origin/claude/train-sym24-f5eaadf9-p3nmr | 2.3704 |
| qw28Q | fork-joly-os-mmllm-claude-train-sym24-943a6369-qw28Q | 2.7532 |
| **mean** | | **2.5618** |
| **best** | | **2.3704** |

## Chain progression R1126 → R1127

Previous harvest: `workers/dispatcher/harvest-6way-r1126_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4762         | 2.5618         | +0.0856 |
| ctrl_bpc best  | 2.3597         | 2.3704         | +0.0107 |

## Per-round trajectory (best bird: p3nmr)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1127 | 5312 | 2.3704 | +0.2437 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1126_sym24`

## Output

`workers/dispatcher/harvest-2way-r1127_sym24/round-1127/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

