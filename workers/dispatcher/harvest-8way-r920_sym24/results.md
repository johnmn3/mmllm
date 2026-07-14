# harvest-8way-r920 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R920 ctrl_bpc |
|--------|--------|--------------:|
| A5ew3 | fork-slaa-us-mmllm-claude-train-sym24-3946392e-A5ew3 | 2.7414 |
| 30lTl | fork-joly-os-mmllm-claude-train-sym24-f281a87a-30lTl | 2.7507 |
| GhDcP | fork-joly-os-mmllm-claude-train-sym24-fc458f88-GhDcP | 2.9281 |
| 29zHy | origin/claude/train-sym24-e55e08e0-29zHy | 2.9289 |
| xYuxg | fork-SeniorCareMarket-mmllm-claude-train-sym24-1c526b7c-xYuxg | 2.9479 |
| fFViO | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-71b51d13-fFViO | 3.1332 |
| Io9Hn | origin/claude/train-sym24-4ff43b74-Io9Hn | 3.1386 |
| lY7ra | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-498e6380-lY7ra | 3.1486 |
| **mean** | | **2.9647** |
| **best** | | **2.7414** |

## Chain progression R919 → R920

Previous harvest: `workers/dispatcher/harvest-5way-r919_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9011         | 2.9647         | +0.0636 |
| ctrl_bpc best  | 2.7279         | 2.7414         | +0.0135 |

## Per-round trajectory (best bird: A5ew3)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 920 | 6722 | 2.7414 | +0.1731 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r919_sym24`
  - `workers/dispatcher/harvest-5way-r919_sym24`

## Output

`workers/dispatcher/harvest-8way-r920_sym24/round-920/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

