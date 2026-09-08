# harvest-2way-r1413 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1413 ctrl_bpc |
|--------|--------|--------------:|
| LecFm | fork-SeniorCareMarket-mmllm-claude-train-sym24-f8198eca-LecFm | 3.3182 |
| A7yeK | origin/claude/train-sym24-a819267f-A7yeK | 3.7050 |
| **mean** | | **3.5116** |
| **best** | | **3.3182** |

## Chain progression R1412 → R1413

Previous harvest: `workers/dispatcher/harvest-1way-r1412_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5872         | 3.5116         | -0.0756 |
| ctrl_bpc best  | 3.5872         | 3.3182         | -0.2690 |

## Per-round trajectory (best bird: LecFm)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1413 | 4306 | 3.3182 | +0.1519 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1412_sym24`

## Output

`workers/dispatcher/harvest-2way-r1413_sym24/round-1413/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

