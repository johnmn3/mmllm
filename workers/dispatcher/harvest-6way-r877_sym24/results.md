# harvest-6way-r877 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R877 ctrl_bpc |
|--------|--------|--------------:|
| NTfze | origin/claude/train-sym24-0f77d349-NTfze | 2.8559 |
| sqXhV | fork-SeniorCareMarket-mmllm-claude-train-sym24-7e7a9123-sqXhV | 2.8571 |
| SqleJ | fork-slaa-us-mmllm-claude-train-sym24-a42c9d0f-SqleJ | 2.9210 |
| M9UFa | fork-joly-os-mmllm-claude-train-sym24-635c9ca0-M9UFa | 3.0086 |
| tGfLF | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-a374ffc1-tGfLF | 3.0193 |
| k8zw6 | origin/claude/train-sym24-f53cd69c-k8zw6 | 3.2350 |
| **mean** | | **2.9828** |
| **best** | | **2.8559** |

## Chain progression R876 → R877

Previous harvest: `workers/dispatcher/harvest-7way-r876_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0438         | 2.9828         | -0.0610 |
| ctrl_bpc best  | 2.8556         | 2.8559         | +0.0003 |

## Per-round trajectory (best bird: NTfze)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 877 | 6666 | 2.8559 | +0.4073 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r876_sym24`
  - `workers/dispatcher/harvest-7way-r876_sym24`

## Output

`workers/dispatcher/harvest-6way-r877_sym24/round-877/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

