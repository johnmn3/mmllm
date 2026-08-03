# harvest-4way-r1098 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1098 ctrl_bpc |
|--------|--------|--------------:|
| o58P4 | fork-joly-os-mmllm-claude-train-sym24-461d09cf-o58P4 | 2.3996 |
| 6JpLD | fork-slaa-us-mmllm-claude-train-sym24-f076bf51-6JpLD | 2.4185 |
| gxgmz | origin/claude/train-sym24-ad5b4a03-gxgmz | 2.4199 |
| bjs7z | origin/claude/train-sym24-9ae0499f-bjs7z | 2.4259 |
| **mean** | | **2.4160** |
| **best** | | **2.3996** |

## Chain progression R1097 → R1098

Previous harvest: `workers/dispatcher/harvest-5way-r1097_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6060         | 2.4160         | -0.1900 |
| ctrl_bpc best  | 2.4016         | 2.3996         | -0.0020 |

## Per-round trajectory (best bird: o58P4)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1098 | 5358 | 2.3996 | +0.2402 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1097_sym24`

## Output

`workers/dispatcher/harvest-4way-r1098_sym24/round-1098/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

