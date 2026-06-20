# harvest-6way-r722 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R722 ctrl_bpc |
|--------|--------|--------------:|
| mKHOv | fork-joly-os-mmllm-claude-train-sym24-1358273a-mKHOv | 3.4965 |
| vuQYl | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-7a98eb61-vuQYl | 3.5101 |
| jSSCu | fork-slaa-us-mmllm-claude-train-sym24-615026ee-jSSCu | 3.5313 |
| nhU4j | origin/claude/train-sym24-9969c2b0-nhU4j | 3.5486 |
| m87JF | fork-SeniorCareMarket-mmllm-claude-train-sym24-dfeb3297-m87JF | 3.8312 |
| KZUFp | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-87b6b3b8-KZUFp | 3.8487 |
| **mean** | | **3.6277** |
| **best** | | **3.4965** |

## Chain progression R721 → R722

Previous harvest: `workers/dispatcher/harvest-4way-r721_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.6852         | 3.6277         | -0.0575 |
| ctrl_bpc best  | 3.5276         | 3.4965         | -0.0311 |

## Per-round trajectory (best bird: mKHOv)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 722 | 6371 | 3.4965 | +0.6383 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r721_sym24`
  - `workers/dispatcher/harvest-4way-r721_sym24`

## Output

`workers/dispatcher/harvest-6way-r722_sym24/round-722/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

