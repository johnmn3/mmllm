# harvest-2way-r824 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R824 ctrl_bpc |
|--------|--------|--------------:|
| quNQf | fork-SeniorCareMarket-mmllm-claude-train-sym24-f05549fa-quNQf | 3.0164 |
| mhgdS | fork-slaa-us-mmllm-claude-train-sym24-739347c5-mhgdS | 3.1511 |
| **mean** | | **3.0838** |
| **best** | | **3.0164** |

## Chain progression R823 → R824

Previous harvest: `workers/dispatcher/harvest-1way-r823_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0171         | 3.0838         | +0.0667 |
| ctrl_bpc best  | 3.0171         | 3.0164         | -0.0007 |

## Per-round trajectory (best bird: quNQf)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 824 | 5447 | 3.0164 | +0.4580 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **1440 steps** from 18 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r823_sym24`

## Output

`workers/dispatcher/harvest-2way-r824_sym24/round-824/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

