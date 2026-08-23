# harvest-5way-r1293 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1293 ctrl_bpc |
|--------|--------|--------------:|
| eML8p | fork-slaa-us-mmllm-claude-train-sym24-ad52e57b-eML8p | 4.3090 |
| m3AtG | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f7da0a5b-m3AtG | 4.3161 |
| AjHGU | origin/claude/train-sym24-dccc789c-AjHGU | 4.3203 |
| TJLMv | fork-slaa-us-mmllm-claude-train-sym24-bde3a49c-TJLMv | 4.3290 |
| m1JGH | fork-SeniorCareMarket-mmllm-claude-train-sym24-fa444ef1-m1JGH | 4.8465 |
| **mean** | | **4.4242** |
| **best** | | **4.3090** |

## Chain progression R1292 → R1293

Previous harvest: `workers/dispatcher/harvest-11way-r1292_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.8701         | 4.4242         | -0.4459 |
| ctrl_bpc best  | 4.5577         | 4.3090         | -0.2487 |

## Per-round trajectory (best bird: eML8p)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1293 | 4318 | 4.3090 | +0.0431 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **1280 steps** from 16 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-11way-r1292_sym24`
  - `workers/dispatcher/harvest-7way-r1292_sym24`

## Output

`workers/dispatcher/harvest-5way-r1293_sym24/round-1293/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

