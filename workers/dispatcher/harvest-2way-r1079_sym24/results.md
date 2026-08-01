# harvest-2way-r1079 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1079 ctrl_bpc |
|--------|--------|--------------:|
| m6JPq | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-b05ece90-m6JPq | 2.6217 |
| tJGU3 | fork-joly-os-mmllm-claude-train-sym24-b744191e-tJGU3 | 2.8149 |
| **mean** | | **2.7183** |
| **best** | | **2.6217** |

## Chain progression R1078 → R1079

Previous harvest: `workers/dispatcher/harvest-6way-r1078_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6244         | 2.7183         | +0.0939 |
| ctrl_bpc best  | 2.4339         | 2.6217         | +0.1878 |

## Per-round trajectory (best bird: m6JPq)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1079 | 3744 | 2.6217 | +0.2129 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1078_sym24`

## Output

`workers/dispatcher/harvest-2way-r1079_sym24/round-1079/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

