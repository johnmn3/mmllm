# harvest-3way-r1359 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1359 ctrl_bpc |
|--------|--------|--------------:|
| gyssC | origin/claude/train-sym24-28dd145d-gyssC | 3.1518 |
| VUr2d | origin/claude/train-sym24-5edd94a1-VUr2d | 3.1894 |
| 1ihdV | fork-slaa-us-mmllm-claude-train-sym24-207d0865-1ihdV | 3.5662 |
| **mean** | | **3.3025** |
| **best** | | **3.1518** |

## Chain progression R1358 → R1359

Previous harvest: `workers/dispatcher/harvest-6way-r1358_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3534         | 3.3025         | -0.0509 |
| ctrl_bpc best  | 3.1601         | 3.1518         | -0.0083 |

## Per-round trajectory (best bird: gyssC)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1359 | 4390 | 3.1518 | +0.1015 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1358_sym24`
  - `workers/dispatcher/harvest-5way-r1358_sym24`

## Output

`workers/dispatcher/harvest-3way-r1359_sym24/round-1359/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

