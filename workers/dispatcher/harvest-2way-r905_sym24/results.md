# harvest-2way-r905 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R905 ctrl_bpc |
|--------|--------|--------------:|
| 1vpLG | origin/claude/train-sym24-6983349b-1vpLG | 2.7863 |
| CuPra | fork-slaa-us-mmllm-claude-train-sym24-d32e8830-CuPra | 2.9713 |
| **mean** | | **2.8788** |
| **best** | | **2.7863** |

## Chain progression R904 → R905

Previous harvest: `workers/dispatcher/harvest-5way-r904_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8179         | 2.8788         | +0.0609 |
| ctrl_bpc best  | 2.7666         | 2.7863         | +0.0197 |

## Per-round trajectory (best bird: 1vpLG)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 905 | 5427 | 2.7863 | +0.2455 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r904_sym24`

## Output

`workers/dispatcher/harvest-2way-r905_sym24/round-905/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

