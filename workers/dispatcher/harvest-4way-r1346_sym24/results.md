# harvest-4way-r1346 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1346 ctrl_bpc |
|--------|--------|--------------:|
| VOW3Q | fork-joly-os-mmllm-claude-train-sym24-18c9d8c1-VOW3Q | 3.2506 |
| 7WTkw | origin/claude/train-sym24-41c87a37-7WTkw | 3.2713 |
| Zbrek | origin/claude/train-sym24-6cf7ace1-Zbrek | 3.3066 |
| HxpkC | origin/claude/train-sym24-b62ee0c4-HxpkC | 3.3317 |
| **mean** | | **3.2900** |
| **best** | | **3.2506** |

## Chain progression R1345 → R1346

Previous harvest: `workers/dispatcher/harvest-4way-r1345_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4771         | 3.2900         | -0.1871 |
| ctrl_bpc best  | 3.2448         | 3.2506         | +0.0058 |

## Per-round trajectory (best bird: VOW3Q)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1346 | 3830 | 3.2506 | +0.1033 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1345_sym24`
  - `workers/dispatcher/harvest-4way-r1345_sym24`

## Output

`workers/dispatcher/harvest-4way-r1346_sym24/round-1346/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

