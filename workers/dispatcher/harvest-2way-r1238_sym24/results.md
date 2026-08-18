# harvest-2way-r1238 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1238 ctrl_bpc |
|--------|--------|--------------:|
| NKdxW | fork-joly-os-mmllm-claude-train-sym24-f18fcc9a-NKdxW | 2.2565 |
| DIuCQ | origin/claude/train-sym24-c050d3ed-DIuCQ | 2.4570 |
| **mean** | | **2.3567** |
| **best** | | **2.2565** |

## Chain progression R1237 → R1238

Previous harvest: `workers/dispatcher/harvest-6way-r1237_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3967         | 2.3567         | -0.0400 |
| ctrl_bpc best  | 2.2652         | 2.2565         | -0.0087 |

## Per-round trajectory (best bird: NKdxW)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1238 | 6390 | 2.2565 | +0.2537 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1237_sym24`

## Output

`workers/dispatcher/harvest-2way-r1238_sym24/round-1238/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

