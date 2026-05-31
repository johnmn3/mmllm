# harvest-4way-r117 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R117 ctrl_bpc |
|--------|--------|--------------:|
| mCDRQ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-bc0d875a-mCDRQ | 2.7119 |
| KvmFN | fork-davidwuchn-mmllm-claude-train-sym24-e5bc9ac1-KvmFN | 2.9840 |
| r9oXn | fork-joly-os-mmllm-claude-train-sym24-dc1d9871-r9oXn | 3.0916 |
| vOUzE | fork-slaa-us-mmllm-claude-train-sym24-a1363e77-vOUzE | 3.1444 |
| **mean** | | **2.9830** |
| **best** | | **2.7119** |

## Per-round trajectory (best bird: mCDRQ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 117 | 5682 | 2.7119 | +0.0567 |

## Cumulative training contribution

- This harvest: **200 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **200 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r116_sym24`

## Output

`workers/dispatcher/harvest-4way-r117_sym24/round-117/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

