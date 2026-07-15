# harvest-5way-r930 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R930 ctrl_bpc |
|--------|--------|--------------:|
| A6Dvu | origin/claude/train-sym24-a7004437-A6Dvu | 2.7118 |
| F8XaF | fork-slaa-us-mmllm-claude-train-sym24-fbfc25a5-F8XaF | 2.7166 |
| KV30y | fork-joly-os-mmllm-claude-train-sym24-547fccb0-KV30y | 2.9013 |
| ooBco | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-73578095-ooBco | 3.1070 |
| J9aKm | fork-SeniorCareMarket-mmllm-claude-train-sym24-880c788f-J9aKm | 3.1194 |
| **mean** | | **2.9112** |
| **best** | | **2.7118** |

## Chain progression R929 → R930

Previous harvest: `workers/dispatcher/harvest-11way-r929_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8411         | 2.9112         | +0.0701 |
| ctrl_bpc best  | 2.7017         | 2.7118         | +0.0101 |

## Per-round trajectory (best bird: A6Dvu)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 930 | 6602 | 2.7118 | +0.2099 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r929_sym24`
  - `workers/dispatcher/harvest-9way-r929_sym24`

## Output

`workers/dispatcher/harvest-5way-r930_sym24/round-930/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

