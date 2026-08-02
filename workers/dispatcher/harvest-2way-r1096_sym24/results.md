# harvest-2way-r1096 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1096 ctrl_bpc |
|--------|--------|--------------:|
| 29Nmi | fork-slaa-us-mmllm-claude-train-sym24-6b1ce837-29Nmi | 2.5960 |
| YIOAY | fork-joly-os-mmllm-claude-train-sym24-e7421406-YIOAY | 2.6113 |
| **mean** | | **2.6037** |
| **best** | | **2.5960** |

## Chain progression R1095 → R1096

Previous harvest: `workers/dispatcher/harvest-11way-r1095_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5547         | 2.6037         | +0.0490 |
| ctrl_bpc best  | 2.3988         | 2.5960         | +0.1972 |

## Per-round trajectory (best bird: 29Nmi)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1096 | 6600 | 2.5960 | +0.2164 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1095_sym24`

## Output

`workers/dispatcher/harvest-2way-r1096_sym24/round-1096/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

