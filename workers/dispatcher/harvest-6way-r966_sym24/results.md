# harvest-6way-r966 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R966 ctrl_bpc |
|--------|--------|--------------:|
| Ft1fR | origin/claude/train-sym24-9cce12d1-Ft1fR | 2.6255 |
| gDsoD | origin/claude/train-sym24-7dad9918-gDsoD | 2.6262 |
| Sljvf | fork-SeniorCareMarket-mmllm-claude-train-sym24-2c62a125-Sljvf | 2.6507 |
| Mo0hx | fork-joly-os-mmllm-claude-train-sym24-8f389259-Mo0hx | 2.8159 |
| 1dkgR | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-290cd959-1dkgR | 2.8188 |
| JgLRP | fork-slaa-us-mmllm-claude-train-sym24-1dc5065d-JgLRP | 2.8259 |
| **mean** | | **2.7272** |
| **best** | | **2.6255** |

## Chain progression R965 → R966

Previous harvest: `workers/dispatcher/harvest-6way-r965_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8086         | 2.7272         | -0.0814 |
| ctrl_bpc best  | 2.6486         | 2.6255         | -0.0231 |

## Per-round trajectory (best bird: Ft1fR)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 966 | 6572 | 2.6255 | +0.1647 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r965_sym24`
  - `workers/dispatcher/harvest-6way-r965_sym24`

## Output

`workers/dispatcher/harvest-6way-r966_sym24/round-966/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

