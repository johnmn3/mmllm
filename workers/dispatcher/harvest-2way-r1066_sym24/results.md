# harvest-2way-r1066 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1066 ctrl_bpc |
|--------|--------|--------------:|
| HkvyC | fork-joly-os-mmllm-claude-train-sym24-120cf186-HkvyC | 2.5283 |
| nrUW7 | origin/claude/train-sym24-51233bea-nrUW7 | 2.6396 |
| **mean** | | **2.5840** |
| **best** | | **2.5283** |

## Chain progression R1065 → R1066

Previous harvest: `workers/dispatcher/harvest-5way-r1065_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6284         | 2.5840         | -0.0444 |
| ctrl_bpc best  | 2.4624         | 2.5283         | +0.0659 |

## Per-round trajectory (best bird: HkvyC)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1066 | 3811 | 2.5283 | +0.2132 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1065_sym24`
  - `workers/dispatcher/harvest-4way-r1065_sym24`

## Output

`workers/dispatcher/harvest-2way-r1066_sym24/round-1066/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

