# harvest-3way-r131 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R131 ctrl_bpc |
|--------|--------|--------------:|
| G4znm | fork-slaa-us-mmllm-claude-train-c3280437-G4znm | 1.0065 |
| 7Vo9E | origin/claude/train-75925d7e-7Vo9E | 1.0122 |
| 3arHo | fork-joly-os-mmllm-claude-train-e18f856c-3arHo | 1.0660 |
| **mean** | | **1.0282** |
| **best** | | **1.0065** |

## Chain progression R129 → R131

Previous harvest: `workers/dispatcher/harvest-3way-r129`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 1.5075         | 1.0282         | -0.4793 |
| ctrl_bpc best  | 1.3191         | 1.0065         | -0.3126 |

## Per-round trajectory (best bird: G4znm)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 127 | 612 | 0.9930 | +0.0022 |
| 128 | 566 | 0.9933 | +0.0081 |
| 129 | 549 | 0.9946 | +0.0112 |
| 130 | 562 | 0.9984 | +0.0067 |
| 131 | 569 | 1.0065 | +0.0103 |

## Cumulative training contribution

- This harvest: **105 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **3292 steps** from 88 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r126`

## Output

`workers/dispatcher/harvest-3way-r131/round-131/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

