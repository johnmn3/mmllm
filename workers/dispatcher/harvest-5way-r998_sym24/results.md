# harvest-5way-r998 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R998 ctrl_bpc |
|--------|--------|--------------:|
| 0ItRN | origin/claude/train-sym24-0efd33c9-0ItRN | 2.5736 |
| 1wYoz | origin/claude/train-sym24-9ef82851-1wYoz | 2.7531 |
| uhlhY | fork-joly-os-mmllm-claude-train-sym24-f754b0a8-uhlhY | 2.9541 |
| K9hDA | fork-slaa-us-mmllm-claude-train-sym24-c065aee7-K9hDA | 2.9745 |
| EkvvQ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-efa8ffbc-EkvvQ | 3.0029 |
| **mean** | | **2.8516** |
| **best** | | **2.5736** |

## Chain progression R997 → R998

Previous harvest: `workers/dispatcher/harvest-4way-r997_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6755         | 2.8516         | +0.1761 |
| ctrl_bpc best  | 2.5719         | 2.5736         | +0.0017 |

## Per-round trajectory (best bird: 0ItRN)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 998 | 6556 | 2.5736 | +0.1759 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r997_sym24`

## Output

`workers/dispatcher/harvest-5way-r998_sym24/round-998/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

