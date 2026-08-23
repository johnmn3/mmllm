# harvest-4way-r1295 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1295 ctrl_bpc |
|--------|--------|--------------:|
| vkJs9 | fork-slaa-us-mmllm-claude-train-sym24-845762d8-vkJs9 | 4.0499 |
| goIbc | fork-joly-os-mmllm-claude-train-sym24-eacb7d06-goIbc | 4.1162 |
| irkpi | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-26db4181-irkpi | 4.1182 |
| TZTeg | fork-SeniorCareMarket-mmllm-claude-train-sym24-fb27e731-TZTeg | 4.4615 |
| **mean** | | **4.1864** |
| **best** | | **4.0499** |

## Chain progression R1294 → R1295

Previous harvest: `workers/dispatcher/harvest-8way-r1294_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.3100         | 4.1864         | -0.1235 |
| ctrl_bpc best  | 4.1198         | 4.0499         | -0.0699 |

## Per-round trajectory (best bird: vkJs9)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1295 | 6581 | 4.0499 | +0.0295 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1294_sym24`

## Output

`workers/dispatcher/harvest-4way-r1295_sym24/round-1295/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

