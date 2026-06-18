# harvest-15way-r702 — sparse-delta merge of 15 birds

## Worker endpoints

| handle | branch | R702 ctrl_bpc |
|--------|--------|--------------:|
| s4SR4 | origin/claude/train-sym24-594ef83c-s4SR4 | 3.6065 |
| zqSFB | origin/claude/train-sym24-461cfd61-zqSFB | 3.6102 |
| oxp6Y | origin/claude/train-sym24-be0872f0-oxp6Y | 3.6138 |
| MSTGl | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-a6bcd52a-MSTGl | 3.6454 |
| uZ6oT | fork-SeniorCareMarket-mmllm-claude-train-sym24-08c25920-uZ6oT | 3.6469 |
| pbt0l | fork-slaa-us-mmllm-claude-train-sym24-6688236c-pbt0l | 3.6486 |
| wLHSH | fork-davidwuchn-mmllm-claude-train-sym24-339c7bbb-wLHSH | 3.6523 |
| hehCi | fork-slaa-us-mmllm-claude-train-sym24-3fbbd732-hehCi | 3.6531 |
| GYaH1 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-fe27ede0-GYaH1 | 3.6641 |
| JgGEG | fork-slaa-us-mmllm-claude-train-sym24-dea4ccaf-JgGEG | 3.6647 |
| 2bA5G | fork-joly-os-mmllm-claude-train-sym24-25d4ae8b-2bA5G | 3.9406 |
| N2m5x | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-2210e62e-N2m5x | 3.9520 |
| hmDdJ | fork-davidwuchn-mmllm-claude-train-sym24-429107ff-hmDdJ | 3.9607 |
| Kv1TW | fork-joly-os-mmllm-claude-train-sym24-45461c7f-Kv1TW | 3.9658 |
| m5BVX | fork-joly-os-mmllm-claude-train-sym24-93c23940-m5BVX | 3.9859 |
| **mean** | | **3.7474** |
| **best** | | **3.6065** |

## Chain progression R701 → R702

Previous harvest: `workers/dispatcher/harvest-7way-r701_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.8313         | 3.7474         | -0.0839 |
| ctrl_bpc best  | 3.6070         | 3.6065         | -0.0005 |

## Per-round trajectory (best bird: s4SR4)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 702 | 6658 | 3.6065 | +0.8344 |

## Cumulative training contribution

- This harvest: **1200 steps** from 15 bird(s)
- Across full ancestry (deduped by bird_id): **1760 steps** from 22 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-10way-r701_sym24`
  - `workers/dispatcher/harvest-7way-r701_sym24`

## Output

`workers/dispatcher/harvest-15way-r702_sym24/round-702/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 15 workers)
- `dense.pt` (averaged across 15 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

