# harvest-4way-r1079 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1079 ctrl_bpc |
|--------|--------|--------------:|
| QttkZ | origin/claude/train-sym24-41abb739-QttkZ | 2.6182 |
| m6JPq | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-b05ece90-m6JPq | 2.6217 |
| 8GXIL | fork-SeniorCareMarket-mmllm-claude-train-sym24-d830bd60-8GXIL | 2.6416 |
| tJGU3 | fork-joly-os-mmllm-claude-train-sym24-b744191e-tJGU3 | 2.8149 |
| **mean** | | **2.6741** |
| **best** | | **2.6182** |

## Chain progression R1078 → R1079

Previous harvest: `workers/dispatcher/harvest-6way-r1078_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6244         | 2.6741         | +0.0497 |
| ctrl_bpc best  | 2.4339         | 2.6182         | +0.1843 |

## Per-round trajectory (best bird: QttkZ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1079 | 6363 | 2.6182 | +0.2129 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1078_sym24`

## Output

`workers/dispatcher/harvest-4way-r1079_sym24/round-1079/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

