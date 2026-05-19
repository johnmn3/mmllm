# harvest-2way-r27 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R27 ctrl_bpc |
|--------|--------|--------------:|
| blah4 | pr-2 | 1.1073 |
| kbfTW | origin/claude/smoke-r27-kbfTW | 1.1133 |
| **mean** | | **1.1103** |
| **best** | | **1.1073** |

## Chain progression R19 → R27

Previous harvest: `workers/dispatcher/harvest-4way-r19`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 1.9561         | 1.1103         | -0.8458 |
| ctrl_bpc best  | 1.9374         | 1.1073         | -0.8301 |

## Per-round trajectory (best bird: blah4)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 23 | 546 | 1.2683 | +0.0116 |
| 24 | 503 | 1.2010 | +0.0085 |
| 25 | 545 | 1.1379 | +0.0120 |
| 26 | 517 | 1.1269 | +0.0005 |
| 27 | 552 | 1.1073 | +0.0089 |

## Output

`workers/dispatcher/harvest-2way-r27/round-27/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

