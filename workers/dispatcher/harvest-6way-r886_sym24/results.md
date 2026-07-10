# harvest-6way-r886 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R886 ctrl_bpc |
|--------|--------|--------------:|
| JN933 | fork-slaa-us-mmllm-claude-train-sym24-36def80e-JN933 | 2.8141 |
| yW0AI | origin/claude/train-sym24-8fedeb92-yW0AI | 2.8337 |
| RcxLY | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-98f47a25-RcxLY | 2.8369 |
| cSH3s | origin/claude/train-sym24-0d352021-cSH3s | 2.8422 |
| jFZZI | fork-SeniorCareMarket-mmllm-claude-train-sym24-dfaae081-jFZZI | 3.2033 |
| Z4CbS | fork-joly-os-mmllm-claude-train-sym24-42a51d10-Z4CbS | 3.2246 |
| **mean** | | **2.9591** |
| **best** | | **2.8141** |

## Chain progression R885 → R886

Previous harvest: `workers/dispatcher/harvest-6way-r885_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0765         | 2.9591         | -0.1174 |
| ctrl_bpc best  | 2.8407         | 2.8141         | -0.0266 |

## Per-round trajectory (best bird: JN933)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 886 | 6627 | 2.8141 | +0.2823 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r885_sym24`

## Output

`workers/dispatcher/harvest-6way-r886_sym24/round-886/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

