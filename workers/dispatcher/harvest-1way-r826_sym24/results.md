# harvest-1way-r826 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R826 ctrl_bpc |
|--------|--------|--------------:|
| GcCuK | fork-joly-os-mmllm-claude-train-sym24-e2296074-GcCuK | 3.3834 |
| **mean** | | **3.3834** |
| **best** | | **3.3834** |

## Chain progression R825 → R826

Previous harvest: `workers/dispatcher/harvest-1way-r825_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1534         | 3.3834         | +0.2300 |
| ctrl_bpc best  | 3.1534         | 3.3834         | +0.2300 |

## Per-round trajectory (best bird: GcCuK)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 826 | 4795 | 3.3834 | +0.3916 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r825_sym24`

## Output

`workers/dispatcher/harvest-1way-r826_sym24/round-826/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

