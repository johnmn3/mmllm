# harvest-1way-r661 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R661 ctrl_bpc |
|--------|--------|--------------:|
| mkdR3 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-cdc6bd7e-mkdR3 | 4.0532 |
| **mean** | | **4.0532** |
| **best** | | **4.0532** |

## Chain progression R660 → R661

Previous harvest: `workers/dispatcher/harvest-13way-r660_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.0634         | 4.0532         | -0.0102 |
| ctrl_bpc best  | 3.9990         | 4.0532         | +0.0542 |

## Per-round trajectory (best bird: mkdR3)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 661 | 4325 | 4.0532 | +0.0918 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-7way-r660_sym24`

## Output

`workers/dispatcher/harvest-1way-r661_sym24/round-661/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

