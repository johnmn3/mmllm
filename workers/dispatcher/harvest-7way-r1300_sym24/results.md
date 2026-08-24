# harvest-7way-r1300 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R1300 ctrl_bpc |
|--------|--------|--------------:|
| YUTeY | fork-joly-os-mmllm-claude-train-sym24-a1354f02-YUTeY | 3.5802 |
| SgWQf | fork-SeniorCareMarket-mmllm-claude-train-sym24-87c54a82-SgWQf | 3.6190 |
| lUdrm | fork-SeniorCareMarket-mmllm-claude-train-sym24-04c91676-lUdrm | 3.6678 |
| Ho9vy | fork-slaa-us-mmllm-claude-train-sym24-9661efb3-Ho9vy | 3.7566 |
| dU71L | fork-slaa-us-mmllm-claude-train-sym24-88947bc8-dU71L | 3.8315 |
| DRdZB | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-ea128156-DRdZB | 4.0857 |
| Or1wF | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-1fe4f081-Or1wF | 4.2149 |
| **mean** | | **3.8222** |
| **best** | | **3.5802** |

## Chain progression R1299 → R1300

Previous harvest: `workers/dispatcher/harvest-11way-r1299_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.9120         | 3.8222         | -0.0898 |
| ctrl_bpc best  | 3.6474         | 3.5802         | -0.0672 |

## Per-round trajectory (best bird: YUTeY)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1300 | 6477 | 3.5802 | +0.0482 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **1440 steps** from 18 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-11way-r1299_sym24`
  - `workers/dispatcher/harvest-8way-r1299_sym24`

## Output

`workers/dispatcher/harvest-7way-r1300_sym24/round-1300/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

