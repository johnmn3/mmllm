# harvest-1way-r1278 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1278 ctrl_bpc |
|--------|--------|--------------:|
| gKZzR | fork-SeniorCareMarket-mmllm-claude-train-sym24-63289deb-gKZzR | 2.4188 |
| **mean** | | **2.4188** |
| **best** | | **2.4188** |

## Chain progression R1277 → R1278

Previous harvest: `workers/dispatcher/harvest-5way-r1277_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3075         | 2.4188         | +0.1113 |
| ctrl_bpc best  | 2.2215         | 2.4188         | +0.1973 |

## Per-round trajectory (best bird: gKZzR)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1278 | 4406 | 2.4188 | +0.2209 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1277_sym24`

## Output

`workers/dispatcher/harvest-1way-r1278_sym24/round-1278/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

