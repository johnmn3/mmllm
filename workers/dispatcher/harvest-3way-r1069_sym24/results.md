# harvest-3way-r1069 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1069 ctrl_bpc |
|--------|--------|--------------:|
| A3lGE | fork-slaa-us-mmllm-claude-train-sym24-4d6bc7db-A3lGE | 2.4445 |
| 0AcjU | fork-joly-os-mmllm-claude-train-sym24-e4ec8c79-0AcjU | 2.4445 |
| PdUye | origin/claude/train-sym24-0568bbaa-PdUye | 2.4454 |
| **mean** | | **2.4448** |
| **best** | | **2.4445** |

## Chain progression R1068 → R1069

Previous harvest: `workers/dispatcher/harvest-8way-r1068_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5985         | 2.4448         | -0.1537 |
| ctrl_bpc best  | 2.4399         | 2.4445         | +0.0046 |

## Per-round trajectory (best bird: A3lGE)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1069 | 6262 | 2.4445 | +0.2206 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1068_sym24`
  - `workers/dispatcher/harvest-6way-r1068_sym24`

## Output

`workers/dispatcher/harvest-3way-r1069_sym24/round-1069/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

