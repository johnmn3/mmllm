# harvest-5way-r993 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R993 ctrl_bpc |
|--------|--------|--------------:|
| Uemcw | fork-joly-os-mmllm-claude-train-sym24-7172bd70-Uemcw | 2.5936 |
| dkVJs | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-b585c4a6-dkVJs | 2.6125 |
| htp8v | fork-SeniorCareMarket-mmllm-claude-train-sym24-a0bf5605-htp8v | 2.7614 |
| eJck7 | origin/claude/train-sym24-756ad985-eJck7 | 2.9677 |
| aIYFp | origin/claude/train-sym24-64809e95-aIYFp | 2.9741 |
| **mean** | | **2.7819** |
| **best** | | **2.5936** |

## Chain progression R992 → R993

Previous harvest: `workers/dispatcher/harvest-6way-r992_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7737         | 2.7819         | +0.0082 |
| ctrl_bpc best  | 2.5721         | 2.5936         | +0.0215 |

## Per-round trajectory (best bird: Uemcw)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 993 | 6303 | 2.5936 | +0.1673 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r992_sym24`

## Output

`workers/dispatcher/harvest-5way-r993_sym24/round-993/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

