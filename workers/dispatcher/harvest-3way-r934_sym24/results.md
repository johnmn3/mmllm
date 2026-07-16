# harvest-3way-r934 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R934 ctrl_bpc |
|--------|--------|--------------:|
| 23SsP | fork-joly-os-mmllm-claude-train-sym24-81759416-23SsP | 2.6981 |
| rgnOo | origin/claude/train-sym24-0b38e053-rgnOo | 2.7404 |
| t7PrQ | origin/claude/train-sym24-474844f3-t7PrQ | 3.1254 |
| **mean** | | **2.8546** |
| **best** | | **2.6981** |

## Chain progression R933 → R934

Previous harvest: `workers/dispatcher/harvest-4way-r933_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7984         | 2.8546         | +0.0562 |
| ctrl_bpc best  | 2.6912         | 2.6981         | +0.0069 |

## Per-round trajectory (best bird: 23SsP)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 934 | 6655 | 2.6981 | +0.1951 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r933_sym24`

## Output

`workers/dispatcher/harvest-3way-r934_sym24/round-934/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

