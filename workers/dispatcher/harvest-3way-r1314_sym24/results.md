# harvest-3way-r1314 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1314 ctrl_bpc |
|--------|--------|--------------:|
| RoDDq | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-dc17a3f2-RoDDq | 3.7887 |
| mo6qp | fork-joly-os-mmllm-claude-train-sym24-0f04d9b1-mo6qp | 3.7912 |
| lzeiF | fork-slaa-us-mmllm-claude-train-sym24-d4226e5b-lzeiF | 3.8030 |
| **mean** | | **3.7943** |
| **best** | | **3.7887** |

## Chain progression R1313 → R1314

Previous harvest: `workers/dispatcher/harvest-9way-r1313_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5143         | 3.7943         | +0.2800 |
| ctrl_bpc best  | 3.4215         | 3.7887         | +0.3672 |

## Per-round trajectory (best bird: RoDDq)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1314 | 3604 | 3.7887 | +0.0454 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1313_sym24`

## Output

`workers/dispatcher/harvest-3way-r1314_sym24/round-1314/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

