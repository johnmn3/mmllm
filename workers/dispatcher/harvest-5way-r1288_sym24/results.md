# harvest-5way-r1288 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1288 ctrl_bpc |
|--------|--------|--------------:|
| hdcMf | fork-slaa-us-mmllm-claude-train-sym24-9c0302eb-hdcMf | 2.2089 |
| Y44Yh | fork-joly-os-mmllm-claude-train-sym24-224e8254-Y44Yh | 2.2258 |
| P5Kj1 | fork-SeniorCareMarket-mmllm-claude-train-sym24-ee89fa79-P5Kj1 | 2.2263 |
| 8NAQ9 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-766ed2ee-8NAQ9 | 2.4208 |
| 5WEsF | fork-SeniorCareMarket-mmllm-claude-train-sym24-8c8f7f71-5WEsF | 2.6385 |
| **mean** | | **2.3441** |
| **best** | | **2.2089** |

## Chain progression R1287 → R1288

Previous harvest: `workers/dispatcher/harvest-11way-r1287_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3329         | 2.3441         | +0.0112 |
| ctrl_bpc best  | 2.2147         | 2.2089         | -0.0058 |

## Per-round trajectory (best bird: hdcMf)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1288 | 4367 | 2.2089 | +0.2489 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **1280 steps** from 16 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-11way-r1287_sym24`
  - `workers/dispatcher/harvest-4way-r1287_sym24`

## Output

`workers/dispatcher/harvest-5way-r1288_sym24/round-1288/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

