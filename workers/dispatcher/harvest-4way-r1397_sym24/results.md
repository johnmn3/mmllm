# harvest-4way-r1397 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1397 ctrl_bpc |
|--------|--------|--------------:|
| PPenZ | fork-joly-os-mmllm-claude-train-sym24-0bc8cd2a-PPenZ | 3.2680 |
| v2Osv | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-ffa6e8e7-v2Osv | 3.4308 |
| lVkLN | fork-SeniorCareMarket-mmllm-claude-train-sym24-ec89ba19-lVkLN | 3.5537 |
| EimFK | origin/claude/train-sym24-daf4c9d4-EimFK | 3.6624 |
| **mean** | | **3.4787** |
| **best** | | **3.2680** |

## Chain progression R1396 → R1397

Previous harvest: `workers/dispatcher/harvest-8way-r1396_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.9022         | 3.4787         | -0.4235 |
| ctrl_bpc best  | 3.4255         | 3.2680         | -0.1575 |

## Per-round trajectory (best bird: PPenZ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1397 | 6450 | 3.2680 | +0.0867 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1396_sym24`

## Output

`workers/dispatcher/harvest-4way-r1397_sym24/round-1397/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

