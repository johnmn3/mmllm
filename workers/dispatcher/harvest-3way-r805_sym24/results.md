# harvest-3way-r805 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R805 ctrl_bpc |
|--------|--------|--------------:|
| bqm16 | fork-slaa-us-mmllm-claude-train-sym24-782522d6-bqm16 | 3.0971 |
| ft1yQ | origin/claude/train-sym24-5b86e21f-ft1yQ | 3.0977 |
| ksxR0 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-45df15b6-ksxR0 | 3.2183 |
| **mean** | | **3.1377** |
| **best** | | **3.0971** |

## Chain progression R804 → R805

Previous harvest: `workers/dispatcher/harvest-2way-r804_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4621         | 3.1377         | -0.3244 |
| ctrl_bpc best  | 3.4606         | 3.0971         | -0.3635 |

## Per-round trajectory (best bird: bqm16)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 805 | 6682 | 3.0971 | +0.5320 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r804_sym24`

## Output

`workers/dispatcher/harvest-3way-r805_sym24/round-805/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

