# harvest-3way-r1062 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1062 ctrl_bpc |
|--------|--------|--------------:|
| G0CWi | fork-slaa-us-mmllm-claude-train-sym24-2ef2bb37-G0CWi | 2.6400 |
| 9Ssl4 | fork-joly-os-mmllm-claude-train-sym24-e3602ba4-9Ssl4 | 2.6445 |
| 38Yly | origin/claude/train-sym24-a34d0472-38Yly | 2.6458 |
| **mean** | | **2.6434** |
| **best** | | **2.6400** |

## Chain progression R1061 → R1062

Previous harvest: `workers/dispatcher/harvest-11way-r1061_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5614         | 2.6434         | +0.0820 |
| ctrl_bpc best  | 2.4555         | 2.6400         | +0.1845 |

## Per-round trajectory (best bird: G0CWi)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1062 | 6510 | 2.6400 | +0.2010 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1061_sym24`

## Output

`workers/dispatcher/harvest-3way-r1062_sym24/round-1062/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

