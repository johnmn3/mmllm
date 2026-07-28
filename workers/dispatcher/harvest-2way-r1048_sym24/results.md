# harvest-2way-r1048 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1048 ctrl_bpc |
|--------|--------|--------------:|
| 6VAuK | origin/claude/train-sym24-ae79933f-6VAuK | 2.8548 |
| lg8u9 | fork-joly-os-mmllm-claude-train-sym24-2996a630-lg8u9 | 2.8578 |
| **mean** | | **2.8563** |
| **best** | | **2.8548** |

## Chain progression R1047 → R1048

Previous harvest: `workers/dispatcher/harvest-4way-r1047_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5919         | 2.8563         | +0.2644 |
| ctrl_bpc best  | 2.5082         | 2.8548         | +0.3466 |

## Per-round trajectory (best bird: 6VAuK)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1048 | 4433 | 2.8548 | +0.1973 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1047_sym24`

## Output

`workers/dispatcher/harvest-2way-r1048_sym24/round-1048/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

