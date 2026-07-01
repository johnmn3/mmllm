# harvest-6way-r818 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R818 ctrl_bpc |
|--------|--------|--------------:|
| GkFCM | fork-SeniorCareMarket-mmllm-claude-train-sym24-e8b7032b-GkFCM | 3.0316 |
| CfFq7 | fork-joly-os-mmllm-claude-train-sym24-5defb9f2-CfFq7 | 3.0392 |
| M1Cjw | origin/claude/train-sym24-ce37eec1-M1Cjw | 3.0504 |
| jkmeD | fork-davidwuchn-mmllm-claude-train-sym24-d8b11f3c-jkmeD | 3.1686 |
| Pv0WJ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-79a4588d-Pv0WJ | 3.1792 |
| TEzbV | fork-joly-os-mmllm-claude-train-sym24-3511443a-TEzbV | 3.4547 |
| **mean** | | **3.1540** |
| **best** | | **3.0316** |

## Chain progression R817 → R818

Previous harvest: `workers/dispatcher/harvest-7way-r817_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1794         | 3.1540         | -0.0254 |
| ctrl_bpc best  | 3.0375         | 3.0316         | -0.0059 |

## Per-round trajectory (best bird: GkFCM)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 818 | 6713 | 3.0316 | +0.5319 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r817_sym24`
  - `workers/dispatcher/harvest-5way-r817_sym24`

## Output

`workers/dispatcher/harvest-6way-r818_sym24/round-818/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

