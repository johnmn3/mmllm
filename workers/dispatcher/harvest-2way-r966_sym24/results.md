# harvest-2way-r966 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R966 ctrl_bpc |
|--------|--------|--------------:|
| Mo0hx | fork-joly-os-mmllm-claude-train-sym24-8f389259-Mo0hx | 2.8159 |
| JgLRP | fork-slaa-us-mmllm-claude-train-sym24-1dc5065d-JgLRP | 2.8259 |
| **mean** | | **2.8209** |
| **best** | | **2.8159** |

## Chain progression R965 → R966

Previous harvest: `workers/dispatcher/harvest-11way-r965_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7800         | 2.8209         | +0.0409 |
| ctrl_bpc best  | 2.6128         | 2.8159         | +0.2031 |

## Per-round trajectory (best bird: Mo0hx)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 966 | 6404 | 2.8159 | +0.1487 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r965_sym24`
  - `workers/dispatcher/harvest-6way-r965_sym24`

## Output

`workers/dispatcher/harvest-2way-r966_sym24/round-966/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

