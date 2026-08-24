# harvest-1way-r1302 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1302 ctrl_bpc |
|--------|--------|--------------:|
| rEk9j | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-a1a47c38-rEk9j | 3.5779 |
| **mean** | | **3.5779** |
| **best** | | **3.5779** |

## Chain progression R1301 → R1302

Previous harvest: `workers/dispatcher/harvest-4way-r1301_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.8760         | 3.5779         | -0.2981 |
| ctrl_bpc best  | 3.6795         | 3.5779         | -0.1016 |

## Per-round trajectory (best bird: rEk9j)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1302 | 3743 | 3.5779 | +0.0770 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1301_sym24`

## Output

`workers/dispatcher/harvest-1way-r1302_sym24/round-1302/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

