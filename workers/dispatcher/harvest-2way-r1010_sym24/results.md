# harvest-2way-r1010 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1010 ctrl_bpc |
|--------|--------|--------------:|
| LBuhv | origin/claude/train-sym24-a193c09f-LBuhv | 2.5773 |
| oiMYF | fork-slaa-us-mmllm-claude-train-sym24-6ac848e5-oiMYF | 2.9247 |
| **mean** | | **2.7510** |
| **best** | | **2.5773** |

## Chain progression R1009 → R1010

Previous harvest: `workers/dispatcher/harvest-6way-r1009_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7386         | 2.7510         | +0.0124 |
| ctrl_bpc best  | 2.5354         | 2.5773         | +0.0419 |

## Per-round trajectory (best bird: LBuhv)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1010 | 4084 | 2.5773 | +0.1729 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1009_sym24`

## Output

`workers/dispatcher/harvest-2way-r1010_sym24/round-1010/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

