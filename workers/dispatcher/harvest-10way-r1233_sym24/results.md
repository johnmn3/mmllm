# harvest-10way-r1233 — sparse-delta merge of 10 birds

## Worker endpoints

| handle | branch | R1233 ctrl_bpc |
|--------|--------|--------------:|
| 0IynS | fork-joly-os-mmllm-claude-train-sym24-71e070de-0IynS | 2.2453 |
| lOrDN | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-6bd297e0-lOrDN | 2.2568 |
| hcIpg | fork-slaa-us-mmllm-claude-train-sym24-6e825041-hcIpg | 2.2570 |
| K8FGU | fork-joly-os-mmllm-claude-train-sym24-c9c09691-K8FGU | 2.2727 |
| tSa7n | origin/claude/train-sym24-5321ae55-tSa7n | 2.4527 |
| YvpRl | fork-SeniorCareMarket-mmllm-claude-train-sym24-426a4e53-YvpRl | 2.4558 |
| cc1Sr | origin/claude/train-sym24-f28cf36a-cc1Sr | 2.4620 |
| oKXXN | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-3219616f-oKXXN | 2.4632 |
| 1XJdn | fork-slaa-us-mmllm-claude-train-sym24-e2144680-1XJdn | 2.4659 |
| tNiB7 | fork-SeniorCareMarket-mmllm-claude-train-sym24-6d0c2955-tNiB7 | 2.6564 |
| **mean** | | **2.3988** |
| **best** | | **2.2453** |

## Chain progression R1232 → R1233

Previous harvest: `workers/dispatcher/harvest-13way-r1232_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4457         | 2.3988         | -0.0469 |
| ctrl_bpc best  | 2.2508         | 2.2453         | -0.0055 |

## Per-round trajectory (best bird: 0IynS)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1233 | 6578 | 2.2453 | +0.2666 |

## Cumulative training contribution

- This harvest: **800 steps** from 10 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-10way-r1232_sym24`
  - `workers/dispatcher/harvest-4way-r1232_sym24`

## Output

`workers/dispatcher/harvest-10way-r1233_sym24/round-1233/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 10 workers)
- `dense.pt` (averaged across 10 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

