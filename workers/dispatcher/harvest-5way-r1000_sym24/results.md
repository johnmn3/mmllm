# harvest-5way-r1000 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1000 ctrl_bpc |
|--------|--------|--------------:|
| SGsNJ | fork-slaa-us-mmllm-claude-train-sym24-015846a2-SGsNJ | 2.5585 |
| yEr2U | origin/claude/train-sym24-03fffc28-yEr2U | 2.5741 |
| bVZHH | fork-SeniorCareMarket-mmllm-claude-train-sym24-d5bac542-bVZHH | 2.7460 |
| Pp0r4 | fork-joly-os-mmllm-claude-train-sym24-0dd31e85-Pp0r4 | 2.7669 |
| KRFmt | origin/claude/train-sym24-d44cbc97-KRFmt | 2.9804 |
| **mean** | | **2.7252** |
| **best** | | **2.5585** |

## Chain progression R999 → R1000

Previous harvest: `workers/dispatcher/harvest-4way-r999_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6289         | 2.7252         | +0.0963 |
| ctrl_bpc best  | 2.5863         | 2.5585         | -0.0278 |

## Per-round trajectory (best bird: SGsNJ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1000 | 6662 | 2.5585 | +0.1665 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r999_sym24`
  - `workers/dispatcher/harvest-4way-r999_sym24`

## Output

`workers/dispatcher/harvest-5way-r1000_sym24/round-1000/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

