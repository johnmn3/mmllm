# harvest-3way-r797 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R797 ctrl_bpc |
|--------|--------|--------------:|
| moo3v | origin/claude/train-sym24-f17702f3-moo3v | 3.2583 |
| PsRNr | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-50b842e5-PsRNr | 3.4988 |
| 3WDid | fork-slaa-us-mmllm-claude-train-sym24-e55847a0-3WDid | 3.4995 |
| **mean** | | **3.4189** |
| **best** | | **3.2583** |

## Chain progression R796 → R797

Previous harvest: `workers/dispatcher/harvest-4way-r796_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2601         | 3.4189         | +0.1588 |
| ctrl_bpc best  | 3.1268         | 3.2583         | +0.1315 |

## Per-round trajectory (best bird: moo3v)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 797 | 6608 | 3.2583 | +0.4898 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r796_sym24`

## Output

`workers/dispatcher/harvest-3way-r797_sym24/round-797/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

