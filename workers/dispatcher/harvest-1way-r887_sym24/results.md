# harvest-1way-r887 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R887 ctrl_bpc |
|--------|--------|--------------:|
| YZyUj | fork-SeniorCareMarket-mmllm-claude-train-sym24-efe7bcce-YZyUj | 3.2228 |
| **mean** | | **3.2228** |
| **best** | | **3.2228** |

## Chain progression R886 → R887

Previous harvest: `workers/dispatcher/harvest-6way-r886_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9591         | 3.2228         | +0.2637 |
| ctrl_bpc best  | 2.8141         | 3.2228         | +0.4087 |

## Per-round trajectory (best bird: YZyUj)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 887 | 5264 | 3.2228 | +0.2793 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r886_sym24`

## Output

`workers/dispatcher/harvest-1way-r887_sym24/round-887/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

