# harvest-6way-r931 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R931 ctrl_bpc |
|--------|--------|--------------:|
| ioNOy | fork-slaa-us-mmllm-claude-train-sym24-ac2ed231-ioNOy | 2.6972 |
| yJWdH | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-e3620322-yJWdH | 2.7542 |
| v8Rct | fork-SeniorCareMarket-mmllm-claude-train-sym24-be42d9fe-v8Rct | 3.0895 |
| kFhEv | origin/claude/train-sym24-f6d55192-kFhEv | 3.0963 |
| ocBqf | origin/claude/train-sym24-17d0c6dd-ocBqf | 3.1073 |
| Vjdxs | fork-joly-os-mmllm-claude-train-sym24-1d2edd75-Vjdxs | 3.1233 |
| **mean** | | **2.9780** |
| **best** | | **2.6972** |

## Chain progression R930 → R931

Previous harvest: `workers/dispatcher/harvest-12way-r930_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8614         | 2.9780         | +0.1166 |
| ctrl_bpc best  | 2.7118         | 2.6972         | -0.0146 |

## Per-round trajectory (best bird: ioNOy)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 931 | 6528 | 2.6972 | +0.2236 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-10way-r930_sym24`
  - `workers/dispatcher/harvest-5way-r930_sym24`

## Output

`workers/dispatcher/harvest-6way-r931_sym24/round-931/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

