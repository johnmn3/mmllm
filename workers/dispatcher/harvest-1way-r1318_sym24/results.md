# harvest-1way-r1318 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1318 ctrl_bpc |
|--------|--------|--------------:|
| ezhX2 | fork-SeniorCareMarket-mmllm-claude-train-sym24-50134e71-ezhX2 | 3.7464 |
| **mean** | | **3.7464** |
| **best** | | **3.7464** |

## Chain progression R1317 → R1318

Previous harvest: `workers/dispatcher/harvest-6way-r1317_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.6536         | 3.7464         | +0.0928 |
| ctrl_bpc best  | 3.3877         | 3.7464         | +0.3587 |

## Per-round trajectory (best bird: ezhX2)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1318 | 3737 | 3.7464 | +0.0593 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1317_sym24`

## Output

`workers/dispatcher/harvest-1way-r1318_sym24/round-1318/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

