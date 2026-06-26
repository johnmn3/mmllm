# harvest-8way-r774 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R774 ctrl_bpc |
|--------|--------|--------------:|
| Pm0c9 | fork-davidwuchn-mmllm-claude-train-sym24-79ac3cc7-Pm0c9 | 3.2072 |
| Rr9Ri | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-e2e713de-Rr9Ri | 3.2151 |
| NApI5 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-fe8d670d-NApI5 | 3.2152 |
| 53fhr | origin/claude/train-sym24-5867707e-53fhr | 3.2311 |
| 30i6Q | origin/claude/train-sym24-2b2134d6-30i6Q | 3.2533 |
| ODbFX | fork-joly-os-mmllm-claude-train-sym24-e5a85b13-ODbFX | 3.3436 |
| zmARP | fork-slaa-us-mmllm-claude-train-sym24-2d65d34c-zmARP | 3.6090 |
| CdZZu | fork-SeniorCareMarket-mmllm-claude-train-sym24-ad32e84a-CdZZu | 3.6113 |
| **mean** | | **3.3357** |
| **best** | | **3.2072** |

## Chain progression R773 → R774

Previous harvest: `workers/dispatcher/harvest-7way-r773_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3572         | 3.3357         | -0.0215 |
| ctrl_bpc best  | 3.2035         | 3.2072         | +0.0037 |

## Per-round trajectory (best bird: Pm0c9)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 774 | 6461 | 3.2072 | +0.6609 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r773_sym24`

## Output

`workers/dispatcher/harvest-8way-r774_sym24/round-774/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

