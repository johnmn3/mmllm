# harvest-4way-r1416 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1416 ctrl_bpc |
|--------|--------|--------------:|
| aCabN | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-73a6d292-aCabN | 3.1610 |
| ap8jN | origin/claude/train-sym24-81e705cc-ap8jN | 3.1680 |
| tn6VS | fork-joly-os-mmllm-claude-train-sym24-a1e3df62-tn6VS | 3.2306 |
| xgStL | fork-SeniorCareMarket-mmllm-claude-train-sym24-afa26983-xgStL | 3.2356 |
| **mean** | | **3.1988** |
| **best** | | **3.1610** |

## Chain progression R1415 → R1416

Previous harvest: `workers/dispatcher/harvest-4way-r1415_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2046         | 3.1988         | -0.0058 |
| ctrl_bpc best  | 3.1685         | 3.1610         | -0.0075 |

## Per-round trajectory (best bird: aCabN)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1416 | 6662 | 3.1610 | +0.1445 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1415_sym24`

## Output

`workers/dispatcher/harvest-4way-r1416_sym24/round-1416/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

