# harvest-12way-r791 — sparse-delta merge of 12 birds

## Worker endpoints

| handle | branch | R791 ctrl_bpc |
|--------|--------|--------------:|
| Z8QAo | fork-davidwuchn-mmllm-claude-train-sym24-bcbd1dd9-Z8QAo | 3.1162 |
| GXvZa | origin/claude/train-sym24-e9550cd6-GXvZa | 3.1265 |
| tfey9 | fork-slaa-us-mmllm-claude-train-sym24-4e150893-tfey9 | 3.1458 |
| piNy5 | fork-davidwuchn-mmllm-claude-train-sym24-71228d7c-piNy5 | 3.1785 |
| G3lpP | origin/claude/train-sym24-9407ccf0-G3lpP | 3.1802 |
| pJQGj | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-9035918d-pJQGj | 3.1850 |
| xJGW3 | origin/claude/train-sym24-12529a46-xJGW3 | 3.2083 |
| Y3dVg | fork-SeniorCareMarket-mmllm-claude-train-sym24-b1f59a90-Y3dVg | 3.2666 |
| VIkjx | fork-joly-os-mmllm-claude-train-sym24-b0fe6066-VIkjx | 3.2679 |
| YmQa1 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-927da648-YmQa1 | 3.2687 |
| PxZeC | fork-joly-os-mmllm-claude-train-sym24-08fde429-PxZeC | 3.2791 |
| aWp65 | fork-joly-os-mmllm-claude-train-sym24-acb1f61f-aWp65 | 3.5966 |
| **mean** | | **3.2349** |
| **best** | | **3.1162** |

## Chain progression R790 → R791

Previous harvest: `workers/dispatcher/harvest-8way-r790_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2036         | 3.2349         | +0.0313 |
| ctrl_bpc best  | 3.1467         | 3.1162         | -0.0305 |

## Per-round trajectory (best bird: Z8QAo)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 791 | 6601 | 3.1162 | +0.4674 |

## Cumulative training contribution

- This harvest: **960 steps** from 12 bird(s)
- Across full ancestry (deduped by bird_id): **1600 steps** from 20 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r790_sym24`
  - `workers/dispatcher/harvest-8way-r790_sym24`

## Output

`workers/dispatcher/harvest-12way-r791_sym24/round-791/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 12 workers)
- `dense.pt` (averaged across 12 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

