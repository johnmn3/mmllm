# harvest-5way-r1273 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1273 ctrl_bpc |
|--------|--------|--------------:|
| T7Xqn | fork-SeniorCareMarket-mmllm-claude-train-sym24-4e9d338e-T7Xqn | 2.2268 |
| TF6PN | fork-joly-os-mmllm-claude-train-sym24-cbe3b6d4-TF6PN | 2.2360 |
| DcjCx | fork-slaa-us-mmllm-claude-train-sym24-1da0e46e-DcjCx | 2.4214 |
| VB25T | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-93f78597-VB25T | 2.4266 |
| bDAiI | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-0a83e767-bDAiI | 2.6244 |
| **mean** | | **2.3870** |
| **best** | | **2.2268** |

## Chain progression R1272 → R1273

Previous harvest: `workers/dispatcher/harvest-6way-r1272_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3680         | 2.3870         | +0.0190 |
| ctrl_bpc best  | 2.2399         | 2.2268         | -0.0131 |

## Per-round trajectory (best bird: T7Xqn)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1273 | 5377 | 2.2268 | +0.2513 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1272_sym24`
  - `workers/dispatcher/harvest-6way-r1272_sym24`

## Output

`workers/dispatcher/harvest-5way-r1273_sym24/round-1273/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

