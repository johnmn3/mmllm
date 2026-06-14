# harvest-5way-r669 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R669 ctrl_bpc |
|--------|--------|--------------:|
| u4VsI | fork-joly-os-mmllm-claude-train-sym24-be2e9ae8-u4VsI | 3.9320 |
| 8qis1 | fork-slaa-us-mmllm-claude-train-sym24-695d6491-8qis1 | 3.9348 |
| 9yvDy | fork-davidwuchn-mmllm-claude-train-sym24-74c3fdf6-9yvDy | 3.9396 |
| hvYIy | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-4a6ec630-hvYIy | 4.2070 |
| l8P3T | fork-SeniorCareMarket-mmllm-claude-train-sym24-8cf56c3b-l8P3T | 4.2297 |
| **mean** | | **4.0486** |
| **best** | | **3.9320** |

## Chain progression R668 → R669

Previous harvest: `workers/dispatcher/harvest-11way-r668_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.0831         | 4.0486         | -0.0345 |
| ctrl_bpc best  | 3.8806         | 3.9320         | +0.0514 |

## Per-round trajectory (best bird: u4VsI)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 669 | 6330 | 3.9320 | +0.3964 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **1280 steps** from 16 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-11way-r668_sym24`
  - `workers/dispatcher/harvest-2way-r668_sym24`

## Output

`workers/dispatcher/harvest-5way-r669_sym24/round-669/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

