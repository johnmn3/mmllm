# harvest-2way-r1403 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1403 ctrl_bpc |
|--------|--------|--------------:|
| WzjT2 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-d338982c-WzjT2 | 3.3663 |
| K2UTB | origin/claude/train-sym24-3005c6c4-K2UTB | 3.4423 |
| **mean** | | **3.4043** |
| **best** | | **3.3663** |

## Chain progression R1402 → R1403

Previous harvest: `workers/dispatcher/harvest-1way-r1402_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3330         | 3.4043         | +0.0713 |
| ctrl_bpc best  | 3.3330         | 3.3663         | +0.0333 |

## Per-round trajectory (best bird: WzjT2)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1403 | 6603 | 3.3663 | +0.0898 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1402_sym24`

## Output

`workers/dispatcher/harvest-2way-r1403_sym24/round-1403/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

