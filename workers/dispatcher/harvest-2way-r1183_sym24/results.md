# harvest-2way-r1183 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1183 ctrl_bpc |
|--------|--------|--------------:|
| gjqxF | origin/claude/train-sym24-22dfc7a6-gjqxF | 2.3330 |
| PkLII | fork-joly-os-mmllm-claude-train-sym24-cac30855-PkLII | 2.5004 |
| **mean** | | **2.4167** |
| **best** | | **2.3330** |

## Chain progression R1182 → R1183

Previous harvest: `workers/dispatcher/harvest-4way-r1182_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5068         | 2.4167         | -0.0901 |
| ctrl_bpc best  | 2.3076         | 2.3330         | +0.0254 |

## Per-round trajectory (best bird: gjqxF)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1183 | 6603 | 2.3330 | +0.2325 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1182_sym24`

## Output

`workers/dispatcher/harvest-2way-r1183_sym24/round-1183/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

