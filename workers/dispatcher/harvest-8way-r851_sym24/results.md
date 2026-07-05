# harvest-8way-r851 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R851 ctrl_bpc |
|--------|--------|--------------:|
| 4H79s | fork-joly-os-mmllm-claude-train-sym24-e2e8e4a3-4H79s | 2.9281 |
| bTURz | fork-SeniorCareMarket-mmllm-claude-train-sym24-dcb7fa23-bTURz | 2.9341 |
| ClmOe | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-4d065304-ClmOe | 2.9581 |
| dwYDl | origin/claude/train-sym24-f222eec4-dwYDl | 3.0837 |
| KaeSf | fork-slaa-us-mmllm-claude-train-sym24-e9551ce5-KaeSf | 3.2954 |
| 0vYX5 | origin/claude/train-sym24-ecace59c-0vYX5 | 3.3053 |
| 4SeoJ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-d076c0aa-4SeoJ | 3.3064 |
| GP7wf | fork-joly-os-mmllm-claude-train-sym24-3f9f81ec-GP7wf | 3.3103 |
| **mean** | | **3.1402** |
| **best** | | **2.9281** |

## Chain progression R850 → R851

Previous harvest: `workers/dispatcher/harvest-9way-r850_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0110         | 3.1402         | +0.1292 |
| ctrl_bpc best  | 2.9288         | 2.9281         | -0.0007 |

## Per-round trajectory (best bird: 4H79s)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 851 | 6593 | 2.9281 | +0.3852 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-11way-r850_sym24`
  - `workers/dispatcher/harvest-5way-r850_sym24`

## Output

`workers/dispatcher/harvest-8way-r851_sym24/round-851/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

