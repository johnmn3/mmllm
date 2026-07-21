# harvest-2way-r987 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R987 ctrl_bpc |
|--------|--------|--------------:|
| tQU4q | fork-joly-os-mmllm-claude-train-sym24-0cdb0ce0-tQU4q | 2.6035 |
| YD97i | fork-SeniorCareMarket-mmllm-claude-train-sym24-498e7767-YD97i | 2.6225 |
| **mean** | | **2.6130** |
| **best** | | **2.6035** |

## Chain progression R986 → R987

Previous harvest: `workers/dispatcher/harvest-9way-r986_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7244         | 2.6130         | -0.1114 |
| ctrl_bpc best  | 2.5851         | 2.6035         | +0.0184 |

## Per-round trajectory (best bird: tQU4q)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 987 | 6303 | 2.6035 | +0.1608 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r986_sym24`

## Output

`workers/dispatcher/harvest-2way-r987_sym24/round-987/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

