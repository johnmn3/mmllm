# harvest-5way-r732 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R732 ctrl_bpc |
|--------|--------|--------------:|
| MlqwC | fork-joly-os-mmllm-claude-train-sym24-f419da75-MlqwC | 3.4669 |
| wSAnx | origin/claude/train-sym24-40631641-wSAnx | 3.4905 |
| rGtRz | fork-slaa-us-mmllm-claude-train-sym24-035e8f0b-rGtRz | 3.7768 |
| cAeiE | origin/claude/train-sym24-61e17b37-cAeiE | 3.7905 |
| v2LOl | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-b2df3350-v2LOl | 3.7949 |
| **mean** | | **3.6639** |
| **best** | | **3.4669** |

## Chain progression R731 → R732

Previous harvest: `workers/dispatcher/harvest-10way-r731_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5622         | 3.6639         | +0.1017 |
| ctrl_bpc best  | 3.4225         | 3.4669         | +0.0444 |

## Per-round trajectory (best bird: MlqwC)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 732 | 6682 | 3.4669 | +0.6479 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r731_sym24`

## Output

`workers/dispatcher/harvest-5way-r732_sym24/round-732/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

