# harvest-1way-r1189 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1189 ctrl_bpc |
|--------|--------|--------------:|
| Z2Yc0 | fork-slaa-us-mmllm-claude-train-sym24-774274c5-Z2Yc0 | 2.4955 |
| **mean** | | **2.4955** |
| **best** | | **2.4955** |

## Chain progression R1188 → R1189

Previous harvest: `workers/dispatcher/harvest-7way-r1188_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4722         | 2.4955         | +0.0233 |
| ctrl_bpc best  | 2.3127         | 2.4955         | +0.1828 |

## Per-round trajectory (best bird: Z2Yc0)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1189 | 6519 | 2.4955 | +0.2220 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1188_sym24`

## Output

`workers/dispatcher/harvest-1way-r1189_sym24/round-1189/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

