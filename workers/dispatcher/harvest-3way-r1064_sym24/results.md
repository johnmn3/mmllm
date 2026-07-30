# harvest-3way-r1064 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1064 ctrl_bpc |
|--------|--------|--------------:|
| cg170 | fork-slaa-us-mmllm-claude-train-sym24-63196804-cg170 | 2.6413 |
| HzChl | fork-joly-os-mmllm-claude-train-sym24-e6948c62-HzChl | 2.8376 |
| TFoyL | origin/claude/train-sym24-608f5cd5-TFoyL | 2.8477 |
| **mean** | | **2.7755** |
| **best** | | **2.6413** |

## Chain progression R1063 → R1064

Previous harvest: `workers/dispatcher/harvest-2way-r1063_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5640         | 2.7755         | +0.2115 |
| ctrl_bpc best  | 2.4839         | 2.6413         | +0.1574 |

## Per-round trajectory (best bird: cg170)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1064 | 6718 | 2.6413 | +0.1891 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1063_sym24`

## Output

`workers/dispatcher/harvest-3way-r1064_sym24/round-1064/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

