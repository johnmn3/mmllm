# harvest-4way-r881 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R881 ctrl_bpc |
|--------|--------|--------------:|
| mi436 | origin/claude/train-sym24-f7f8e80f-mi436 | 3.0597 |
| 4qkLp | fork-SeniorCareMarket-mmllm-claude-train-sym24-7c218f0d-4qkLp | 3.2023 |
| yHyJc | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-3ce9d291-yHyJc | 3.2133 |
| donQP | fork-joly-os-mmllm-claude-train-sym24-c5d602c7-donQP | 3.2539 |
| **mean** | | **3.1823** |
| **best** | | **3.0597** |

## Chain progression R880 → R881

Previous harvest: `workers/dispatcher/harvest-10way-r880_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0243         | 3.1823         | +0.1580 |
| ctrl_bpc best  | 2.8392         | 3.0597         | +0.2205 |

## Per-round trajectory (best bird: mi436)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 881 | 4356 | 3.0597 | +0.2349 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r880_sym24`
  - `workers/dispatcher/harvest-8way-r880_sym24`

## Output

`workers/dispatcher/harvest-4way-r881_sym24/round-881/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

