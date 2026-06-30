# harvest-9way-r811 — sparse-delta merge of 9 birds

## Worker endpoints

| handle | branch | R811 ctrl_bpc |
|--------|--------|--------------:|
| Sq0F8 | fork-davidwuchn-mmllm-claude-train-sym24-7a3c2b6c-Sq0F8 | 3.0709 |
| 8rCvI | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-9704444d-8rCvI | 3.0762 |
| POCD1 | origin/claude/train-sym24-3b7a6647-POCD1 | 3.0938 |
| qjVcV | fork-slaa-us-mmllm-claude-train-sym24-d755ca3e-qjVcV | 3.1926 |
| WXi2V | origin/claude/train-sym24-52787350-WXi2V | 3.1947 |
| pw0z6 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-88771043-pw0z6 | 3.4169 |
| LMZDG | fork-slaa-us-mmllm-claude-train-sym24-ccbf167c-LMZDG | 3.4336 |
| 7jUDl | fork-joly-os-mmllm-claude-train-sym24-da6b23ed-7jUDl | 3.4355 |
| ITre4 | fork-davidwuchn-mmllm-claude-train-sym24-261aac1f-ITre4 | 3.4631 |
| **mean** | | **3.2641** |
| **best** | | **3.0709** |

## Chain progression R810 → R811

Previous harvest: `workers/dispatcher/harvest-6way-r810_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3400         | 3.2641         | -0.0759 |
| ctrl_bpc best  | 3.0707         | 3.0709         | +0.0002 |

## Per-round trajectory (best bird: Sq0F8)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 811 | 4198 | 3.0709 | +0.5846 |

## Cumulative training contribution

- This harvest: **720 steps** from 9 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r810_sym24`
  - `workers/dispatcher/harvest-6way-r810_sym24`

## Output

`workers/dispatcher/harvest-9way-r811_sym24/round-811/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 9 workers)
- `dense.pt` (averaged across 9 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

