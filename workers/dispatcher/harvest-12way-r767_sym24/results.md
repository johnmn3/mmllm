# harvest-12way-r767 — sparse-delta merge of 12 birds

## Worker endpoints

| handle | branch | R767 ctrl_bpc |
|--------|--------|--------------:|
| Es81o | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-c3a0e2ce-Es81o | 3.2354 |
| L35YH | fork-slaa-us-mmllm-claude-train-sym24-281385b7-L35YH | 3.2357 |
| oDTNG | fork-joly-os-mmllm-claude-train-sym24-a7430f76-oDTNG | 3.2381 |
| dQleW | origin/claude/train-sym24-357c2a95-dQleW | 3.2643 |
| YUlAP | fork-SeniorCareMarket-mmllm-claude-train-sym24-f9190db4-YUlAP | 3.2874 |
| bbzGD | fork-joly-os-mmllm-claude-train-sym24-3ed51d7d-bbzGD | 3.2911 |
| iZs7y | fork-slaa-us-mmllm-claude-train-sym24-8ef05b5e-iZs7y | 3.2920 |
| uxcfp | fork-davidwuchn-mmllm-claude-train-sym24-81b03135-uxcfp | 3.3630 |
| An4mn | origin/claude/train-sym24-330ebc13-An4mn | 3.3675 |
| JgWwA | fork-davidwuchn-mmllm-claude-train-sym24-ec80a8d9-JgWwA | 3.3680 |
| QmSdP | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-e6c355b3-QmSdP | 3.3696 |
| pSDQD | fork-joly-os-mmllm-claude-train-sym24-263e558c-pSDQD | 3.3737 |
| **mean** | | **3.3072** |
| **best** | | **3.2354** |

## Chain progression R766 → R767

Previous harvest: `workers/dispatcher/harvest-4way-r766_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4540         | 3.3072         | -0.1469 |
| ctrl_bpc best  | 3.2492         | 3.2354         | -0.0138 |

## Per-round trajectory (best bird: Es81o)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 767 | 6398 | 3.2354 | +0.6233 |

## Cumulative training contribution

- This harvest: **960 steps** from 12 bird(s)
- Across full ancestry (deduped by bird_id): **1280 steps** from 16 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-10way-r766_sym24`
  - `workers/dispatcher/harvest-3way-r766_sym24`
  - `workers/dispatcher/harvest-4way-r766_sym24`

## Output

`workers/dispatcher/harvest-12way-r767_sym24/round-767/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 12 workers)
- `dense.pt` (averaged across 12 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

