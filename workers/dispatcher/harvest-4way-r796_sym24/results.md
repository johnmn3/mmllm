# harvest-4way-r796 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R796 ctrl_bpc |
|--------|--------|--------------:|
| ttBzr | fork-davidwuchn-mmllm-claude-train-sym24-b18e9cfd-ttBzr | 3.1268 |
| aCmeX | fork-joly-os-mmllm-claude-train-sym24-7462742e-aCmeX | 3.1421 |
| F7suM | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-756f5b9f-F7suM | 3.2654 |
| Mquog | fork-slaa-us-mmllm-claude-train-sym24-b9a9f8ad-Mquog | 3.5060 |
| **mean** | | **3.2601** |
| **best** | | **3.1268** |

## Chain progression R795 → R796

Previous harvest: `workers/dispatcher/harvest-17way-r795_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2074         | 3.2601         | +0.0527 |
| ctrl_bpc best  | 3.1109         | 3.1268         | +0.0159 |

## Per-round trajectory (best bird: ttBzr)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 796 | 6644 | 3.1268 | +0.6927 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-11way-r795_sym24`
  - `workers/dispatcher/harvest-5way-r795_sym24`

## Output

`workers/dispatcher/harvest-4way-r796_sym24/round-796/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

