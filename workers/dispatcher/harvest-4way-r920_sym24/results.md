# harvest-4way-r920 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R920 ctrl_bpc |
|--------|--------|--------------:|
| GhDcP | fork-joly-os-mmllm-claude-train-sym24-fc458f88-GhDcP | 2.9281 |
| 29zHy | origin/claude/train-sym24-e55e08e0-29zHy | 2.9289 |
| xYuxg | fork-SeniorCareMarket-mmllm-claude-train-sym24-1c526b7c-xYuxg | 2.9479 |
| lY7ra | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-498e6380-lY7ra | 3.1486 |
| **mean** | | **2.9884** |
| **best** | | **2.9281** |

## Chain progression R919 → R920

Previous harvest: `workers/dispatcher/harvest-5way-r919_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9011         | 2.9884         | +0.0873 |
| ctrl_bpc best  | 2.7279         | 2.9281         | +0.2002 |

## Per-round trajectory (best bird: GhDcP)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 920 | 6603 | 2.9281 | +0.1858 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r919_sym24`

## Output

`workers/dispatcher/harvest-4way-r920_sym24/round-920/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

