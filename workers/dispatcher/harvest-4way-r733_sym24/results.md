# harvest-4way-r733 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R733 ctrl_bpc |
|--------|--------|--------------:|
| twnP7 | fork-slaa-us-mmllm-claude-train-sym24-4699522e-twnP7 | 3.4251 |
| xyYXN | fork-joly-os-mmllm-claude-train-sym24-7a2218ad-xyYXN | 3.4367 |
| ikg8B | fork-davidwuchn-mmllm-claude-train-sym24-72baedfb-ikg8B | 3.4837 |
| 4QQYx | fork-SeniorCareMarket-mmllm-claude-train-sym24-d67f1fa8-4QQYx | 3.7596 |
| **mean** | | **3.5263** |
| **best** | | **3.4251** |

## Chain progression R732 → R733

Previous harvest: `workers/dispatcher/harvest-16way-r732_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5288         | 3.5263         | -0.0025 |
| ctrl_bpc best  | 3.4177         | 3.4251         | +0.0074 |

## Per-round trajectory (best bird: twnP7)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 733 | 6595 | 3.4251 | +0.6685 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r732_sym24`

## Output

`workers/dispatcher/harvest-4way-r733_sym24/round-733/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

