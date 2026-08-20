# harvest-6way-r1262 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1262 ctrl_bpc |
|--------|--------|--------------:|
| 1WClJ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-95c5568a-1WClJ | 2.2318 |
| L73wI | fork-slaa-us-mmllm-claude-train-sym24-ccc93d1e-L73wI | 2.2328 |
| rA9S5 | fork-SeniorCareMarket-mmllm-claude-train-sym24-3aef5771-rA9S5 | 2.2343 |
| UwF7F | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-4f0305bc-UwF7F | 2.2412 |
| PSwdA | fork-slaa-us-mmllm-claude-train-sym24-522f867c-PSwdA | 2.4227 |
| vOJEO | fork-joly-os-mmllm-claude-train-sym24-e6156223-vOJEO | 2.4337 |
| **mean** | | **2.2994** |
| **best** | | **2.2318** |

## Chain progression R1261 → R1262

Previous harvest: `workers/dispatcher/harvest-6way-r1261_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4089         | 2.2994         | -0.1095 |
| ctrl_bpc best  | 2.2392         | 2.2318         | -0.0074 |

## Per-round trajectory (best bird: 1WClJ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1262 | 4475 | 2.2318 | +0.2602 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1261_sym24`
  - `workers/dispatcher/harvest-6way-r1261_sym24`

## Output

`workers/dispatcher/harvest-6way-r1262_sym24/round-1262/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

