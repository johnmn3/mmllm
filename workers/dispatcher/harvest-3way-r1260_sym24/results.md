# harvest-3way-r1260 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1260 ctrl_bpc |
|--------|--------|--------------:|
| qtnEy | fork-slaa-us-mmllm-claude-train-sym24-44f66371-qtnEy | 2.2477 |
| yk6uC | fork-SeniorCareMarket-mmllm-claude-train-sym24-42d95df5-yk6uC | 2.2602 |
| WVxZW | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-d5a624d4-WVxZW | 2.2658 |
| **mean** | | **2.2579** |
| **best** | | **2.2477** |

## Chain progression R1259 → R1260

Previous harvest: `workers/dispatcher/harvest-7way-r1259_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3541         | 2.2579         | -0.0962 |
| ctrl_bpc best  | 2.2343         | 2.2477         | +0.0134 |

## Per-round trajectory (best bird: qtnEy)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1260 | 6777 | 2.2477 | +0.2543 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1259_sym24`

## Output

`workers/dispatcher/harvest-3way-r1260_sym24/round-1260/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

