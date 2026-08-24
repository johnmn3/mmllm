# harvest-7way-r1308 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R1308 ctrl_bpc |
|--------|--------|--------------:|
| xxzd6 | fork-SeniorCareMarket-mmllm-claude-train-sym24-e4f231d9-xxzd6 | 3.4082 |
| 5SXBU | origin/claude/train-sym24-0d3b8658-5SXBU | 3.4175 |
| pbCmk | fork-slaa-us-mmllm-claude-train-sym24-61976d65-pbCmk | 3.5260 |
| vn8hM | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-b4fe17f4-vn8hM | 3.5334 |
| KGcsT | fork-joly-os-mmllm-claude-train-sym24-f174fa38-KGcsT | 3.5378 |
| dddCU | fork-slaa-us-mmllm-claude-train-sym24-243b1a65-dddCU | 3.8610 |
| qWL68 | origin/claude/train-sym24-e7faad92-qWL68 | 3.9627 |
| **mean** | | **3.6067** |
| **best** | | **3.4082** |

## Chain progression R1307 → R1308

Previous harvest: `workers/dispatcher/harvest-5way-r1307_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.6191         | 3.6067         | -0.0124 |
| ctrl_bpc best  | 3.4116         | 3.4082         | -0.0034 |

## Per-round trajectory (best bird: xxzd6)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1308 | 6547 | 3.4082 | +0.1013 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1307_sym24`
  - `workers/dispatcher/harvest-5way-r1307_sym24`

## Output

`workers/dispatcher/harvest-7way-r1308_sym24/round-1308/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

