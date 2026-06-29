# harvest-17way-r795 — sparse-delta merge of 17 birds

## Worker endpoints

| handle | branch | R795 ctrl_bpc |
|--------|--------|--------------:|
| rfYSk | origin/claude/train-sym24-9c91d6a3-rfYSk | 3.1109 |
| wWDQr | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-b1c9dd0a-wWDQr | 3.1130 |
| j2c3I | fork-SeniorCareMarket-mmllm-claude-train-sym24-88d2ffc4-j2c3I | 3.1174 |
| 8LPN0 | fork-joly-os-mmllm-claude-train-sym24-85894239-8LPN0 | 3.1206 |
| T28wl | fork-slaa-us-mmllm-claude-train-sym24-c13c6148-T28wl | 3.1217 |
| eq1uN | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-87f6799b-eq1uN | 3.1340 |
| O10rf | origin/claude/train-sym24-483f7535-O10rf | 3.1487 |
| K1Nn9 | fork-davidwuchn-mmllm-claude-train-sym24-db2caa5e-K1Nn9 | 3.1536 |
| 9BjLG | fork-davidwuchn-mmllm-claude-train-sym24-767a9167-9BjLG | 3.1584 |
| 2lQgu | fork-SeniorCareMarket-mmllm-claude-train-sym24-90154d46-2lQgu | 3.2495 |
| irq1W | fork-davidwuchn-mmllm-claude-train-sym24-52f3c8c7-irq1W | 3.2513 |
| 1eQV7 | fork-slaa-us-mmllm-claude-train-sym24-37b440b5-1eQV7 | 3.2595 |
| dUR3R | fork-joly-os-mmllm-claude-train-sym24-7414bd8c-dUR3R | 3.2612 |
| RrJ7B | fork-slaa-us-mmllm-claude-train-sym24-47a5512f-RrJ7B | 3.2659 |
| IKINg | origin/claude/train-sym24-d79fa5f0-IKINg | 3.2684 |
| QiLIj | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-909365fa-QiLIj | 3.2751 |
| BBnqr | fork-joly-os-mmllm-claude-train-sym24-bba19d17-BBnqr | 3.5165 |
| **mean** | | **3.2074** |
| **best** | | **3.1109** |

## Chain progression R794 → R795

Previous harvest: `workers/dispatcher/harvest-5way-r794_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2475         | 3.2074         | -0.0401 |
| ctrl_bpc best  | 3.1226         | 3.1109         | -0.0117 |

## Per-round trajectory (best bird: rfYSk)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 795 | 6799 | 3.1109 | +0.4571 |

## Cumulative training contribution

- This harvest: **1360 steps** from 17 bird(s)
- Across full ancestry (deduped by bird_id): **1760 steps** from 22 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-13way-r794_sym24`
  - `workers/dispatcher/harvest-4way-r794_sym24`
  - `workers/dispatcher/harvest-5way-r794_sym24`

## Output

`workers/dispatcher/harvest-17way-r795_sym24/round-795/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 17 workers)
- `dense.pt` (averaged across 17 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

