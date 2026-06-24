# harvest-12way-r750 — sparse-delta merge of 12 birds

## Worker endpoints

| handle | branch | R750 ctrl_bpc |
|--------|--------|--------------:|
| RE8h2 | fork-joly-os-mmllm-claude-train-sym24-5c7efbb2-RE8h2 | 3.3407 |
| PcV93 | fork-slaa-us-mmllm-claude-train-sym24-432c9afd-PcV93 | 3.3423 |
| 9DVLR | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-ee101fdc-9DVLR | 3.3433 |
| i3p24 | fork-SeniorCareMarket-mmllm-claude-train-sym24-5fc061a7-i3p24 | 3.3435 |
| yVPjf | origin/claude/train-sym24-3df861b8-yVPjf | 3.3700 |
| yPOMd | fork-davidwuchn-mmllm-claude-train-sym24-c409b03d-yPOMd | 3.3735 |
| qAiqp | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-1265d0b2-qAiqp | 3.4046 |
| pryjh | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-bc9d17c0-pryjh | 3.4160 |
| T5HvR | fork-slaa-us-mmllm-claude-train-sym24-fc37eb01-T5HvR | 3.6787 |
| mAAMh | fork-davidwuchn-mmllm-claude-train-sym24-bc13c520-mAAMh | 3.6807 |
| Ai65e | fork-joly-os-mmllm-claude-train-sym24-a99b9a0b-Ai65e | 3.7065 |
| VMZjp | origin/claude/train-sym24-02c51425-VMZjp | 3.7198 |
| **mean** | | **3.4766** |
| **best** | | **3.3407** |

## Chain progression R749 → R750

Previous harvest: `workers/dispatcher/harvest-8way-r749_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4501         | 3.4766         | +0.0265 |
| ctrl_bpc best  | 3.3586         | 3.3407         | -0.0179 |

## Per-round trajectory (best bird: RE8h2)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 750 | 6425 | 3.3407 | +0.6708 |

## Cumulative training contribution

- This harvest: **960 steps** from 12 bird(s)
- Across full ancestry (deduped by bird_id): **1360 steps** from 17 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r749_sym24`
  - `workers/dispatcher/harvest-5way-r749_sym24`

## Output

`workers/dispatcher/harvest-12way-r750_sym24/round-750/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 12 workers)
- `dense.pt` (averaged across 12 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

