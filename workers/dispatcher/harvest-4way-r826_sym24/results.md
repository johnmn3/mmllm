# harvest-4way-r826 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R826 ctrl_bpc |
|--------|--------|--------------:|
| wAswn | fork-slaa-us-mmllm-claude-train-sym24-7837cf32-wAswn | 3.0224 |
| g7omh | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-30959e14-g7omh | 3.1528 |
| GcCuK | fork-joly-os-mmllm-claude-train-sym24-e2296074-GcCuK | 3.3834 |
| gv3f9 | fork-SeniorCareMarket-mmllm-claude-train-sym24-ce9dc927-gv3f9 | 3.3846 |
| **mean** | | **3.2358** |
| **best** | | **3.0224** |

## Chain progression R825 → R826

Previous harvest: `workers/dispatcher/harvest-1way-r825_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1534         | 3.2358         | +0.0824 |
| ctrl_bpc best  | 3.1534         | 3.0224         | -0.1310 |

## Per-round trajectory (best bird: wAswn)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 826 | 6512 | 3.0224 | +0.6536 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r825_sym24`

## Output

`workers/dispatcher/harvest-4way-r826_sym24/round-826/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

