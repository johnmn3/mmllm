# harvest-3way-r1124 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1124 ctrl_bpc |
|--------|--------|--------------:|
| AduFU | origin/claude/train-sym24-e9593c52-AduFU | 2.3630 |
| ZBDhh | fork-joly-os-mmllm-claude-train-sym24-7814a285-ZBDhh | 2.3854 |
| jON2q | origin/claude/train-sym24-3a2d32ac-jON2q | 2.3890 |
| **mean** | | **2.3791** |
| **best** | | **2.3630** |

## Chain progression R1123 → R1124

Previous harvest: `workers/dispatcher/harvest-4way-r1123_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6706         | 2.3791         | -0.2915 |
| ctrl_bpc best  | 2.3817         | 2.3630         | -0.0187 |

## Per-round trajectory (best bird: AduFU)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1124 | 4205 | 2.3630 | +0.2544 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1123_sym24`

## Output

`workers/dispatcher/harvest-3way-r1124_sym24/round-1124/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

