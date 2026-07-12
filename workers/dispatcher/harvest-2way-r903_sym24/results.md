# harvest-2way-r903 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R903 ctrl_bpc |
|--------|--------|--------------:|
| Vb59F | fork-joly-os-mmllm-claude-train-sym24-253470a9-Vb59F | 2.7960 |
| uIOEo | origin/claude/train-sym24-7bd7bb69-uIOEo | 3.1723 |
| **mean** | | **2.9841** |
| **best** | | **2.7960** |

## Chain progression R902 → R903

Previous harvest: `workers/dispatcher/harvest-9way-r902_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8448         | 2.9841         | +0.1393 |
| ctrl_bpc best  | 2.7724         | 2.7960         | +0.0236 |

## Per-round trajectory (best bird: Vb59F)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 903 | 4437 | 2.7960 | +0.4062 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r902_sym24`

## Output

`workers/dispatcher/harvest-2way-r903_sym24/round-903/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

