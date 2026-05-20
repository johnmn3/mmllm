# harvest-2way-r31 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R31 ctrl_bpc |
|--------|--------|--------------:|
| Iixhi | fork-SeniorCareMarket-mmllm-claude-train-2b64bdaf-Iixhi | 1.1196 |
| rARVw | fork-joly-os-mmllm-claude-train-94b400a4-rARVw | 1.2989 |
| **mean** | | **1.2092** |
| **best** | | **1.1196** |

## Chain progression R30 → R31

Previous harvest: `workers/dispatcher/harvest-1way-r30`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 1.1424         | 1.2092         | +0.0668 |
| ctrl_bpc best  | 1.1424         | 1.1196         | -0.0228 |

## Per-round trajectory (best bird: Iixhi)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 31 | 529 | 1.1196 | +0.0081 |

## Cumulative training contribution

- This harvest: **14 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **35 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r30`

## Output

`workers/dispatcher/harvest-2way-r31/round-31/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

