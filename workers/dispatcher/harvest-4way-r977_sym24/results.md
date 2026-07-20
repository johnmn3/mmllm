# harvest-4way-r977 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R977 ctrl_bpc |
|--------|--------|--------------:|
| eYoAZ | fork-joly-os-mmllm-claude-train-sym24-411bc05d-eYoAZ | 2.6082 |
| T4bwA | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-b3d28fa3-T4bwA | 2.6356 |
| FNkq9 | origin/claude/train-sym24-175570a2-FNkq9 | 2.8003 |
| TH9w3 | origin/claude/train-sym24-ee936c7b-TH9w3 | 2.9932 |
| **mean** | | **2.7593** |
| **best** | | **2.6082** |

## Chain progression R976 → R977

Previous harvest: `workers/dispatcher/harvest-3way-r976_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6189         | 2.7593         | +0.1404 |
| ctrl_bpc best  | 2.6002         | 2.6082         | +0.0080 |

## Per-round trajectory (best bird: eYoAZ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 977 | 6301 | 2.6082 | +0.1714 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r976_sym24`

## Output

`workers/dispatcher/harvest-4way-r977_sym24/round-977/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

