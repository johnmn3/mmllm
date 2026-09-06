# harvest-5way-r1399 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1399 ctrl_bpc |
|--------|--------|--------------:|
| zPKtc | fork-SeniorCareMarket-mmllm-claude-train-sym24-ad5d7f6a-zPKtc | 3.3309 |
| mMQ8p | fork-joly-os-mmllm-claude-train-sym24-343a2d3f-mMQ8p | 3.4839 |
| Rb3bv | fork-joly-os-mmllm-claude-train-sym24-4cec859d-Rb3bv | 3.7559 |
| KzzpU | origin/claude/train-sym24-90ad8321-KzzpU | 3.7561 |
| 59FZC | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-0a3774b3-59FZC | 4.0846 |
| **mean** | | **3.6823** |
| **best** | | **3.3309** |

## Chain progression R1398 → R1399

Previous harvest: `workers/dispatcher/harvest-8way-r1398_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.7130         | 3.6823         | -0.0307 |
| ctrl_bpc best  | 3.3661         | 3.3309         | -0.0352 |

## Per-round trajectory (best bird: zPKtc)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1399 | 5300 | 3.3309 | +0.0678 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **1680 steps** from 21 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1398_sym24`
  - `workers/dispatcher/harvest-8way-r1398_sym24`

## Output

`workers/dispatcher/harvest-5way-r1399_sym24/round-1399/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

