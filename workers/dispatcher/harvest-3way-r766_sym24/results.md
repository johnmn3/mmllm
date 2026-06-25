# harvest-3way-r766 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R766 ctrl_bpc |
|--------|--------|--------------:|
| ufn3S | fork-davidwuchn-mmllm-claude-train-sym24-09c92c32-ufn3S | 3.2492 |
| jljf8 | fork-joly-os-mmllm-claude-train-sym24-b05da8b6-jljf8 | 3.2942 |
| yBXO5 | fork-SeniorCareMarket-mmllm-claude-train-sym24-814993fa-yBXO5 | 3.6384 |
| **mean** | | **3.3939** |
| **best** | | **3.2492** |

## Chain progression R765 → R766

Previous harvest: `workers/dispatcher/harvest-8way-r765_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4707         | 3.3939         | -0.0768 |
| ctrl_bpc best  | 3.2432         | 3.2492         | +0.0060 |

## Per-round trajectory (best bird: ufn3S)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 766 | 5336 | 3.2492 | +0.6996 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r765_sym24`

## Output

`workers/dispatcher/harvest-3way-r766_sym24/round-766/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

