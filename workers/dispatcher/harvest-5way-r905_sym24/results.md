# harvest-5way-r905 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R905 ctrl_bpc |
|--------|--------|--------------:|
| B0njX | fork-SeniorCareMarket-mmllm-claude-train-sym24-b40f8905-B0njX | 2.7738 |
| 1vpLG | origin/claude/train-sym24-6983349b-1vpLG | 2.7863 |
| 4zRAC | origin/claude/train-sym24-646c2395-4zRAC | 2.7904 |
| CuPra | fork-slaa-us-mmllm-claude-train-sym24-d32e8830-CuPra | 2.9713 |
| jHk4H | fork-joly-os-mmllm-claude-train-sym24-89a2d216-jHk4H | 3.1434 |
| **mean** | | **2.8930** |
| **best** | | **2.7738** |

## Chain progression R904 → R905

Previous harvest: `workers/dispatcher/harvest-5way-r904_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8179         | 2.8930         | +0.0751 |
| ctrl_bpc best  | 2.7666         | 2.7738         | +0.0072 |

## Per-round trajectory (best bird: B0njX)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 905 | 6565 | 2.7738 | +0.3486 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r904_sym24`

## Output

`workers/dispatcher/harvest-5way-r905_sym24/round-905/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

