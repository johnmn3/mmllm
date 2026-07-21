# harvest-2way-r985 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R985 ctrl_bpc |
|--------|--------|--------------:|
| GWIgD | fork-joly-os-mmllm-claude-train-sym24-fccb6878-GWIgD | 2.7883 |
| duQzS | fork-slaa-us-mmllm-claude-train-sym24-d32219dc-duQzS | 2.9648 |
| **mean** | | **2.8765** |
| **best** | | **2.7883** |

## Chain progression R984 → R985

Previous harvest: `workers/dispatcher/harvest-6way-r984_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7619         | 2.8765         | +0.1147 |
| ctrl_bpc best  | 2.5851         | 2.7883         | +0.2032 |

## Per-round trajectory (best bird: GWIgD)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 985 | 3759 | 2.7883 | +0.1358 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r984_sym24`

## Output

`workers/dispatcher/harvest-2way-r985_sym24/round-985/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

