# harvest-20way-r750 — sparse-delta merge of 20 birds

## Worker endpoints

| handle | branch | R750 ctrl_bpc |
|--------|--------|--------------:|
| eb7jV | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-3b98398e-eb7jV | 3.3279 |
| RE8h2 | fork-joly-os-mmllm-claude-train-sym24-5c7efbb2-RE8h2 | 3.3407 |
| PcV93 | fork-slaa-us-mmllm-claude-train-sym24-432c9afd-PcV93 | 3.3423 |
| 9DVLR | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-ee101fdc-9DVLR | 3.3433 |
| i3p24 | fork-SeniorCareMarket-mmllm-claude-train-sym24-5fc061a7-i3p24 | 3.3435 |
| GRaHe | origin/claude/train-sym24-1268663f-GRaHe | 3.3687 |
| xP7UD | fork-slaa-us-mmllm-claude-train-sym24-a70c4a1d-xP7UD | 3.3687 |
| yVPjf | origin/claude/train-sym24-3df861b8-yVPjf | 3.3700 |
| bh3cX | fork-davidwuchn-mmllm-claude-train-sym24-0d650d10-bh3cX | 3.3713 |
| QbkPX | fork-joly-os-mmllm-claude-train-sym24-1e8e8fbf-QbkPX | 3.3729 |
| yPOMd | fork-davidwuchn-mmllm-claude-train-sym24-c409b03d-yPOMd | 3.3735 |
| qAiqp | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-1265d0b2-qAiqp | 3.4046 |
| 7nQmT | origin/claude/train-sym24-4c6e2ebe-7nQmT | 3.4062 |
| pryjh | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-bc9d17c0-pryjh | 3.4160 |
| 2C6DG | fork-slaa-us-mmllm-claude-train-sym24-8faeb856-2C6DG | 3.5650 |
| T5HvR | fork-slaa-us-mmllm-claude-train-sym24-fc37eb01-T5HvR | 3.6787 |
| mAAMh | fork-davidwuchn-mmllm-claude-train-sym24-bc13c520-mAAMh | 3.6807 |
| ucrnw | fork-SeniorCareMarket-mmllm-claude-train-sym24-3238961e-ucrnw | 3.6842 |
| Ai65e | fork-joly-os-mmllm-claude-train-sym24-a99b9a0b-Ai65e | 3.7065 |
| VMZjp | origin/claude/train-sym24-02c51425-VMZjp | 3.7198 |
| **mean** | | **3.4592** |
| **best** | | **3.3279** |

## Chain progression R749 → R750

Previous harvest: `workers/dispatcher/harvest-8way-r749_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4501         | 3.4592         | +0.0091 |
| ctrl_bpc best  | 3.3586         | 3.3279         | -0.0307 |

## Per-round trajectory (best bird: eb7jV)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 750 | 6529 | 3.3279 | +0.4350 |

## Cumulative training contribution

- This harvest: **1600 steps** from 20 bird(s)
- Across full ancestry (deduped by bird_id): **2240 steps** from 28 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r749_sym24`
  - `workers/dispatcher/harvest-5way-r749_sym24`
  - `workers/dispatcher/harvest-8way-r749_sym24`

## Output

`workers/dispatcher/harvest-20way-r750_sym24/round-750/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 20 workers)
- `dense.pt` (averaged across 20 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

