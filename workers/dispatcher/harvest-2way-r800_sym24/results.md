# harvest-2way-r800 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R800 ctrl_bpc |
|--------|--------|--------------:|
| nS8Nk | origin/claude/train-sym24-71ae97b9-nS8Nk | 3.2511 |
| BSdGv | fork-joly-os-mmllm-claude-train-sym24-80c4ec60-BSdGv | 3.4896 |
| **mean** | | **3.3704** |
| **best** | | **3.2511** |

## Chain progression R799 → R800

Previous harvest: `workers/dispatcher/harvest-10way-r799_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2920         | 3.3704         | +0.0784 |
| ctrl_bpc best  | 3.0997         | 3.2511         | +0.1514 |

## Per-round trajectory (best bird: nS8Nk)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 800 | 6367 | 3.2511 | +0.4776 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-7way-r799_sym24`

## Output

`workers/dispatcher/harvest-2way-r800_sym24/round-800/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

