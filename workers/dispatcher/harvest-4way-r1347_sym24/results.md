# harvest-4way-r1347 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1347 ctrl_bpc |
|--------|--------|--------------:|
| MS2Dr | origin/claude/train-sym24-ef04327d-MS2Dr | 3.1834 |
| pSHXy | origin/claude/train-sym24-c16c7d36-pSHXy | 3.2167 |
| n6dpI | origin/claude/train-sym24-316911e1-n6dpI | 3.2302 |
| OC5oh | fork-slaa-us-mmllm-claude-train-sym24-a0cb8b7c-OC5oh | 3.3473 |
| **mean** | | **3.2444** |
| **best** | | **3.1834** |

## Chain progression R1346 → R1347

Previous harvest: `workers/dispatcher/harvest-4way-r1346_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2900         | 3.2444         | -0.0456 |
| ctrl_bpc best  | 3.2506         | 3.1834         | -0.0672 |

## Per-round trajectory (best bird: MS2Dr)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1347 | 6638 | 3.1834 | +0.1024 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1346_sym24`
  - `workers/dispatcher/harvest-4way-r1346_sym24`

## Output

`workers/dispatcher/harvest-4way-r1347_sym24/round-1347/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

