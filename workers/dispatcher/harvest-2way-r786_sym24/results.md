# harvest-2way-r786 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R786 ctrl_bpc |
|--------|--------|--------------:|
| Bvd9y | origin/claude/train-sym24-7fb8a613-Bvd9y | 3.1602 |
| TdnfK | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-5f12c70f-TdnfK | 3.1866 |
| **mean** | | **3.1734** |
| **best** | | **3.1602** |

## Chain progression R785 → R786

Previous harvest: `workers/dispatcher/harvest-5way-r785_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3430         | 3.1734         | -0.1696 |
| ctrl_bpc best  | 3.1653         | 3.1602         | -0.0051 |

## Per-round trajectory (best bird: Bvd9y)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 786 | 4347 | 3.1602 | +0.5172 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r785_sym24`

## Output

`workers/dispatcher/harvest-2way-r786_sym24/round-786/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

