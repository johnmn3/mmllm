# harvest-3way-r815 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R815 ctrl_bpc |
|--------|--------|--------------:|
| DUcgX | origin/claude/train-sym24-913523de-DUcgX | 3.0700 |
| W0n5X | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-3d58d787-W0n5X | 3.4256 |
| NQHtd | fork-joly-os-mmllm-claude-train-sym24-4c4e01e4-NQHtd | 3.4287 |
| **mean** | | **3.3081** |
| **best** | | **3.0700** |

## Chain progression R814 → R815

Previous harvest: `workers/dispatcher/harvest-5way-r814_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1128         | 3.3081         | +0.1953 |
| ctrl_bpc best  | 3.0590         | 3.0700         | +0.0110 |

## Per-round trajectory (best bird: DUcgX)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 815 | 6370 | 3.0700 | +0.5854 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r814_sym24`

## Output

`workers/dispatcher/harvest-3way-r815_sym24/round-815/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

