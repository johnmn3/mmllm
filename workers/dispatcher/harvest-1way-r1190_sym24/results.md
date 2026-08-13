# harvest-1way-r1190 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1190 ctrl_bpc |
|--------|--------|--------------:|
| Gvy41 | fork-slaa-us-mmllm-claude-train-sym24-c5534148-Gvy41 | 2.2908 |
| **mean** | | **2.2908** |
| **best** | | **2.2908** |

## Chain progression R1189 → R1190

Previous harvest: `workers/dispatcher/harvest-4way-r1189_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5480         | 2.2908         | -0.2572 |
| ctrl_bpc best  | 2.3203         | 2.2908         | -0.0295 |

## Per-round trajectory (best bird: Gvy41)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1190 | 4434 | 2.2908 | +0.2548 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1189_sym24`

## Output

`workers/dispatcher/harvest-1way-r1190_sym24/round-1190/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

