# harvest-2way-r1059 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1059 ctrl_bpc |
|--------|--------|--------------:|
| T97sO | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-fa0195a8-T97sO | 2.4928 |
| 644dw | fork-joly-os-mmllm-claude-train-sym24-718689f2-644dw | 2.6515 |
| **mean** | | **2.5721** |
| **best** | | **2.4928** |

## Chain progression R1058 → R1059

Previous harvest: `workers/dispatcher/harvest-5way-r1058_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6276         | 2.5721         | -0.0555 |
| ctrl_bpc best  | 2.4905         | 2.4928         | +0.0023 |

## Per-round trajectory (best bird: T97sO)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1059 | 6424 | 2.4928 | +0.2222 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1058_sym24`

## Output

`workers/dispatcher/harvest-2way-r1059_sym24/round-1059/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

