# harvest-4way-r662 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R662 ctrl_bpc |
|--------|--------|--------------:|
| CP1n3 | origin/claude/train-sym24-bd1b8fe6-CP1n3 | 3.9717 |
| YjFUZ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-c745defd-YjFUZ | 3.9780 |
| mGXrN | fork-slaa-us-mmllm-claude-train-sym24-dce6a368-mGXrN | 4.0226 |
| aBsTP | fork-davidwuchn-mmllm-claude-train-sym24-7b07178d-aBsTP | 4.3915 |
| **mean** | | **4.0909** |
| **best** | | **3.9717** |

## Chain progression R661 → R662

Previous harvest: `workers/dispatcher/harvest-1way-r661_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.0532         | 4.0909         | +0.0377 |
| ctrl_bpc best  | 4.0532         | 3.9717         | -0.0815 |

## Per-round trajectory (best bird: CP1n3)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 662 | 6798 | 3.9717 | +0.1709 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r661_sym24`

## Output

`workers/dispatcher/harvest-4way-r662_sym24/round-662/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

