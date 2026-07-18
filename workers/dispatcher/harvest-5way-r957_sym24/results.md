# harvest-5way-r957 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R957 ctrl_bpc |
|--------|--------|--------------:|
| hJVuh | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-8a1972a2-hJVuh | 2.6423 |
| 7Cxjd | fork-SeniorCareMarket-mmllm-claude-train-sym24-c51ddded-7Cxjd | 2.6577 |
| 88Dh8 | fork-slaa-us-mmllm-claude-train-sym24-03c652ed-88Dh8 | 2.6725 |
| 5fP8Y | origin/claude/train-sym24-b6a58b1c-5fP8Y | 3.0261 |
| jBpWE | fork-slaa-us-mmllm-claude-train-sym24-3df8cb05-jBpWE | 3.0460 |
| **mean** | | **2.8089** |
| **best** | | **2.6423** |

## Chain progression R956 → R957

Previous harvest: `workers/dispatcher/harvest-5way-r956_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7988         | 2.8089         | +0.0101 |
| ctrl_bpc best  | 2.6360         | 2.6423         | +0.0063 |

## Per-round trajectory (best bird: hJVuh)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 957 | 6500 | 2.6423 | +0.2034 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r956_sym24`
  - `workers/dispatcher/harvest-5way-r956_sym24`

## Output

`workers/dispatcher/harvest-5way-r957_sym24/round-957/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

