# harvest-4way-r1077 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1077 ctrl_bpc |
|--------|--------|--------------:|
| 8cFEt | fork-SeniorCareMarket-mmllm-claude-train-sym24-9cf87157-8cFEt | 2.4653 |
| u55TY | fork-joly-os-mmllm-claude-train-sym24-aaaa0d62-u55TY | 2.4670 |
| EETuK | fork-slaa-us-mmllm-claude-train-sym24-ba53b3ad-EETuK | 2.6217 |
| ZNcFf | origin/claude/train-sym24-356be1bb-ZNcFf | 2.6223 |
| **mean** | | **2.5441** |
| **best** | | **2.4653** |

## Chain progression R1076 → R1077

Previous harvest: `workers/dispatcher/harvest-6way-r1076_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5413         | 2.5441         | +0.0028 |
| ctrl_bpc best  | 2.4328         | 2.4653         | +0.0325 |

## Per-round trajectory (best bird: 8cFEt)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1077 | 4145 | 2.4653 | +0.2249 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1076_sym24`

## Output

`workers/dispatcher/harvest-4way-r1077_sym24/round-1077/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

