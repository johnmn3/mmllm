# harvest-3way-r1006 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1006 ctrl_bpc |
|--------|--------|--------------:|
| ugwfn | fork-joly-os-mmllm-claude-train-sym24-ce9ad9ac-ugwfn | 2.5637 |
| Q3vQX | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-2b2dfb8a-Q3vQX | 2.7571 |
| 1wb0v | fork-SeniorCareMarket-mmllm-claude-train-sym24-0a193354-1wb0v | 2.9267 |
| **mean** | | **2.7492** |
| **best** | | **2.5637** |

## Chain progression R1005 → R1006

Previous harvest: `workers/dispatcher/harvest-9way-r1005_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7793         | 2.7492         | -0.0301 |
| ctrl_bpc best  | 2.5466         | 2.5637         | +0.0171 |

## Per-round trajectory (best bird: ugwfn)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1006 | 6380 | 2.5637 | +0.1557 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1005_sym24`
  - `workers/dispatcher/harvest-5way-r1005_sym24`

## Output

`workers/dispatcher/harvest-3way-r1006_sym24/round-1006/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

