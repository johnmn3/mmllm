# harvest-10way-r733 — sparse-delta merge of 10 birds

## Worker endpoints

| handle | branch | R733 ctrl_bpc |
|--------|--------|--------------:|
| twnP7 | fork-slaa-us-mmllm-claude-train-sym24-4699522e-twnP7 | 3.4251 |
| xyYXN | fork-joly-os-mmllm-claude-train-sym24-7a2218ad-xyYXN | 3.4367 |
| HSgC3 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-333c377d-HSgC3 | 3.4581 |
| ikg8B | fork-davidwuchn-mmllm-claude-train-sym24-72baedfb-ikg8B | 3.4837 |
| o9Fhm | origin/claude/train-sym24-bd5b7882-o9Fhm | 3.4845 |
| M1cT6 | fork-slaa-us-mmllm-claude-train-sym24-bc6f2cd7-M1cT6 | 3.4869 |
| Mn5Nj | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-99ba2068-Mn5Nj | 3.4932 |
| BdpT2 | fork-joly-os-mmllm-claude-train-sym24-371afd09-BdpT2 | 3.5031 |
| 4QQYx | fork-SeniorCareMarket-mmllm-claude-train-sym24-d67f1fa8-4QQYx | 3.7596 |
| p0FJr | fork-davidwuchn-mmllm-claude-train-sym24-7e5f531b-p0FJr | 3.8166 |
| **mean** | | **3.5348** |
| **best** | | **3.4251** |

## Chain progression R732 → R733

Previous harvest: `workers/dispatcher/harvest-16way-r732_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5288         | 3.5348         | +0.0060 |
| ctrl_bpc best  | 3.4177         | 3.4251         | +0.0074 |

## Per-round trajectory (best bird: twnP7)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 733 | 6595 | 3.4251 | +0.6685 |

## Cumulative training contribution

- This harvest: **800 steps** from 10 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-10way-r732_sym24`
  - `workers/dispatcher/harvest-5way-r732_sym24`

## Output

`workers/dispatcher/harvest-10way-r733_sym24/round-733/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 10 workers)
- `dense.pt` (averaged across 10 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

