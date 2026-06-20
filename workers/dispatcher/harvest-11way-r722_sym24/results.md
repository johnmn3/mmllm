# harvest-11way-r722 — sparse-delta merge of 11 birds

## Worker endpoints

| handle | branch | R722 ctrl_bpc |
|--------|--------|--------------:|
| mKHOv | fork-joly-os-mmllm-claude-train-sym24-1358273a-mKHOv | 3.4965 |
| vuQYl | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-7a98eb61-vuQYl | 3.5101 |
| z342P | fork-joly-os-mmllm-claude-train-sym24-d878230d-z342P | 3.5269 |
| jSSCu | fork-slaa-us-mmllm-claude-train-sym24-615026ee-jSSCu | 3.5313 |
| HcFXz | fork-davidwuchn-mmllm-claude-train-sym24-5b3bdcd3-HcFXz | 3.5334 |
| zgYDV | fork-davidwuchn-mmllm-claude-train-sym24-600d35b0-zgYDV | 3.5442 |
| nhU4j | origin/claude/train-sym24-9969c2b0-nhU4j | 3.5486 |
| m87JF | fork-SeniorCareMarket-mmllm-claude-train-sym24-dfeb3297-m87JF | 3.8312 |
| DL0Ox | origin/claude/train-sym24-6aea757c-DL0Ox | 3.8315 |
| NST3o | fork-slaa-us-mmllm-claude-train-sym24-f0b188b9-NST3o | 3.8463 |
| KZUFp | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-87b6b3b8-KZUFp | 3.8487 |
| **mean** | | **3.6408** |
| **best** | | **3.4965** |

## Chain progression R721 → R722

Previous harvest: `workers/dispatcher/harvest-4way-r721_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.6852         | 3.6408         | -0.0444 |
| ctrl_bpc best  | 3.5276         | 3.4965         | -0.0311 |

## Per-round trajectory (best bird: mKHOv)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 722 | 6371 | 3.4965 | +0.6383 |

## Cumulative training contribution

- This harvest: **880 steps** from 11 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r721_sym24`
  - `workers/dispatcher/harvest-4way-r721_sym24`

## Output

`workers/dispatcher/harvest-11way-r722_sym24/round-722/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 11 workers)
- `dense.pt` (averaged across 11 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

