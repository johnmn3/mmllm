# harvest-6way-r882 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R882 ctrl_bpc |
|--------|--------|--------------:|
| 8cjUG | origin/claude/train-sym24-67e5a08f-8cjUG | 2.8336 |
| DYD6G | fork-joly-os-mmllm-claude-train-sym24-33ef55f1-DYD6G | 2.8375 |
| k8JaH | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-4ec9d2d8-k8JaH | 2.8442 |
| o6Pad | origin/claude/train-sym24-d0b73420-o6Pad | 3.2201 |
| KtS84 | fork-SeniorCareMarket-mmllm-claude-train-sym24-d7807866-KtS84 | 3.2204 |
| S2FVo | fork-slaa-us-mmllm-claude-train-sym24-ca99f001-S2FVo | 3.2238 |
| **mean** | | **3.0299** |
| **best** | | **2.8336** |

## Chain progression R881 → R882

Previous harvest: `workers/dispatcher/harvest-7way-r881_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1131         | 3.0299         | -0.0832 |
| ctrl_bpc best  | 2.8444         | 2.8336         | -0.0108 |

## Per-round trajectory (best bird: 8cjUG)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 882 | 6719 | 2.8336 | +0.4025 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r881_sym24`
  - `workers/dispatcher/harvest-7way-r881_sym24`

## Output

`workers/dispatcher/harvest-6way-r882_sym24/round-882/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

