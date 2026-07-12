# harvest-7way-r903 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R903 ctrl_bpc |
|--------|--------|--------------:|
| lER06 | fork-joly-os-mmllm-claude-train-sym24-08d7bcec-lER06 | 2.7893 |
| Vb59F | fork-joly-os-mmllm-claude-train-sym24-253470a9-Vb59F | 2.7960 |
| BHXj1 | fork-SeniorCareMarket-mmllm-claude-train-sym24-346e3cd0-BHXj1 | 2.7969 |
| jVP6v | origin/claude/train-sym24-599c3ad5-jVP6v | 2.9586 |
| cAjDo | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f3233bed-cAjDo | 2.9729 |
| LUgqj | fork-slaa-us-mmllm-claude-train-sym24-37fc2061-LUgqj | 3.1556 |
| uIOEo | origin/claude/train-sym24-7bd7bb69-uIOEo | 3.1723 |
| **mean** | | **2.9488** |
| **best** | | **2.7893** |

## Chain progression R902 → R903

Previous harvest: `workers/dispatcher/harvest-9way-r902_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8448         | 2.9488         | +0.1040 |
| ctrl_bpc best  | 2.7724         | 2.7893         | +0.0169 |

## Per-round trajectory (best bird: lER06)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 903 | 4366 | 2.7893 | +0.2587 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r902_sym24`
  - `workers/dispatcher/harvest-7way-r902_sym24`

## Output

`workers/dispatcher/harvest-7way-r903_sym24/round-903/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

