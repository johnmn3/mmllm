# harvest-9way-r1155 — sparse-delta merge of 9 birds

## Worker endpoints

| handle | branch | R1155 ctrl_bpc |
|--------|--------|--------------:|
| B1A7Z | origin/claude/train-sym24-35a2f051-B1A7Z | 2.3277 |
| Qv1af | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-2d365271-Qv1af | 2.3387 |
| nzuru | origin/claude/train-sym24-07d9d260-nzuru | 2.3547 |
| KTu3c | fork-slaa-us-mmllm-claude-train-sym24-b3f43460-KTu3c | 2.3549 |
| Gal7J | fork-SeniorCareMarket-mmllm-claude-train-sym24-eb3ba357-Gal7J | 2.3615 |
| ozvUZ | fork-SeniorCareMarket-mmllm-claude-train-sym24-499c8f17-ozvUZ | 2.3636 |
| M4k3D | fork-joly-os-mmllm-claude-train-sym24-83b65ae7-M4k3D | 2.7154 |
| n5KZT | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-01122453-n5KZT | 2.7273 |
| a4xKr | fork-joly-os-mmllm-claude-train-sym24-1676ef7e-a4xKr | 2.7441 |
| **mean** | | **2.4764** |
| **best** | | **2.3277** |

## Chain progression R1154 → R1155

Previous harvest: `workers/dispatcher/harvest-6way-r1154_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6273         | 2.4764         | -0.1509 |
| ctrl_bpc best  | 2.3659         | 2.3277         | -0.0382 |

## Per-round trajectory (best bird: B1A7Z)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1155 | 6702 | 2.3277 | +0.2562 |

## Cumulative training contribution

- This harvest: **720 steps** from 9 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1154_sym24`
  - `workers/dispatcher/harvest-6way-r1154_sym24`

## Output

`workers/dispatcher/harvest-9way-r1155_sym24/round-1155/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 9 workers)
- `dense.pt` (averaged across 9 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

