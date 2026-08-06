# harvest-2way-r1128 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1128 ctrl_bpc |
|--------|--------|--------------:|
| AY5Wk | origin/claude/train-sym24-c7b0845c-AY5Wk | 2.3651 |
| xo6uI | fork-joly-os-mmllm-claude-train-sym24-ff42287d-xo6uI | 2.5605 |
| **mean** | | **2.4628** |
| **best** | | **2.3651** |

## Chain progression R1127 → R1128

Previous harvest: `workers/dispatcher/harvest-5way-r1127_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5211         | 2.4628         | -0.0583 |
| ctrl_bpc best  | 2.3575         | 2.3651         | +0.0076 |

## Per-round trajectory (best bird: AY5Wk)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1128 | 6534 | 2.3651 | +0.2444 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1127_sym24`

## Output

`workers/dispatcher/harvest-2way-r1128_sym24/round-1128/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

