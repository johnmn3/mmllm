# harvest-3way-r779 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R779 ctrl_bpc |
|--------|--------|--------------:|
| 8Hdw5 | fork-SeniorCareMarket-mmllm-claude-train-sym24-1d130140-8Hdw5 | 3.2283 |
| Q0OjS | origin/claude/train-sym24-00133f1a-Q0OjS | 3.2544 |
| XnJgM | fork-joly-os-mmllm-claude-train-sym24-aa05b2fc-XnJgM | 3.5756 |
| **mean** | | **3.3528** |
| **best** | | **3.2283** |

## Chain progression R778 → R779

Previous harvest: `workers/dispatcher/harvest-6way-r778_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2314         | 3.3528         | +0.1214 |
| ctrl_bpc best  | 3.1993         | 3.2283         | +0.0290 |

## Per-round trajectory (best bird: 8Hdw5)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 779 | 6502 | 3.2283 | +0.5990 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-6way-r778_sym24`

## Output

`workers/dispatcher/harvest-3way-r779_sym24/round-779/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

