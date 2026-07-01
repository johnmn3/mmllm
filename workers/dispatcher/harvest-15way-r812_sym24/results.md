# harvest-15way-r812 — sparse-delta merge of 15 birds

## Worker endpoints

| handle | branch | R812 ctrl_bpc |
|--------|--------|--------------:|
| 8sfJp | fork-SeniorCareMarket-mmllm-claude-train-sym24-e4d28adc-8sfJp | 3.0603 |
| Ti3MK | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-288b1dbf-Ti3MK | 3.0627 |
| w1BJ0 | fork-joly-os-mmllm-claude-train-sym24-7f665514-w1BJ0 | 3.0749 |
| 5SJwb | fork-davidwuchn-mmllm-claude-train-sym24-b6856a1a-5SJwb | 3.0751 |
| 7tGuU | fork-SeniorCareMarket-mmllm-claude-train-sym24-d13bbc8c-7tGuU | 3.0822 |
| zspga | fork-slaa-us-mmllm-claude-train-sym24-6f031d6c-zspga | 3.1836 |
| WiX8x | fork-joly-os-mmllm-claude-train-sym24-dcb054c2-WiX8x | 3.1869 |
| jav3m | fork-davidwuchn-mmllm-claude-train-sym24-8ae4a57b-jav3m | 3.1872 |
| kUJjH | fork-slaa-us-mmllm-claude-train-sym24-27efc45b-kUJjH | 3.1886 |
| I0b9G | origin/claude/train-sym24-91829ce0-I0b9G | 3.2038 |
| XSN1U | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-09d608cf-XSN1U | 3.2225 |
| pWeu7 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-2b0a1ae3-pWeu7 | 3.4227 |
| TtEHV | fork-slaa-us-mmllm-claude-train-sym24-f67e29d1-TtEHV | 3.4278 |
| FqzPj | origin/claude/train-sym24-c1096e6e-FqzPj | 3.4320 |
| JnsTt | origin/claude/train-sym24-54d993a6-JnsTt | 3.4326 |
| **mean** | | **3.2162** |
| **best** | | **3.0603** |

## Chain progression R811 → R812

Previous harvest: `workers/dispatcher/harvest-9way-r811_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2641         | 3.2162         | -0.0479 |
| ctrl_bpc best  | 3.0709         | 3.0603         | -0.0106 |

## Per-round trajectory (best bird: 8sfJp)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 812 | 6623 | 3.0603 | +0.6028 |

## Cumulative training contribution

- This harvest: **1200 steps** from 15 bird(s)
- Across full ancestry (deduped by bird_id): **1680 steps** from 21 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r811_sym24`
  - `workers/dispatcher/harvest-6way-r811_sym24`

## Output

`workers/dispatcher/harvest-15way-r812_sym24/round-812/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 15 workers)
- `dense.pt` (averaged across 15 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

