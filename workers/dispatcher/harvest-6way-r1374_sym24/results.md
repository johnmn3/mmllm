# harvest-6way-r1374 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1374 ctrl_bpc |
|--------|--------|--------------:|
| iBObq | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-d105d770-iBObq | 3.1043 |
| qdQMw | fork-SeniorCareMarket-mmllm-claude-train-sym24-8fce137e-qdQMw | 3.1450 |
| U6T8D | fork-joly-os-mmllm-claude-train-sym24-a450d4cf-U6T8D | 3.1901 |
| 767QQ | origin/claude/train-sym24-e30d8022-767QQ | 3.2137 |
| rGmAY | origin/claude/train-sym24-3b954dde-rGmAY | 3.2396 |
| TE8pM | origin/claude/train-sym24-52572c6e-TE8pM | 3.6095 |
| **mean** | | **3.2504** |
| **best** | | **3.1043** |

## Chain progression R1373 → R1374

Previous harvest: `workers/dispatcher/harvest-2way-r1373_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3405         | 3.2504         | -0.0901 |
| ctrl_bpc best  | 3.0797         | 3.1043         | +0.0246 |

## Per-round trajectory (best bird: iBObq)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1374 | 3667 | 3.1043 | +0.1336 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1373_sym24`
  - `workers/dispatcher/harvest-2way-r1373_sym24`

## Output

`workers/dispatcher/harvest-6way-r1374_sym24/round-1374/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

