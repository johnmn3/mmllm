# harvest-3way-r996 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R996 ctrl_bpc |
|--------|--------|--------------:|
| A1Afi | origin/claude/train-sym24-2112edde-A1Afi | 2.5872 |
| EFd1V | fork-joly-os-mmllm-claude-train-sym24-c481fd8b-EFd1V | 2.7559 |
| nLF9d | fork-SeniorCareMarket-mmllm-claude-train-sym24-c5d18df7-nLF9d | 2.9630 |
| **mean** | | **2.7687** |
| **best** | | **2.5872** |

## Chain progression R995 → R996

Previous harvest: `workers/dispatcher/harvest-3way-r995_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6392         | 2.7687         | +0.1295 |
| ctrl_bpc best  | 2.5605         | 2.5872         | +0.0267 |

## Per-round trajectory (best bird: A1Afi)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 996 | 6746 | 2.5872 | +0.1710 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r995_sym24`

## Output

`workers/dispatcher/harvest-3way-r996_sym24/round-996/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

