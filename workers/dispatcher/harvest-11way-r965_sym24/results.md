# harvest-11way-r965 — sparse-delta merge of 11 birds

## Worker endpoints

| handle | branch | R965 ctrl_bpc |
|--------|--------|--------------:|
| blHRz | fork-slaa-us-mmllm-claude-train-sym24-887bfa88-blHRz | 2.6128 |
| 9BfFy | fork-SeniorCareMarket-mmllm-claude-train-sym24-5d62de33-9BfFy | 2.6132 |
| rjGXE | origin/claude/train-sym24-14478184-rjGXE | 2.6486 |
| JPVYV | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-e67e0054-JPVYV | 2.6536 |
| 1BKtw | fork-joly-os-mmllm-claude-train-sym24-bfbe9731-1BKtw | 2.6557 |
| AP9H7 | fork-SeniorCareMarket-mmllm-claude-train-sym24-31633759-AP9H7 | 2.6994 |
| S4aUB | fork-joly-os-mmllm-claude-train-sym24-ec4f501f-S4aUB | 2.8233 |
| nAfSL | origin/claude/train-sym24-838dbbb0-nAfSL | 2.8299 |
| l210L | origin/claude/train-sym24-51554229-l210L | 3.0129 |
| btMez | fork-slaa-us-mmllm-claude-train-sym24-846c714e-btMez | 3.0135 |
| tkgXA | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-6601f6a2-tkgXA | 3.0176 |
| **mean** | | **2.7800** |
| **best** | | **2.6128** |

## Chain progression R964 → R965

Previous harvest: `workers/dispatcher/harvest-5way-r964_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8376         | 2.7800         | -0.0576 |
| ctrl_bpc best  | 2.6209         | 2.6128         | -0.0081 |

## Per-round trajectory (best bird: blHRz)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 965 | 6406 | 2.6128 | +0.1756 |

## Cumulative training contribution

- This harvest: **880 steps** from 11 bird(s)
- Across full ancestry (deduped by bird_id): **1280 steps** from 16 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r964_sym24`
  - `workers/dispatcher/harvest-4way-r964_sym24`
  - `workers/dispatcher/harvest-5way-r964_sym24`

## Output

`workers/dispatcher/harvest-11way-r965_sym24/round-965/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 11 workers)
- `dense.pt` (averaged across 11 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

