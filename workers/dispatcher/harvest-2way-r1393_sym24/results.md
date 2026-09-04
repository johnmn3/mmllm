# harvest-2way-r1393 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1393 ctrl_bpc |
|--------|--------|--------------:|
| lAcqT | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-0346a306-lAcqT | 3.6921 |
| 46udK | fork-SeniorCareMarket-mmllm-claude-train-sym24-87908379-46udK | 3.7914 |
| **mean** | | **3.7417** |
| **best** | | **3.6921** |

## Chain progression R1392 → R1393

Previous harvest: `workers/dispatcher/harvest-2way-r1392_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4722         | 3.7417         | +0.2695 |
| ctrl_bpc best  | 3.1357         | 3.6921         | +0.5564 |

## Per-round trajectory (best bird: lAcqT)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1393 | 4457 | 3.6921 | +0.0536 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1392_sym24`

## Output

`workers/dispatcher/harvest-2way-r1393_sym24/round-1393/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

