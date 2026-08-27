# harvest-4way-r1333 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1333 ctrl_bpc |
|--------|--------|--------------:|
| S6bvq | fork-slaa-us-mmllm-claude-train-sym24-0676ee6a-S6bvq | 3.3036 |
| IybJ1 | origin/claude/train-sym24-7411d82c-IybJ1 | 3.3198 |
| 8y9cC | fork-joly-os-mmllm-claude-train-sym24-2542798d-8y9cC | 3.3413 |
| 9VP3C | origin/claude/train-sym24-cac9d1d0-9VP3C | 3.6453 |
| **mean** | | **3.4025** |
| **best** | | **3.3036** |

## Chain progression R1332 → R1333

Previous harvest: `workers/dispatcher/harvest-2way-r1332_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3550         | 3.4025         | +0.0475 |
| ctrl_bpc best  | 3.3489         | 3.3036         | -0.0453 |

## Per-round trajectory (best bird: S6bvq)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1333 | 6534 | 3.3036 | +0.1083 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1332_sym24`

## Output

`workers/dispatcher/harvest-4way-r1333_sym24/round-1333/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

