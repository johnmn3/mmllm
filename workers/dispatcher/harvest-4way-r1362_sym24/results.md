# harvest-4way-r1362 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1362 ctrl_bpc |
|--------|--------|--------------:|
| 2IswF | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-4a96f584-2IswF | 3.1311 |
| vD9XB | fork-SeniorCareMarket-mmllm-claude-train-sym24-743842d5-vD9XB | 3.1754 |
| Tu866 | fork-slaa-us-mmllm-claude-train-sym24-ed7a6357-Tu866 | 3.1825 |
| axdk8 | fork-slaa-us-mmllm-claude-train-sym24-b711058d-axdk8 | 3.5269 |
| **mean** | | **3.2540** |
| **best** | | **3.1311** |

## Chain progression R610 → R1362

Previous harvest: `workers/dispatcher/harvest-2way-merge-r610_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.1372         | 3.2540         | +1.1168 |
| ctrl_bpc best  | 2.1268         | 3.1311         | +1.0043 |

## Per-round trajectory (best bird: 2IswF)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1362 | 6453 | 3.1311 | +0.0990 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1361_sym24`
  - `workers/dispatcher/harvest-7way-r1361_sym24`

## Output

`workers/dispatcher/harvest-4way-r1362_sym24/round-1362/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

