# harvest-2way-r1327 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1327 ctrl_bpc |
|--------|--------|--------------:|
| ojVxS | fork-joly-os-mmllm-claude-train-sym24-d9446a15-ojVxS | 3.3823 |
| c21SV | fork-SeniorCareMarket-mmllm-claude-train-sym24-3b804734-c21SV | 3.6882 |
| **mean** | | **3.5353** |
| **best** | | **3.3823** |

## Chain progression R1326 → R1327

Previous harvest: `workers/dispatcher/harvest-7way-r1326_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4238         | 3.5353         | +0.1115 |
| ctrl_bpc best  | 3.3055         | 3.3823         | +0.0768 |

## Per-round trajectory (best bird: ojVxS)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1327 | 3486 | 3.3823 | +0.0743 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1326_sym24`

## Output

`workers/dispatcher/harvest-2way-r1327_sym24/round-1327/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

