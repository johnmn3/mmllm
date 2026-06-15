# harvest-10way-r684 — sparse-delta merge of 10 birds

## Worker endpoints

| handle | branch | R684 ctrl_bpc |
|--------|--------|--------------:|
| oWbIq | fork-davidwuchn-mmllm-claude-train-sym24-724da7ca-oWbIq | 3.7548 |
| XH4Xe | fork-slaa-us-mmllm-claude-train-sym24-2c33f07f-XH4Xe | 3.7671 |
| YAPAM | origin/claude/train-sym24-b393038e-YAPAM | 3.7774 |
| TOHhf | fork-joly-os-mmllm-claude-train-sym24-9673c0ad-TOHhf | 3.7848 |
| fb3Dz | fork-joly-os-mmllm-claude-train-sym24-fad83f7b-fb3Dz | 3.7884 |
| QonDD | origin/claude/train-sym24-20c241da-QonDD | 3.7894 |
| bfn65 | fork-SeniorCareMarket-mmllm-claude-train-sym24-b7658f3c-bfn65 | 3.8228 |
| s1ZrP | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-2c53b4d2-s1ZrP | 4.0715 |
| xlLDu | fork-slaa-us-mmllm-claude-train-sym24-1cd75932-xlLDu | 4.0761 |
| wYEhL | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-d2e5496a-wYEhL | 4.0809 |
| **mean** | | **3.8713** |
| **best** | | **3.7548** |

## Chain progression R683 → R684

Previous harvest: `workers/dispatcher/harvest-7way-r683_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.8825         | 3.8713         | -0.0112 |
| ctrl_bpc best  | 3.7654         | 3.7548         | -0.0106 |

## Per-round trajectory (best bird: oWbIq)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 684 | 6830 | 3.7548 | +0.4364 |

## Cumulative training contribution

- This harvest: **800 steps** from 10 bird(s)
- Across full ancestry (deduped by bird_id): **1360 steps** from 17 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r683_sym24`
  - `workers/dispatcher/harvest-7way-r683_sym24`

## Output

`workers/dispatcher/harvest-10way-r684_sym24/round-684/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 10 workers)
- `dense.pt` (averaged across 10 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

