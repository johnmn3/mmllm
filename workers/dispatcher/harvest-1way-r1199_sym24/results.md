# harvest-1way-r1199 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1199 ctrl_bpc |
|--------|--------|--------------:|
| Ky72m | fork-slaa-us-mmllm-claude-train-sym24-c208a083-Ky72m | 2.6862 |
| **mean** | | **2.6862** |
| **best** | | **2.6862** |

## Chain progression R1198 → R1199

Previous harvest: `workers/dispatcher/harvest-3way-r1198_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4804         | 2.6862         | +0.2058 |
| ctrl_bpc best  | 2.2824         | 2.6862         | +0.4038 |

## Per-round trajectory (best bird: Ky72m)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1199 | 3806 | 2.6862 | +0.2414 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1198_sym24`

## Output

`workers/dispatcher/harvest-1way-r1199_sym24/round-1199/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

