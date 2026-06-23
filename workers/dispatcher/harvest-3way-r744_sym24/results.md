# harvest-3way-r744 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R744 ctrl_bpc |
|--------|--------|--------------:|
| sLVNV | fork-slaa-us-mmllm-claude-train-sym24-861a4882-sLVNV | 3.4064 |
| JyDoS | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-3c2b6807-JyDoS | 3.7141 |
| 4W521 | origin/claude/train-sym24-39f2cbbc-4W521 | 3.7345 |
| **mean** | | **3.6183** |
| **best** | | **3.4064** |

## Chain progression R743 → R744

Previous harvest: `workers/dispatcher/harvest-3way-r743_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.6120         | 3.6183         | +0.0063 |
| ctrl_bpc best  | 3.3924         | 3.4064         | +0.0140 |

## Per-round trajectory (best bird: sLVNV)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 744 | 4446 | 3.4064 | +0.5542 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r743_sym24`

## Output

`workers/dispatcher/harvest-3way-r744_sym24/round-744/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

