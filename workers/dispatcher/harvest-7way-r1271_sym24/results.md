# harvest-7way-r1271 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R1271 ctrl_bpc |
|--------|--------|--------------:|
| 92g00 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-9015b6e9-92g00 | 2.2257 |
| kcFFo | fork-SeniorCareMarket-mmllm-claude-train-sym24-0cb98477-kcFFo | 2.2414 |
| hLqYg | fork-joly-os-mmllm-claude-train-sym24-0d79fdf5-hLqYg | 2.2498 |
| OwZHZ | fork-joly-os-mmllm-claude-train-sym24-316803b0-OwZHZ | 2.4197 |
| O0gll | fork-slaa-us-mmllm-claude-train-sym24-52f96a39-O0gll | 2.6232 |
| lVeed | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f034f72d-lVeed | 2.6242 |
| lgQLG | origin/claude/train-sym24-2936304d-lgQLG | 2.6437 |
| **mean** | | **2.4325** |
| **best** | | **2.2257** |

## Chain progression R1270 → R1271

Previous harvest: `workers/dispatcher/harvest-6way-r1270_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3007         | 2.4325         | +0.1318 |
| ctrl_bpc best  | 2.2241         | 2.2257         | +0.0016 |

## Per-round trajectory (best bird: 92g00)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1271 | 5335 | 2.2257 | +0.2463 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1270_sym24`
  - `workers/dispatcher/harvest-6way-r1270_sym24`

## Output

`workers/dispatcher/harvest-7way-r1271_sym24/round-1271/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

