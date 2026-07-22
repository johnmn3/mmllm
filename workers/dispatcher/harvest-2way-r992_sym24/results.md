# harvest-2way-r992 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R992 ctrl_bpc |
|--------|--------|--------------:|
| XErcm | origin/claude/train-sym24-b53716b0-XErcm | 2.9621 |
| ootUu | fork-SeniorCareMarket-mmllm-claude-train-sym24-e6d77aa1-ootUu | 2.9705 |
| **mean** | | **2.9663** |
| **best** | | **2.9621** |

## Chain progression R991 → R992

Previous harvest: `workers/dispatcher/harvest-5way-r991_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7361         | 2.9663         | +0.2302 |
| ctrl_bpc best  | 2.5847         | 2.9621         | +0.3774 |

## Per-round trajectory (best bird: XErcm)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 992 | 6596 | 2.9621 | +0.1827 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r991_sym24`

## Output

`workers/dispatcher/harvest-2way-r992_sym24/round-992/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

