# harvest-4way-r928 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R928 ctrl_bpc |
|--------|--------|--------------:|
| qFpOU | fork-joly-os-mmllm-claude-train-sym24-c11dfb23-qFpOU | 2.7143 |
| yKUTs | fork-SeniorCareMarket-mmllm-claude-train-sym24-ba7dfd2e-yKUTs | 2.7654 |
| FFISx | origin/claude/train-sym24-e5a66d12-FFISx | 2.9110 |
| syFMa | origin/claude/train-sym24-0d47e4e1-syFMa | 2.9135 |
| **mean** | | **2.8260** |
| **best** | | **2.7143** |

## Chain progression R927 → R928

Previous harvest: `workers/dispatcher/harvest-5way-r927_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9218         | 2.8260         | -0.0958 |
| ctrl_bpc best  | 2.7310         | 2.7143         | -0.0167 |

## Per-round trajectory (best bird: qFpOU)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 928 | 6520 | 2.7143 | +0.1649 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r927_sym24`
  - `workers/dispatcher/harvest-5way-r927_sym24`

## Output

`workers/dispatcher/harvest-4way-r928_sym24/round-928/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

