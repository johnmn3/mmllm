# harvest-1way-r737 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R737 ctrl_bpc |
|--------|--------|--------------:|
| X50ga | fork-slaa-us-mmllm-claude-train-sym24-68ee43ab-X50ga | 3.4074 |
| **mean** | | **3.4074** |
| **best** | | **3.4074** |

## Chain progression R736 → R737

Previous harvest: `workers/dispatcher/harvest-2way-r736_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4356         | 3.4074         | -0.0282 |
| ctrl_bpc best  | 3.4352         | 3.4074         | -0.0278 |

## Per-round trajectory (best bird: X50ga)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 737 | 6594 | 3.4074 | +0.7295 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r736_sym24`

## Output

`workers/dispatcher/harvest-1way-r737_sym24/round-737/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

