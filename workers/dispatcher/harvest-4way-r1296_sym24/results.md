# harvest-4way-r1296 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1296 ctrl_bpc |
|--------|--------|--------------:|
| qFEUD | fork-slaa-us-mmllm-claude-train-sym24-46ecb53b-qFEUD | 3.9342 |
| v3Ans | fork-SeniorCareMarket-mmllm-claude-train-sym24-66eb3f00-v3Ans | 3.9397 |
| tAcm5 | fork-joly-os-mmllm-claude-train-sym24-5a44d473-tAcm5 | 4.0007 |
| ZVick | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-678e7450-ZVick | 4.0646 |
| **mean** | | **3.9848** |
| **best** | | **3.9342** |

## Chain progression R1295 → R1296

Previous harvest: `workers/dispatcher/harvest-4way-r1295_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.1864         | 3.9848         | -0.2016 |
| ctrl_bpc best  | 4.0499         | 3.9342         | -0.1157 |

## Per-round trajectory (best bird: qFEUD)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1296 | 6734 | 3.9342 | +0.0362 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1295_sym24`

## Output

`workers/dispatcher/harvest-4way-r1296_sym24/round-1296/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

