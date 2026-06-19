# harvest-10way-r715 — sparse-delta merge of 10 birds

## Worker endpoints

| handle | branch | R715 ctrl_bpc |
|--------|--------|--------------:|
| ZyM3G | fork-SeniorCareMarket-mmllm-claude-train-sym24-850db881-ZyM3G | 3.5691 |
| drleb | fork-slaa-us-mmllm-claude-train-sym24-738c2c00-drleb | 3.5700 |
| zL0Zi | fork-joly-os-mmllm-claude-train-sym24-d29ca8a7-zL0Zi | 3.5814 |
| g3WGf | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-c59e94da-g3WGf | 3.8635 |
| ZEg0t | fork-slaa-us-mmllm-claude-train-sym24-cc25a995-ZEg0t | 3.8673 |
| GT5H3 | fork-davidwuchn-mmllm-claude-train-sym24-c6cceef9-GT5H3 | 3.8679 |
| npI3p | origin/claude/train-sym24-87c334e5-npI3p | 3.8708 |
| BMNuk | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f46120da-BMNuk | 3.8713 |
| aLn5d | fork-joly-os-mmllm-claude-train-sym24-82e41e6e-aLn5d | 3.8732 |
| fvaQu | origin/claude/train-sym24-daa5c3fe-fvaQu | 3.8893 |
| **mean** | | **3.7824** |
| **best** | | **3.5691** |

## Chain progression R714 → R715

Previous harvest: `workers/dispatcher/harvest-3way-r714_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5679         | 3.7824         | +0.2145 |
| ctrl_bpc best  | 3.5427         | 3.5691         | +0.0264 |

## Per-round trajectory (best bird: ZyM3G)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 715 | 6438 | 3.5691 | +1.4050 |

## Cumulative training contribution

- This harvest: **800 steps** from 10 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-10way-r714_sym24`
  - `workers/dispatcher/harvest-3way-r714_sym24`

## Output

`workers/dispatcher/harvest-10way-r715_sym24/round-715/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 10 workers)
- `dense.pt` (averaged across 10 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

