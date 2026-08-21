# harvest-6way-r1278 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1278 ctrl_bpc |
|--------|--------|--------------:|
| zJyFE | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-8f4913ce-zJyFE | 2.2282 |
| os3u3 | fork-joly-os-mmllm-claude-train-sym24-576ea786-os3u3 | 2.2361 |
| cO4py | fork-slaa-us-mmllm-claude-train-sym24-d9b301b4-cO4py | 2.2478 |
| tbD2U | fork-slaa-us-mmllm-claude-train-sym24-164e99bc-tbD2U | 2.2544 |
| NxQsL | fork-joly-os-mmllm-claude-train-sym24-d5ee643b-NxQsL | 2.4132 |
| gKZzR | fork-SeniorCareMarket-mmllm-claude-train-sym24-63289deb-gKZzR | 2.4188 |
| **mean** | | **2.2997** |
| **best** | | **2.2282** |

## Chain progression R1277 → R1278

Previous harvest: `workers/dispatcher/harvest-5way-r1277_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3075         | 2.2997         | -0.0078 |
| ctrl_bpc best  | 2.2215         | 2.2282         | +0.0067 |

## Per-round trajectory (best bird: zJyFE)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1278 | 6585 | 2.2282 | +0.2499 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1277_sym24`
  - `workers/dispatcher/harvest-5way-r1277_sym24`

## Output

`workers/dispatcher/harvest-6way-r1278_sym24/round-1278/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

