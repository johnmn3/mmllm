# harvest-2way-r1003 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1003 ctrl_bpc |
|--------|--------|--------------:|
| iipfp | origin/claude/train-sym24-4c8e9a70-iipfp | 2.5769 |
| FNq3S | origin/claude/train-sym24-64435894-FNq3S | 2.7494 |
| **mean** | | **2.6631** |
| **best** | | **2.5769** |

## Chain progression R1002 → R1003

Previous harvest: `workers/dispatcher/harvest-5way-r1002_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7112         | 2.6631         | -0.0480 |
| ctrl_bpc best  | 2.5607         | 2.5769         | +0.0162 |

## Per-round trajectory (best bird: iipfp)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1003 | 6245 | 2.5769 | +0.1621 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1002_sym24`

## Output

`workers/dispatcher/harvest-2way-r1003_sym24/round-1003/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

