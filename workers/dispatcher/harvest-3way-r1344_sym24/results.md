# harvest-3way-r1344 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1344 ctrl_bpc |
|--------|--------|--------------:|
| GQryj | fork-slaa-us-mmllm-claude-train-sym24-ab5dd27c-GQryj | 3.2132 |
| qRmKj | origin/claude/train-sym24-d1bc5c46-qRmKj | 3.2919 |
| wEylN | fork-joly-os-mmllm-claude-train-sym24-c27ddbbd-wEylN | 3.3586 |
| **mean** | | **3.2879** |
| **best** | | **3.2132** |

## Chain progression R1343 → R1344

Previous harvest: `workers/dispatcher/harvest-2way-r1343_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5273         | 3.2879         | -0.2394 |
| ctrl_bpc best  | 3.2806         | 3.2132         | -0.0674 |

## Per-round trajectory (best bird: GQryj)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1344 | 5554 | 3.2132 | +0.0963 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1343_sym24`

## Output

`workers/dispatcher/harvest-3way-r1344_sym24/round-1344/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

