# harvest-1way-r997 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R997 ctrl_bpc |
|--------|--------|--------------:|
| m5dkO | fork-joly-os-mmllm-claude-train-sym24-beda557d-m5dkO | 2.5885 |
| **mean** | | **2.5885** |
| **best** | | **2.5885** |

## Chain progression R996 → R997

Previous harvest: `workers/dispatcher/harvest-7way-r996_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7601         | 2.5885         | -0.1716 |
| ctrl_bpc best  | 2.5694         | 2.5885         | +0.0191 |

## Per-round trajectory (best bird: m5dkO)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 997 | 3998 | 2.5885 | +0.1807 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r996_sym24`

## Output

`workers/dispatcher/harvest-1way-r997_sym24/round-997/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

