# harvest-3way-r1186 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1186 ctrl_bpc |
|--------|--------|--------------:|
| FcyST | fork-joly-os-mmllm-claude-train-sym24-e6e43de4-FcyST | 2.6815 |
| 0FaOb | fork-slaa-us-mmllm-claude-train-sym24-f3a63d24-0FaOb | 2.6951 |
| 1cEus | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-30bd1c91-1cEus | 2.6977 |
| **mean** | | **2.6914** |
| **best** | | **2.6815** |

## Chain progression R1185 → R1186

Previous harvest: `workers/dispatcher/harvest-10way-r1185_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4619         | 2.6914         | +0.2295 |
| ctrl_bpc best  | 2.2968         | 2.6815         | +0.3847 |

## Per-round trajectory (best bird: FcyST)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1186 | 6343 | 2.6815 | +0.2202 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1185_sym24`

## Output

`workers/dispatcher/harvest-3way-r1186_sym24/round-1186/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

