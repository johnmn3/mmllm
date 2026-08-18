# harvest-4way-r1246 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1246 ctrl_bpc |
|--------|--------|--------------:|
| A1qcc | origin/claude/train-sym24-9d87f845-A1qcc | 2.2411 |
| bJF2b | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-078c550d-bJF2b | 2.2590 |
| foLFO | fork-SeniorCareMarket-mmllm-claude-train-sym24-549dabb3-foLFO | 2.6343 |
| XfHA0 | fork-slaa-us-mmllm-claude-train-sym24-57c54c17-XfHA0 | 2.6392 |
| **mean** | | **2.4434** |
| **best** | | **2.2411** |

## Chain progression R1245 → R1246

Previous harvest: `workers/dispatcher/harvest-9way-r1245_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3652         | 2.4434         | +0.0782 |
| ctrl_bpc best  | 2.2568         | 2.2411         | -0.0157 |

## Per-round trajectory (best bird: A1qcc)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1246 | 5567 | 2.2411 | +0.2544 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1245_sym24`

## Output

`workers/dispatcher/harvest-4way-r1246_sym24/round-1246/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

