# harvest-1way-r1336 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1336 ctrl_bpc |
|--------|--------|--------------:|
| aTpQN | origin/claude/train-sym24-f1f44370-aTpQN | 3.6172 |
| **mean** | | **3.6172** |
| **best** | | **3.6172** |

## Chain progression R1335 → R1336

Previous harvest: `workers/dispatcher/harvest-5way-r1335_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3241         | 3.6172         | +0.2931 |
| ctrl_bpc best  | 3.2503         | 3.6172         | +0.3669 |

## Per-round trajectory (best bird: aTpQN)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1336 | 5205 | 3.6172 | +0.0788 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1335_sym24`

## Output

`workers/dispatcher/harvest-1way-r1336_sym24/round-1336/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

