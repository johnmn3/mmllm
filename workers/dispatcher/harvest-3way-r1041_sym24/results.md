# harvest-3way-r1041 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1041 ctrl_bpc |
|--------|--------|--------------:|
| dn766 | fork-slaa-us-mmllm-claude-train-sym24-f5da513d-dn766 | 2.4803 |
| obn5a | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f6ef0d6a-obn5a | 2.8730 |
| a4dsw | fork-SeniorCareMarket-mmllm-claude-train-sym24-974be485-a4dsw | 2.8766 |
| **mean** | | **2.7433** |
| **best** | | **2.4803** |

## Chain progression R1040 → R1041

Previous harvest: `workers/dispatcher/harvest-7way-r1040_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6142         | 2.7433         | +0.1291 |
| ctrl_bpc best  | 2.5029         | 2.4803         | -0.0226 |

## Per-round trajectory (best bird: dn766)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1041 | 7003 | 2.4803 | +0.2258 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1040_sym24`

## Output

`workers/dispatcher/harvest-3way-r1041_sym24/round-1041/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

