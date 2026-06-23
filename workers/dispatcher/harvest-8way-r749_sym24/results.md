# harvest-8way-r749 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R749 ctrl_bpc |
|--------|--------|--------------:|
| w3pWy | origin/claude/train-sym24-a7899b7f-w3pWy | 3.3586 |
| R1jxL | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-67afa0bb-R1jxL | 3.4106 |
| 2oBVS | fork-joly-os-mmllm-claude-train-sym24-50046e33-2oBVS | 3.4172 |
| YU7mR | origin/claude/train-sym24-9e5d4b1f-YU7mR | 3.4186 |
| w91Ej | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-0da0bb7a-w91Ej | 3.4282 |
| T0RTJ | fork-slaa-us-mmllm-claude-train-sym24-43c6b2dd-T0RTJ | 3.4317 |
| 3IgkB | fork-slaa-us-mmllm-claude-train-sym24-7cf43bc0-3IgkB | 3.4468 |
| WWsMm | fork-davidwuchn-mmllm-claude-train-sym24-ec794e16-WWsMm | 3.6892 |
| **mean** | | **3.4501** |
| **best** | | **3.3586** |

## Chain progression R748 → R749

Previous harvest: `workers/dispatcher/harvest-8way-r748_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4495         | 3.4501         | +0.0006 |
| ctrl_bpc best  | 3.3437         | 3.3586         | +0.0149 |

## Per-round trajectory (best bird: w3pWy)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 749 | 6752 | 3.3586 | +0.4835 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r748_sym24`

## Output

`workers/dispatcher/harvest-8way-r749_sym24/round-749/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

