# harvest-2way-r1028 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1028 ctrl_bpc |
|--------|--------|--------------:|
| r81pJ | fork-slaa-us-mmllm-claude-train-sym24-2c6b47e5-r81pJ | 2.5051 |
| ehwO9 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-376ea5ee-ehwO9 | 2.5403 |
| **mean** | | **2.5227** |
| **best** | | **2.5051** |

## Chain progression R1027 → R1028

Previous harvest: `workers/dispatcher/harvest-4way-r1027_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6040         | 2.5227         | -0.0813 |
| ctrl_bpc best  | 2.5032         | 2.5051         | +0.0019 |

## Per-round trajectory (best bird: r81pJ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1028 | 6482 | 2.5051 | +0.1906 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1027_sym24`

## Output

`workers/dispatcher/harvest-2way-r1028_sym24/round-1028/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

