# harvest-7way-r1314 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R1314 ctrl_bpc |
|--------|--------|--------------:|
| aF9YA | fork-joly-os-mmllm-claude-train-sym24-736459fe-aF9YA | 3.4246 |
| KHJCS | fork-SeniorCareMarket-mmllm-claude-train-sym24-58d96ebe-KHJCS | 3.4777 |
| Skuwc | origin/claude/train-sym24-6390a52d-Skuwc | 3.4956 |
| HHXFZ | fork-SeniorCareMarket-mmllm-claude-train-sym24-6b697c1b-HHXFZ | 3.7799 |
| RoDDq | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-dc17a3f2-RoDDq | 3.7887 |
| mo6qp | fork-joly-os-mmllm-claude-train-sym24-0f04d9b1-mo6qp | 3.7912 |
| lzeiF | fork-slaa-us-mmllm-claude-train-sym24-d4226e5b-lzeiF | 3.8030 |
| **mean** | | **3.6515** |
| **best** | | **3.4246** |

## Chain progression R1313 → R1314

Previous harvest: `workers/dispatcher/harvest-9way-r1313_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5143         | 3.6515         | +0.1372 |
| ctrl_bpc best  | 3.4215         | 3.4246         | +0.0031 |

## Per-round trajectory (best bird: aF9YA)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1314 | 5386 | 3.4246 | +0.0587 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **1280 steps** from 16 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1313_sym24`
  - `workers/dispatcher/harvest-9way-r1313_sym24`

## Output

`workers/dispatcher/harvest-7way-r1314_sym24/round-1314/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

