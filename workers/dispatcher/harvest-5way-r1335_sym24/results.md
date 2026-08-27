# harvest-5way-r1335 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1335 ctrl_bpc |
|--------|--------|--------------:|
| QOZwC | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-c7aa7116-QOZwC | 3.2503 |
| pj2CZ | origin/claude/train-sym24-a8dac88a-pj2CZ | 3.3014 |
| Ux8uV | fork-SeniorCareMarket-mmllm-claude-train-sym24-55461976-Ux8uV | 3.3386 |
| apMTP | fork-slaa-us-mmllm-claude-train-sym24-7e9a4c4f-apMTP | 3.3545 |
| p7BZy | origin/claude/train-sym24-a6747aa1-p7BZy | 3.3759 |
| **mean** | | **3.3241** |
| **best** | | **3.2503** |

## Chain progression R1334 → R1335

Previous harvest: `workers/dispatcher/harvest-1way-r1334_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.6180         | 3.3241         | -0.2939 |
| ctrl_bpc best  | 3.6180         | 3.2503         | -0.3677 |

## Per-round trajectory (best bird: QOZwC)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1335 | 6465 | 3.2503 | +0.1086 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1334_sym24`

## Output

`workers/dispatcher/harvest-5way-r1335_sym24/round-1335/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

