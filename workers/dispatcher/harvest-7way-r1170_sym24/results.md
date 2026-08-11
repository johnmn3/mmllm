# harvest-7way-r1170 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R1170 ctrl_bpc |
|--------|--------|--------------:|
| X42o2 | fork-joly-os-mmllm-claude-train-sym24-6efd849d-X42o2 | 2.3084 |
| IDXwY | fork-slaa-us-mmllm-claude-train-sym24-5d473562-IDXwY | 2.3181 |
| JMqqo | origin/claude/train-sym24-defc8909-JMqqo | 2.3202 |
| ZCe8j | fork-joly-os-mmllm-claude-train-sym24-ce67056c-ZCe8j | 2.3457 |
| GORjt | origin/claude/train-sym24-a0fff66c-GORjt | 2.3496 |
| OH5jy | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-ea5e7116-OH5jy | 2.5315 |
| TlkkT | fork-SeniorCareMarket-mmllm-claude-train-sym24-107859a7-TlkkT | 2.7157 |
| **mean** | | **2.4127** |
| **best** | | **2.3084** |

## Chain progression R1169 → R1170

Previous harvest: `workers/dispatcher/harvest-6way-r1169_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4845         | 2.4127         | -0.0718 |
| ctrl_bpc best  | 2.3114         | 2.3084         | -0.0030 |

## Per-round trajectory (best bird: X42o2)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1170 | 6856 | 2.3084 | +0.2658 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1169_sym24`
  - `workers/dispatcher/harvest-4way-r1169_sym24`

## Output

`workers/dispatcher/harvest-7way-r1170_sym24/round-1170/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

