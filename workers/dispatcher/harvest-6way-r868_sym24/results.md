# harvest-6way-r868 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R868 ctrl_bpc |
|--------|--------|--------------:|
| WvHNj | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-673f9c32-WvHNj | 2.8663 |
| 12gvT | fork-joly-os-mmllm-claude-train-sym24-7936e8bf-12gvT | 2.8966 |
| gOjql | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-a6683517-gOjql | 3.0398 |
| br8Aw | origin/claude/train-sym24-ff4531a2-br8Aw | 3.0446 |
| ic7QU | fork-SeniorCareMarket-mmllm-claude-train-sym24-0547bf47-ic7QU | 3.0638 |
| gAgJE | fork-slaa-us-mmllm-claude-train-sym24-9735b789-gAgJE | 3.2539 |
| **mean** | | **3.0275** |
| **best** | | **2.8663** |

## Chain progression R867 → R868

Previous harvest: `workers/dispatcher/harvest-5way-r867_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0255         | 3.0275         | +0.0020 |
| ctrl_bpc best  | 2.8680         | 2.8663         | -0.0017 |

## Per-round trajectory (best bird: WvHNj)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 868 | 6603 | 2.8663 | +0.4331 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r867_sym24`
  - `workers/dispatcher/harvest-5way-r867_sym24`

## Output

`workers/dispatcher/harvest-6way-r868_sym24/round-868/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

