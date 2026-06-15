# harvest-2way-r680 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R680 ctrl_bpc |
|--------|--------|--------------:|
| nc57h | origin/claude/train-sym24-864500f0-nc57h | 3.8210 |
| RVFpY | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-ce37fdc1-RVFpY | 4.0922 |
| **mean** | | **3.9566** |
| **best** | | **3.8210** |

## Chain progression R679 → R680

Previous harvest: `workers/dispatcher/harvest-3way-r679_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.9341         | 3.9566         | +0.0225 |
| ctrl_bpc best  | 3.8387         | 3.8210         | -0.0177 |

## Per-round trajectory (best bird: nc57h)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 680 | 6608 | 3.8210 | +0.5837 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r679_sym24`

## Output

`workers/dispatcher/harvest-2way-r680_sym24/round-680/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

