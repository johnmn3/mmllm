# harvest-2way-r791 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R791 ctrl_bpc |
|--------|--------|--------------:|
| G3lpP | origin/claude/train-sym24-9407ccf0-G3lpP | 3.1802 |
| YmQa1 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-927da648-YmQa1 | 3.2687 |
| **mean** | | **3.2245** |
| **best** | | **3.1802** |

## Chain progression R790 → R791

Previous harvest: `workers/dispatcher/harvest-8way-r790_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2036         | 3.2245         | +0.0209 |
| ctrl_bpc best  | 3.1467         | 3.1802         | +0.0335 |

## Per-round trajectory (best bird: G3lpP)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 791 | 4331 | 3.1802 | +0.5502 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r790_sym24`

## Output

`workers/dispatcher/harvest-2way-r791_sym24/round-791/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

