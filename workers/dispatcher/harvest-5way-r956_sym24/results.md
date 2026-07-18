# harvest-5way-r956 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R956 ctrl_bpc |
|--------|--------|--------------:|
| ShJqG | origin/claude/train-sym24-1d4e9542-ShJqG | 2.6360 |
| ocZad | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-c79ca58c-ocZad | 2.6464 |
| ZNlDx | fork-SeniorCareMarket-mmllm-claude-train-sym24-8e5697f0-ZNlDx | 2.8339 |
| yNAef | fork-slaa-us-mmllm-claude-train-sym24-48f18456-yNAef | 2.8404 |
| VZhCg | fork-joly-os-mmllm-claude-train-sym24-aa8ff932-VZhCg | 3.0375 |
| **mean** | | **2.7988** |
| **best** | | **2.6360** |

## Chain progression R955 → R956

Previous harvest: `workers/dispatcher/harvest-7way-r955_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8590         | 2.7988         | -0.0602 |
| ctrl_bpc best  | 2.6530         | 2.6360         | -0.0170 |

## Per-round trajectory (best bird: ShJqG)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 956 | 6657 | 2.6360 | +0.1690 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r955_sym24`

## Output

`workers/dispatcher/harvest-5way-r956_sym24/round-956/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

