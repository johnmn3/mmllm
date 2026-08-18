# harvest-6way-r1242 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1242 ctrl_bpc |
|--------|--------|--------------:|
| kERwH | origin/claude/train-sym24-bf594e28-kERwH | 2.2500 |
| XDCrV | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-3b21fe39-XDCrV | 2.2677 |
| Mxf9f | fork-SeniorCareMarket-mmllm-claude-train-sym24-3002c3ae-Mxf9f | 2.2755 |
| EK25b | fork-joly-os-mmllm-claude-train-sym24-53b0644c-EK25b | 2.4378 |
| WjF5w | fork-slaa-us-mmllm-claude-train-sym24-e4e16228-WjF5w | 2.4441 |
| fMbid | origin/claude/train-sym24-c9f55a7e-fMbid | 2.4502 |
| **mean** | | **2.3542** |
| **best** | | **2.2500** |

## Chain progression R1241 → R1242

Previous harvest: `workers/dispatcher/harvest-7way-r1241_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4284         | 2.3542         | -0.0742 |
| ctrl_bpc best  | 2.2649         | 2.2500         | -0.0149 |

## Per-round trajectory (best bird: kERwH)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1242 | 6342 | 2.2500 | +0.2399 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1241_sym24`

## Output

`workers/dispatcher/harvest-6way-r1242_sym24/round-1242/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

