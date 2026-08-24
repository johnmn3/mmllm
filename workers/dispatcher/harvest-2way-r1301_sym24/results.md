# harvest-2way-r1301 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1301 ctrl_bpc |
|--------|--------|--------------:|
| yBq81 | fork-joly-os-mmllm-claude-train-sym24-4471e447-yBq81 | 3.6795 |
| VTxUM | origin/claude/train-sym24-1dd2a5d8-VTxUM | 4.0434 |
| **mean** | | **3.8615** |
| **best** | | **3.6795** |

## Chain progression R1300 → R1301

Previous harvest: `workers/dispatcher/harvest-7way-r1300_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.8222         | 3.8615         | +0.0393 |
| ctrl_bpc best  | 3.5802         | 3.6795         | +0.0993 |

## Per-round trajectory (best bird: yBq81)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1301 | 6797 | 3.6795 | +0.0836 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1300_sym24`

## Output

`workers/dispatcher/harvest-2way-r1301_sym24/round-1301/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

