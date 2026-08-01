# harvest-1way-r1083 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1083 ctrl_bpc |
|--------|--------|--------------:|
| aRtOn | fork-SeniorCareMarket-mmllm-claude-train-sym24-eebd6ba6-aRtOn | 2.6000 |
| **mean** | | **2.6000** |
| **best** | | **2.6000** |

## Chain progression R1082 → R1083

Previous harvest: `workers/dispatcher/harvest-4way-r1082_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6199         | 2.6000         | -0.0199 |
| ctrl_bpc best  | 2.4308         | 2.6000         | +0.1692 |

## Per-round trajectory (best bird: aRtOn)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1083 | 3577 | 2.6000 | +0.2112 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1082_sym24`

## Output

`workers/dispatcher/harvest-1way-r1083_sym24/round-1083/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

