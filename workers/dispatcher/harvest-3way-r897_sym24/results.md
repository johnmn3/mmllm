# harvest-3way-r897 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R897 ctrl_bpc |
|--------|--------|--------------:|
| bWHYo | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-0f5a47f3-bWHYo | 2.7932 |
| 8rkSb | fork-joly-os-mmllm-claude-train-sym24-a97fba48-8rkSb | 2.8082 |
| FunLQ | fork-SeniorCareMarket-mmllm-claude-train-sym24-cf42b5bb-FunLQ | 3.1737 |
| **mean** | | **2.9250** |
| **best** | | **2.7932** |

## Chain progression R896 → R897

Previous harvest: `workers/dispatcher/harvest-12way-r896_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9566         | 2.9250         | -0.0316 |
| ctrl_bpc best  | 2.7845         | 2.7932         | +0.0087 |

## Per-round trajectory (best bird: bWHYo)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 897 | 5512 | 2.7932 | +0.2219 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r896_sym24`

## Output

`workers/dispatcher/harvest-3way-r897_sym24/round-897/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

