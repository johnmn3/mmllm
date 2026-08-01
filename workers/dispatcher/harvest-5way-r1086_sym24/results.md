# harvest-5way-r1086 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1086 ctrl_bpc |
|--------|--------|--------------:|
| ca4wG | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-1634cab4-ca4wG | 2.4134 |
| th8jH | fork-joly-os-mmllm-claude-train-sym24-bcd681bb-th8jH | 2.4211 |
| Hgfs6 | fork-SeniorCareMarket-mmllm-claude-train-sym24-62fae167-Hgfs6 | 2.6154 |
| RHvSP | origin/claude/train-sym24-9776accd-RHvSP | 2.8065 |
| mZZmA | origin/claude/train-sym24-ec01499d-mZZmA | 2.8355 |
| **mean** | | **2.6184** |
| **best** | | **2.4134** |

## Chain progression R1085 → R1086

Previous harvest: `workers/dispatcher/harvest-6way-r1085_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6627         | 2.6184         | -0.0443 |
| ctrl_bpc best  | 2.4499         | 2.4134         | -0.0365 |

## Per-round trajectory (best bird: ca4wG)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1086 | 6696 | 2.4134 | +0.2358 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1085_sym24`

## Output

`workers/dispatcher/harvest-5way-r1086_sym24/round-1086/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

