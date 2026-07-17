# harvest-3way-r947 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R947 ctrl_bpc |
|--------|--------|--------------:|
| n5f9C | origin/claude/train-sym24-f30d8960-n5f9C | 2.6663 |
| oNQY0 | fork-joly-os-mmllm-claude-train-sym24-60fb8017-oNQY0 | 2.8610 |
| K1Yqd | origin/claude/train-sym24-aed09962-K1Yqd | 2.8648 |
| **mean** | | **2.7974** |
| **best** | | **2.6663** |

## Chain progression R946 → R947

Previous harvest: `workers/dispatcher/harvest-7way-r946_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8237         | 2.7974         | -0.0263 |
| ctrl_bpc best  | 2.6733         | 2.6663         | -0.0070 |

## Per-round trajectory (best bird: n5f9C)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 947 | 6495 | 2.6663 | +0.2081 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r946_sym24`

## Output

`workers/dispatcher/harvest-3way-r947_sym24/round-947/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

