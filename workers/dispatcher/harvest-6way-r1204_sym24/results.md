# harvest-6way-r1204 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1204 ctrl_bpc |
|--------|--------|--------------:|
| 7iSgU | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-48a0e843-7iSgU | 2.2789 |
| VWva7 | origin/claude/train-sym24-f6c9d0a7-VWva7 | 2.2819 |
| I9c7W | origin/claude/train-sym24-70b69887-I9c7W | 2.4742 |
| 5D0GF | fork-slaa-us-mmllm-claude-train-sym24-da948ef6-5D0GF | 2.4779 |
| ACO8Q | fork-joly-os-mmllm-claude-train-sym24-a3765ffa-ACO8Q | 2.4792 |
| 3MH4D | fork-SeniorCareMarket-mmllm-claude-train-sym24-271775a9-3MH4D | 2.6683 |
| **mean** | | **2.4434** |
| **best** | | **2.2789** |

## Chain progression R1203 → R1204

Previous harvest: `workers/dispatcher/harvest-13way-r1203_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4533         | 2.4434         | -0.0099 |
| ctrl_bpc best  | 2.2775         | 2.2789         | +0.0014 |

## Per-round trajectory (best bird: 7iSgU)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1204 | 6704 | 2.2789 | +0.2521 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-10way-r1203_sym24`
  - `workers/dispatcher/harvest-6way-r1203_sym24`

## Output

`workers/dispatcher/harvest-6way-r1204_sym24/round-1204/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

