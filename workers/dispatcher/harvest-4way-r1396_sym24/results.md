# harvest-4way-r1396 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1396 ctrl_bpc |
|--------|--------|--------------:|
| 01orh | fork-SeniorCareMarket-mmllm-claude-train-sym24-8813597e-01orh | 3.4255 |
| J59Ng | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-4a1f2057-J59Ng | 3.7358 |
| ff67D | origin/claude/train-sym24-dd94509e-ff67D | 3.7807 |
| WDkLU | fork-joly-os-mmllm-claude-train-sym24-ee8debb3-WDkLU | 3.8758 |
| **mean** | | **3.7045** |
| **best** | | **3.4255** |

## Chain progression R1395 → R1396

Previous harvest: `workers/dispatcher/harvest-4way-r1395_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.7100         | 3.7045         | -0.0055 |
| ctrl_bpc best  | 3.5131         | 3.4255         | -0.0876 |

## Per-round trajectory (best bird: 01orh)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1396 | 6671 | 3.4255 | +0.0712 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1395_sym24`

## Output

`workers/dispatcher/harvest-4way-r1396_sym24/round-1396/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

