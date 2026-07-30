# harvest-5way-r1065 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1065 ctrl_bpc |
|--------|--------|--------------:|
| 2q7Zb | origin/claude/train-sym24-9bf5d011-2q7Zb | 2.4624 |
| SvNvE | fork-joly-os-mmllm-claude-train-sym24-42fb8f23-SvNvE | 2.4718 |
| sxPjJ | fork-SeniorCareMarket-mmllm-claude-train-sym24-3fe2d7e2-sxPjJ | 2.4774 |
| tizPo | fork-slaa-us-mmllm-claude-train-sym24-0b63067e-tizPo | 2.8424 |
| 0AyT3 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-d413872d-0AyT3 | 2.8882 |
| **mean** | | **2.6284** |
| **best** | | **2.4624** |

## Chain progression R1064 → R1065

Previous harvest: `workers/dispatcher/harvest-3way-r1064_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7755         | 2.6284         | -0.1471 |
| ctrl_bpc best  | 2.6413         | 2.4624         | -0.1789 |

## Per-round trajectory (best bird: 2q7Zb)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1065 | 6653 | 2.4624 | +0.2153 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1064_sym24`
  - `workers/dispatcher/harvest-3way-r1064_sym24`

## Output

`workers/dispatcher/harvest-5way-r1065_sym24/round-1065/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

