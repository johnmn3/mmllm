# harvest-8way-r787 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R787 ctrl_bpc |
|--------|--------|--------------:|
| XgTZX | fork-slaa-us-mmllm-claude-train-sym24-282ac777-XgTZX | 3.1477 |
| zj9GS | origin/claude/train-sym24-335a4e75-zj9GS | 3.1711 |
| gL1BT | fork-SeniorCareMarket-mmllm-claude-train-sym24-61b0033c-gL1BT | 3.1847 |
| eO1kR | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-088aed67-eO1kR | 3.2016 |
| CSR3X | origin/claude/train-sym24-b036a4bd-CSR3X | 3.2241 |
| HUbuA | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-cbb346c9-HUbuA | 3.3000 |
| SsnXs | fork-joly-os-mmllm-claude-train-sym24-66a6fbd8-SsnXs | 3.3006 |
| WiOiu | fork-davidwuchn-mmllm-claude-train-sym24-1865671e-WiOiu | 3.5493 |
| **mean** | | **3.2599** |
| **best** | | **3.1477** |

## Chain progression R786 → R787

Previous harvest: `workers/dispatcher/harvest-6way-r786_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2236         | 3.2599         | +0.0363 |
| ctrl_bpc best  | 3.1602         | 3.1477         | -0.0125 |

## Per-round trajectory (best bird: XgTZX)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 787 | 6528 | 3.1477 | +0.3621 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r786_sym24`

## Output

`workers/dispatcher/harvest-8way-r787_sym24/round-787/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

