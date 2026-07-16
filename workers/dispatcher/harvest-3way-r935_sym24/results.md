# harvest-3way-r935 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R935 ctrl_bpc |
|--------|--------|--------------:|
| Zv9xG | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-120c38b5-Zv9xG | 2.6912 |
| VtqUp | fork-slaa-us-mmllm-claude-train-sym24-72496c2b-VtqUp | 2.7029 |
| 0CTTp | origin/claude/train-sym24-f455971b-0CTTp | 3.1019 |
| **mean** | | **2.8320** |
| **best** | | **2.6912** |

## Chain progression R934 → R935

Previous harvest: `workers/dispatcher/harvest-3way-r934_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8546         | 2.8320         | -0.0226 |
| ctrl_bpc best  | 2.6981         | 2.6912         | -0.0069 |

## Per-round trajectory (best bird: Zv9xG)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 935 | 6458 | 2.6912 | +0.2197 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r934_sym24`

## Output

`workers/dispatcher/harvest-3way-r935_sym24/round-935/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

