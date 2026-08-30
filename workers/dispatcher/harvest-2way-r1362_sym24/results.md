# harvest-2way-r1362 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1362 ctrl_bpc |
|--------|--------|--------------:|
| axdk8 | fork-slaa-us-mmllm-claude-train-sym24-b711058d-axdk8 | 3.5269 |
| CKbCe | origin/claude/train-sym24-6dccee0d-CKbCe | 3.5331 |
| **mean** | | **3.5300** |
| **best** | | **3.5269** |

## Chain progression R1361 → R1362

Previous harvest: `workers/dispatcher/harvest-7way-r1361_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2939         | 3.5300         | +0.2361 |
| ctrl_bpc best  | 3.1082         | 3.5269         | +0.4187 |

## Per-round trajectory (best bird: axdk8)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1362 | 6554 | 3.5269 | +0.0821 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1361_sym24`

## Output

`workers/dispatcher/harvest-2way-r1362_sym24/round-1362/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

