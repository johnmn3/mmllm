# harvest-3way-r1273 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1273 ctrl_bpc |
|--------|--------|--------------:|
| TF6PN | fork-joly-os-mmllm-claude-train-sym24-cbe3b6d4-TF6PN | 2.2360 |
| DcjCx | fork-slaa-us-mmllm-claude-train-sym24-1da0e46e-DcjCx | 2.4214 |
| VB25T | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-93f78597-VB25T | 2.4266 |
| **mean** | | **2.3613** |
| **best** | | **2.2360** |

## Chain progression R1272 → R1273

Previous harvest: `workers/dispatcher/harvest-6way-r1272_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3680         | 2.3613         | -0.0067 |
| ctrl_bpc best  | 2.2399         | 2.2360         | -0.0039 |

## Per-round trajectory (best bird: TF6PN)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1273 | 5361 | 2.2360 | +0.2674 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1272_sym24`

## Output

`workers/dispatcher/harvest-3way-r1273_sym24/round-1273/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

