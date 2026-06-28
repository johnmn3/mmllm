# harvest-5way-r791 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R791 ctrl_bpc |
|--------|--------|--------------:|
| G3lpP | origin/claude/train-sym24-9407ccf0-G3lpP | 3.1802 |
| pJQGj | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-9035918d-pJQGj | 3.1850 |
| VIkjx | fork-joly-os-mmllm-claude-train-sym24-b0fe6066-VIkjx | 3.2679 |
| YmQa1 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-927da648-YmQa1 | 3.2687 |
| PxZeC | fork-joly-os-mmllm-claude-train-sym24-08fde429-PxZeC | 3.2791 |
| **mean** | | **3.2362** |
| **best** | | **3.1802** |

## Chain progression R790 → R791

Previous harvest: `workers/dispatcher/harvest-8way-r790_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2036         | 3.2362         | +0.0326 |
| ctrl_bpc best  | 3.1467         | 3.1802         | +0.0335 |

## Per-round trajectory (best bird: G3lpP)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 791 | 4331 | 3.1802 | +0.5502 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r790_sym24`
  - `workers/dispatcher/harvest-8way-r790_sym24`

## Output

`workers/dispatcher/harvest-5way-r791_sym24/round-791/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

