# harvest-4way-r1189 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1189 ctrl_bpc |
|--------|--------|--------------:|
| RF5Od | fork-joly-os-mmllm-claude-train-sym24-5bc569ab-RF5Od | 2.3203 |
| Z2Yc0 | fork-slaa-us-mmllm-claude-train-sym24-774274c5-Z2Yc0 | 2.4955 |
| a7oBX | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-82c7344c-a7oBX | 2.6844 |
| e3uW3 | fork-SeniorCareMarket-mmllm-claude-train-sym24-a3dffe67-e3uW3 | 2.6919 |
| **mean** | | **2.5480** |
| **best** | | **2.3203** |

## Chain progression R1188 → R1189

Previous harvest: `workers/dispatcher/harvest-7way-r1188_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4722         | 2.5480         | +0.0758 |
| ctrl_bpc best  | 2.3127         | 2.3203         | +0.0076 |

## Per-round trajectory (best bird: RF5Od)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1189 | 3569 | 2.3203 | +0.2388 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1188_sym24`
  - `workers/dispatcher/harvest-7way-r1188_sym24`

## Output

`workers/dispatcher/harvest-4way-r1189_sym24/round-1189/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

