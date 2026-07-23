# harvest-3way-r1002 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1002 ctrl_bpc |
|--------|--------|--------------:|
| 6VGas | fork-joly-os-mmllm-claude-train-sym24-c7d2cf73-6VGas | 2.5743 |
| YOMgS | origin/claude/train-sym24-920edfb4-YOMgS | 2.7366 |
| OfeuA | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-5f1372b4-OfeuA | 2.7398 |
| **mean** | | **2.6836** |
| **best** | | **2.5743** |

## Chain progression R1001 → R1002

Previous harvest: `workers/dispatcher/harvest-6way-r1001_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7599         | 2.6836         | -0.0763 |
| ctrl_bpc best  | 2.5630         | 2.5743         | +0.0113 |

## Per-round trajectory (best bird: 6VGas)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1002 | 4389 | 2.5743 | +0.1621 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1001_sym24`

## Output

`workers/dispatcher/harvest-3way-r1002_sym24/round-1002/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

