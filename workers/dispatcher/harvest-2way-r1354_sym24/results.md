# harvest-2way-r1354 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1354 ctrl_bpc |
|--------|--------|--------------:|
| O1XkF | origin/claude/train-sym24-f7bfae52-O1XkF | 3.2913 |
| IrpcJ | fork-slaa-us-mmllm-claude-train-sym24-629204d0-IrpcJ | 3.3057 |
| **mean** | | **3.2985** |
| **best** | | **3.2913** |

## Chain progression R1353 → R1354

Previous harvest: `workers/dispatcher/harvest-4way-r1353_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3781         | 3.2985         | -0.0796 |
| ctrl_bpc best  | 3.2853         | 3.2913         | +0.0060 |

## Per-round trajectory (best bird: O1XkF)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1354 | 3494 | 3.2913 | +0.0791 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1353_sym24`

## Output

`workers/dispatcher/harvest-2way-r1354_sym24/round-1354/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

