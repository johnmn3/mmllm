# harvest-2way-r1105 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1105 ctrl_bpc |
|--------|--------|--------------:|
| 4YgDS | fork-slaa-us-mmllm-claude-train-sym24-ad080999-4YgDS | 2.4124 |
| D4z5I | fork-SeniorCareMarket-mmllm-claude-train-sym24-fdd8d3f0-D4z5I | 2.5943 |
| **mean** | | **2.5034** |
| **best** | | **2.4124** |

## Chain progression R1104 → R1105

Previous harvest: `workers/dispatcher/harvest-9way-r1104_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5141         | 2.5034         | -0.0107 |
| ctrl_bpc best  | 2.3954         | 2.4124         | +0.0170 |

## Per-round trajectory (best bird: 4YgDS)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1105 | 4387 | 2.4124 | +0.2337 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1104_sym24`

## Output

`workers/dispatcher/harvest-2way-r1105_sym24/round-1105/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

