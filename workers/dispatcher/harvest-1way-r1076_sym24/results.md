# harvest-1way-r1076 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1076 ctrl_bpc |
|--------|--------|--------------:|
| avNbf | fork-slaa-us-mmllm-claude-train-sym24-1e487d48-avNbf | 2.4669 |
| **mean** | | **2.4669** |
| **best** | | **2.4669** |

## Chain progression R1075 → R1076

Previous harvest: `workers/dispatcher/harvest-9way-r1075_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5905         | 2.4669         | -0.1236 |
| ctrl_bpc best  | 2.4375         | 2.4669         | +0.0294 |

## Per-round trajectory (best bird: avNbf)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1076 | 6539 | 2.4669 | +0.2228 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1075_sym24`

## Output

`workers/dispatcher/harvest-1way-r1076_sym24/round-1076/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

