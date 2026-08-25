# harvest-4way-r1319 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1319 ctrl_bpc |
|--------|--------|--------------:|
| 8CcXR | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-8d99e412-8CcXR | 3.4495 |
| ipQDs | origin/claude/train-sym24-d723be7a-ipQDs | 3.4915 |
| zF9pa | fork-slaa-us-mmllm-claude-train-sym24-b062cff8-zF9pa | 3.5485 |
| li3Yg | fork-SeniorCareMarket-mmllm-claude-train-sym24-d582db96-li3Yg | 3.7216 |
| **mean** | | **3.5528** |
| **best** | | **3.4495** |

## Chain progression R1318 → R1319

Previous harvest: `workers/dispatcher/harvest-5way-r1318_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5564         | 3.5528         | -0.0036 |
| ctrl_bpc best  | 3.3899         | 3.4495         | +0.0596 |

## Per-round trajectory (best bird: 8CcXR)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1319 | 5319 | 3.4495 | +0.0490 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1318_sym24`

## Output

`workers/dispatcher/harvest-4way-r1319_sym24/round-1319/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

