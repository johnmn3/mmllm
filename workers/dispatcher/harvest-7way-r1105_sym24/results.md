# harvest-7way-r1105 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R1105 ctrl_bpc |
|--------|--------|--------------:|
| QXjGC | fork-SeniorCareMarket-mmllm-claude-train-sym24-23321e85-QXjGC | 2.3893 |
| Tkuyu | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-7ed3ff95-Tkuyu | 2.4007 |
| HvxKj | origin/claude/train-sym24-0bbe3cf2-HvxKj | 2.4092 |
| 4YgDS | fork-slaa-us-mmllm-claude-train-sym24-ad080999-4YgDS | 2.4124 |
| LihDE | fork-joly-os-mmllm-claude-train-sym24-038af4e6-LihDE | 2.4310 |
| D4z5I | fork-SeniorCareMarket-mmllm-claude-train-sym24-fdd8d3f0-D4z5I | 2.5943 |
| OnoEA | origin/claude/train-sym24-dc4e2963-OnoEA | 2.8195 |
| **mean** | | **2.4938** |
| **best** | | **2.3893** |

## Chain progression R1104 → R1105

Previous harvest: `workers/dispatcher/harvest-9way-r1104_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5141         | 2.4938         | -0.0203 |
| ctrl_bpc best  | 2.3954         | 2.3893         | -0.0061 |

## Per-round trajectory (best bird: QXjGC)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1105 | 5309 | 2.3893 | +0.2501 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1104_sym24`
  - `workers/dispatcher/harvest-7way-r1104_sym24`

## Output

`workers/dispatcher/harvest-7way-r1105_sym24/round-1105/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

