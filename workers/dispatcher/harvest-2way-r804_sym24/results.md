# harvest-2way-r804 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R804 ctrl_bpc |
|--------|--------|--------------:|
| MUUaW | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-9c27e081-MUUaW | 3.4606 |
| t5a55 | fork-slaa-us-mmllm-claude-train-sym24-9cf9dcb0-t5a55 | 3.4636 |
| **mean** | | **3.4621** |
| **best** | | **3.4606** |

## Chain progression R803 → R804

Previous harvest: `workers/dispatcher/harvest-11way-r803_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2338         | 3.4621         | +0.2283 |
| ctrl_bpc best  | 3.0874         | 3.4606         | +0.3732 |

## Per-round trajectory (best bird: MUUaW)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 804 | 6325 | 3.4606 | +0.6603 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-6way-r803_sym24`

## Output

`workers/dispatcher/harvest-2way-r804_sym24/round-804/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

