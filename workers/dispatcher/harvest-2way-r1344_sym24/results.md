# harvest-2way-r1344 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1344 ctrl_bpc |
|--------|--------|--------------:|
| qRmKj | origin/claude/train-sym24-d1bc5c46-qRmKj | 3.2919 |
| wEylN | fork-joly-os-mmllm-claude-train-sym24-c27ddbbd-wEylN | 3.3586 |
| **mean** | | **3.3253** |
| **best** | | **3.2919** |

## Chain progression R1343 → R1344

Previous harvest: `workers/dispatcher/harvest-2way-r1343_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5273         | 3.3253         | -0.2020 |
| ctrl_bpc best  | 3.2806         | 3.2919         | +0.0113 |

## Per-round trajectory (best bird: qRmKj)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1344 | 6963 | 3.2919 | +0.0789 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1343_sym24`

## Output

`workers/dispatcher/harvest-2way-r1344_sym24/round-1344/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

