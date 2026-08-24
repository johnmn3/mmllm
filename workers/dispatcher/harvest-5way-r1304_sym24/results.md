# harvest-5way-r1304 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1304 ctrl_bpc |
|--------|--------|--------------:|
| GBZth | fork-slaa-us-mmllm-claude-train-sym24-cfda6820-GBZth | 3.5458 |
| lffLu | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-b7ebc66b-lffLu | 3.5563 |
| z7ilS | fork-joly-os-mmllm-claude-train-sym24-6e97a0a9-z7ilS | 3.5564 |
| NS2h8 | fork-SeniorCareMarket-mmllm-claude-train-sym24-e9f60ee9-NS2h8 | 3.5805 |
| i7HVa | origin/claude/train-sym24-6177d488-i7HVa | 3.8958 |
| **mean** | | **3.6270** |
| **best** | | **3.5458** |

## Chain progression R1303 → R1304

Previous harvest: `workers/dispatcher/harvest-4way-r1303_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.6021         | 3.6270         | +0.0249 |
| ctrl_bpc best  | 3.5844         | 3.5458         | -0.0386 |

## Per-round trajectory (best bird: GBZth)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1304 | 6559 | 3.5458 | +0.0573 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1303_sym24`

## Output

`workers/dispatcher/harvest-5way-r1304_sym24/round-1304/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

