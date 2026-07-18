# harvest-5way-r953 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R953 ctrl_bpc |
|--------|--------|--------------:|
| GzSrB | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-5789e527-GzSrB | 2.6462 |
| ldgwT | origin/claude/train-sym24-ea2a6a8e-ldgwT | 2.6674 |
| JSL5U | fork-slaa-us-mmllm-claude-train-sym24-203cbebf-JSL5U | 2.8524 |
| cSgFs | fork-joly-os-mmllm-claude-train-sym24-ffb40b6a-cSgFs | 3.0430 |
| gzkOd | fork-SeniorCareMarket-mmllm-claude-train-sym24-8a6cd278-gzkOd | 3.0491 |
| **mean** | | **2.8516** |
| **best** | | **2.6462** |

## Chain progression R952 → R953

Previous harvest: `workers/dispatcher/harvest-4way-r952_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8001         | 2.8516         | +0.0515 |
| ctrl_bpc best  | 2.6406         | 2.6462         | +0.0056 |

## Per-round trajectory (best bird: GzSrB)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 953 | 5324 | 2.6462 | +0.1886 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r952_sym24`
  - `workers/dispatcher/harvest-4way-r952_sym24`

## Output

`workers/dispatcher/harvest-5way-r953_sym24/round-953/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

