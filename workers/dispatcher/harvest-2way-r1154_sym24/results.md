# harvest-2way-r1154 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1154 ctrl_bpc |
|--------|--------|--------------:|
| FKcKs | fork-slaa-us-mmllm-claude-train-sym24-0c83586d-FKcKs | 2.3659 |
| Ixp41 | fork-SeniorCareMarket-mmllm-claude-train-sym24-58d80125-Ixp41 | 2.5293 |
| **mean** | | **2.4476** |
| **best** | | **2.3659** |

## Chain progression R1153 → R1154

Previous harvest: `workers/dispatcher/harvest-5way-r1153_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6046         | 2.4476         | -0.1570 |
| ctrl_bpc best  | 2.3313         | 2.3659         | +0.0346 |

## Per-round trajectory (best bird: FKcKs)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1154 | 4469 | 2.3659 | +0.2556 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1153_sym24`

## Output

`workers/dispatcher/harvest-2way-r1154_sym24/round-1154/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

