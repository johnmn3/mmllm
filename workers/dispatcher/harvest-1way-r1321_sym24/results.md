# harvest-1way-r1321 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1321 ctrl_bpc |
|--------|--------|--------------:|
| eq39R | fork-SeniorCareMarket-mmllm-claude-train-sym24-024e2a72-eq39R | 3.4590 |
| **mean** | | **3.4590** |
| **best** | | **3.4590** |

## Chain progression R1320 → R1321

Previous harvest: `workers/dispatcher/harvest-3way-r1320_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4815         | 3.4590         | -0.0225 |
| ctrl_bpc best  | 3.4712         | 3.4590         | -0.0122 |

## Per-round trajectory (best bird: eq39R)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1321 | 4399 | 3.4590 | +0.0547 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1320_sym24`

## Output

`workers/dispatcher/harvest-1way-r1321_sym24/round-1321/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

