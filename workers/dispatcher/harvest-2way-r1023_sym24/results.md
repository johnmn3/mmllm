# harvest-2way-r1023 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1023 ctrl_bpc |
|--------|--------|--------------:|
| Hg5kn | origin/claude/train-sym24-d3af0560-Hg5kn | 2.5369 |
| fhLCQ | fork-joly-os-mmllm-claude-train-sym24-34850986-fhLCQ | 2.9148 |
| **mean** | | **2.7259** |
| **best** | | **2.5369** |

## Chain progression R1022 → R1023

Previous harvest: `workers/dispatcher/harvest-8way-r1022_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6228         | 2.7259         | +0.1031 |
| ctrl_bpc best  | 2.5121         | 2.5369         | +0.0248 |

## Per-round trajectory (best bird: Hg5kn)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1023 | 6549 | 2.5369 | +0.1710 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r1022_sym24`

## Output

`workers/dispatcher/harvest-2way-r1023_sym24/round-1023/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

