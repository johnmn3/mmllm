# harvest-6way-r1209 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1209 ctrl_bpc |
|--------|--------|--------------:|
| cZev1 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-0591aee5-cZev1 | 2.2915 |
| Ulf3G | fork-slaa-us-mmllm-claude-train-sym24-65a5c0a9-Ulf3G | 2.2946 |
| nV0D0 | origin/claude/train-sym24-92826860-nV0D0 | 2.4645 |
| vtT7r | fork-SeniorCareMarket-mmllm-claude-train-sym24-b94d73aa-vtT7r | 2.4683 |
| fHqIW | fork-joly-os-mmllm-claude-train-sym24-a0e0c82c-fHqIW | 2.6564 |
| FU3Xu | fork-slaa-us-mmllm-claude-train-sym24-7b4c0964-FU3Xu | 2.6725 |
| **mean** | | **2.4746** |
| **best** | | **2.2915** |

## Chain progression R1208 → R1209

Previous harvest: `workers/dispatcher/harvest-8way-r1208_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4342         | 2.4746         | +0.0404 |
| ctrl_bpc best  | 2.2958         | 2.2915         | -0.0043 |

## Per-round trajectory (best bird: cZev1)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1209 | 4432 | 2.2915 | +0.2550 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1208_sym24`
  - `workers/dispatcher/harvest-6way-r1208_sym24`
  - `workers/dispatcher/harvest-8way-r1208_sym24`

## Output

`workers/dispatcher/harvest-6way-r1209_sym24/round-1209/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

