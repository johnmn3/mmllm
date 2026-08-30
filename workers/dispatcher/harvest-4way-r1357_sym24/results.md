# harvest-4way-r1357 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1357 ctrl_bpc |
|--------|--------|--------------:|
| evFfQ | origin/claude/train-sym24-59f50277-evFfQ | 3.2695 |
| dLJoM | fork-slaa-us-mmllm-claude-train-sym24-e7d74490-dLJoM | 3.2777 |
| 99N4t | origin/claude/train-sym24-85e4c4e0-99N4t | 3.3395 |
| rYwRA | origin/claude/train-sym24-a81b0c97-rYwRA | 3.5815 |
| **mean** | | **3.3670** |
| **best** | | **3.2695** |

## Chain progression R1356 → R1357

Previous harvest: `workers/dispatcher/harvest-6way-r1356_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3254         | 3.3670         | +0.0416 |
| ctrl_bpc best  | 3.1885         | 3.2695         | +0.0810 |

## Per-round trajectory (best bird: evFfQ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1357 | 4444 | 3.2695 | +0.1091 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1356_sym24`
  - `workers/dispatcher/harvest-4way-r1356_sym24`
  - `workers/dispatcher/harvest-6way-r1356_sym24`

## Output

`workers/dispatcher/harvest-4way-r1357_sym24/round-1357/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

