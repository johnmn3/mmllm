# harvest-8way-r702 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R702 ctrl_bpc |
|--------|--------|--------------:|
| oxp6Y | origin/claude/train-sym24-be0872f0-oxp6Y | 3.6138 |
| pbt0l | fork-slaa-us-mmllm-claude-train-sym24-6688236c-pbt0l | 3.6486 |
| wLHSH | fork-davidwuchn-mmllm-claude-train-sym24-339c7bbb-wLHSH | 3.6523 |
| hehCi | fork-slaa-us-mmllm-claude-train-sym24-3fbbd732-hehCi | 3.6531 |
| GYaH1 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-fe27ede0-GYaH1 | 3.6641 |
| 2bA5G | fork-joly-os-mmllm-claude-train-sym24-25d4ae8b-2bA5G | 3.9406 |
| N2m5x | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-2210e62e-N2m5x | 3.9520 |
| m5BVX | fork-joly-os-mmllm-claude-train-sym24-93c23940-m5BVX | 3.9859 |
| **mean** | | **3.7638** |
| **best** | | **3.6138** |

## Chain progression R701 → R702

Previous harvest: `workers/dispatcher/harvest-15way-r701_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.7541         | 3.7638         | +0.0097 |
| ctrl_bpc best  | 3.6058         | 3.6138         | +0.0080 |

## Per-round trajectory (best bird: oxp6Y)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 702 | 6511 | 3.6138 | +1.0088 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-10way-r701_sym24`
  - `workers/dispatcher/harvest-7way-r701_sym24`

## Output

`workers/dispatcher/harvest-8way-r702_sym24/round-702/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

