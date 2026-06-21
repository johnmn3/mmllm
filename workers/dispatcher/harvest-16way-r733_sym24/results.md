# harvest-16way-r733 — sparse-delta merge of 16 birds

## Worker endpoints

| handle | branch | R733 ctrl_bpc |
|--------|--------|--------------:|
| OIF22 | fork-davidwuchn-mmllm-claude-train-sym24-11a5768c-OIF22 | 3.4157 |
| twnP7 | fork-slaa-us-mmllm-claude-train-sym24-4699522e-twnP7 | 3.4251 |
| UETdF | fork-SeniorCareMarket-mmllm-claude-train-sym24-85ddb314-UETdF | 3.4261 |
| rLvXo | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-ed16deb8-rLvXo | 3.4286 |
| xyYXN | fork-joly-os-mmllm-claude-train-sym24-7a2218ad-xyYXN | 3.4367 |
| HSgC3 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-333c377d-HSgC3 | 3.4581 |
| c35VF | fork-slaa-us-mmllm-claude-train-sym24-075e878a-c35VF | 3.4642 |
| ikg8B | fork-davidwuchn-mmllm-claude-train-sym24-72baedfb-ikg8B | 3.4837 |
| o9Fhm | origin/claude/train-sym24-bd5b7882-o9Fhm | 3.4845 |
| M1cT6 | fork-slaa-us-mmllm-claude-train-sym24-bc6f2cd7-M1cT6 | 3.4869 |
| Mn5Nj | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-99ba2068-Mn5Nj | 3.4932 |
| BdpT2 | fork-joly-os-mmllm-claude-train-sym24-371afd09-BdpT2 | 3.5031 |
| 4QQYx | fork-SeniorCareMarket-mmllm-claude-train-sym24-d67f1fa8-4QQYx | 3.7596 |
| X6UDy | fork-joly-os-mmllm-claude-train-sym24-c20d5a8e-X6UDy | 3.7655 |
| 4ws8B | origin/claude/train-sym24-6abd0bb2-4ws8B | 3.7897 |
| p0FJr | fork-davidwuchn-mmllm-claude-train-sym24-7e5f531b-p0FJr | 3.8166 |
| **mean** | | **3.5398** |
| **best** | | **3.4157** |

## Chain progression R732 → R733

Previous harvest: `workers/dispatcher/harvest-5way-r732_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.6639         | 3.5398         | -0.1241 |
| ctrl_bpc best  | 3.4669         | 3.4157         | -0.0512 |

## Per-round trajectory (best bird: OIF22)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 733 | 4409 | 3.4157 | +0.6296 |

## Cumulative training contribution

- This harvest: **1280 steps** from 16 bird(s)
- Across full ancestry (deduped by bird_id): **1680 steps** from 21 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-10way-r732_sym24`
  - `workers/dispatcher/harvest-16way-r732_sym24`
  - `workers/dispatcher/harvest-5way-r732_sym24`

## Output

`workers/dispatcher/harvest-16way-r733_sym24/round-733/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 16 workers)
- `dense.pt` (averaged across 16 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

