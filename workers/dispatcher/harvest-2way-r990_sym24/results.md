# harvest-2way-r990 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R990 ctrl_bpc |
|--------|--------|--------------:|
| UwkH0 | fork-SeniorCareMarket-mmllm-claude-train-sym24-4449f39a-UwkH0 | 2.6003 |
| PyWEG | origin/claude/train-sym24-1af20b06-PyWEG | 2.7902 |
| **mean** | | **2.6952** |
| **best** | | **2.6003** |

## Chain progression R989 → R990

Previous harvest: `workers/dispatcher/harvest-4way-r989_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6795         | 2.6952         | +0.0157 |
| ctrl_bpc best  | 2.5785         | 2.6003         | +0.0218 |

## Per-round trajectory (best bird: UwkH0)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 990 | 6590 | 2.6003 | +0.1491 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r989_sym24`

## Output

`workers/dispatcher/harvest-2way-r990_sym24/round-990/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

