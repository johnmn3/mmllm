# harvest-3way-r712 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R712 ctrl_bpc |
|--------|--------|--------------:|
| cn4uo | origin/claude/train-sym24-def66b53-cn4uo | 3.5411 |
| eai8g | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-d4d3aa80-eai8g | 3.8822 |
| ash0Y | fork-davidwuchn-mmllm-claude-train-sym24-9176fade-ash0Y | 3.8933 |
| **mean** | | **3.7722** |
| **best** | | **3.5411** |

## Chain progression R711 → R712

Previous harvest: `workers/dispatcher/harvest-4way-r711_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.6847         | 3.7722         | +0.0875 |
| ctrl_bpc best  | 3.6008         | 3.5411         | -0.0597 |

## Per-round trajectory (best bird: cn4uo)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 712 | 6680 | 3.5411 | +1.6290 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r711_sym24`

## Output

`workers/dispatcher/harvest-3way-r712_sym24/round-712/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

