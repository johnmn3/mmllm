# harvest-17way-r653 — sparse-delta merge of 17 birds

## Worker endpoints

| handle | branch | R653 ctrl_bpc |
|--------|--------|--------------:|
| Wrd1t | fork-davidwuchn-mmllm-claude-train-sym24-98d059ff-Wrd1t | 4.1705 |
| 3V8eN | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-31716792-3V8eN | 4.1760 |
| AMvAT | fork-slaa-us-mmllm-claude-train-sym24-f0660ac8-AMvAT | 4.2051 |
| 8KLIF | fork-joly-os-mmllm-claude-train-sym24-be441326-8KLIF | 4.2088 |
| mZA5o | fork-davidwuchn-mmllm-claude-train-sym24-e15786b8-mZA5o | 4.2147 |
| RbkEU | fork-joly-os-mmllm-claude-train-sym24-c4157bf0-RbkEU | 4.2194 |
| Fv3GY | fork-slaa-us-mmllm-claude-train-sym24-6e5744b7-Fv3GY | 4.2211 |
| 3AuOt | origin/claude/train-sym24-46040a68-3AuOt | 4.2241 |
| MnWzT | fork-slaa-us-mmllm-claude-train-sym24-9d97d252-MnWzT | 4.5924 |
| hl0xY | fork-slaa-us-mmllm-claude-train-sym24-c3d0cba5-hl0xY | 4.5934 |
| Gbqma | origin/claude/train-sym24-533d4d33-Gbqma | 4.5993 |
| LndsO | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-470e5771-LndsO | 4.5994 |
| Trcaq | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-d99aa0ce-Trcaq | 4.6018 |
| LGCKS | fork-davidwuchn-mmllm-claude-train-sym24-6dc88ac2-LGCKS | 4.6038 |
| BrABc | fork-joly-os-mmllm-claude-train-sym24-13c55de8-BrABc | 4.6056 |
| GtAro | fork-SeniorCareMarket-mmllm-claude-train-sym24-5074b17e-GtAro | 4.6166 |
| LIVW16 | origin/claude/train-sym24-LIVW16 | — |
| **mean** | | **4.4032** |
| **best** | | **4.1705** |

## Chain progression R652 → R653

Previous harvest: `workers/dispatcher/harvest-1way-r652_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.2079         | 4.4032         | +0.1953 |
| ctrl_bpc best  | 4.2079         | 4.1705         | -0.0374 |

## Per-round trajectory (best bird: Wrd1t)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 653 | 6524 | 4.1705 | +0.0287 |

## Cumulative training contribution

- This harvest: **1280 steps** from 17 bird(s)
- Across full ancestry (deduped by bird_id): **1760 steps** from 23 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r652_sym24`

## Output

`workers/dispatcher/harvest-17way-r653_sym24/round-653/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 17 workers)
- `dense.pt` (averaged across 17 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

