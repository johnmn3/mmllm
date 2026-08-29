# harvest-7way-r1352 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R1352 ctrl_bpc |
|--------|--------|--------------:|
| gfzjq | fork-slaa-us-mmllm-claude-train-sym24-7b6c5263-gfzjq | 3.2234 |
| yPzsW | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-c103e9ad-yPzsW | 3.2376 |
| WPY5x | origin/claude/train-sym24-758d4751-WPY5x | 3.2384 |
| EQMIa | origin/claude/train-sym24-88ad1c41-EQMIa | 3.2436 |
| ewSi2 | fork-joly-os-mmllm-claude-train-sym24-b2099ad9-ewSi2 | 3.2783 |
| F8atj | fork-SeniorCareMarket-mmllm-claude-train-sym24-445ede4c-F8atj | 3.3191 |
| qM4lm | origin/claude/train-sym24-bfb19912-qM4lm | 3.6003 |
| **mean** | | **3.3058** |
| **best** | | **3.2234** |

## Chain progression R1351 → R1352

Previous harvest: `workers/dispatcher/harvest-4way-r1351_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2788         | 3.3058         | +0.0270 |
| ctrl_bpc best  | 3.2310         | 3.2234         | -0.0076 |

## Per-round trajectory (best bird: gfzjq)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1352 | 6340 | 3.2234 | +0.0901 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1351_sym24`
  - `workers/dispatcher/harvest-3way-r1351_sym24`
  - `workers/dispatcher/harvest-4way-r1351_sym24`

## Output

`workers/dispatcher/harvest-7way-r1352_sym24/round-1352/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

