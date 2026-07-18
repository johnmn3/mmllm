# harvest-5way-r959 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R959 ctrl_bpc |
|--------|--------|--------------:|
| HyyCm | fork-joly-os-mmllm-claude-train-sym24-4bc0f81d-HyyCm | 2.6484 |
| 7isKs | fork-slaa-us-mmllm-claude-train-sym24-05dad6cf-7isKs | 2.6486 |
| QKCRp | fork-SeniorCareMarket-mmllm-claude-train-sym24-cbfb81db-QKCRp | 2.6522 |
| ZfoW9 | origin/claude/train-sym24-8c4f4ac8-ZfoW9 | 2.8385 |
| 5Zk0K | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-0837e308-5Zk0K | 2.8412 |
| **mean** | | **2.7258** |
| **best** | | **2.6484** |

## Chain progression R958 → R959

Previous harvest: `workers/dispatcher/harvest-9way-r958_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7706         | 2.7258         | -0.0448 |
| ctrl_bpc best  | 2.6279         | 2.6484         | +0.0205 |

## Per-round trajectory (best bird: HyyCm)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 959 | 6569 | 2.6484 | +0.1630 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r958_sym24`

## Output

`workers/dispatcher/harvest-5way-r959_sym24/round-959/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

