# harvest-4way-r602 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R602 ctrl_bpc |
|--------|--------|--------------:|
| sNGIi | fork-slaa-us-mmllm-claude-train-sym24-a683e51a-sNGIi | 2.1266 |
| 0l8IY | fork-davidwuchn-mmllm-claude-train-sym24-8d3df644-0l8IY | 2.1281 |
| Xmi2v | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-b66c641b-Xmi2v | 2.1305 |
| 8u2pM | fork-joly-os-mmllm-claude-train-sym24-5d08aea9-8u2pM | 2.6115 |
| **mean** | | **2.2492** |
| **best** | | **2.1266** |

## Chain progression R601 → R602

Previous harvest: `workers/dispatcher/harvest-2way-r601_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.1778         | 2.2492         | +0.0714 |
| ctrl_bpc best  | 2.1658         | 2.1266         | -0.0392 |

## Per-round trajectory (best bird: sNGIi)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 602 | 5783 | 2.1266 | +0.0177 |

## Cumulative training contribution

- This harvest: **200 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **200 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r601_sym24`

## Output

`workers/dispatcher/harvest-4way-r602_sym24/round-602/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

