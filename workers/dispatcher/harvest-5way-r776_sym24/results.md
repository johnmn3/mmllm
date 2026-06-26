# harvest-5way-r776 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R776 ctrl_bpc |
|--------|--------|--------------:|
| 2Sd8N | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-b420b794-2Sd8N | 3.2216 |
| w6N9D | origin/claude/train-sym24-b853bda6-w6N9D | 3.2551 |
| agQhY | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-b2e4cddd-agQhY | 3.3236 |
| 8BSZ9 | fork-slaa-us-mmllm-claude-train-sym24-f2976c3d-8BSZ9 | 3.3549 |
| j2xGs | fork-davidwuchn-mmllm-claude-train-sym24-3fd29166-j2xGs | 3.6037 |
| **mean** | | **3.3518** |
| **best** | | **3.2216** |

## Chain progression R775 → R776

Previous harvest: `workers/dispatcher/harvest-6way-r775_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3253         | 3.3518         | +0.0265 |
| ctrl_bpc best  | 3.1992         | 3.2216         | +0.0224 |

## Per-round trajectory (best bird: 2Sd8N)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 776 | 4411 | 3.2216 | +0.4484 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r775_sym24`

## Output

`workers/dispatcher/harvest-5way-r776_sym24/round-776/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

