# harvest-3way-r690 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R690 ctrl_bpc |
|--------|--------|--------------:|
| Z8uBM | fork-SeniorCareMarket-mmllm-claude-train-sym24-f922b5e6-Z8uBM | 3.7260 |
| qFvvX | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-4667b76b-qFvvX | 3.7443 |
| RRGRG | fork-slaa-us-mmllm-claude-train-sym24-6bb66de8-RRGRG | 4.0100 |
| **mean** | | **3.8268** |
| **best** | | **3.7260** |

## Chain progression R689 → R690

Previous harvest: `workers/dispatcher/harvest-8way-r689_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.7660         | 3.8268         | +0.0608 |
| ctrl_bpc best  | 3.7351         | 3.7260         | -0.0091 |

## Per-round trajectory (best bird: Z8uBM)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 690 | 6706 | 3.7260 | +0.8104 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r689_sym24`

## Output

`workers/dispatcher/harvest-3way-r690_sym24/round-690/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

