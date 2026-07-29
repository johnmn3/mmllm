# harvest-5way-r1059 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1059 ctrl_bpc |
|--------|--------|--------------:|
| FMWud | fork-slaa-us-mmllm-claude-train-sym24-d5228d21-FMWud | 2.4619 |
| MayyL | origin/claude/train-sym24-bc8224d8-MayyL | 2.4909 |
| T97sO | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-fa0195a8-T97sO | 2.4928 |
| 644dw | fork-joly-os-mmllm-claude-train-sym24-718689f2-644dw | 2.6515 |
| MYaA7 | fork-SeniorCareMarket-mmllm-claude-train-sym24-cb6d454e-MYaA7 | 2.6549 |
| **mean** | | **2.5504** |
| **best** | | **2.4619** |

## Chain progression R1058 → R1059

Previous harvest: `workers/dispatcher/harvest-5way-r1058_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6276         | 2.5504         | -0.0772 |
| ctrl_bpc best  | 2.4905         | 2.4619         | -0.0286 |

## Per-round trajectory (best bird: FMWud)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1059 | 6360 | 2.4619 | +0.2097 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1058_sym24`
  - `workers/dispatcher/harvest-5way-r1058_sym24`

## Output

`workers/dispatcher/harvest-5way-r1059_sym24/round-1059/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

