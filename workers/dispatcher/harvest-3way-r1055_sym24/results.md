# harvest-3way-r1055 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1055 ctrl_bpc |
|--------|--------|--------------:|
| pe7vT | origin/claude/train-sym24-46ac99bf-pe7vT | 2.4823 |
| Mr467 | fork-joly-os-mmllm-claude-train-sym24-795c8923-Mr467 | 2.4915 |
| QxQ2U | fork-SeniorCareMarket-mmllm-claude-train-sym24-78892790-QxQ2U | 2.6639 |
| **mean** | | **2.5459** |
| **best** | | **2.4823** |

## Chain progression R1054 → R1055

Previous harvest: `workers/dispatcher/harvest-1way-r1054_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8569         | 2.5459         | -0.3110 |
| ctrl_bpc best  | 2.8569         | 2.4823         | -0.3746 |

## Per-round trajectory (best bird: pe7vT)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1055 | 6384 | 2.4823 | +0.2114 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1054_sym24`

## Output

`workers/dispatcher/harvest-3way-r1055_sym24/round-1055/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

