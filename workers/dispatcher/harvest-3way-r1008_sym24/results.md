# harvest-3way-r1008 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1008 ctrl_bpc |
|--------|--------|--------------:|
| Npyi3 | origin/claude/train-sym24-8811dfc4-Npyi3 | 2.7262 |
| JMtz7 | origin/claude/train-sym24-6837d90d-JMtz7 | 2.7318 |
| XFX6m | fork-joly-os-mmllm-claude-train-sym24-580afbe5-XFX6m | 2.7387 |
| **mean** | | **2.7322** |
| **best** | | **2.7262** |

## Chain progression R1007 → R1008

Previous harvest: `workers/dispatcher/harvest-4way-r1007_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6193         | 2.7322         | +0.1129 |
| ctrl_bpc best  | 2.5633         | 2.7262         | +0.1629 |

## Per-round trajectory (best bird: Npyi3)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1008 | 3631 | 2.7262 | +0.1633 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1007_sym24`

## Output

`workers/dispatcher/harvest-3way-r1008_sym24/round-1008/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

