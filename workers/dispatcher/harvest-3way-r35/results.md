# harvest-3way-r35 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R35 ctrl_bpc |
|--------|--------|--------------:|
| qGhOx | origin/claude/train-24b5e7d1-qGhOx | 1.0027 |
| Iixhi | fork-SeniorCareMarket-mmllm-claude-train-2b64bdaf-Iixhi | 1.1670 |
| rARVw | fork-joly-os-mmllm-claude-train-94b400a4-rARVw | 1.1818 |
| **mean** | | **1.1172** |
| **best** | | **1.0027** |

## Chain progression R31 → R35

Previous harvest: `workers/dispatcher/harvest-2way-r31`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 1.2092         | 1.1172         | -0.0920 |
| ctrl_bpc best  | 1.1196         | 1.0027         | -0.1169 |

## Per-round trajectory (best bird: qGhOx)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 32 | 532 | 1.0649 | +0.0064 |
| 33 | 522 | 1.0225 | +0.0074 |
| 34 | 553 | 0.9918 | +0.0034 |
| 35 | 518 | 1.0027 | +0.0086 |

## Cumulative training contribution

- This harvest: **98 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **119 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r30`
  - `workers/dispatcher/harvest-2way-r31`

## Output

`workers/dispatcher/harvest-3way-r35/round-35/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

