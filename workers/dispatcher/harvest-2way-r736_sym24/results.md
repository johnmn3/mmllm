# harvest-2way-r736 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R736 ctrl_bpc |
|--------|--------|--------------:|
| MA2mj | origin/claude/train-sym24-2f941a41-MA2mj | 3.4352 |
| TbLLx | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-db5a4815-TbLLx | 3.4361 |
| **mean** | | **3.4356** |
| **best** | | **3.4352** |

## Chain progression R735 → R736

Previous harvest: `workers/dispatcher/harvest-5way-r735_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5171         | 3.4356         | -0.0815 |
| ctrl_bpc best  | 3.3996         | 3.4352         | +0.0356 |

## Per-round trajectory (best bird: MA2mj)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 736 | 6406 | 3.4352 | +0.6534 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r735_sym24`

## Output

`workers/dispatcher/harvest-2way-r736_sym24/round-736/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

