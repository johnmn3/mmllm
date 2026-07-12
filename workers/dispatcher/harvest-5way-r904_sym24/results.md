# harvest-5way-r904 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R904 ctrl_bpc |
|--------|--------|--------------:|
| 2ej36 | fork-joly-os-mmllm-claude-train-sym24-c05b845c-2ej36 | 2.7666 |
| 299sO | fork-SeniorCareMarket-mmllm-claude-train-sym24-6b005272-299sO | 2.7789 |
| kI7UP | origin/claude/train-sym24-fa0e2889-kI7UP | 2.7895 |
| EC0E7 | origin/claude/train-sym24-33a461ac-EC0E7 | 2.7949 |
| JGR9C | fork-slaa-us-mmllm-claude-train-sym24-dd75776d-JGR9C | 2.9595 |
| **mean** | | **2.8179** |
| **best** | | **2.7666** |

## Chain progression R903 → R904

Previous harvest: `workers/dispatcher/harvest-7way-r903_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9488         | 2.8179         | -0.1309 |
| ctrl_bpc best  | 2.7893         | 2.7666         | -0.0227 |

## Per-round trajectory (best bird: 2ej36)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 904 | 4407 | 2.7666 | +0.3558 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r903_sym24`

## Output

`workers/dispatcher/harvest-5way-r904_sym24/round-904/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

