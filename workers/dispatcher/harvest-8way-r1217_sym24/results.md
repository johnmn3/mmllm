# harvest-8way-r1217 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R1217 ctrl_bpc |
|--------|--------|--------------:|
| Qlqlj | fork-slaa-us-mmllm-claude-train-sym24-71712104-Qlqlj | 2.2655 |
| EIARu | fork-slaa-us-mmllm-claude-train-sym24-0b86f474-EIARu | 2.2690 |
| WnWEG | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-cadcad20-WnWEG | 2.2915 |
| Iwube | origin/claude/train-sym24-fc956016-Iwube | 2.4662 |
| R5dMC | fork-joly-os-mmllm-claude-train-sym24-43a6a707-R5dMC | 2.4669 |
| wRHLb | fork-joly-os-mmllm-claude-train-sym24-743e5af3-wRHLb | 2.4705 |
| 4RYzV | fork-SeniorCareMarket-mmllm-claude-train-sym24-b187e507-4RYzV | 2.4709 |
| Lh1Ij | origin/claude/train-sym24-f240adba-Lh1Ij | 2.4737 |
| **mean** | | **2.3968** |
| **best** | | **2.2655** |

## Chain progression R1216 → R1217

Previous harvest: `workers/dispatcher/harvest-5way-r1216_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3921         | 2.3968         | +0.0047 |
| ctrl_bpc best  | 2.2672         | 2.2655         | -0.0017 |

## Per-round trajectory (best bird: Qlqlj)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1217 | 6508 | 2.2655 | +0.2593 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1216_sym24`
  - `workers/dispatcher/harvest-5way-r1216_sym24`

## Output

`workers/dispatcher/harvest-8way-r1217_sym24/round-1217/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

