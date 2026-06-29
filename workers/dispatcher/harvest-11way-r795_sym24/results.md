# harvest-11way-r795 — sparse-delta merge of 11 birds

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
| 9BjLG | fork-davidwuchn-mmllm-claude-train-sym24-767a9167-9BjLG | 3.1584 |
| irq1W | fork-davidwuchn-mmllm-claude-train-sym24-52f3c8c7-irq1W | 3.2513 |
| 1eQV7 | fork-slaa-us-mmllm-claude-train-sym24-37b440b5-1eQV7 | 3.2595 |
| dUR3R | fork-joly-os-mmllm-claude-train-sym24-7414bd8c-dUR3R | 3.2612 |
| **mean** | | **3.1633** |
| **best** | | **3.1109** |

## Chain progression R794 → R795

Previous harvest: `workers/dispatcher/harvest-5way-r794_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2475         | 3.1633         | -0.0842 |
| ctrl_bpc best  | 3.1226         | 3.1109         | -0.0117 |

## Per-round trajectory (best bird: rfYSk)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 795 | 6799 | 3.1109 | +0.4571 |

## Cumulative training contribution

- This harvest: **880 steps** from 11 bird(s)
- Across full ancestry (deduped by bird_id): **1280 steps** from 16 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r794_sym24`
  - `workers/dispatcher/harvest-5way-r794_sym24`

## Output

`workers/dispatcher/harvest-11way-r795_sym24/round-795/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 11 workers)
- `dense.pt` (averaged across 11 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

