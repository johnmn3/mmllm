# harvest-6way-r1030 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1030 ctrl_bpc |
|--------|--------|--------------:|
| 4pMYR | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-2a5d26a9-4pMYR | 2.7134 |
| KAYIX | fork-joly-os-mmllm-claude-train-sym24-6bf0291e-KAYIX | 2.8902 |
| M39Vi | fork-slaa-us-mmllm-claude-train-sym24-6b99cd5b-M39Vi | 2.8918 |
| AMnQB | fork-SeniorCareMarket-mmllm-claude-train-sym24-81db6857-AMnQB | 2.8950 |
| zyzDx | fork-joly-os-mmllm-claude-train-sym24-ac433cc0-zyzDx | 2.8989 |
| fZ6X9 | origin/claude/train-sym24-1160bc4f-fZ6X9 | 2.9050 |
| **mean** | | **2.8657** |
| **best** | | **2.7134** |

## Chain progression R1029 → R1030

Previous harvest: `workers/dispatcher/harvest-8way-r1029_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7346         | 2.8657         | +0.1311 |
| ctrl_bpc best  | 2.5272         | 2.7134         | +0.1862 |

## Per-round trajectory (best bird: 4pMYR)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1030 | 5340 | 2.7134 | +0.1653 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1029_sym24`
  - `workers/dispatcher/harvest-8way-r1029_sym24`

## Output

`workers/dispatcher/harvest-6way-r1030_sym24/round-1030/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

