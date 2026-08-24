# harvest-2way-r1300 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1300 ctrl_bpc |
|--------|--------|--------------:|
| dU71L | fork-slaa-us-mmllm-claude-train-sym24-88947bc8-dU71L | 3.8315 |
| DRdZB | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-ea128156-DRdZB | 4.0857 |
| **mean** | | **3.9586** |
| **best** | | **3.8315** |

## Chain progression R1299 → R1300

Previous harvest: `workers/dispatcher/harvest-11way-r1299_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.9120         | 3.9586         | +0.0466 |
| ctrl_bpc best  | 3.6474         | 3.8315         | +0.1841 |

## Per-round trajectory (best bird: dU71L)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1300 | 5255 | 3.8315 | +0.0527 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **1280 steps** from 16 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-8way-r1299_sym24`

## Output

`workers/dispatcher/harvest-2way-r1300_sym24/round-1300/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

