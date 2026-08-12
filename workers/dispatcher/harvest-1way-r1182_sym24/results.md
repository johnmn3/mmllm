# harvest-1way-r1182 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1182 ctrl_bpc |
|--------|--------|--------------:|
| CPYgN | fork-joly-os-mmllm-claude-train-sym24-f4d5f7fe-CPYgN | 2.7181 |
| **mean** | | **2.7181** |
| **best** | | **2.7181** |

## Chain progression R1181 → R1182

Previous harvest: `workers/dispatcher/harvest-4way-r1181_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4147         | 2.7181         | +0.3034 |
| ctrl_bpc best  | 2.3155         | 2.7181         | +0.4026 |

## Per-round trajectory (best bird: CPYgN)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1182 | 4517 | 2.7181 | +0.2192 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1181_sym24`

## Output

`workers/dispatcher/harvest-1way-r1182_sym24/round-1182/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

