# harvest-3way-r1099 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1099 ctrl_bpc |
|--------|--------|--------------:|
| iSlBD | origin/claude/train-sym24-0c5b8a78-iSlBD | 2.4171 |
| nN14H | fork-joly-os-mmllm-claude-train-sym24-971f2e8a-nN14H | 2.4223 |
| 9mkO6 | origin/claude/train-sym24-e8da2d89-9mkO6 | 2.6021 |
| **mean** | | **2.4805** |
| **best** | | **2.4171** |

## Chain progression R1098 → R1099

Previous harvest: `workers/dispatcher/harvest-4way-r1098_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4160         | 2.4805         | +0.0645 |
| ctrl_bpc best  | 2.3996         | 2.4171         | +0.0175 |

## Per-round trajectory (best bird: iSlBD)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1099 | 5312 | 2.4171 | +0.2300 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1098_sym24`

## Output

`workers/dispatcher/harvest-3way-r1099_sym24/round-1099/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

