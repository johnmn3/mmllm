# harvest-1way-r1046 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1046 ctrl_bpc |
|--------|--------|--------------:|
| Qiy9I | fork-slaa-us-mmllm-claude-train-sym24-ccc1772a-Qiy9I | 2.5146 |
| **mean** | | **2.5146** |
| **best** | | **2.5146** |

## Chain progression R1045 → R1046

Previous harvest: `workers/dispatcher/harvest-3way-r1045_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6812         | 2.5146         | -0.1666 |
| ctrl_bpc best  | 2.4859         | 2.5146         | +0.0287 |

## Per-round trajectory (best bird: Qiy9I)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1046 | 3676 | 2.5146 | +0.1899 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1045_sym24`

## Output

`workers/dispatcher/harvest-1way-r1046_sym24/round-1046/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

