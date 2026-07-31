# harvest-1way-r1071 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1071 ctrl_bpc |
|--------|--------|--------------:|
| TRRx3 | origin/claude/train-sym24-f5998394-TRRx3 | 2.4404 |
| **mean** | | **2.4404** |
| **best** | | **2.4404** |

## Chain progression R1070 → R1071

Previous harvest: `workers/dispatcher/harvest-7way-r1070_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5612         | 2.4404         | -0.1208 |
| ctrl_bpc best  | 2.4377         | 2.4404         | +0.0027 |

## Per-round trajectory (best bird: TRRx3)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1071 | 6567 | 2.4404 | +0.2302 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1070_sym24`

## Output

`workers/dispatcher/harvest-1way-r1071_sym24/round-1071/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

