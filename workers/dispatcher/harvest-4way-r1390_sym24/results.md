# harvest-4way-r1390 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1390 ctrl_bpc |
|--------|--------|--------------:|
| OD5X5 | origin/claude/train-sym24-89a1860a-OD5X5 | 3.0950 |
| 9Iq9x | fork-SeniorCareMarket-mmllm-claude-train-sym24-b7e9932d-9Iq9x | 3.1557 |
| QzFle | fork-joly-os-mmllm-claude-train-sym24-e0ba33c3-QzFle | 3.4584 |
| WQGgu | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-ed10a84f-WQGgu | 3.4673 |
| **mean** | | **3.2941** |
| **best** | | **3.0950** |

## Chain progression R1389 → R1390

Previous harvest: `workers/dispatcher/harvest-5way-r1389_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1328         | 3.2941         | +0.1613 |
| ctrl_bpc best  | 3.0448         | 3.0950         | +0.0502 |

## Per-round trajectory (best bird: OD5X5)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1390 | 6290 | 3.0950 | +0.1508 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1389_sym24`

## Output

`workers/dispatcher/harvest-4way-r1390_sym24/round-1390/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

