# harvest-4way-r794 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R794 ctrl_bpc |
|--------|--------|--------------:|
| MID40 | fork-joly-os-mmllm-claude-train-sym24-2283cb11-MID40 | 3.1226 |
| pEEfK | fork-slaa-us-mmllm-claude-train-sym24-0920b25a-pEEfK | 3.1653 |
| kle0k | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-0e4ed3e0-kle0k | 3.1674 |
| fGw91 | fork-davidwuchn-mmllm-claude-train-sym24-dbe356a7-fGw91 | 3.2620 |
| **mean** | | **3.1793** |
| **best** | | **3.1226** |

## Chain progression R793 → R794

Previous harvest: `workers/dispatcher/harvest-17way-r793_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2829         | 3.1793         | -0.1036 |
| ctrl_bpc best  | 3.1185         | 3.1226         | +0.0041 |

## Per-round trajectory (best bird: MID40)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 794 | 6642 | 3.1226 | +0.4331 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r793_sym24`

## Output

`workers/dispatcher/harvest-4way-r794_sym24/round-794/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

