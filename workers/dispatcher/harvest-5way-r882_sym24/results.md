# harvest-5way-r882 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R882 ctrl_bpc |
|--------|--------|--------------:|
| DYD6G | fork-joly-os-mmllm-claude-train-sym24-33ef55f1-DYD6G | 2.8375 |
| k8JaH | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-4ec9d2d8-k8JaH | 2.8442 |
| o6Pad | origin/claude/train-sym24-d0b73420-o6Pad | 3.2201 |
| KtS84 | fork-SeniorCareMarket-mmllm-claude-train-sym24-d7807866-KtS84 | 3.2204 |
| S2FVo | fork-slaa-us-mmllm-claude-train-sym24-ca99f001-S2FVo | 3.2238 |
| **mean** | | **3.0692** |
| **best** | | **2.8375** |

## Chain progression R881 → R882

Previous harvest: `workers/dispatcher/harvest-7way-r881_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1131         | 3.0692         | -0.0439 |
| ctrl_bpc best  | 2.8444         | 2.8375         | -0.0069 |

## Per-round trajectory (best bird: DYD6G)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 882 | 6513 | 2.8375 | +0.2685 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r881_sym24`
  - `workers/dispatcher/harvest-7way-r881_sym24`

## Output

`workers/dispatcher/harvest-5way-r882_sym24/round-882/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

