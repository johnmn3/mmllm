# harvest-4way-r1131 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1131 ctrl_bpc |
|--------|--------|--------------:|
| tQLWr | origin/claude/train-sym24-b9403777-tQLWr | 2.3510 |
| myiYB | fork-joly-os-mmllm-claude-train-sym24-75c26605-myiYB | 2.3769 |
| WFKsd | origin/claude/train-sym24-d1b364a6-WFKsd | 2.5550 |
| bMpzk | fork-slaa-us-mmllm-claude-train-sym24-739f22e5-bMpzk | 2.7558 |
| **mean** | | **2.5097** |
| **best** | | **2.3510** |

## Chain progression R1130 → R1131

Previous harvest: `workers/dispatcher/harvest-2way-r1130_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5551         | 2.5097         | -0.0454 |
| ctrl_bpc best  | 2.5534         | 2.3510         | -0.2024 |

## Per-round trajectory (best bird: tQLWr)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1131 | 6373 | 2.3510 | +0.2558 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1130_sym24`

## Output

`workers/dispatcher/harvest-4way-r1131_sym24/round-1131/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

