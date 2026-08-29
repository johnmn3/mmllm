# harvest-3way-r1351 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1351 ctrl_bpc |
|--------|--------|--------------:|
| qRcLb | fork-joly-os-mmllm-claude-train-sym24-67ffacc3-qRcLb | 3.2310 |
| yd3g5 | origin/claude/train-sym24-e2a4536f-yd3g5 | 3.2597 |
| RONwX | origin/claude/train-sym24-0e2a25f6-RONwX | 3.3788 |
| **mean** | | **3.2898** |
| **best** | | **3.2310** |

## Chain progression R1350 → R1351

Previous harvest: `workers/dispatcher/harvest-3way-r1350_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4590         | 3.2898         | -0.1692 |
| ctrl_bpc best  | 3.3321         | 3.2310         | -0.1011 |

## Per-round trajectory (best bird: qRcLb)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1351 | 4405 | 3.2310 | +0.1279 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1350_sym24`
  - `workers/dispatcher/harvest-3way-r1350_sym24`

## Output

`workers/dispatcher/harvest-3way-r1351_sym24/round-1351/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

