# harvest-2way-r1043 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1043 ctrl_bpc |
|--------|--------|--------------:|
| zM7Qr | origin/claude/train-sym24-adf9f00b-zM7Qr | 2.5248 |
| T0wP2 | fork-slaa-us-mmllm-claude-train-sym24-fa70fa35-T0wP2 | 2.6764 |
| **mean** | | **2.6006** |
| **best** | | **2.5248** |

## Chain progression R1042 → R1043

Previous harvest: `workers/dispatcher/harvest-4way-r1042_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6860         | 2.6006         | -0.0854 |
| ctrl_bpc best  | 2.4828         | 2.5248         | +0.0420 |

## Per-round trajectory (best bird: zM7Qr)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1043 | 6573 | 2.5248 | +0.1845 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1042_sym24`

## Output

`workers/dispatcher/harvest-2way-r1043_sym24/round-1043/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

