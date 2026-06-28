# harvest-2way-r787 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R787 ctrl_bpc |
|--------|--------|--------------:|
| CSR3X | origin/claude/train-sym24-b036a4bd-CSR3X | 3.2241 |
| HUbuA | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-cbb346c9-HUbuA | 3.3000 |
| **mean** | | **3.2620** |
| **best** | | **3.2241** |

## Chain progression R786 → R787

Previous harvest: `workers/dispatcher/harvest-6way-r786_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2236         | 3.2620         | +0.0385 |
| ctrl_bpc best  | 3.1602         | 3.2241         | +0.0639 |

## Per-round trajectory (best bird: CSR3X)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 787 | 6581 | 3.2241 | +0.8101 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r786_sym24`

## Output

`workers/dispatcher/harvest-2way-r787_sym24/round-787/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

