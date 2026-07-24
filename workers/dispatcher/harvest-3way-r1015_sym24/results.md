# harvest-3way-r1015 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1015 ctrl_bpc |
|--------|--------|--------------:|
| qElNF | fork-SeniorCareMarket-mmllm-claude-train-sym24-5b5e5e21-qElNF | 2.5366 |
| KrIeY | fork-joly-os-mmllm-claude-train-sym24-2d7afce3-KrIeY | 2.7282 |
| D44s1 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-1c1e3b63-D44s1 | 2.9068 |
| **mean** | | **2.7239** |
| **best** | | **2.5366** |

## Chain progression R1014 → R1015

Previous harvest: `workers/dispatcher/harvest-9way-r1014_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6681         | 2.7239         | +0.0558 |
| ctrl_bpc best  | 2.5271         | 2.5366         | +0.0095 |

## Per-round trajectory (best bird: qElNF)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1015 | 6387 | 2.5366 | +0.1740 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1014_sym24`

## Output

`workers/dispatcher/harvest-3way-r1015_sym24/round-1015/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

