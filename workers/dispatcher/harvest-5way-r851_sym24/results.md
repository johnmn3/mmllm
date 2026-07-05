# harvest-5way-r851 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R851 ctrl_bpc |
|--------|--------|--------------:|
| 4H79s | fork-joly-os-mmllm-claude-train-sym24-e2e8e4a3-4H79s | 2.9281 |
| bTURz | fork-SeniorCareMarket-mmllm-claude-train-sym24-dcb7fa23-bTURz | 2.9341 |
| ClmOe | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-4d065304-ClmOe | 2.9581 |
| KaeSf | fork-slaa-us-mmllm-claude-train-sym24-e9551ce5-KaeSf | 3.2954 |
| 0vYX5 | origin/claude/train-sym24-ecace59c-0vYX5 | 3.3053 |
| **mean** | | **3.0842** |
| **best** | | **2.9281** |

## Chain progression R850 → R851

Previous harvest: `workers/dispatcher/harvest-11way-r850_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0322         | 3.0842         | +0.0520 |
| ctrl_bpc best  | 2.9288         | 2.9281         | -0.0007 |

## Per-round trajectory (best bird: 4H79s)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 851 | 6593 | 2.9281 | +0.3852 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r850_sym24`

## Output

`workers/dispatcher/harvest-5way-r851_sym24/round-851/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

