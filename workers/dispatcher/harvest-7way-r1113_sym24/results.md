# harvest-7way-r1113 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R1113 ctrl_bpc |
|--------|--------|--------------:|
| AR0zf | fork-joly-os-mmllm-claude-train-sym24-e991eb36-AR0zf | 2.3935 |
| Ags0q | fork-slaa-us-mmllm-claude-train-sym24-83d13b26-Ags0q | 2.3949 |
| 6l6JG | fork-slaa-us-mmllm-claude-train-sym24-93b3c5b8-6l6JG | 2.3977 |
| 6owaJ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-e53a1889-6owaJ | 2.5758 |
| eAkcC | fork-SeniorCareMarket-mmllm-claude-train-sym24-76e1f5c5-eAkcC | 2.7733 |
| rrLK4 | origin/claude/train-sym24-610b1331-rrLK4 | 2.7777 |
| oGt1E | origin/claude/train-sym24-7e3fb63d-oGt1E | 2.7944 |
| **mean** | | **2.5868** |
| **best** | | **2.3935** |

## Chain progression R1112 → R1113

Previous harvest: `workers/dispatcher/harvest-7way-r1112_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5253         | 2.5868         | +0.0615 |
| ctrl_bpc best  | 2.3729         | 2.3935         | +0.0206 |

## Per-round trajectory (best bird: AR0zf)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1113 | 6593 | 2.3935 | +0.2410 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1112_sym24`
  - `workers/dispatcher/harvest-3way-r1112_sym24`

## Output

`workers/dispatcher/harvest-7way-r1113_sym24/round-1113/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

