# harvest-7way-r881 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R881 ctrl_bpc |
|--------|--------|--------------:|
| edUbs | origin/claude/train-sym24-205d4307-edUbs | 2.8444 |
| HG4Zh | fork-slaa-us-mmllm-claude-train-sym24-abadbd16-HG4Zh | 3.0003 |
| mi436 | origin/claude/train-sym24-f7f8e80f-mi436 | 3.0597 |
| 4qkLp | fork-SeniorCareMarket-mmllm-claude-train-sym24-7c218f0d-4qkLp | 3.2023 |
| yHyJc | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-3ce9d291-yHyJc | 3.2133 |
| hf6sm | fork-joly-os-mmllm-claude-train-sym24-b7348271-hf6sm | 3.2179 |
| donQP | fork-joly-os-mmllm-claude-train-sym24-c5d602c7-donQP | 3.2539 |
| **mean** | | **3.1131** |
| **best** | | **2.8444** |

## Chain progression R880 → R881

Previous harvest: `workers/dispatcher/harvest-8way-r880_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0278         | 3.1131         | +0.0853 |
| ctrl_bpc best  | 2.8392         | 2.8444         | +0.0052 |

## Per-round trajectory (best bird: edUbs)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 881 | 6636 | 2.8444 | +0.1830 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r880_sym24`
  - `workers/dispatcher/harvest-8way-r880_sym24`

## Output

`workers/dispatcher/harvest-7way-r881_sym24/round-881/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

