# harvest-5way-r1198 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1198 ctrl_bpc |
|--------|--------|--------------:|
| xfI6t | fork-joly-os-mmllm-claude-train-sym24-04ae9e5d-xfI6t | 2.4742 |
| vXV5r | fork-SeniorCareMarket-mmllm-claude-train-sym24-2980ad7e-vXV5r | 2.4846 |
| 1Ko41 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-91ba2503-1Ko41 | 2.4923 |
| IGEa4 | fork-joly-os-mmllm-claude-train-sym24-19859b39-IGEa4 | 2.6743 |
| 5FVAZ | fork-slaa-us-mmllm-claude-train-sym24-8bb96957-5FVAZ | 2.6809 |
| **mean** | | **2.5613** |
| **best** | | **2.4742** |

## Chain progression R1197 → R1198

Previous harvest: `workers/dispatcher/harvest-6way-r1197_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3324         | 2.5613         | +0.2289 |
| ctrl_bpc best  | 2.2859         | 2.4742         | +0.1883 |

## Per-round trajectory (best bird: xfI6t)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1198 | 6513 | 2.4742 | +0.2292 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1197_sym24`
  - `workers/dispatcher/harvest-6way-r1197_sym24`

## Output

`workers/dispatcher/harvest-5way-r1198_sym24/round-1198/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

