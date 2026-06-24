# harvest-4way-r753 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R753 ctrl_bpc |
|--------|--------|--------------:|
| yS3lP | fork-slaa-us-mmllm-claude-train-sym24-dbcf695b-yS3lP | 3.3173 |
| jcF62 | origin/claude/train-sym24-faa42397-jcF62 | 3.3286 |
| NsZHR | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-7a0d83ee-NsZHR | 3.3516 |
| IvU3t | fork-joly-os-mmllm-claude-train-sym24-07ab6a39-IvU3t | 3.4057 |
| **mean** | | **3.3508** |
| **best** | | **3.3173** |

## Chain progression R752 → R753

Previous harvest: `workers/dispatcher/harvest-2way-r752_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3580         | 3.3508         | -0.0072 |
| ctrl_bpc best  | 3.3561         | 3.3173         | -0.0388 |

## Per-round trajectory (best bird: yS3lP)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 753 | 6646 | 3.3173 | +0.6637 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r752_sym24`

## Output

`workers/dispatcher/harvest-4way-r753_sym24/round-753/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

