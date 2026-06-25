# harvest-4way-r766 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R766 ctrl_bpc |
|--------|--------|--------------:|
| ufn3S | fork-davidwuchn-mmllm-claude-train-sym24-09c92c32-ufn3S | 3.2492 |
| jljf8 | fork-joly-os-mmllm-claude-train-sym24-b05da8b6-jljf8 | 3.2942 |
| C6puk | fork-joly-os-mmllm-claude-train-sym24-bc512900-C6puk | 3.6343 |
| yBXO5 | fork-SeniorCareMarket-mmllm-claude-train-sym24-814993fa-yBXO5 | 3.6384 |
| **mean** | | **3.4540** |
| **best** | | **3.2492** |

## Chain progression R765 → R766

Previous harvest: `workers/dispatcher/harvest-8way-r765_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4707         | 3.4540         | -0.0167 |
| ctrl_bpc best  | 3.2432         | 3.2492         | +0.0060 |

## Per-round trajectory (best bird: ufn3S)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 766 | 5336 | 3.2492 | +0.6996 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r765_sym24`
  - `workers/dispatcher/harvest-7way-r765_sym24`

## Output

`workers/dispatcher/harvest-4way-r766_sym24/round-766/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

