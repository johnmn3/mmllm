# harvest-1way-r1235 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1235 ctrl_bpc |
|--------|--------|--------------:|
| WX2WX | fork-slaa-us-mmllm-claude-train-sym24-f792b0eb-WX2WX | 2.2685 |
| **mean** | | **2.2685** |
| **best** | | **2.2685** |

## Chain progression R1234 → R1235

Previous harvest: `workers/dispatcher/harvest-10way-r1234_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4217         | 2.2685         | -0.1532 |
| ctrl_bpc best  | 2.2531         | 2.2685         | +0.0154 |

## Per-round trajectory (best bird: WX2WX)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1235 | 3609 | 2.2685 | +0.2473 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-7way-r1234_sym24`

## Output

`workers/dispatcher/harvest-1way-r1235_sym24/round-1235/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

