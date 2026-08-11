# harvest-9way-r1173 — sparse-delta merge of 9 birds

## Worker endpoints

| handle | branch | R1173 ctrl_bpc |
|--------|--------|--------------:|
| pSHVZ | fork-joly-os-mmllm-claude-train-sym24-4023a9f4-pSHVZ | 2.3085 |
| De4NC | origin/claude/train-sym24-75ead6fd-De4NC | 2.3151 |
| yXkeC | fork-SeniorCareMarket-mmllm-claude-train-sym24-bdaf991c-yXkeC | 2.3307 |
| FQ2b6 | fork-SeniorCareMarket-mmllm-claude-train-sym24-0a08e6aa-FQ2b6 | 2.3358 |
| ggWmB | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-7607e67d-ggWmB | 2.5072 |
| iGXpB | fork-slaa-us-mmllm-claude-train-sym24-8af05a61-iGXpB | 2.5198 |
| hg3RB | fork-joly-os-mmllm-claude-train-sym24-db800429-hg3RB | 2.6946 |
| hgpK3 | origin/claude/train-sym24-fa573510-hgpK3 | 2.7213 |
| aLq1F | fork-slaa-us-mmllm-claude-train-sym24-046ad067-aLq1F | 2.7257 |
| **mean** | | **2.4954** |
| **best** | | **2.3085** |

## Chain progression R1172 → R1173

Previous harvest: `workers/dispatcher/harvest-8way-r1172_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4974         | 2.4954         | -0.0020 |
| ctrl_bpc best  | 2.3251         | 2.3085         | -0.0166 |

## Per-round trajectory (best bird: pSHVZ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1173 | 6532 | 2.3085 | +0.2625 |

## Cumulative training contribution

- This harvest: **720 steps** from 9 bird(s)
- Across full ancestry (deduped by bird_id): **1360 steps** from 17 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1172_sym24`
  - `workers/dispatcher/harvest-8way-r1172_sym24`

## Output

`workers/dispatcher/harvest-9way-r1173_sym24/round-1173/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 9 workers)
- `dense.pt` (averaged across 9 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

