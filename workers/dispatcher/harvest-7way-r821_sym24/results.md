# harvest-7way-r821 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R821 ctrl_bpc |
|--------|--------|--------------:|
| ejbhY | fork-slaa-us-mmllm-claude-train-sym24-f45b6ddb-ejbhY | 3.0212 |
| mYRGj | fork-joly-os-mmllm-claude-train-sym24-1f0af589-mYRGj | 3.0312 |
| 1RlZM | origin/claude/train-sym24-e17c9b58-1RlZM | 3.0474 |
| VXBgj | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-e3a9dbfa-VXBgj | 3.1615 |
| Cjf3O | origin/claude/train-sym24-ac09ea49-Cjf3O | 3.1762 |
| fncW9 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-9fc63b54-fncW9 | 3.4098 |
| g41hM | fork-slaa-us-mmllm-claude-train-sym24-edc55f00-g41hM | 3.4168 |
| **mean** | | **3.1806** |
| **best** | | **3.0212** |

## Chain progression R820 → R821

Previous harvest: `workers/dispatcher/harvest-7way-r820_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1216         | 3.1806         | +0.0590 |
| ctrl_bpc best  | 3.0266         | 3.0212         | -0.0054 |

## Per-round trajectory (best bird: ejbhY)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 821 | 6576 | 3.0212 | +0.5002 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r820_sym24`

## Output

`workers/dispatcher/harvest-7way-r821_sym24/round-821/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

