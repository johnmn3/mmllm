# harvest-5way-r1115 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1115 ctrl_bpc |
|--------|--------|--------------:|
| hOrtG | fork-joly-os-mmllm-claude-train-sym24-24d2e039-hOrtG | 2.3667 |
| Yph4G | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-bfdfc201-Yph4G | 2.3669 |
| bV8IC | fork-SeniorCareMarket-mmllm-claude-train-sym24-721f9d1b-bV8IC | 2.4100 |
| obfbR | fork-joly-os-mmllm-claude-train-sym24-e7b9888a-obfbR | 2.5674 |
| nmON1 | origin/claude/train-sym24-321ec2d4-nmON1 | 2.5722 |
| **mean** | | **2.4566** |
| **best** | | **2.3667** |

## Chain progression R1114 → R1115

Previous harvest: `workers/dispatcher/harvest-10way-r1114_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4821         | 2.4566         | -0.0255 |
| ctrl_bpc best  | 2.3741         | 2.3667         | -0.0074 |

## Per-round trajectory (best bird: hOrtG)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1115 | 6399 | 2.3667 | +0.2531 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1114_sym24`
  - `workers/dispatcher/harvest-8way-r1114_sym24`

## Output

`workers/dispatcher/harvest-5way-r1115_sym24/round-1115/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

