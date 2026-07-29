# harvest-5way-r1058 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1058 ctrl_bpc |
|--------|--------|--------------:|
| sZwA4 | fork-joly-os-mmllm-claude-train-sym24-25846add-sZwA4 | 2.4905 |
| BOHul | origin/claude/train-sym24-508c847e-BOHul | 2.4974 |
| 8TV8F | origin/claude/train-sym24-72254b39-8TV8F | 2.6454 |
| J8ohF | fork-SeniorCareMarket-mmllm-claude-train-sym24-487efe88-J8ohF | 2.6522 |
| PGXP6 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-7754350a-PGXP6 | 2.8525 |
| **mean** | | **2.6276** |
| **best** | | **2.4905** |

## Chain progression R1057 → R1058

Previous harvest: `workers/dispatcher/harvest-6way-r1057_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6277         | 2.6276         | -0.0001 |
| ctrl_bpc best  | 2.4609         | 2.4905         | +0.0296 |

## Per-round trajectory (best bird: sZwA4)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1058 | 6624 | 2.4905 | +0.1931 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1057_sym24`
  - `workers/dispatcher/harvest-3way-r1057_sym24`

## Output

`workers/dispatcher/harvest-5way-r1058_sym24/round-1058/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

