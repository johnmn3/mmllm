# harvest-2way-r645 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R645 ctrl_bpc |
|--------|--------|--------------:|
| pdrqv | origin/claude/train-sym24-df785b37-pdrqv | 4.4850 |
| J4K09 | fork-davidwuchn-mmllm-claude-train-sym24-c1b90fef-J4K09 | 4.5000 |
| **mean** | | **4.4925** |
| **best** | | **4.4850** |

## Chain progression R644 → R645

Previous harvest: `workers/dispatcher/harvest-3way-r644_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.5374         | 4.4925         | -0.0449 |
| ctrl_bpc best  | 4.5335         | 4.4850         | -0.0485 |

## Per-round trajectory (best bird: pdrqv)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 645 | 6246 | 4.4850 | +0.0348 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **1360 steps** from 17 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r644_sym24`

## Output

`workers/dispatcher/harvest-2way-r645_sym24/round-645/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

