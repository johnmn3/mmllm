# harvest-2way-r829 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R829 ctrl_bpc |
|--------|--------|--------------:|
| 45zXz | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-ae1ea101-45zXz | 2.9854 |
| sUha1 | fork-slaa-us-mmllm-claude-train-sym24-56eaa97a-sUha1 | 3.1533 |
| **mean** | | **3.0694** |
| **best** | | **2.9854** |

## Chain progression R828 → R829

Previous harvest: `workers/dispatcher/harvest-4way-r828_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0948         | 3.0694         | -0.0255 |
| ctrl_bpc best  | 2.9988         | 2.9854         | -0.0134 |

## Per-round trajectory (best bird: 45zXz)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 829 | 4076 | 2.9854 | +0.4585 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r828_sym24`

## Output

`workers/dispatcher/harvest-2way-r829_sym24/round-829/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

