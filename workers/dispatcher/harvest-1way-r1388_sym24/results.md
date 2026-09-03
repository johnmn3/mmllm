# harvest-1way-r1388 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1388 ctrl_bpc |
|--------|--------|--------------:|
| 9YIXn | fork-joly-os-mmllm-claude-train-sym24-8895ef6e-9YIXn | 3.0661 |
| **mean** | | **3.0661** |
| **best** | | **3.0661** |

## Chain progression R1387 → R1388

Previous harvest: `workers/dispatcher/harvest-3way-r1387_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3342         | 3.0661         | -0.2681 |
| ctrl_bpc best  | 3.0837         | 3.0661         | -0.0176 |

## Per-round trajectory (best bird: 9YIXn)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1388 | 6582 | 3.0661 | +0.1180 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1387_sym24`

## Output

`workers/dispatcher/harvest-1way-r1388_sym24/round-1388/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

