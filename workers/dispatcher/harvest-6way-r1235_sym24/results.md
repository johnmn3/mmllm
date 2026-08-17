# harvest-6way-r1235 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1235 ctrl_bpc |
|--------|--------|--------------:|
| 6nfoy | fork-SeniorCareMarket-mmllm-claude-train-sym24-34939be3-6nfoy | 2.2648 |
| WX2WX | fork-slaa-us-mmllm-claude-train-sym24-f792b0eb-WX2WX | 2.2685 |
| NXU5l | origin/claude/train-sym24-f308cc23-NXU5l | 2.2693 |
| bUjyX | fork-joly-os-mmllm-claude-train-sym24-dab676a7-bUjyX | 2.4578 |
| wJ3rj | fork-SeniorCareMarket-mmllm-claude-train-sym24-42a3daa7-wJ3rj | 2.6580 |
| UqJKT | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f9061a1e-UqJKT | 2.6607 |
| **mean** | | **2.4298** |
| **best** | | **2.2648** |

## Chain progression R1234 → R1235

Previous harvest: `workers/dispatcher/harvest-10way-r1234_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4217         | 2.4298         | +0.0081 |
| ctrl_bpc best  | 2.2531         | 2.2648         | +0.0117 |

## Per-round trajectory (best bird: 6nfoy)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1235 | 5375 | 2.2648 | +0.2409 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **1280 steps** from 16 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-10way-r1234_sym24`
  - `workers/dispatcher/harvest-7way-r1234_sym24`

## Output

`workers/dispatcher/harvest-6way-r1235_sym24/round-1235/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

