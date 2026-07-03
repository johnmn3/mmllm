# harvest-3way-r831 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R831 ctrl_bpc |
|--------|--------|--------------:|
| vl0lI | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-e2cab311-vl0lI | 2.9870 |
| eo8hD | fork-SeniorCareMarket-mmllm-claude-train-sym24-8064438c-eo8hD | 3.0066 |
| Tl3kU | fork-slaa-us-mmllm-claude-train-sym24-a9c2473d-Tl3kU | 3.3813 |
| **mean** | | **3.1250** |
| **best** | | **2.9870** |

## Chain progression R830 → R831

Previous harvest: `workers/dispatcher/harvest-4way-r830_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0828         | 3.1250         | +0.0422 |
| ctrl_bpc best  | 2.9814         | 2.9870         | +0.0056 |

## Per-round trajectory (best bird: vl0lI)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 831 | 4397 | 2.9870 | +0.4849 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r830_sym24`

## Output

`workers/dispatcher/harvest-3way-r831_sym24/round-831/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

