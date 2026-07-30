# harvest-4way-r1066 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1066 ctrl_bpc |
|--------|--------|--------------:|
| 3vL0i | fork-SeniorCareMarket-mmllm-claude-train-sym24-2ef21fe3-3vL0i | 2.4812 |
| HkvyC | fork-joly-os-mmllm-claude-train-sym24-120cf186-HkvyC | 2.5283 |
| nrUW7 | origin/claude/train-sym24-51233bea-nrUW7 | 2.6396 |
| OOo7T | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-7878acb8-OOo7T | 2.6610 |
| **mean** | | **2.5775** |
| **best** | | **2.4812** |

## Chain progression R1065 → R1066

Previous harvest: `workers/dispatcher/harvest-5way-r1065_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6284         | 2.5775         | -0.0509 |
| ctrl_bpc best  | 2.4624         | 2.4812         | +0.0188 |

## Per-round trajectory (best bird: 3vL0i)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1066 | 6339 | 2.4812 | +0.2018 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1065_sym24`
  - `workers/dispatcher/harvest-4way-r1065_sym24`

## Output

`workers/dispatcher/harvest-4way-r1066_sym24/round-1066/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

