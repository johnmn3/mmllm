# harvest-14way-r818 — sparse-delta merge of 14 birds

## Worker endpoints

| handle | branch | R818 ctrl_bpc |
|--------|--------|--------------:|
| GkFCM | fork-SeniorCareMarket-mmllm-claude-train-sym24-e8b7032b-GkFCM | 3.0316 |
| vdMOM | fork-slaa-us-mmllm-claude-train-sym24-efc28a72-vdMOM | 3.0339 |
| CfFq7 | fork-joly-os-mmllm-claude-train-sym24-5defb9f2-CfFq7 | 3.0392 |
| BlMYi | fork-davidwuchn-mmllm-claude-train-sym24-892b3eab-BlMYi | 3.0399 |
| s2p3S | fork-slaa-us-mmllm-claude-train-sym24-f1232444-s2p3S | 3.0461 |
| za4ZX | origin/claude/train-sym24-41f02708-za4ZX | 3.0504 |
| M1Cjw | origin/claude/train-sym24-ce37eec1-M1Cjw | 3.0504 |
| TvB0q | fork-davidwuchn-mmllm-claude-train-sym24-ae14b678-TvB0q | 3.0722 |
| jkmeD | fork-davidwuchn-mmllm-claude-train-sym24-d8b11f3c-jkmeD | 3.1686 |
| T0sln | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-e7184557-T0sln | 3.1696 |
| Pv0WJ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-79a4588d-Pv0WJ | 3.1792 |
| DfyFb | origin/claude/train-sym24-6ae51006-DfyFb | 3.4024 |
| A3SnJ | fork-joly-os-mmllm-claude-train-sym24-317e1bf5-A3SnJ | 3.4185 |
| TEzbV | fork-joly-os-mmllm-claude-train-sym24-3511443a-TEzbV | 3.4547 |
| **mean** | | **3.1541** |
| **best** | | **3.0316** |

## Chain progression R817 → R818

Previous harvest: `workers/dispatcher/harvest-7way-r817_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1794         | 3.1541         | -0.0253 |
| ctrl_bpc best  | 3.0375         | 3.0316         | -0.0059 |

## Per-round trajectory (best bird: GkFCM)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 818 | 6713 | 3.0316 | +0.5319 |

## Cumulative training contribution

- This harvest: **1120 steps** from 14 bird(s)
- Across full ancestry (deduped by bird_id): **1680 steps** from 21 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r817_sym24`
  - `workers/dispatcher/harvest-5way-r817_sym24`
  - `workers/dispatcher/harvest-7way-r817_sym24`

## Output

`workers/dispatcher/harvest-14way-r818_sym24/round-818/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 14 workers)
- `dense.pt` (averaged across 14 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

