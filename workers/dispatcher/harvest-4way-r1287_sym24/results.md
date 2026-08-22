# harvest-4way-r1287 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1287 ctrl_bpc |
|--------|--------|--------------:|
| T6r3M | fork-joly-os-mmllm-claude-train-sym24-0961503a-T6r3M | 2.2147 |
| EavOq | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-d4930477-EavOq | 2.2295 |
| VcP9h | fork-slaa-us-mmllm-claude-train-sym24-faf04225-VcP9h | 2.2325 |
| UTbF0 | fork-SeniorCareMarket-mmllm-claude-train-sym24-f028b58e-UTbF0 | 2.6129 |
| **mean** | | **2.3224** |
| **best** | | **2.2147** |

## Chain progression R1286 → R1287

Previous harvest: `workers/dispatcher/harvest-11way-r1286_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3511         | 2.3224         | -0.0287 |
| ctrl_bpc best  | 2.2176         | 2.2147         | -0.0029 |

## Per-round trajectory (best bird: T6r3M)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1287 | 6385 | 2.2147 | +0.2594 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1286_sym24`

## Output

`workers/dispatcher/harvest-4way-r1287_sym24/round-1287/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

