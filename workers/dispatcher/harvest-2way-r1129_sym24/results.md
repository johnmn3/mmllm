# harvest-2way-r1129 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1129 ctrl_bpc |
|--------|--------|--------------:|
| JvhW0 | origin/claude/train-sym24-b12f11e7-JvhW0 | 2.3562 |
| iJtoi | fork-joly-os-mmllm-claude-train-sym24-1ec24814-iJtoi | 2.7579 |
| **mean** | | **2.5570** |
| **best** | | **2.3562** |

## Chain progression R1128 → R1129

Previous harvest: `workers/dispatcher/harvest-6way-r1128_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5271         | 2.5570         | +0.0299 |
| ctrl_bpc best  | 2.3548         | 2.3562         | +0.0014 |

## Per-round trajectory (best bird: JvhW0)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1129 | 6694 | 2.3562 | +0.2459 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1128_sym24`

## Output

`workers/dispatcher/harvest-2way-r1129_sym24/round-1129/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

