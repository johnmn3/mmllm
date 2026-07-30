# harvest-9way-r1062 — sparse-delta merge of 9 birds

## Worker endpoints

| handle | branch | R1062 ctrl_bpc |
|--------|--------|--------------:|
| 0Ggl2 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-0a40d49e-0Ggl2 | 2.4487 |
| Eomp6 | fork-joly-os-mmllm-claude-train-sym24-61e71574-Eomp6 | 2.4624 |
| dJLo9 | fork-SeniorCareMarket-mmllm-claude-train-sym24-a79ac868-dJLo9 | 2.4671 |
| 59LPN | origin/claude/train-sym24-54201984-59LPN | 2.4870 |
| G0CWi | fork-slaa-us-mmllm-claude-train-sym24-2ef2bb37-G0CWi | 2.6400 |
| 9Ssl4 | fork-joly-os-mmllm-claude-train-sym24-e3602ba4-9Ssl4 | 2.6445 |
| 38Yly | origin/claude/train-sym24-a34d0472-38Yly | 2.6458 |
| TnvKR | fork-joly-os-mmllm-claude-train-sym24-f8d2d03a-TnvKR | 2.6539 |
| zkToZ | origin/claude/train-sym24-2f828286-zkToZ | 2.8803 |
| **mean** | | **2.5922** |
| **best** | | **2.4487** |

## Chain progression R1061 → R1062

Previous harvest: `workers/dispatcher/harvest-7way-r1061_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5845         | 2.5922         | +0.0077 |
| ctrl_bpc best  | 2.4555         | 2.4487         | -0.0068 |

## Per-round trajectory (best bird: 0Ggl2)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1062 | 5346 | 2.4487 | +0.2193 |

## Cumulative training contribution

- This harvest: **720 steps** from 9 bird(s)
- Across full ancestry (deduped by bird_id): **1280 steps** from 16 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-11way-r1061_sym24`
  - `workers/dispatcher/harvest-3way-r1061_sym24`
  - `workers/dispatcher/harvest-7way-r1061_sym24`

## Output

`workers/dispatcher/harvest-9way-r1062_sym24/round-1062/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 9 workers)
- `dense.pt` (averaged across 9 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

