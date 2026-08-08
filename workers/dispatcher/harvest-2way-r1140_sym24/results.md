# harvest-2way-r1140 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1140 ctrl_bpc |
|--------|--------|--------------:|
| UeRE9 | fork-SeniorCareMarket-mmllm-claude-train-sym24-a29795f2-UeRE9 | 2.3424 |
| Jlx6J | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-65ffe76c-Jlx6J | 2.5367 |
| **mean** | | **2.4396** |
| **best** | | **2.3424** |

## Chain progression R1139 → R1140

Previous harvest: `workers/dispatcher/harvest-7way-r1139_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5014         | 2.4396         | -0.0618 |
| ctrl_bpc best  | 2.3423         | 2.3424         | +0.0001 |

## Per-round trajectory (best bird: UeRE9)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1140 | 6675 | 2.3424 | +0.2464 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1139_sym24`

## Output

`workers/dispatcher/harvest-2way-r1140_sym24/round-1140/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

