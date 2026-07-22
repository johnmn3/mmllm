# harvest-4way-r994 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R994 ctrl_bpc |
|--------|--------|--------------:|
| ItBMM | origin/claude/train-sym24-ec2511a0-ItBMM | 2.5717 |
| SH2a2 | origin/claude/train-sym24-92608b89-SH2a2 | 2.7645 |
| kNkzA | fork-SeniorCareMarket-mmllm-claude-train-sym24-75f81a4e-kNkzA | 2.7659 |
| JyIr8 | fork-slaa-us-mmllm-claude-train-sym24-58284148-JyIr8 | 2.9816 |
| **mean** | | **2.7709** |
| **best** | | **2.5717** |

## Chain progression R993 → R994

Previous harvest: `workers/dispatcher/harvest-5way-r993_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7819         | 2.7709         | -0.0110 |
| ctrl_bpc best  | 2.5936         | 2.5717         | -0.0219 |

## Per-round trajectory (best bird: ItBMM)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 994 | 4484 | 2.5717 | +0.1648 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r993_sym24`

## Output

`workers/dispatcher/harvest-4way-r994_sym24/round-994/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

