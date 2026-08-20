# harvest-9way-r1260 — sparse-delta merge of 9 birds

## Worker endpoints

| handle | branch | R1260 ctrl_bpc |
|--------|--------|--------------:|
| qtnEy | fork-slaa-us-mmllm-claude-train-sym24-44f66371-qtnEy | 2.2477 |
| O1wzN | origin/claude/train-sym24-c734f470-O1wzN | 2.2567 |
| jmTVZ | fork-joly-os-mmllm-claude-train-sym24-550a623a-jmTVZ | 2.2585 |
| yk6uC | fork-SeniorCareMarket-mmllm-claude-train-sym24-42d95df5-yk6uC | 2.2602 |
| MSa2f | origin/claude/train-sym24-f81cfa5a-MSa2f | 2.2647 |
| WVxZW | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-d5a624d4-WVxZW | 2.2658 |
| KIXns | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-dff64c18-KIXns | 2.4352 |
| EClGT | fork-slaa-us-mmllm-claude-train-sym24-08f28458-EClGT | 2.6283 |
| NNQqm | fork-joly-os-mmllm-claude-train-sym24-dbff61c4-NNQqm | 2.6632 |
| **mean** | | **2.3645** |
| **best** | | **2.2477** |

## Chain progression R1259 → R1260

Previous harvest: `workers/dispatcher/harvest-7way-r1259_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3541         | 2.3645         | +0.0104 |
| ctrl_bpc best  | 2.2343         | 2.2477         | +0.0134 |

## Per-round trajectory (best bird: qtnEy)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1260 | 6777 | 2.2477 | +0.2543 |

## Cumulative training contribution

- This harvest: **720 steps** from 9 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1259_sym24`
  - `workers/dispatcher/harvest-5way-r1259_sym24`

## Output

`workers/dispatcher/harvest-9way-r1260_sym24/round-1260/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 9 workers)
- `dense.pt` (averaged across 9 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

