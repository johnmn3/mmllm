# harvest-3way-r78 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R78 ctrl_bpc |
|--------|--------|--------------:|
| SRW00 | origin/claude/train-c0df53bf-SRW00 | 0.9208 |
| 1hnSa | origin/claude/train-4b11df55-1hnSa | 0.9644 |
| UIYOe | origin/claude/train-6abbbf8f-UIYOe | 1.0953 |
| **mean** | | **0.9935** |
| **best** | | **0.9208** |

## Chain progression R77 → R78

Previous harvest: `workers/dispatcher/harvest-fold33way-r77`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 0.9826         | 0.9935         | +0.0109 |
| ctrl_bpc best  | 0.9015         | 0.9208         | +0.0193 |

## Per-round trajectory (best bird: SRW00)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 78 | 3602 | 0.9208 | +0.0052 |

## Cumulative training contribution

- This harvest: **150 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **1439 steps** from 36 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-fold33way-r77`

## Output

`workers/dispatcher/harvest-3way-r78/round-78/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

