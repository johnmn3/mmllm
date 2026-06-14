# harvest-2way-r674 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R674 ctrl_bpc |
|--------|--------|--------------:|
| j7lgy | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-54a90b4e-j7lgy | 3.8302 |
| iZNxX | origin/claude/train-sym24-94d17e23-iZNxX | 3.8449 |
| **mean** | | **3.8376** |
| **best** | | **3.8302** |

## Chain progression R673 → R674

Previous harvest: `workers/dispatcher/harvest-13way-r673_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.9039         | 3.8376         | -0.0663 |
| ctrl_bpc best  | 3.8499         | 3.8302         | -0.0197 |

## Per-round trajectory (best bird: j7lgy)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 674 | 5340 | 3.8302 | +0.4391 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r673_sym24`

## Output

`workers/dispatcher/harvest-2way-r674_sym24/round-674/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

