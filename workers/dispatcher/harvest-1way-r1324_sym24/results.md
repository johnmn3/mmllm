# harvest-1way-r1324 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1324 ctrl_bpc |
|--------|--------|--------------:|
| s5m4E | fork-joly-os-mmllm-claude-train-sym24-a67a49ae-s5m4E | 3.3336 |
| **mean** | | **3.3336** |
| **best** | | **3.3336** |

## Chain progression R1323 → R1324

Previous harvest: `workers/dispatcher/harvest-10way-r1323_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5739         | 3.3336         | -0.2403 |
| ctrl_bpc best  | 3.3853         | 3.3336         | -0.0517 |

## Per-round trajectory (best bird: s5m4E)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1324 | 4463 | 3.3336 | +0.0837 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r1323_sym24`

## Output

`workers/dispatcher/harvest-1way-r1324_sym24/round-1324/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

