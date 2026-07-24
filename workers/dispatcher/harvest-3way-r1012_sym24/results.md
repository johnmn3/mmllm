# harvest-3way-r1012 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1012 ctrl_bpc |
|--------|--------|--------------:|
| Ajanr | fork-SeniorCareMarket-mmllm-claude-train-sym24-effcd105-Ajanr | 2.5503 |
| fBkYJ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-93ac48e5-fBkYJ | 2.5601 |
| F01Os | origin/claude/train-sym24-0d8061bf-F01Os | 2.6357 |
| **mean** | | **2.5820** |
| **best** | | **2.5503** |

## Chain progression R1011 → R1012

Previous harvest: `workers/dispatcher/harvest-8way-r1011_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6384         | 2.5820         | -0.0564 |
| ctrl_bpc best  | 2.5378         | 2.5503         | +0.0125 |

## Per-round trajectory (best bird: Ajanr)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1012 | 6264 | 2.5503 | +0.1630 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1011_sym24`

## Output

`workers/dispatcher/harvest-3way-r1012_sym24/round-1012/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

