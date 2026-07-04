# harvest-5way-r844 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R844 ctrl_bpc |
|--------|--------|--------------:|
| qjVux | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-5a5df481-qjVux | 2.9499 |
| 59SP9 | origin/claude/train-sym24-cf61e8dd-59SP9 | 2.9527 |
| 7v6lw | fork-SeniorCareMarket-mmllm-claude-train-sym24-703c0889-7v6lw | 2.9572 |
| zIytk | fork-slaa-us-mmllm-claude-train-sym24-a3df2735-zIytk | 3.3205 |
| zsJcQ | fork-joly-os-mmllm-claude-train-sym24-4b8a1cff-zsJcQ | 3.3286 |
| **mean** | | **3.1018** |
| **best** | | **2.9499** |

## Chain progression R843 → R844

Previous harvest: `workers/dispatcher/harvest-3way-r843_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0021         | 3.1018         | +0.0997 |
| ctrl_bpc best  | 2.9531         | 2.9499         | -0.0032 |

## Per-round trajectory (best bird: qjVux)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 844 | 6594 | 2.9499 | +0.3207 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r843_sym24`
  - `workers/dispatcher/harvest-3way-r843_sym24`

## Output

`workers/dispatcher/harvest-5way-r844_sym24/round-844/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

