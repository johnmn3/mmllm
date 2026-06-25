# harvest-3way-r763 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R763 ctrl_bpc |
|--------|--------|--------------:|
| LFWVD | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-0fdb0521-LFWVD | 3.2594 |
| eMpnd | fork-SeniorCareMarket-mmllm-claude-train-sym24-6d08d4b0-eMpnd | 3.2759 |
| YjXwE | origin/claude/train-sym24-5e602fab-YjXwE | 3.6502 |
| **mean** | | **3.3952** |
| **best** | | **3.2594** |

## Chain progression R762 → R763

Previous harvest: `workers/dispatcher/harvest-1way-r762_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3235         | 3.3952         | +0.0717 |
| ctrl_bpc best  | 3.3235         | 3.2594         | -0.0641 |

## Per-round trajectory (best bird: LFWVD)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 763 | 5379 | 3.2594 | +0.5712 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r762_sym24`

## Output

`workers/dispatcher/harvest-3way-r763_sym24/round-763/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

