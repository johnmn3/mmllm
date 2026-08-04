# harvest-2way-r1113 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1113 ctrl_bpc |
|--------|--------|--------------:|
| Ags0q | fork-slaa-us-mmllm-claude-train-sym24-83d13b26-Ags0q | 2.3949 |
| 6owaJ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-e53a1889-6owaJ | 2.5758 |
| **mean** | | **2.4853** |
| **best** | | **2.3949** |

## Chain progression R1112 → R1113

Previous harvest: `workers/dispatcher/harvest-7way-r1112_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5253         | 2.4853         | -0.0400 |
| ctrl_bpc best  | 2.3729         | 2.3949         | +0.0220 |

## Per-round trajectory (best bird: Ags0q)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1113 | 6478 | 2.3949 | +0.2304 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1112_sym24`
  - `workers/dispatcher/harvest-3way-r1112_sym24`

## Output

`workers/dispatcher/harvest-2way-r1113_sym24/round-1113/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

