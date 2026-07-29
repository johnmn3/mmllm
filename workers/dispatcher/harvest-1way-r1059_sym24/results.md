# harvest-1way-r1059 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1059 ctrl_bpc |
|--------|--------|--------------:|
| 644dw | fork-joly-os-mmllm-claude-train-sym24-718689f2-644dw | 2.6515 |
| **mean** | | **2.6515** |
| **best** | | **2.6515** |

## Chain progression R1058 → R1059

Previous harvest: `workers/dispatcher/harvest-5way-r1058_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6276         | 2.6515         | +0.0239 |
| ctrl_bpc best  | 2.4905         | 2.6515         | +0.1610 |

## Per-round trajectory (best bird: 644dw)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1059 | 3802 | 2.6515 | +0.1896 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1058_sym24`

## Output

`workers/dispatcher/harvest-1way-r1059_sym24/round-1059/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

