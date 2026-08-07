# harvest-2way-r1130 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1130 ctrl_bpc |
|--------|--------|--------------:|
| 5Ck5c | origin/claude/train-sym24-db52aa19-5Ck5c | 2.5534 |
| CK31C | fork-joly-os-mmllm-claude-train-sym24-ea1f7eac-CK31C | 2.5568 |
| **mean** | | **2.5551** |
| **best** | | **2.5534** |

## Chain progression R1129 → R1130

Previous harvest: `workers/dispatcher/harvest-6way-r1129_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5958         | 2.5551         | -0.0407 |
| ctrl_bpc best  | 2.3562         | 2.5534         | +0.1972 |

## Per-round trajectory (best bird: 5Ck5c)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1130 | 6449 | 2.5534 | +0.2190 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1129_sym24`

## Output

`workers/dispatcher/harvest-2way-r1130_sym24/round-1130/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

