# harvest-3way-r986 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R986 ctrl_bpc |
|--------|--------|--------------:|
| vdJmb | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-8487efd2-vdJmb | 2.5851 |
| tYBy0 | origin/claude/train-sym24-598f8b09-tYBy0 | 2.6119 |
| Z3eEl | fork-slaa-us-mmllm-claude-train-sym24-2d0c1bd5-Z3eEl | 2.9758 |
| **mean** | | **2.7243** |
| **best** | | **2.5851** |

## Chain progression R985 → R986

Previous harvest: `workers/dispatcher/harvest-6way-r985_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7615         | 2.7243         | -0.0372 |
| ctrl_bpc best  | 2.6128         | 2.5851         | -0.0277 |

## Per-round trajectory (best bird: vdJmb)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 986 | 5390 | 2.5851 | +0.1896 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r985_sym24`

## Output

`workers/dispatcher/harvest-3way-r986_sym24/round-986/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

