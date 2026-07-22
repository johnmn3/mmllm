# harvest-4way-r989 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R989 ctrl_bpc |
|--------|--------|--------------:|
| XAc31 | fork-joly-os-mmllm-claude-train-sym24-8a940e4a-XAc31 | 2.5785 |
| rn3jr | origin/claude/train-sym24-d8e4cd6b-rn3jr | 2.5794 |
| 1spKG | origin/claude/train-sym24-1fa96a28-1spKG | 2.7742 |
| haqEL | fork-slaa-us-mmllm-claude-train-sym24-477f9a32-haqEL | 2.7859 |
| **mean** | | **2.6795** |
| **best** | | **2.5785** |

## Chain progression R988 → R989

Previous harvest: `workers/dispatcher/harvest-5way-r988_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7524         | 2.6795         | -0.0729 |
| ctrl_bpc best  | 2.5960         | 2.5785         | -0.0175 |

## Per-round trajectory (best bird: XAc31)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 989 | 6368 | 2.5785 | +0.1804 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r988_sym24`
  - `workers/dispatcher/harvest-5way-r988_sym24`

## Output

`workers/dispatcher/harvest-4way-r989_sym24/round-989/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

