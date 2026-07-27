# harvest-5way-r1037 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1037 ctrl_bpc |
|--------|--------|--------------:|
| H9HsC | fork-slaa-us-mmllm-claude-train-sym24-ec5831d4-H9HsC | 2.4912 |
| KwYTW | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-d16e1bc1-KwYTW | 2.4914 |
| OByzL | fork-joly-os-mmllm-claude-train-sym24-cf11e192-OByzL | 2.5136 |
| n8JYY | fork-joly-os-mmllm-claude-train-sym24-4bbb739a-n8JYY | 2.6840 |
| AISpN | fork-SeniorCareMarket-mmllm-claude-train-sym24-964d412f-AISpN | 2.8831 |
| **mean** | | **2.6127** |
| **best** | | **2.4912** |

## Chain progression R610 → R1037

Previous harvest: `workers/dispatcher/harvest-2way-merge-r610_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.1372         | 2.6127         | +0.4755 |
| ctrl_bpc best  | 2.1268         | 2.4912         | +0.3644 |

## Per-round trajectory (best bird: H9HsC)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1037 | 6439 | 2.4912 | +0.1728 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1036_sym24`
  - `workers/dispatcher/harvest-5way-r1036_sym24`

## Output

`workers/dispatcher/harvest-5way-r1037_sym24/round-1037/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

