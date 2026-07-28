# harvest-2way-r1046 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1046 ctrl_bpc |
|--------|--------|--------------:|
| Qiy9I | fork-slaa-us-mmllm-claude-train-sym24-ccc1772a-Qiy9I | 2.5146 |
| CAFH4 | origin/claude/train-sym24-ab0b394e-CAFH4 | 2.8774 |
| **mean** | | **2.6960** |
| **best** | | **2.5146** |

## Chain progression R1045 → R1046

Previous harvest: `workers/dispatcher/harvest-3way-r1045_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6812         | 2.6960         | +0.0148 |
| ctrl_bpc best  | 2.4859         | 2.5146         | +0.0287 |

## Per-round trajectory (best bird: Qiy9I)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1046 | 3676 | 2.5146 | +0.1899 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1045_sym24`

## Output

`workers/dispatcher/harvest-2way-r1046_sym24/round-1046/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

