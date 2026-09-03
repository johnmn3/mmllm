# harvest-5way-r1389 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1389 ctrl_bpc |
|--------|--------|--------------:|
| r7E0m | fork-joly-os-mmllm-claude-train-sym24-a2f9c30e-r7E0m | 3.0448 |
| smZv8 | origin/claude/train-sym24-20cd043e-smZv8 | 3.0469 |
| 1WoEb | fork-SeniorCareMarket-mmllm-claude-train-sym24-83d5b5e8-1WoEb | 3.0560 |
| 33SOK | fork-joly-os-mmllm-claude-train-sym24-6e38a001-33SOK | 3.1160 |
| 72Aw2 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-72bc3773-72Aw2 | 3.4002 |
| **mean** | | **3.1328** |
| **best** | | **3.0448** |

## Chain progression R1388 → R1389

Previous harvest: `workers/dispatcher/harvest-1way-r1388_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0661         | 3.1328         | +0.0667 |
| ctrl_bpc best  | 3.0661         | 3.0448         | -0.0213 |

## Per-round trajectory (best bird: r7E0m)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1389 | 5374 | 3.0448 | +0.1118 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1388_sym24`

## Output

`workers/dispatcher/harvest-5way-r1389_sym24/round-1389/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

