# harvest-2way-r886 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R886 ctrl_bpc |
|--------|--------|--------------:|
| yW0AI | origin/claude/train-sym24-8fedeb92-yW0AI | 2.8337 |
| Z4CbS | fork-joly-os-mmllm-claude-train-sym24-42a51d10-Z4CbS | 3.2246 |
| **mean** | | **3.0292** |
| **best** | | **2.8337** |

## Chain progression R885 → R886

Previous harvest: `workers/dispatcher/harvest-6way-r885_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0765         | 3.0292         | -0.0473 |
| ctrl_bpc best  | 2.8407         | 2.8337         | -0.0070 |

## Per-round trajectory (best bird: yW0AI)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 886 | 6684 | 2.8337 | +0.3412 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r885_sym24`

## Output

`workers/dispatcher/harvest-2way-r886_sym24/round-886/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

