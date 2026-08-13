# harvest-2way-r1195 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1195 ctrl_bpc |
|--------|--------|--------------:|
| KmHG8 | fork-SeniorCareMarket-mmllm-claude-train-sym24-0c4e6757-KmHG8 | 2.3101 |
| 0IRXW | fork-slaa-us-mmllm-claude-train-sym24-ecc2e52a-0IRXW | 2.6841 |
| **mean** | | **2.4971** |
| **best** | | **2.3101** |

## Chain progression R1194 → R1195

Previous harvest: `workers/dispatcher/harvest-6way-r1194_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3659         | 2.4971         | +0.1312 |
| ctrl_bpc best  | 2.2894         | 2.3101         | +0.0207 |

## Per-round trajectory (best bird: KmHG8)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1195 | 3731 | 2.3101 | +0.2419 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1194_sym24`

## Output

`workers/dispatcher/harvest-2way-r1195_sym24/round-1195/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

