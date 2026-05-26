# harvest-1way-r188 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R188 ctrl_bpc |
|--------|--------|--------------:|
| LzQ4K | fork-davidwuchn-mmllm-claude-train-d526eb07-LzQ4K | 1.1057 |
| **mean** | | **1.1057** |
| **best** | | **1.1057** |

## Chain progression R183 → R188

Previous harvest: `workers/dispatcher/harvest-2way-r183`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 1.1387         | 1.1057         | -0.0330 |
| ctrl_bpc best  | 1.1046         | 1.1057         | +0.0011 |

## Per-round trajectory (best bird: LzQ4K)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 184 | 609 | 1.1151 | +0.0006 |
| 185 | 533 | 1.0878 | -0.0009 |
| 186 | 582 | 1.1324 | +0.0012 |
| 187 | 536 | 1.1199 | +0.0061 |
| 188 | 576 | 1.1057 | +0.0065 |

## Cumulative training contribution

- This harvest: **35 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **3698 steps** from 102 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r183`

## Output

`workers/dispatcher/harvest-1way-r188/round-188/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

