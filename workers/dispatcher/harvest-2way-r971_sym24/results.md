# harvest-2way-r971 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R971 ctrl_bpc |
|--------|--------|--------------:|
| eDIok | origin/claude/train-sym24-3f2fda45-eDIok | 2.6572 |
| hPHP6 | fork-joly-os-mmllm-claude-train-sym24-82acd91b-hPHP6 | 3.0112 |
| **mean** | | **2.8342** |
| **best** | | **2.6572** |

## Chain progression R970 → R971

Previous harvest: `workers/dispatcher/harvest-2way-r970_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6365         | 2.8342         | +0.1977 |
| ctrl_bpc best  | 2.6210         | 2.6572         | +0.0362 |

## Per-round trajectory (best bird: eDIok)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 971 | 6396 | 2.6572 | +0.1458 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r970_sym24`

## Output

`workers/dispatcher/harvest-2way-r971_sym24/round-971/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

