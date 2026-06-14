# harvest-1way-r677 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R677 ctrl_bpc |
|--------|--------|--------------:|
| hHQC9 | fork-slaa-us-mmllm-claude-train-sym24-88144682-hHQC9 | 4.1512 |
| **mean** | | **4.1512** |
| **best** | | **4.1512** |

## Chain progression R676 → R677

Previous harvest: `workers/dispatcher/harvest-7way-r676_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.8577         | 4.1512         | +0.2935 |
| ctrl_bpc best  | 3.8016         | 4.1512         | +0.3496 |

## Per-round trajectory (best bird: hHQC9)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 677 | 4432 | 4.1512 | +0.3599 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r676_sym24`

## Output

`workers/dispatcher/harvest-1way-r677_sym24/round-677/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

