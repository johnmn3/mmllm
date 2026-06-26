# harvest-4way-r774 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R774 ctrl_bpc |
|--------|--------|--------------:|
| Rr9Ri | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-e2e713de-Rr9Ri | 3.2151 |
| NApI5 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-fe8d670d-NApI5 | 3.2152 |
| 30i6Q | origin/claude/train-sym24-2b2134d6-30i6Q | 3.2533 |
| CdZZu | fork-SeniorCareMarket-mmllm-claude-train-sym24-ad32e84a-CdZZu | 3.6113 |
| **mean** | | **3.3237** |
| **best** | | **3.2151** |

## Chain progression R773 → R774

Previous harvest: `workers/dispatcher/harvest-7way-r773_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3572         | 3.3237         | -0.0335 |
| ctrl_bpc best  | 3.2035         | 3.2151         | +0.0116 |

## Per-round trajectory (best bird: Rr9Ri)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 774 | 6819 | 3.2151 | +0.4541 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r773_sym24`

## Output

`workers/dispatcher/harvest-4way-r774_sym24/round-774/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

