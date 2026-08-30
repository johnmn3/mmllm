# harvest-2way-r1353 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1353 ctrl_bpc |
|--------|--------|--------------:|
| C0md8 | fork-SeniorCareMarket-mmllm-claude-train-sym24-c7a23249-C0md8 | 3.2853 |
| WX3Yi | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-9996754c-WX3Yi | 3.6116 |
| **mean** | | **3.4485** |
| **best** | | **3.2853** |

## Chain progression R610 → R1353

Previous harvest: `workers/dispatcher/harvest-2way-merge-r610_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.1372         | 3.4485         | +1.3113 |
| ctrl_bpc best  | 2.1268         | 3.2853         | +1.1585 |

## Per-round trajectory (best bird: C0md8)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1353 | 6777 | 3.2853 | +0.1200 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r1352_sym24`

## Output

`workers/dispatcher/harvest-2way-r1353_sym24/round-1353/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

