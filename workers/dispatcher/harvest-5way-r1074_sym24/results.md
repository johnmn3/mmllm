# harvest-5way-r1074 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1074 ctrl_bpc |
|--------|--------|--------------:|
| 9ozAw | fork-SeniorCareMarket-mmllm-claude-train-sym24-8e697867-9ozAw | 2.4634 |
| fAuDi | origin/claude/train-sym24-08185aa7-fAuDi | 2.4773 |
| RCGlP | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-03f5f635-RCGlP | 2.6524 |
| g2sZM | fork-joly-os-mmllm-claude-train-sym24-6169b6b2-g2sZM | 2.8218 |
| iWzvC | fork-slaa-us-mmllm-claude-train-sym24-52e336cc-iWzvC | 2.8343 |
| **mean** | | **2.6498** |
| **best** | | **2.4634** |

## Chain progression R1073 → R1074

Previous harvest: `workers/dispatcher/harvest-4way-r1073_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6873         | 2.6498         | -0.0375 |
| ctrl_bpc best  | 2.4531         | 2.4634         | +0.0103 |

## Per-round trajectory (best bird: 9ozAw)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1074 | 6510 | 2.4634 | +0.2124 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1073_sym24`
  - `workers/dispatcher/harvest-4way-r1073_sym24`

## Output

`workers/dispatcher/harvest-5way-r1074_sym24/round-1074/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

