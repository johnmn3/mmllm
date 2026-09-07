# harvest-4way-r1409 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1409 ctrl_bpc |
|--------|--------|--------------:|
| VZfBR | fork-SeniorCareMarket-mmllm-claude-train-sym24-c6f66c57-VZfBR | 3.3167 |
| mkAH1 | fork-joly-os-mmllm-claude-train-sym24-4d5de750-mkAH1 | 3.6045 |
| 2rHid | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-2d074d08-2rHid | 3.6409 |
| 6qPM8 | origin/claude/train-sym24-f950d253-6qPM8 | 3.7253 |
| **mean** | | **3.5718** |
| **best** | | **3.3167** |

## Chain progression R1408 → R1409

Previous harvest: `workers/dispatcher/harvest-4way-r1408_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3480         | 3.5718         | +0.2239 |
| ctrl_bpc best  | 3.2298         | 3.3167         | +0.0869 |

## Per-round trajectory (best bird: VZfBR)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1409 | 6528 | 3.3167 | +0.1623 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1408_sym24`

## Output

`workers/dispatcher/harvest-4way-r1409_sym24/round-1409/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

