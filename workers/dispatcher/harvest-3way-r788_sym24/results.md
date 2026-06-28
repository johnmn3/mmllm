# harvest-3way-r788 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R788 ctrl_bpc |
|--------|--------|--------------:|
| Xr9zT | fork-davidwuchn-mmllm-claude-train-sym24-3cc6337a-Xr9zT | 3.1429 |
| knGc6 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-3330d8ad-knGc6 | 3.2874 |
| dtu37 | fork-slaa-us-mmllm-claude-train-sym24-1a51f8b9-dtu37 | 3.5585 |
| **mean** | | **3.3296** |
| **best** | | **3.1429** |

## Chain progression R787 → R788

Previous harvest: `workers/dispatcher/harvest-8way-r787_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2599         | 3.3296         | +0.0697 |
| ctrl_bpc best  | 3.1477         | 3.1429         | -0.0048 |

## Per-round trajectory (best bird: Xr9zT)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 788 | 4264 | 3.1429 | +0.4503 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r787_sym24`

## Output

`workers/dispatcher/harvest-3way-r788_sym24/round-788/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

