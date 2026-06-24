# harvest-2way-r752 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R752 ctrl_bpc |
|--------|--------|--------------:|
| vnBBQ | fork-SeniorCareMarket-mmllm-claude-train-sym24-7ed29293-vnBBQ | 3.3561 |
| ROT33 | fork-joly-os-mmllm-claude-train-sym24-37c5bc88-ROT33 | 3.3599 |
| **mean** | | **3.3580** |
| **best** | | **3.3561** |

## Chain progression R751 → R752

Previous harvest: `workers/dispatcher/harvest-5way-r751_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4279         | 3.3580         | -0.0699 |
| ctrl_bpc best  | 3.3417         | 3.3561         | +0.0144 |

## Per-round trajectory (best bird: vnBBQ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 752 | 3732 | 3.3561 | +0.5232 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r751_sym24`

## Output

`workers/dispatcher/harvest-2way-r752_sym24/round-752/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

