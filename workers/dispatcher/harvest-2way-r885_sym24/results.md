# harvest-2way-r885 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R885 ctrl_bpc |
|--------|--------|--------------:|
| lFYLD | fork-joly-os-mmllm-claude-train-sym24-9fd16e6b-lFYLD | 2.8407 |
| gEUdP | origin/claude/train-sym24-7a0dc233-gEUdP | 3.2072 |
| **mean** | | **3.0240** |
| **best** | | **2.8407** |

## Chain progression R884 → R885

Previous harvest: `workers/dispatcher/harvest-4way-r884_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9773         | 3.0240         | +0.0467 |
| ctrl_bpc best  | 2.8253         | 2.8407         | +0.0154 |

## Per-round trajectory (best bird: lFYLD)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 885 | 6464 | 2.8407 | +0.3989 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r884_sym24`

## Output

`workers/dispatcher/harvest-2way-r885_sym24/round-885/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

