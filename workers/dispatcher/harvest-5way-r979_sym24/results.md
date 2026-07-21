# harvest-5way-r979 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R979 ctrl_bpc |
|--------|--------|--------------:|
| bxJYO | fork-joly-os-mmllm-claude-train-sym24-15b7e20a-bxJYO | 2.5999 |
| XDDuB | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-471f5631-XDDuB | 2.6397 |
| cX5IX | origin/claude/train-sym24-038b6f2e-cX5IX | 2.6415 |
| LTMlH | fork-SeniorCareMarket-mmllm-claude-train-sym24-e8b08f79-LTMlH | 2.7855 |
| LxKHi | fork-slaa-us-mmllm-claude-train-sym24-f3510e67-LxKHi | 2.9730 |
| **mean** | | **2.7279** |
| **best** | | **2.5999** |

## Chain progression R978 → R979

Previous harvest: `workers/dispatcher/harvest-8way-r978_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7374         | 2.7279         | -0.0095 |
| ctrl_bpc best  | 2.6021         | 2.5999         | -0.0022 |

## Per-round trajectory (best bird: bxJYO)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 979 | 6554 | 2.5999 | +0.1676 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r978_sym24`

## Output

`workers/dispatcher/harvest-5way-r979_sym24/round-979/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

