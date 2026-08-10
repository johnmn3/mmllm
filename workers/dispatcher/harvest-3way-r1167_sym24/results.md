# harvest-3way-r1167 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1167 ctrl_bpc |
|--------|--------|--------------:|
| eUzZa | fork-joly-os-mmllm-claude-train-sym24-2ca08794-eUzZa | 2.3392 |
| 6Fu5X | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-2a432718-6Fu5X | 2.3461 |
| 7TQb4 | origin/claude/train-sym24-9c826297-7TQb4 | 2.7025 |
| **mean** | | **2.4626** |
| **best** | | **2.3392** |

## Chain progression R1166 → R1167

Previous harvest: `workers/dispatcher/harvest-6way-r1166_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4984         | 2.4626         | -0.0358 |
| ctrl_bpc best  | 2.3462         | 2.3392         | -0.0070 |

## Per-round trajectory (best bird: eUzZa)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1167 | 4417 | 2.3392 | +0.2453 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1166_sym24`

## Output

`workers/dispatcher/harvest-3way-r1167_sym24/round-1167/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

