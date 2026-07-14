# harvest-4way-r916 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R916 ctrl_bpc |
|--------|--------|--------------:|
| cguVd | fork-joly-os-mmllm-claude-train-sym24-ba605b3b-cguVd | 2.7383 |
| lLHuD | origin/claude/train-sym24-ecaf5f17-lLHuD | 2.7570 |
| 3Eyzc | origin/claude/train-sym24-21ce254a-3Eyzc | 2.7618 |
| kU5r2 | fork-slaa-us-mmllm-claude-train-sym24-23282dcf-kU5r2 | 2.7724 |
| **mean** | | **2.7574** |
| **best** | | **2.7383** |

## Chain progression R915 → R916

Previous harvest: `workers/dispatcher/harvest-6way-r915_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8852         | 2.7574         | -0.1278 |
| ctrl_bpc best  | 2.7381         | 2.7383         | +0.0002 |

## Per-round trajectory (best bird: cguVd)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 916 | 6984 | 2.7383 | +0.1898 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r915_sym24`
  - `workers/dispatcher/harvest-6way-r915_sym24`

## Output

`workers/dispatcher/harvest-4way-r916_sym24/round-916/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

