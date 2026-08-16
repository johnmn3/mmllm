# harvest-4way-r1224 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1224 ctrl_bpc |
|--------|--------|--------------:|
| Xx2KL | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-560b051d-Xx2KL | 2.2800 |
| uUkVQ | fork-joly-os-mmllm-claude-train-sym24-aee7c9c8-uUkVQ | 2.4749 |
| Odj7d | fork-slaa-us-mmllm-claude-train-sym24-27e26fd6-Odj7d | 2.4754 |
| HV75w | fork-SeniorCareMarket-mmllm-claude-train-sym24-691b9fe1-HV75w | 2.6747 |
| **mean** | | **2.4762** |
| **best** | | **2.2800** |

## Chain progression R1223 → R1224

Previous harvest: `workers/dispatcher/harvest-11way-r1223_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3413         | 2.4762         | +0.1349 |
| ctrl_bpc best  | 2.2555         | 2.2800         | +0.0245 |

## Per-round trajectory (best bird: Xx2KL)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1224 | 5339 | 2.2800 | +0.2414 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1223_sym24`

## Output

`workers/dispatcher/harvest-4way-r1224_sym24/round-1224/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

