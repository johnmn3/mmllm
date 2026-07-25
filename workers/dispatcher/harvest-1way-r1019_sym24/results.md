# harvest-1way-r1019 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1019 ctrl_bpc |
|--------|--------|--------------:|
| agP7i | origin/claude/train-sym24-2e1bbfbf-agP7i | 2.9228 |
| **mean** | | **2.9228** |
| **best** | | **2.9228** |

## Chain progression R1018 → R1019

Previous harvest: `workers/dispatcher/harvest-5way-r1018_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8012         | 2.9228         | +0.1216 |
| ctrl_bpc best  | 2.5171         | 2.9228         | +0.4057 |

## Per-round trajectory (best bird: agP7i)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1019 | 4293 | 2.9228 | +0.1670 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1018_sym24`

## Output

`workers/dispatcher/harvest-1way-r1019_sym24/round-1019/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

