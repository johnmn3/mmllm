# harvest-4way-r1170 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1170 ctrl_bpc |
|--------|--------|--------------:|
| X42o2 | fork-joly-os-mmllm-claude-train-sym24-6efd849d-X42o2 | 2.3084 |
| IDXwY | fork-slaa-us-mmllm-claude-train-sym24-5d473562-IDXwY | 2.3181 |
| JMqqo | origin/claude/train-sym24-defc8909-JMqqo | 2.3202 |
| GORjt | origin/claude/train-sym24-a0fff66c-GORjt | 2.3496 |
| **mean** | | **2.3241** |
| **best** | | **2.3084** |

## Chain progression R1169 → R1170

Previous harvest: `workers/dispatcher/harvest-6way-r1169_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4845         | 2.3241         | -0.1604 |
| ctrl_bpc best  | 2.3114         | 2.3084         | -0.0030 |

## Per-round trajectory (best bird: X42o2)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1170 | 6856 | 2.3084 | +0.2658 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1169_sym24`

## Output

`workers/dispatcher/harvest-4way-r1170_sym24/round-1170/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

