# harvest-6way-r671 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R671 ctrl_bpc |
|--------|--------|--------------:|
| G4tmb | fork-davidwuchn-mmllm-claude-train-sym24-ecf5b5b6-G4tmb | 3.8549 |
| UxUo5 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-3b183491-UxUo5 | 3.8860 |
| M4h5B | fork-joly-os-mmllm-claude-train-sym24-e2411454-M4h5B | 3.8923 |
| Ii2KY | fork-davidwuchn-mmllm-claude-train-sym24-482c2d9c-Ii2KY | 3.8949 |
| aeaa7 | fork-slaa-us-mmllm-claude-train-sym24-7a5c88d5-aeaa7 | 3.9134 |
| PPhTZ | fork-joly-os-mmllm-claude-train-sym24-d30b6338-PPhTZ | 3.9317 |
| **mean** | | **3.8955** |
| **best** | | **3.8549** |

## Chain progression R610 → R671

Previous harvest: `workers/dispatcher/harvest-2way-merge-r610_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.1372         | 3.8955         | +1.7583 |
| ctrl_bpc best  | 2.1268         | 3.8549         | +1.7281 |

## Per-round trajectory (best bird: G4tmb)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 671 | 6490 | 3.8549 | +0.4312 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-10way-r670_sym24`
  - `workers/dispatcher/harvest-6way-r670_sym24`

## Output

`workers/dispatcher/harvest-6way-r671_sym24/round-671/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

