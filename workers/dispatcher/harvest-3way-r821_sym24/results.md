# harvest-3way-r821 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R821 ctrl_bpc |
|--------|--------|--------------:|
| ejbhY | fork-slaa-us-mmllm-claude-train-sym24-f45b6ddb-ejbhY | 3.0212 |
| Cjf3O | origin/claude/train-sym24-ac09ea49-Cjf3O | 3.1762 |
| fncW9 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-9fc63b54-fncW9 | 3.4098 |
| **mean** | | **3.2024** |
| **best** | | **3.0212** |

## Chain progression R820 → R821

Previous harvest: `workers/dispatcher/harvest-7way-r820_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1216         | 3.2024         | +0.0808 |
| ctrl_bpc best  | 3.0266         | 3.0212         | -0.0054 |

## Per-round trajectory (best bird: ejbhY)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 821 | 6576 | 3.0212 | +0.5002 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r820_sym24`

## Output

`workers/dispatcher/harvest-3way-r821_sym24/round-821/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

