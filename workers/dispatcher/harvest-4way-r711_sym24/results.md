# harvest-4way-r711 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R711 ctrl_bpc |
|--------|--------|--------------:|
| CGyC2 | fork-davidwuchn-mmllm-claude-train-sym24-a867144d-CGyC2 | 3.6008 |
| T2t0i | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-6cfdd4be-T2t0i | 3.6120 |
| 3Z2eB | fork-slaa-us-mmllm-claude-train-sym24-342144f6-3Z2eB | 3.6182 |
| 5D6rl | fork-joly-os-mmllm-claude-train-sym24-4cc2d45d-5D6rl | 3.9078 |
| **mean** | | **3.6847** |
| **best** | | **3.6008** |

## Chain progression R710 → R711

Previous harvest: `workers/dispatcher/harvest-16way-r710_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.6891         | 3.6847         | -0.0044 |
| ctrl_bpc best  | 3.5547         | 3.6008         | +0.0461 |

## Per-round trajectory (best bird: CGyC2)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 711 | 6348 | 3.6008 | +0.9789 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r710_sym24`

## Output

`workers/dispatcher/harvest-4way-r711_sym24/round-711/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

