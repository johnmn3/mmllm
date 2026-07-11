# harvest-3way-r894 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R894 ctrl_bpc |
|--------|--------|--------------:|
| bsc9i | fork-joly-os-mmllm-claude-train-sym24-9d72f4c8-bsc9i | 3.1771 |
| uxLW8 | origin/claude/train-sym24-cf109578-uxLW8 | 3.1897 |
| LrnFA | fork-slaa-us-mmllm-claude-train-sym24-c007c55e-LrnFA | 3.1986 |
| **mean** | | **3.1885** |
| **best** | | **3.1771** |

## Chain progression R893 → R894

Previous harvest: `workers/dispatcher/harvest-6way-r893_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8737         | 3.1885         | +0.3148 |
| ctrl_bpc best  | 2.8070         | 3.1771         | +0.3701 |

## Per-round trajectory (best bird: bsc9i)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 894 | 6482 | 3.1771 | +0.2540 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r893_sym24`

## Output

`workers/dispatcher/harvest-3way-r894_sym24/round-894/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

