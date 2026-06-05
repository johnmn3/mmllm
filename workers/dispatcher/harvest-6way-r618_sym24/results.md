# harvest-6way-r618 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R618 ctrl_bpc |
|--------|--------|--------------:|
| eUk1n | origin/claude/train-sym24-9768f9c4-eUk1n | 2.1206 |
| Thq1L | fork-slaa-us-mmllm-claude-train-sym24-e68b6516-Thq1L | 2.1438 |
| LVV9e | fork-davidwuchn-mmllm-claude-train-sym24-f0d3de54-LVV9e | 2.1438 |
| ZhvBg | fork-joly-os-mmllm-claude-train-sym24-951c40d3-ZhvBg | 2.3434 |
| jEpAd | fork-SeniorCareMarket-mmllm-claude-train-sym24-5f6d95c5-jEpAd | 2.5955 |
| dL7Y7 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-4d0dbb5b-dL7Y7 | 2.6004 |
| **mean** | | **2.3246** |
| **best** | | **2.1206** |

## Chain progression R617 → R618

Previous harvest: `workers/dispatcher/harvest-3way-r617_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3543         | 2.3246         | -0.0297 |
| ctrl_bpc best  | 2.1231         | 2.1206         | -0.0025 |

## Per-round trajectory (best bird: eUk1n)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 618 | 5413 | 2.1206 | +0.0304 |

## Cumulative training contribution

- This harvest: **300 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **650 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r617_sym24`

## Output

`workers/dispatcher/harvest-6way-r618_sym24/round-618/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

