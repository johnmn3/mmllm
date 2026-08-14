# harvest-3way-r1198 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1198 ctrl_bpc |
|--------|--------|--------------:|
| cYNII | origin/claude/train-sym24-d0495263-cYNII | 2.2824 |
| vXV5r | fork-SeniorCareMarket-mmllm-claude-train-sym24-2980ad7e-vXV5r | 2.4846 |
| IGEa4 | fork-joly-os-mmllm-claude-train-sym24-19859b39-IGEa4 | 2.6743 |
| **mean** | | **2.4804** |
| **best** | | **2.2824** |

## Chain progression R1197 → R1198

Previous harvest: `workers/dispatcher/harvest-6way-r1197_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3324         | 2.4804         | +0.1480 |
| ctrl_bpc best  | 2.2859         | 2.2824         | -0.0035 |

## Per-round trajectory (best bird: cYNII)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1198 | 6377 | 2.2824 | +0.2692 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1197_sym24`

## Output

`workers/dispatcher/harvest-3way-r1198_sym24/round-1198/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

