# harvest-6way-r936 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R936 ctrl_bpc |
|--------|--------|--------------:|
| lQEly | origin/claude/train-sym24-cbc99989-lQEly | 2.6920 |
| ydmiz | fork-slaa-us-mmllm-claude-train-sym24-b256be69-ydmiz | 2.6937 |
| fKTSI | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-db810aaa-fKTSI | 2.7183 |
| oGJGm | fork-joly-os-mmllm-claude-train-sym24-c6cf9c4e-oGJGm | 2.7237 |
| AdCtU | origin/claude/train-sym24-ce32a90d-AdCtU | 2.8868 |
| J8Gme | fork-SeniorCareMarket-mmllm-claude-train-sym24-f3faee9d-J8Gme | 3.0952 |
| **mean** | | **2.8016** |
| **best** | | **2.6920** |

## Chain progression R935 → R936

Previous harvest: `workers/dispatcher/harvest-6way-r935_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8712         | 2.8016         | -0.0696 |
| ctrl_bpc best  | 2.6912         | 2.6920         | +0.0008 |

## Per-round trajectory (best bird: lQEly)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 936 | 3822 | 2.6920 | +0.1977 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r935_sym24`
  - `workers/dispatcher/harvest-5way-r935_sym24`

## Output

`workers/dispatcher/harvest-6way-r936_sym24/round-936/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

