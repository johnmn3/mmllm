# harvest-1way-r119 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R119 ctrl_bpc |
|--------|--------|--------------:|
| oPEy9 | fork-SeniorCareMarket-mmllm-claude-train-sym24-ee620cf0-oPEy9 | 2.9943 |
| **mean** | | **2.9943** |
| **best** | | **2.9943** |

## Chain progression R118 → R119

Previous harvest: `workers/dispatcher/harvest-3way-r118_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8149         | 2.9943         | +0.1794 |
| ctrl_bpc best  | 2.6739         | 2.9943         | +0.3204 |

## Per-round trajectory (best bird: oPEy9)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 119 | 5680 | 2.9943 | +0.0321 |

## Cumulative training contribution

- This harvest: **50 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **310 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r118_sym24`

## Output

`workers/dispatcher/harvest-1way-r119_sym24/round-119/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

