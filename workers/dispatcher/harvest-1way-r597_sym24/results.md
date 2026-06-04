# harvest-1way-r597 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R597 ctrl_bpc |
|--------|--------|--------------:|
| Ta7nG | fork-SeniorCareMarket-mmllm-claude-train-sym24-c8e462db-Ta7nG | 2.1379 |
| **mean** | | **2.1379** |
| **best** | | **2.1379** |

## Chain progression R140 → R597

Previous harvest: `workers/dispatcher/harvest-2way-merge-r140_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.0510         | 2.1379         | +0.0869 |
| ctrl_bpc best  | 1.8188         | 2.1379         | +0.3191 |

## Per-round trajectory (best bird: Ta7nG)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 597 | 4640 | 2.1379 | +0.0219 |

## Cumulative training contribution

- This harvest: **50 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **50 steps** from 1 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r596_sym24`

## Output

`workers/dispatcher/harvest-1way-r597_sym24/round-597/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

