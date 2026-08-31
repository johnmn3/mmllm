# harvest-3way-r1369 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1369 ctrl_bpc |
|--------|--------|--------------:|
| gCm4D | origin/claude/train-sym24-f07d1b66-gCm4D | 3.0918 |
| oHmRp | fork-joly-os-mmllm-claude-train-sym24-b2afd2c9-oHmRp | 3.1903 |
| HOVyn | origin/claude/train-sym24-c717b1ab-HOVyn | 3.2173 |
| **mean** | | **3.1665** |
| **best** | | **3.0918** |

## Chain progression R1368 → R1369

Previous harvest: `workers/dispatcher/harvest-1way-r1368_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2665         | 3.1665         | -0.1000 |
| ctrl_bpc best  | 3.2665         | 3.0918         | -0.1747 |

## Per-round trajectory (best bird: gCm4D)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1369 | 3804 | 3.0918 | +0.1017 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1368_sym24`

## Output

`workers/dispatcher/harvest-3way-r1369_sym24/round-1369/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

