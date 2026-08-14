# harvest-2way-r1204 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1204 ctrl_bpc |
|--------|--------|--------------:|
| 5D0GF | fork-slaa-us-mmllm-claude-train-sym24-da948ef6-5D0GF | 2.4779 |
| ACO8Q | fork-joly-os-mmllm-claude-train-sym24-a3765ffa-ACO8Q | 2.4792 |
| **mean** | | **2.4786** |
| **best** | | **2.4779** |

## Chain progression R1203 → R1204

Previous harvest: `workers/dispatcher/harvest-13way-r1203_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4533         | 2.4786         | +0.0253 |
| ctrl_bpc best  | 2.2775         | 2.4779         | +0.2004 |

## Per-round trajectory (best bird: 5D0GF)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1204 | 6592 | 2.4779 | +0.2223 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-6way-r1203_sym24`

## Output

`workers/dispatcher/harvest-2way-r1204_sym24/round-1204/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

