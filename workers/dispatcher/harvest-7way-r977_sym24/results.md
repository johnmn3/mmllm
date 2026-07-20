# harvest-7way-r977 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R977 ctrl_bpc |
|--------|--------|--------------:|
| eYoAZ | fork-joly-os-mmllm-claude-train-sym24-411bc05d-eYoAZ | 2.6082 |
| EolZ1 | fork-slaa-us-mmllm-claude-train-sym24-21281d5c-EolZ1 | 2.6347 |
| T4bwA | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-b3d28fa3-T4bwA | 2.6356 |
| DEfum | origin/claude/train-sym24-be8476e8-DEfum | 2.7896 |
| FNkq9 | origin/claude/train-sym24-175570a2-FNkq9 | 2.8003 |
| MqsAk | fork-SeniorCareMarket-mmllm-claude-train-sym24-9b98eb00-MqsAk | 2.8065 |
| TH9w3 | origin/claude/train-sym24-ee936c7b-TH9w3 | 2.9932 |
| **mean** | | **2.7526** |
| **best** | | **2.6082** |

## Chain progression R976 → R977

Previous harvest: `workers/dispatcher/harvest-3way-r976_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6189         | 2.7526         | +0.1337 |
| ctrl_bpc best  | 2.6002         | 2.6082         | +0.0080 |

## Per-round trajectory (best bird: eYoAZ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 977 | 6301 | 2.6082 | +0.1714 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r976_sym24`
  - `workers/dispatcher/harvest-3way-r976_sym24`

## Output

`workers/dispatcher/harvest-7way-r977_sym24/round-977/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

