# harvest-2way-r1193 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1193 ctrl_bpc |
|--------|--------|--------------:|
| yEXFT | origin/claude/train-sym24-91914b2f-yEXFT | 2.3101 |
| VuRgc | fork-joly-os-mmllm-claude-train-sym24-816d0e4f-VuRgc | 2.3117 |
| **mean** | | **2.3109** |
| **best** | | **2.3101** |

## Chain progression R1192 → R1193

Previous harvest: `workers/dispatcher/harvest-6way-r1192_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5233         | 2.3109         | -0.2124 |
| ctrl_bpc best  | 2.2912         | 2.3101         | +0.0189 |

## Per-round trajectory (best bird: yEXFT)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1193 | 5413 | 2.3101 | +0.2398 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1192_sym24`

## Output

`workers/dispatcher/harvest-2way-r1193_sym24/round-1193/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

