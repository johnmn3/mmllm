# harvest-2way-r1024 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1024 ctrl_bpc |
|--------|--------|--------------:|
| LOqPJ | fork-joly-os-mmllm-claude-train-sym24-24d103f7-LOqPJ | 2.5207 |
| 8sKWH | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-267f6fed-8sKWH | 2.7080 |
| **mean** | | **2.6143** |
| **best** | | **2.5207** |

## Chain progression R1023 → R1024

Previous harvest: `workers/dispatcher/harvest-2way-r1023_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7259         | 2.6143         | -0.1116 |
| ctrl_bpc best  | 2.5369         | 2.5207         | -0.0162 |

## Per-round trajectory (best bird: LOqPJ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1024 | 4414 | 2.5207 | +0.1814 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1023_sym24`

## Output

`workers/dispatcher/harvest-2way-r1024_sym24/round-1024/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

