# harvest-3way-r932 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R932 ctrl_bpc |
|--------|--------|--------------:|
| p7CAa | origin/claude/train-sym24-9c7c2145-p7CAa | 2.7116 |
| Aa4t8 | origin/claude/train-sym24-772320ea-Aa4t8 | 2.7318 |
| Ry3xd | fork-joly-os-mmllm-claude-train-sym24-f83561ae-Ry3xd | 2.9020 |
| **mean** | | **2.7818** |
| **best** | | **2.7116** |

## Chain progression R931 → R932

Previous harvest: `workers/dispatcher/harvest-6way-r931_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9780         | 2.7818         | -0.1962 |
| ctrl_bpc best  | 2.6972         | 2.7116         | +0.0144 |

## Per-round trajectory (best bird: p7CAa)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 932 | 3668 | 2.7116 | +0.1854 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r931_sym24`

## Output

`workers/dispatcher/harvest-3way-r932_sym24/round-932/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

