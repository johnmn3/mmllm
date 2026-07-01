# harvest-1way-r819 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R819 ctrl_bpc |
|--------|--------|--------------:|
| WCqIk | fork-SeniorCareMarket-mmllm-claude-train-sym24-47072ca1-WCqIk | 3.0507 |
| **mean** | | **3.0507** |
| **best** | | **3.0507** |

## Chain progression R818 → R819

Previous harvest: `workers/dispatcher/harvest-14way-r818_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1541         | 3.0507         | -0.1034 |
| ctrl_bpc best  | 3.0316         | 3.0507         | +0.0191 |

## Per-round trajectory (best bird: WCqIk)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 819 | 6624 | 3.0507 | +0.4316 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r818_sym24`

## Output

`workers/dispatcher/harvest-1way-r819_sym24/round-819/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

