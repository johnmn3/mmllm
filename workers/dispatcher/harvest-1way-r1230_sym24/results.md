# harvest-1way-r1230 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1230 ctrl_bpc |
|--------|--------|--------------:|
| smGRm | fork-joly-os-mmllm-claude-train-sym24-1f916a25-smGRm | 2.2561 |
| **mean** | | **2.2561** |
| **best** | | **2.2561** |

## Chain progression R1229 → R1230

Previous harvest: `workers/dispatcher/harvest-3way-r1229_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4008         | 2.2561         | -0.1447 |
| ctrl_bpc best  | 2.2552         | 2.2561         | +0.0009 |

## Per-round trajectory (best bird: smGRm)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1230 | 4371 | 2.2561 | +0.2482 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1229_sym24`

## Output

`workers/dispatcher/harvest-1way-r1230_sym24/round-1230/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

