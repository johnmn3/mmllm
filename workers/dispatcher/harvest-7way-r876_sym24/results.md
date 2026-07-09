# harvest-7way-r876 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R876 ctrl_bpc |
|--------|--------|--------------:|
| 6u0In | fork-joly-os-mmllm-claude-train-sym24-4363bd5e-6u0In | 2.8556 |
| 40dXX | fork-joly-os-mmllm-claude-train-sym24-e8eeda43-40dXX | 2.8705 |
| dMPTW | fork-SeniorCareMarket-mmllm-claude-train-sym24-107b1f26-dMPTW | 3.0176 |
| DWFU6 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-c6cb415c-DWFU6 | 3.0334 |
| wk98S | origin/claude/train-sym24-19c494e8-wk98S | 3.0664 |
| lla1t | fork-slaa-us-mmllm-claude-train-sym24-1ce18f20-lla1t | 3.2208 |
| rP1iW | origin/claude/train-sym24-c98a2328-rP1iW | 3.2425 |
| **mean** | | **3.0438** |
| **best** | | **2.8556** |

## Chain progression R875 → R876

Previous harvest: `workers/dispatcher/harvest-4way-r875_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8565         | 3.0438         | +0.1873 |
| ctrl_bpc best  | 2.8377         | 2.8556         | +0.0179 |

## Per-round trajectory (best bird: 6u0In)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 876 | 6662 | 2.8556 | +0.4291 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r875_sym24`
  - `workers/dispatcher/harvest-4way-r875_sym24`

## Output

`workers/dispatcher/harvest-7way-r876_sym24/round-876/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

