# harvest-2way-r1242 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1242 ctrl_bpc |
|--------|--------|--------------:|
| kERwH | origin/claude/train-sym24-bf594e28-kERwH | 2.2500 |
| XDCrV | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-3b21fe39-XDCrV | 2.2677 |
| **mean** | | **2.2588** |
| **best** | | **2.2500** |

## Chain progression R1241 → R1242

Previous harvest: `workers/dispatcher/harvest-7way-r1241_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4284         | 2.2588         | -0.1696 |
| ctrl_bpc best  | 2.2649         | 2.2500         | -0.0149 |

## Per-round trajectory (best bird: kERwH)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1242 | 6342 | 2.2500 | +0.2399 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1241_sym24`

## Output

`workers/dispatcher/harvest-2way-r1242_sym24/round-1242/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

