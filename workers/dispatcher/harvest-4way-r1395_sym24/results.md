# harvest-4way-r1395 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1395 ctrl_bpc |
|--------|--------|--------------:|
| 8h2Yy | fork-SeniorCareMarket-mmllm-claude-train-sym24-ebf5313a-8h2Yy | 3.5131 |
| sLxXr | fork-joly-os-mmllm-claude-train-sym24-5d6549a2-sLxXr | 3.6488 |
| NH45n | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-69fa3b8f-NH45n | 3.6512 |
| iirNn | origin/claude/train-sym24-2a57d71d-iirNn | 4.0269 |
| **mean** | | **3.7100** |
| **best** | | **3.5131** |

## Chain progression R1394 → R1395

Previous harvest: `workers/dispatcher/harvest-4way-r1394_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.7251         | 3.7100         | -0.0151 |
| ctrl_bpc best  | 3.6153         | 3.5131         | -0.1022 |

## Per-round trajectory (best bird: 8h2Yy)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1395 | 3912 | 3.5131 | +0.0782 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1394_sym24`

## Output

`workers/dispatcher/harvest-4way-r1395_sym24/round-1395/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

