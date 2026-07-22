# harvest-2way-r988 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R988 ctrl_bpc |
|--------|--------|--------------:|
| r9lpE | fork-joly-os-mmllm-claude-train-sym24-e8e76820-r9lpE | 2.8005 |
| pHqnb | origin/claude/train-sym24-dbe4d10d-pHqnb | 2.9822 |
| **mean** | | **2.8914** |
| **best** | | **2.8005** |

## Chain progression R987 → R988

Previous harvest: `workers/dispatcher/harvest-5way-r987_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6106         | 2.8914         | +0.2808 |
| ctrl_bpc best  | 2.5988         | 2.8005         | +0.2017 |

## Per-round trajectory (best bird: r9lpE)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 988 | 3841 | 2.8005 | +0.1590 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r987_sym24`

## Output

`workers/dispatcher/harvest-2way-r988_sym24/round-988/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

