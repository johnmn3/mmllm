# harvest-6way-r782 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R782 ctrl_bpc |
|--------|--------|--------------:|
| zfou2 | fork-davidwuchn-mmllm-claude-train-sym24-d3551c32-zfou2 | 3.2139 |
| Z46uk | fork-slaa-us-mmllm-claude-train-sym24-79be89bc-Z46uk | 3.2193 |
| MM8Rh | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-89d6d7d4-MM8Rh | 3.2194 |
| 6ICuC | origin/claude/train-sym24-27939f7f-6ICuC | 3.3053 |
| M56dS | origin/claude/train-sym24-f4e7d445-M56dS | 3.3296 |
| ISRrw | fork-joly-os-mmllm-claude-train-sym24-11637ad9-ISRrw | 3.5708 |
| **mean** | | **3.3097** |
| **best** | | **3.2139** |

## Chain progression R781 → R782

Previous harvest: `workers/dispatcher/harvest-10way-r781_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2585         | 3.3097         | +0.0512 |
| ctrl_bpc best  | 3.1777         | 3.2139         | +0.0362 |

## Per-round trajectory (best bird: zfou2)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 782 | 6512 | 3.2139 | +0.5709 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r781_sym24`

## Output

`workers/dispatcher/harvest-6way-r782_sym24/round-782/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

