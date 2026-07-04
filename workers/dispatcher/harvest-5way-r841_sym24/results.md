# harvest-5way-r841 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R841 ctrl_bpc |
|--------|--------|--------------:|
| TJpJo | origin/claude/train-sym24-ab4c8ae6-TJpJo | 2.9606 |
| RI33L | fork-slaa-us-mmllm-claude-train-sym24-2403f969-RI33L | 3.1043 |
| MRGsI | fork-SeniorCareMarket-mmllm-claude-train-sym24-6010779c-MRGsI | 3.1178 |
| gJ2mo | fork-joly-os-mmllm-claude-train-sym24-e5190469-gJ2mo | 3.3294 |
| dRieZ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-180db8c2-dRieZ | 3.3303 |
| **mean** | | **3.1685** |
| **best** | | **2.9606** |

## Chain progression R840 → R841

Previous harvest: `workers/dispatcher/harvest-1way-r840_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1526         | 3.1685         | +0.0159 |
| ctrl_bpc best  | 3.1526         | 2.9606         | -0.1920 |

## Per-round trajectory (best bird: TJpJo)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 841 | 6785 | 2.9606 | +0.3635 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r840_sym24`

## Output

`workers/dispatcher/harvest-5way-r841_sym24/round-841/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

