# harvest-2way-r1037 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1037 ctrl_bpc |
|--------|--------|--------------:|
| OByzL | fork-joly-os-mmllm-claude-train-sym24-cf11e192-OByzL | 2.5136 |
| u4sfk | origin/claude/train-sym24-7efe5af1-u4sfk | 2.5571 |
| **mean** | | **2.5354** |
| **best** | | **2.5136** |

## Chain progression R1036 → R1037

Previous harvest: `workers/dispatcher/harvest-5way-r1036_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7457         | 2.5354         | -0.2103 |
| ctrl_bpc best  | 2.5111         | 2.5136         | +0.0025 |

## Per-round trajectory (best bird: OByzL)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1037 | 6523 | 2.5136 | +0.1846 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1036_sym24`

## Output

`workers/dispatcher/harvest-2way-r1037_sym24/round-1037/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

