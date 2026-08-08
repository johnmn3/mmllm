# harvest-6way-r1140 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1140 ctrl_bpc |
|--------|--------|--------------:|
| UeRE9 | fork-SeniorCareMarket-mmllm-claude-train-sym24-a29795f2-UeRE9 | 2.3424 |
| AvoQU | fork-slaa-us-mmllm-claude-train-sym24-024392af-AvoQU | 2.3642 |
| Jzoqa | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-e11615f3-Jzoqa | 2.3668 |
| DebFD | origin/claude/train-sym24-fd290d05-DebFD | 2.3719 |
| Jlx6J | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-65ffe76c-Jlx6J | 2.5367 |
| 5T3iw | fork-joly-os-mmllm-claude-train-sym24-31491639-5T3iw | 2.7470 |
| **mean** | | **2.4548** |
| **best** | | **2.3424** |

## Chain progression R1139 → R1140

Previous harvest: `workers/dispatcher/harvest-7way-r1139_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5014         | 2.4548         | -0.0466 |
| ctrl_bpc best  | 2.3423         | 2.3424         | +0.0001 |

## Per-round trajectory (best bird: UeRE9)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1140 | 6675 | 2.3424 | +0.2464 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1139_sym24`
  - `workers/dispatcher/harvest-5way-r1139_sym24`

## Output

`workers/dispatcher/harvest-6way-r1140_sym24/round-1140/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

