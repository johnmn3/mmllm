# harvest-4way-r835 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R835 ctrl_bpc |
|--------|--------|--------------:|
| PwgiV | fork-slaa-us-mmllm-claude-train-sym24-6d1cb36e-PwgiV | 2.9673 |
| F8tZE | origin/claude/train-sym24-7b3bbbc9-F8tZE | 2.9677 |
| DLFNW | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-a32eecec-DLFNW | 3.1187 |
| 8ORy8 | fork-SeniorCareMarket-mmllm-claude-train-sym24-f528161c-8ORy8 | 3.4139 |
| **mean** | | **3.1169** |
| **best** | | **2.9673** |

## Chain progression R834 → R835

Previous harvest: `workers/dispatcher/harvest-4way-r834_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2146         | 3.1169         | -0.0977 |
| ctrl_bpc best  | 2.9712         | 2.9673         | -0.0039 |

## Per-round trajectory (best bird: PwgiV)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 835 | 6561 | 2.9673 | +0.4474 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r834_sym24`

## Output

`workers/dispatcher/harvest-4way-r835_sym24/round-835/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

