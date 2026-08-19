# harvest-3way-r1256 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1256 ctrl_bpc |
|--------|--------|--------------:|
| xGJW4 | fork-slaa-us-mmllm-claude-train-sym24-4bf7dbc8-xGJW4 | 2.2385 |
| P29nb | origin/claude/train-sym24-5ce26482-P29nb | 2.2562 |
| ukOyY | fork-joly-os-mmllm-claude-train-sym24-101e634e-ukOyY | 2.6288 |
| **mean** | | **2.3745** |
| **best** | | **2.2385** |

## Chain progression R1255 → R1256

Previous harvest: `workers/dispatcher/harvest-5way-r1255_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3995         | 2.3745         | -0.0250 |
| ctrl_bpc best  | 2.2357         | 2.2385         | +0.0028 |

## Per-round trajectory (best bird: xGJW4)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1256 | 3946 | 2.2385 | +0.2484 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1255_sym24`

## Output

`workers/dispatcher/harvest-3way-r1256_sym24/round-1256/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

