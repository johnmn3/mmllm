# harvest-2way-r1174 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1174 ctrl_bpc |
|--------|--------|--------------:|
| L0kvo | fork-joly-os-mmllm-claude-train-sym24-b8047900-L0kvo | 2.3127 |
| HkfZU | fork-slaa-us-mmllm-claude-train-sym24-f58c7496-HkfZU | 2.5111 |
| **mean** | | **2.4119** |
| **best** | | **2.3127** |

## Chain progression R1173 → R1174

Previous harvest: `workers/dispatcher/harvest-13way-r1173_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4740         | 2.4119         | -0.0621 |
| ctrl_bpc best  | 2.3085         | 2.3127         | +0.0042 |

## Per-round trajectory (best bird: L0kvo)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1174 | 6512 | 2.3127 | +0.2672 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-6way-r1173_sym24`

## Output

`workers/dispatcher/harvest-2way-r1174_sym24/round-1174/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

