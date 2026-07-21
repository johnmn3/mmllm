# harvest-5way-r987 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R987 ctrl_bpc |
|--------|--------|--------------:|
| 3PTiM | fork-slaa-us-mmllm-claude-train-sym24-0d882d22-3PTiM | 2.5988 |
| tQU4q | fork-joly-os-mmllm-claude-train-sym24-0cdb0ce0-tQU4q | 2.6035 |
| TaYJP | origin/claude/train-sym24-62c0365f-TaYJP | 2.6058 |
| YD97i | fork-SeniorCareMarket-mmllm-claude-train-sym24-498e7767-YD97i | 2.6225 |
| KbO5f | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-8ae6d8a6-KbO5f | 2.6226 |
| **mean** | | **2.6106** |
| **best** | | **2.5988** |

## Chain progression R986 → R987

Previous harvest: `workers/dispatcher/harvest-9way-r986_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7244         | 2.6106         | -0.1138 |
| ctrl_bpc best  | 2.5851         | 2.5988         | +0.0137 |

## Per-round trajectory (best bird: 3PTiM)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 987 | 4075 | 2.5988 | +0.1546 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r986_sym24`
  - `workers/dispatcher/harvest-7way-r986_sym24`

## Output

`workers/dispatcher/harvest-5way-r987_sym24/round-987/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

