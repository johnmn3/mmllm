# harvest-4way-r1044 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1044 ctrl_bpc |
|--------|--------|--------------:|
| C4nG2 | origin/claude/train-sym24-7dfde4fe-C4nG2 | 2.4833 |
| GZOgT | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-a1df774d-GZOgT | 2.5089 |
| islq2 | fork-joly-os-mmllm-claude-train-sym24-9c831670-islq2 | 2.8555 |
| bEBvO | origin/claude/train-sym24-459b2901-bEBvO | 2.8805 |
| **mean** | | **2.6821** |
| **best** | | **2.4833** |

## Chain progression R1043 → R1044

Previous harvest: `workers/dispatcher/harvest-8way-r1043_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5516         | 2.6821         | +0.1305 |
| ctrl_bpc best  | 2.4812         | 2.4833         | +0.0021 |

## Per-round trajectory (best bird: C4nG2)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1044 | 6572 | 2.4833 | +0.1919 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1043_sym24`
  - `workers/dispatcher/harvest-8way-r1043_sym24`

## Output

`workers/dispatcher/harvest-4way-r1044_sym24/round-1044/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

