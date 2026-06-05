# harvest-3way-r617 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R617 ctrl_bpc |
|--------|--------|--------------:|
| Yt42a | fork-slaa-us-mmllm-claude-train-sym24-f28bf347-Yt42a | 2.1231 |
| 4ZAtT | origin/claude/train-sym24-610dc7fe-4ZAtT | 2.3421 |
| P4XKh | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-60f05f44-P4XKh | 2.5976 |
| **mean** | | **2.3543** |
| **best** | | **2.1231** |

## Chain progression R616 → R617

Previous harvest: `workers/dispatcher/harvest-1way-r616_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.1452         | 2.3543         | +0.2091 |
| ctrl_bpc best  | 2.1452         | 2.1231         | -0.0221 |

## Per-round trajectory (best bird: Yt42a)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 617 | 5809 | 2.1231 | +0.0320 |

## Cumulative training contribution

- This harvest: **150 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r616_sym24`

## Output

`workers/dispatcher/harvest-3way-r617_sym24/round-617/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

