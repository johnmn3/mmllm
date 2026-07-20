# harvest-2way-r972 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R972 ctrl_bpc |
|--------|--------|--------------:|
| ov3V8 | origin/claude/train-sym24-1b508a6c-ov3V8 | 2.6081 |
| myu8P | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-bc708d3e-myu8P | 2.8036 |
| **mean** | | **2.7058** |
| **best** | | **2.6081** |

## Chain progression R971 → R972

Previous harvest: `workers/dispatcher/harvest-2way-r971_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8342         | 2.7058         | -0.1284 |
| ctrl_bpc best  | 2.6572         | 2.6081         | -0.0491 |

## Per-round trajectory (best bird: ov3V8)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 972 | 4155 | 2.6081 | +0.1663 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r971_sym24`

## Output

`workers/dispatcher/harvest-2way-r972_sym24/round-972/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

