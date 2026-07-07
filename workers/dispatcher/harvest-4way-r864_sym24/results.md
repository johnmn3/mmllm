# harvest-4way-r864 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R864 ctrl_bpc |
|--------|--------|--------------:|
| NoBz2 | fork-joly-os-mmllm-claude-train-sym24-872f8373-NoBz2 | 2.8695 |
| 8fyxx | fork-SeniorCareMarket-mmllm-claude-train-sym24-a732ebc3-8fyxx | 2.9006 |
| 8ryog | origin/claude/train-sym24-4b1d99f8-8ryog | 3.0497 |
| zO5AB | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f5374901-zO5AB | 3.2766 |
| **mean** | | **3.0241** |
| **best** | | **2.8695** |

## Chain progression R863 → R864

Previous harvest: `workers/dispatcher/harvest-4way-r863_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1735         | 3.0241         | -0.1494 |
| ctrl_bpc best  | 2.8813         | 2.8695         | -0.0118 |

## Per-round trajectory (best bird: NoBz2)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 864 | 6469 | 2.8695 | +0.4357 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r863_sym24`

## Output

`workers/dispatcher/harvest-4way-r864_sym24/round-864/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

