# harvest-2way-r1098 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1098 ctrl_bpc |
|--------|--------|--------------:|
| o58P4 | fork-joly-os-mmllm-claude-train-sym24-461d09cf-o58P4 | 2.3996 |
| gxgmz | origin/claude/train-sym24-ad5b4a03-gxgmz | 2.4199 |
| **mean** | | **2.4097** |
| **best** | | **2.3996** |

## Chain progression R1097 → R1098

Previous harvest: `workers/dispatcher/harvest-5way-r1097_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6060         | 2.4097         | -0.1963 |
| ctrl_bpc best  | 2.4016         | 2.3996         | -0.0020 |

## Per-round trajectory (best bird: o58P4)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1098 | 5358 | 2.3996 | +0.2402 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1097_sym24`

## Output

`workers/dispatcher/harvest-2way-r1098_sym24/round-1098/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

