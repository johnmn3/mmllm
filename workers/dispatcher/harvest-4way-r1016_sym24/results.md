# harvest-4way-r1016 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1016 ctrl_bpc |
|--------|--------|--------------:|
| yHn8G | origin/claude/train-sym24-f8433b26-yHn8G | 2.6038 |
| 7ZgTP | fork-SeniorCareMarket-mmllm-claude-train-sym24-0f6562ae-7ZgTP | 2.9243 |
| 0IuYk | fork-joly-os-mmllm-claude-train-sym24-61fac533-0IuYk | 2.9295 |
| NV6FU | fork-joly-os-mmllm-claude-train-sym24-2cd858ec-NV6FU | 2.9400 |
| **mean** | | **2.8494** |
| **best** | | **2.6038** |

## Chain progression R1015 → R1016

Previous harvest: `workers/dispatcher/harvest-11way-r1015_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7335         | 2.8494         | +0.1159 |
| ctrl_bpc best  | 2.5366         | 2.6038         | +0.0672 |

## Per-round trajectory (best bird: yHn8G)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1016 | 6617 | 2.6038 | +0.2152 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1015_sym24`
  - `workers/dispatcher/harvest-7way-r1015_sym24`

## Output

`workers/dispatcher/harvest-4way-r1016_sym24/round-1016/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

