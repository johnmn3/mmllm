# harvest-6way-r885 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R885 ctrl_bpc |
|--------|--------|--------------:|
| lFYLD | fork-joly-os-mmllm-claude-train-sym24-9fd16e6b-lFYLD | 2.8407 |
| Mbefx | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-b59ec54b-Mbefx | 2.9824 |
| sWBOe | origin/claude/train-sym24-d1246e96-sWBOe | 2.9985 |
| gEUdP | origin/claude/train-sym24-7a0dc233-gEUdP | 3.2072 |
| DvDsC | fork-slaa-us-mmllm-claude-train-sym24-2e86ff6c-DvDsC | 3.2121 |
| MZBdN | fork-SeniorCareMarket-mmllm-claude-train-sym24-7c4994b2-MZBdN | 3.2184 |
| **mean** | | **3.0765** |
| **best** | | **2.8407** |

## Chain progression R884 → R885

Previous harvest: `workers/dispatcher/harvest-4way-r884_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9773         | 3.0765         | +0.0992 |
| ctrl_bpc best  | 2.8253         | 2.8407         | +0.0154 |

## Per-round trajectory (best bird: lFYLD)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 885 | 6464 | 2.8407 | +0.3989 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r884_sym24`

## Output

`workers/dispatcher/harvest-6way-r885_sym24/round-885/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

