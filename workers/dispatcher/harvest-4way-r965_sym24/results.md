# harvest-4way-r965 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R965 ctrl_bpc |
|--------|--------|--------------:|
| JPVYV | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-e67e0054-JPVYV | 2.6536 |
| AP9H7 | fork-SeniorCareMarket-mmllm-claude-train-sym24-31633759-AP9H7 | 2.6994 |
| S4aUB | fork-joly-os-mmllm-claude-train-sym24-ec4f501f-S4aUB | 2.8233 |
| l210L | origin/claude/train-sym24-51554229-l210L | 3.0129 |
| **mean** | | **2.7973** |
| **best** | | **2.6536** |

## Chain progression R964 → R965

Previous harvest: `workers/dispatcher/harvest-5way-r964_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8376         | 2.7973         | -0.0403 |
| ctrl_bpc best  | 2.6209         | 2.6536         | +0.0327 |

## Per-round trajectory (best bird: JPVYV)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 965 | 7463 | 2.6536 | +0.1524 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r964_sym24`

## Output

`workers/dispatcher/harvest-4way-r965_sym24/round-965/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

