# harvest-3way-r1068 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1068 ctrl_bpc |
|--------|--------|--------------:|
| JZQ17 | fork-slaa-us-mmllm-claude-train-sym24-ddde5a34-JZQ17 | 2.4399 |
| EbPM2 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-bccd3998-EbPM2 | 2.4502 |
| swp7L | fork-SeniorCareMarket-mmllm-claude-train-sym24-f9556aab-swp7L | 2.8480 |
| **mean** | | **2.5794** |
| **best** | | **2.4399** |

## Chain progression R1067 → R1068

Previous harvest: `workers/dispatcher/harvest-8way-r1067_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5958         | 2.5794         | -0.0164 |
| ctrl_bpc best  | 2.4475         | 2.4399         | -0.0076 |

## Per-round trajectory (best bird: JZQ17)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1068 | 3552 | 2.4399 | +0.2309 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r1067_sym24`

## Output

`workers/dispatcher/harvest-3way-r1068_sym24/round-1068/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

