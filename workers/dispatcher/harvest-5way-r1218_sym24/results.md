# harvest-5way-r1218 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1218 ctrl_bpc |
|--------|--------|--------------:|
| MEmmb | fork-joly-os-mmllm-claude-train-sym24-81c66ece-MEmmb | 2.2675 |
| iVE8P | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-e2cad16f-iVE8P | 2.2838 |
| m0JXg | fork-SeniorCareMarket-mmllm-claude-train-sym24-b33c4d28-m0JXg | 2.2876 |
| 1VbtM | fork-slaa-us-mmllm-claude-train-sym24-63266b40-1VbtM | 2.2894 |
| hijyb | origin/claude/train-sym24-43985d6c-hijyb | 2.4629 |
| **mean** | | **2.3182** |
| **best** | | **2.2675** |

## Chain progression R1217 → R1218

Previous harvest: `workers/dispatcher/harvest-8way-r1217_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3968         | 2.3182         | -0.0786 |
| ctrl_bpc best  | 2.2655         | 2.2675         | +0.0020 |

## Per-round trajectory (best bird: MEmmb)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1218 | 6506 | 2.2675 | +0.2683 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1217_sym24`
  - `workers/dispatcher/harvest-8way-r1217_sym24`

## Output

`workers/dispatcher/harvest-5way-r1218_sym24/round-1218/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

