# harvest-2way-r1347 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1347 ctrl_bpc |
|--------|--------|--------------:|
| n6dpI | origin/claude/train-sym24-316911e1-n6dpI | 3.2302 |
| OC5oh | fork-slaa-us-mmllm-claude-train-sym24-a0cb8b7c-OC5oh | 3.3473 |
| **mean** | | **3.2888** |
| **best** | | **3.2302** |

## Chain progression R1346 → R1347

Previous harvest: `workers/dispatcher/harvest-4way-r1346_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2900         | 3.2888         | -0.0012 |
| ctrl_bpc best  | 3.2506         | 3.2302         | -0.0204 |

## Per-round trajectory (best bird: n6dpI)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1347 | 6374 | 3.2302 | +0.0819 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1346_sym24`

## Output

`workers/dispatcher/harvest-2way-r1347_sym24/round-1347/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

