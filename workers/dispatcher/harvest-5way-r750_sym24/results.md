# harvest-5way-r750 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R750 ctrl_bpc |
|--------|--------|--------------:|
| RE8h2 | fork-joly-os-mmllm-claude-train-sym24-5c7efbb2-RE8h2 | 3.3407 |
| PcV93 | fork-slaa-us-mmllm-claude-train-sym24-432c9afd-PcV93 | 3.3423 |
| i3p24 | fork-SeniorCareMarket-mmllm-claude-train-sym24-5fc061a7-i3p24 | 3.3435 |
| pryjh | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-bc9d17c0-pryjh | 3.4160 |
| VMZjp | origin/claude/train-sym24-02c51425-VMZjp | 3.7198 |
| **mean** | | **3.4325** |
| **best** | | **3.3407** |

## Chain progression R749 → R750

Previous harvest: `workers/dispatcher/harvest-8way-r749_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4501         | 3.4325         | -0.0176 |
| ctrl_bpc best  | 3.3586         | 3.3407         | -0.0179 |

## Per-round trajectory (best bird: RE8h2)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 750 | 6425 | 3.3407 | +0.6708 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r749_sym24`

## Output

`workers/dispatcher/harvest-5way-r750_sym24/round-750/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

