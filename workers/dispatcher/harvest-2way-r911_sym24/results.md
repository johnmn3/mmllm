# harvest-2way-r911 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R911 ctrl_bpc |
|--------|--------|--------------:|
| iuZKM | fork-slaa-us-mmllm-claude-train-sym24-8ef3b8a8-iuZKM | 2.7713 |
| FEYqS | origin/claude/train-sym24-f3840cbc-FEYqS | 2.9442 |
| **mean** | | **2.8578** |
| **best** | | **2.7713** |

## Chain progression R910 → R911

Previous harvest: `workers/dispatcher/harvest-5way-r910_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7722         | 2.8578         | +0.0856 |
| ctrl_bpc best  | 2.7511         | 2.7713         | +0.0202 |

## Per-round trajectory (best bird: iuZKM)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 911 | 3818 | 2.7713 | +0.1777 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r910_sym24`

## Output

`workers/dispatcher/harvest-2way-r911_sym24/round-911/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

