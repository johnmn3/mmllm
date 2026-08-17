# harvest-3way-r1229 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1229 ctrl_bpc |
|--------|--------|--------------:|
| 4uD5k | fork-slaa-us-mmllm-claude-train-sym24-5a9f9b7f-4uD5k | 2.2552 |
| LwClp | fork-SeniorCareMarket-mmllm-claude-train-sym24-e78d7258-LwClp | 2.2761 |
| qJwHt | fork-joly-os-mmllm-claude-train-sym24-17b7eae1-qJwHt | 2.6710 |
| **mean** | | **2.4008** |
| **best** | | **2.2552** |

## Chain progression R1228 → R1229

Previous harvest: `workers/dispatcher/harvest-6way-r1228_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4274         | 2.4008         | -0.0266 |
| ctrl_bpc best  | 2.2490         | 2.2552         | +0.0062 |

## Per-round trajectory (best bird: 4uD5k)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1229 | 4114 | 2.2552 | +0.2463 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1228_sym24`
  - `workers/dispatcher/harvest-6way-r1228_sym24`

## Output

`workers/dispatcher/harvest-3way-r1229_sym24/round-1229/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

