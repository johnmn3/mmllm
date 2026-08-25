# harvest-3way-r1313 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1313 ctrl_bpc |
|--------|--------|--------------:|
| N3ccL | fork-SeniorCareMarket-mmllm-claude-train-sym24-93f7f4bc-N3ccL | 3.4215 |
| zLjgE | fork-slaa-us-mmllm-claude-train-sym24-36e35dc3-zLjgE | 3.4580 |
| FMSGn | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f5a3751c-FMSGn | 3.5111 |
| **mean** | | **3.4635** |
| **best** | | **3.4215** |

## Chain progression R1312 → R1313

Previous harvest: `workers/dispatcher/harvest-7way-r1312_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5125         | 3.4635         | -0.0490 |
| ctrl_bpc best  | 3.4164         | 3.4215         | +0.0051 |

## Per-round trajectory (best bird: N3ccL)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1313 | 6644 | 3.4215 | +0.0615 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1312_sym24`

## Output

`workers/dispatcher/harvest-3way-r1313_sym24/round-1313/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

