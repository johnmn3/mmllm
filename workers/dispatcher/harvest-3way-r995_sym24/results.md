# harvest-3way-r995 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R995 ctrl_bpc |
|--------|--------|--------------:|
| ZchNF | fork-SeniorCareMarket-mmllm-claude-train-sym24-181c71f1-ZchNF | 2.5605 |
| buEFj | fork-slaa-us-mmllm-claude-train-sym24-794b5966-buEFj | 2.5980 |
| xTso1 | fork-joly-os-mmllm-claude-train-sym24-e56a8dec-xTso1 | 2.7592 |
| **mean** | | **2.6392** |
| **best** | | **2.5605** |

## Chain progression R994 → R995

Previous harvest: `workers/dispatcher/harvest-4way-r994_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7709         | 2.6392         | -0.1317 |
| ctrl_bpc best  | 2.5717         | 2.5605         | -0.0112 |

## Per-round trajectory (best bird: ZchNF)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 995 | 6628 | 2.5605 | +0.1842 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r994_sym24`

## Output

`workers/dispatcher/harvest-3way-r995_sym24/round-995/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

