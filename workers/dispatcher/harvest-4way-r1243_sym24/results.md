# harvest-4way-r1243 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1243 ctrl_bpc |
|--------|--------|--------------:|
| qn1fy | fork-slaa-us-mmllm-claude-train-sym24-b4f2c235-qn1fy | 2.2525 |
| Q8Q5U | fork-SeniorCareMarket-mmllm-claude-train-sym24-1a9eb27a-Q8Q5U | 2.2688 |
| dcKcI | fork-joly-os-mmllm-claude-train-sym24-c2bca63e-dcKcI | 2.4486 |
| g6jKG | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-14ac5d34-g6jKG | 2.6507 |
| **mean** | | **2.4051** |
| **best** | | **2.2525** |

## Chain progression R1242 → R1243

Previous harvest: `workers/dispatcher/harvest-10way-r1242_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3357         | 2.4051         | +0.0694 |
| ctrl_bpc best  | 2.2494         | 2.2525         | +0.0031 |

## Per-round trajectory (best bird: qn1fy)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1243 | 6360 | 2.2525 | +0.2517 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1242_sym24`

## Output

`workers/dispatcher/harvest-4way-r1243_sym24/round-1243/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

