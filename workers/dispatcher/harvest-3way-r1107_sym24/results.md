# harvest-3way-r1107 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1107 ctrl_bpc |
|--------|--------|--------------:|
| ncpse | origin/claude/train-sym24-49924bc7-ncpse | 2.4036 |
| Np3Y1 | fork-joly-os-mmllm-claude-train-sym24-567adb8c-Np3Y1 | 2.4148 |
| Mpnqw | origin/claude/train-sym24-54d66ea7-Mpnqw | 2.5818 |
| **mean** | | **2.4667** |
| **best** | | **2.4036** |

## Chain progression R1106 → R1107

Previous harvest: `workers/dispatcher/harvest-6way-r1106_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5318         | 2.4667         | -0.0651 |
| ctrl_bpc best  | 2.3908         | 2.4036         | +0.0128 |

## Per-round trajectory (best bird: ncpse)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1107 | 3665 | 2.4036 | +0.2343 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1106_sym24`

## Output

`workers/dispatcher/harvest-3way-r1107_sym24/round-1107/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

