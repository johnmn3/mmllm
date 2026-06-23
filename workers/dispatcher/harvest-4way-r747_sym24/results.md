# harvest-4way-r747 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R747 ctrl_bpc |
|--------|--------|--------------:|
| C49xn | fork-joly-os-mmllm-claude-train-sym24-a0f1bcf6-C49xn | 3.3343 |
| 6n6SF | fork-davidwuchn-mmllm-claude-train-sym24-3e26ae01-6n6SF | 3.7052 |
| Rj5WI | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-6a2aa62e-Rj5WI | 3.7091 |
| P5DXU | origin/claude/train-sym24-9b956a82-P5DXU | 3.7196 |
| **mean** | | **3.6170** |
| **best** | | **3.3343** |

## Chain progression R746 → R747

Previous harvest: `workers/dispatcher/harvest-8way-r746_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4707         | 3.6170         | +0.1463 |
| ctrl_bpc best  | 3.3555         | 3.3343         | -0.0212 |

## Per-round trajectory (best bird: C49xn)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 747 | 6510 | 3.3343 | +0.4978 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r746_sym24`

## Output

`workers/dispatcher/harvest-4way-r747_sym24/round-747/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

