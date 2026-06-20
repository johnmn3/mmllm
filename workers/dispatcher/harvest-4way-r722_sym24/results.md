# harvest-4way-r722 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R722 ctrl_bpc |
|--------|--------|--------------:|
| jSSCu | fork-slaa-us-mmllm-claude-train-sym24-615026ee-jSSCu | 3.5313 |
| nhU4j | origin/claude/train-sym24-9969c2b0-nhU4j | 3.5486 |
| m87JF | fork-SeniorCareMarket-mmllm-claude-train-sym24-dfeb3297-m87JF | 3.8312 |
| KZUFp | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-87b6b3b8-KZUFp | 3.8487 |
| **mean** | | **3.6899** |
| **best** | | **3.5313** |

## Chain progression R721 → R722

Previous harvest: `workers/dispatcher/harvest-4way-r721_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.6852         | 3.6899         | +0.0047 |
| ctrl_bpc best  | 3.5276         | 3.5313         | +0.0037 |

## Per-round trajectory (best bird: jSSCu)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 722 | 6440 | 3.5313 | +1.2722 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r721_sym24`

## Output

`workers/dispatcher/harvest-4way-r722_sym24/round-722/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

