# harvest-2way-r1089 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1089 ctrl_bpc |
|--------|--------|--------------:|
| 03XTM | fork-slaa-us-mmllm-claude-train-sym24-66e82bc0-03XTM | 2.4040 |
| 16FTE | fork-joly-os-mmllm-claude-train-sym24-5105c8d4-16FTE | 2.4261 |
| **mean** | | **2.4150** |
| **best** | | **2.4040** |

## Chain progression R1088 → R1089

Previous harvest: `workers/dispatcher/harvest-11way-r1088_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4762         | 2.4150         | -0.0612 |
| ctrl_bpc best  | 2.4082         | 2.4040         | -0.0042 |

## Per-round trajectory (best bird: 03XTM)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1089 | 4272 | 2.4040 | +0.2435 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r1088_sym24`

## Output

`workers/dispatcher/harvest-2way-r1089_sym24/round-1089/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

