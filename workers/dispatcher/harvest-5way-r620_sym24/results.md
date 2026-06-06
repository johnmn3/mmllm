# harvest-5way-r620 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R620 ctrl_bpc |
|--------|--------|--------------:|
| 84NW1 | fork-joly-os-mmllm-claude-train-sym24-33dcc0a2-84NW1 | 2.1241 |
| ghjGs | origin/claude/train-sym24-33091713-ghjGs | 2.1361 |
| mKmDJ | fork-davidwuchn-mmllm-claude-train-sym24-f5500c5a-mKmDJ | 2.1388 |
| Yhu8Q | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-6cdb5c94-Yhu8Q | 2.5890 |
| Nz9hf | fork-slaa-us-mmllm-claude-train-sym24-2856e860-Nz9hf | 2.5903 |
| **mean** | | **2.3157** |
| **best** | | **2.1241** |

## Chain progression R619 → R620

Previous harvest: `workers/dispatcher/harvest-5way-r619_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3086         | 2.3157         | +0.0071 |
| ctrl_bpc best  | 2.1229         | 2.1241         | +0.0012 |

## Per-round trajectory (best bird: 84NW1)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 620 | 5451 | 2.1241 | +0.0347 |

## Cumulative training contribution

- This harvest: **250 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **950 steps** from 19 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r619_sym24`

## Output

`workers/dispatcher/harvest-5way-r620_sym24/round-620/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

