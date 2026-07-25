# harvest-8way-r1020 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R1020 ctrl_bpc |
|--------|--------|--------------:|
| Bdesl | origin/claude/train-sym24-94435370-Bdesl | 2.5192 |
| RddC7 | origin/claude/train-sym24-53b9365e-RddC7 | 2.5204 |
| 4NdT0 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-63424715-4NdT0 | 2.5220 |
| qN0UV | fork-SeniorCareMarket-mmllm-claude-train-sym24-9b0ef885-qN0UV | 2.5274 |
| rbQUz | fork-joly-os-mmllm-claude-train-sym24-53b031a1-rbQUz | 2.5522 |
| O57f1 | origin/claude/train-sym24-2476a574-O57f1 | 2.5739 |
| 32oRB | fork-slaa-us-mmllm-claude-train-sym24-90c546ed-32oRB | 2.8977 |
| 2GFF8 | fork-joly-os-mmllm-claude-train-sym24-d8207324-2GFF8 | 2.9199 |
| **mean** | | **2.6291** |
| **best** | | **2.5192** |

## Chain progression R1019 → R1020

Previous harvest: `workers/dispatcher/harvest-6way-r1019_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6935         | 2.6291         | -0.0644 |
| ctrl_bpc best  | 2.5160         | 2.5192         | +0.0032 |

## Per-round trajectory (best bird: Bdesl)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1020 | 6592 | 2.5192 | +0.1776 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1019_sym24`
  - `workers/dispatcher/harvest-2way-r1019_sym24`

## Output

`workers/dispatcher/harvest-8way-r1020_sym24/round-1020/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

