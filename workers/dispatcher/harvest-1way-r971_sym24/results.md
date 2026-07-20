# harvest-1way-r971 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R971 ctrl_bpc |
|--------|--------|--------------:|
| hPHP6 | fork-joly-os-mmllm-claude-train-sym24-82acd91b-hPHP6 | 3.0112 |
| **mean** | | **3.0112** |
| **best** | | **3.0112** |

## Chain progression R970 → R971

Previous harvest: `workers/dispatcher/harvest-2way-r970_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6365         | 3.0112         | +0.3747 |
| ctrl_bpc best  | 2.6210         | 3.0112         | +0.3902 |

## Per-round trajectory (best bird: hPHP6)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 971 | 3582 | 3.0112 | +0.1435 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r970_sym24`

## Output

`workers/dispatcher/harvest-1way-r971_sym24/round-971/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

