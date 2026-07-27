# harvest-6way-r1035 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1035 ctrl_bpc |
|--------|--------|--------------:|
| jKI37 | origin/claude/train-sym24-484e7594-jKI37 | 2.4881 |
| gDAfS | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-0811bbb4-gDAfS | 2.6321 |
| 414X2 | fork-SeniorCareMarket-mmllm-claude-train-sym24-e85d11c0-414X2 | 2.6850 |
| 7hhjL | fork-joly-os-mmllm-claude-train-sym24-2c735b3c-7hhjL | 2.6877 |
| dF9j2 | fork-slaa-us-mmllm-claude-train-sym24-8449922d-dF9j2 | 2.6976 |
| UZzv6 | origin/claude/train-sym24-6c1c056c-UZzv6 | 2.9053 |
| **mean** | | **2.6826** |
| **best** | | **2.4881** |

## Chain progression R1034 → R1035

Previous harvest: `workers/dispatcher/harvest-6way-r1034_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6076         | 2.6826         | +0.0750 |
| ctrl_bpc best  | 2.5112         | 2.4881         | -0.0231 |

## Per-round trajectory (best bird: jKI37)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1035 | 6544 | 2.4881 | +0.1911 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1034_sym24`
  - `workers/dispatcher/harvest-6way-r1034_sym24`

## Output

`workers/dispatcher/harvest-6way-r1035_sym24/round-1035/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

