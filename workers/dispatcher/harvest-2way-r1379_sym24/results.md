# harvest-2way-r1379 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1379 ctrl_bpc |
|--------|--------|--------------:|
| ETeH4 | fork-SeniorCareMarket-mmllm-claude-train-sym24-5004b331-ETeH4 | 3.0921 |
| cQoR7 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-c16db73b-cQoR7 | 3.1101 |
| **mean** | | **3.1011** |
| **best** | | **3.0921** |

## Chain progression R1378 → R1379

Previous harvest: `workers/dispatcher/harvest-4way-r1378_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3352         | 3.1011         | -0.2341 |
| ctrl_bpc best  | 3.1221         | 3.0921         | -0.0300 |

## Per-round trajectory (best bird: ETeH4)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1379 | 6632 | 3.0921 | +0.1234 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1378_sym24`

## Output

`workers/dispatcher/harvest-2way-r1379_sym24/round-1379/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

