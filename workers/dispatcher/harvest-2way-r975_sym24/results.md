# harvest-2way-r975 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R975 ctrl_bpc |
|--------|--------|--------------:|
| k8fgS | fork-slaa-us-mmllm-claude-train-sym24-abdd38ec-k8fgS | 2.6027 |
| by7bn | origin/claude/train-sym24-9067230b-by7bn | 3.0268 |
| **mean** | | **2.8148** |
| **best** | | **2.6027** |

## Chain progression R974 → R975

Previous harvest: `workers/dispatcher/harvest-1way-r974_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7955         | 2.8148         | +0.0192 |
| ctrl_bpc best  | 2.7955         | 2.6027         | -0.1928 |

## Per-round trajectory (best bird: k8fgS)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 975 | 6488 | 2.6027 | +0.1725 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r974_sym24`

## Output

`workers/dispatcher/harvest-2way-r975_sym24/round-975/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

