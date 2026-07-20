# harvest-2way-r970 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R970 ctrl_bpc |
|--------|--------|--------------:|
| crDkc | origin/claude/train-sym24-85bf8735-crDkc | 2.6210 |
| aX4em | fork-slaa-us-mmllm-claude-train-sym24-aebbce7f-aX4em | 2.6521 |
| **mean** | | **2.6365** |
| **best** | | **2.6210** |

## Chain progression R969 → R970

Previous harvest: `workers/dispatcher/harvest-7way-r969_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7861         | 2.6365         | -0.1496 |
| ctrl_bpc best  | 2.6097         | 2.6210         | +0.0113 |

## Per-round trajectory (best bird: crDkc)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 970 | 6380 | 2.6210 | +0.1984 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r969_sym24`

## Output

`workers/dispatcher/harvest-2way-r970_sym24/round-970/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

