# harvest-4way-r857 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R857 ctrl_bpc |
|--------|--------|--------------:|
| yX2H9 | origin/claude/train-sym24-eff2cc8b-yX2H9 | 2.9031 |
| QJJT5 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-5b9aa131-QJJT5 | 2.9137 |
| gJmVh | fork-slaa-us-mmllm-claude-train-sym24-99d67307-gJmVh | 3.0639 |
| bjXEt | fork-joly-os-mmllm-claude-train-sym24-7ee44c9b-bjXEt | 3.0797 |
| **mean** | | **2.9901** |
| **best** | | **2.9031** |

## Chain progression R856 → R857

Previous harvest: `workers/dispatcher/harvest-5way-r856_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0197         | 2.9901         | -0.0296 |
| ctrl_bpc best  | 2.9048         | 2.9031         | -0.0017 |

## Per-round trajectory (best bird: yX2H9)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 857 | 6505 | 2.9031 | +0.4296 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r856_sym24`

## Output

`workers/dispatcher/harvest-4way-r857_sym24/round-857/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

