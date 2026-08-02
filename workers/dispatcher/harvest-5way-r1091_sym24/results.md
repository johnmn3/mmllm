# harvest-5way-r1091 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1091 ctrl_bpc |
|--------|--------|--------------:|
| NrZ0M | fork-slaa-us-mmllm-claude-train-sym24-4d473c0e-NrZ0M | 2.4054 |
| iXm2J | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-df039fb3-iXm2J | 2.4076 |
| FeK5K | origin/claude/train-sym24-e3f9e4a7-FeK5K | 2.4082 |
| tcPrf | fork-SeniorCareMarket-mmllm-claude-train-sym24-4dafaf35-tcPrf | 2.4106 |
| PnKhD | fork-joly-os-mmllm-claude-train-sym24-3e3f0439-PnKhD | 2.8264 |
| **mean** | | **2.4916** |
| **best** | | **2.4054** |

## Chain progression R1090 → R1091

Previous harvest: `workers/dispatcher/harvest-5way-r1090_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5807         | 2.4916         | -0.0891 |
| ctrl_bpc best  | 2.4119         | 2.4054         | -0.0065 |

## Per-round trajectory (best bird: NrZ0M)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1091 | 6550 | 2.4054 | +0.2430 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1090_sym24`
  - `workers/dispatcher/harvest-5way-r1090_sym24`

## Output

`workers/dispatcher/harvest-5way-r1091_sym24/round-1091/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

