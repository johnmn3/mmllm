# harvest-7way-r1283 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R1283 ctrl_bpc |
|--------|--------|--------------:|
| Z2Rn9 | fork-joly-os-mmllm-claude-train-sym24-1427f2c9-Z2Rn9 | 2.2156 |
| f3TqF | origin/claude/train-sym24-f8f48a44-f3TqF | 2.2230 |
| gcs8b | fork-slaa-us-mmllm-claude-train-sym24-bb7f31fa-gcs8b | 2.2246 |
| coHPD | origin/claude/train-sym24-7d185b89-coHPD | 2.2440 |
| m2kWP | fork-SeniorCareMarket-mmllm-claude-train-sym24-edfd610e-m2kWP | 2.4103 |
| 3nbXJ | fork-slaa-us-mmllm-claude-train-sym24-5661eed6-3nbXJ | 2.4106 |
| KUKa5 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-921dd9bb-KUKa5 | 2.6204 |
| **mean** | | **2.3355** |
| **best** | | **2.2156** |

## Chain progression R1282 → R1283

Previous harvest: `workers/dispatcher/harvest-7way-r1282_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3443         | 2.3355         | -0.0088 |
| ctrl_bpc best  | 2.2278         | 2.2156         | -0.0122 |

## Per-round trajectory (best bird: Z2Rn9)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1283 | 4206 | 2.2156 | +0.2544 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1282_sym24`
  - `workers/dispatcher/harvest-7way-r1282_sym24`

## Output

`workers/dispatcher/harvest-7way-r1283_sym24/round-1283/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

