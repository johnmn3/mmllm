# harvest-3way-r770 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R770 ctrl_bpc |
|--------|--------|--------------:|
| nOPIi | fork-joly-os-mmllm-claude-train-sym24-66d76c65-nOPIi | 3.2650 |
| 1dbaI | fork-SeniorCareMarket-mmllm-claude-train-sym24-c6fc627a-1dbaI | 3.2663 |
| aGTS9 | origin/claude/train-sym24-2ed42e6a-aGTS9 | 3.2739 |
| **mean** | | **3.2684** |
| **best** | | **3.2650** |

## Chain progression R769 → R770

Previous harvest: `workers/dispatcher/harvest-5way-r769_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3439         | 3.2684         | -0.0755 |
| ctrl_bpc best  | 3.2235         | 3.2650         | +0.0415 |

## Per-round trajectory (best bird: nOPIi)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 770 | 6564 | 3.2650 | +0.6214 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r769_sym24`

## Output

`workers/dispatcher/harvest-3way-r770_sym24/round-770/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

