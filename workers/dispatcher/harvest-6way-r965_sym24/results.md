# harvest-6way-r965 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R965 ctrl_bpc |
|--------|--------|--------------:|
| rjGXE | origin/claude/train-sym24-14478184-rjGXE | 2.6486 |
| JPVYV | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-e67e0054-JPVYV | 2.6536 |
| AP9H7 | fork-SeniorCareMarket-mmllm-claude-train-sym24-31633759-AP9H7 | 2.6994 |
| S4aUB | fork-joly-os-mmllm-claude-train-sym24-ec4f501f-S4aUB | 2.8233 |
| l210L | origin/claude/train-sym24-51554229-l210L | 3.0129 |
| btMez | fork-slaa-us-mmllm-claude-train-sym24-846c714e-btMez | 3.0135 |
| **mean** | | **2.8086** |
| **best** | | **2.6486** |

## Chain progression R964 → R965

Previous harvest: `workers/dispatcher/harvest-5way-r964_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8376         | 2.8086         | -0.0290 |
| ctrl_bpc best  | 2.6209         | 2.6486         | +0.0277 |

## Per-round trajectory (best bird: rjGXE)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 965 | 6756 | 2.6486 | +0.1349 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r964_sym24`
  - `workers/dispatcher/harvest-4way-r964_sym24`

## Output

`workers/dispatcher/harvest-6way-r965_sym24/round-965/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

