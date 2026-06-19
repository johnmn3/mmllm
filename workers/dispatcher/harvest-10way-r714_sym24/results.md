# harvest-10way-r714 — sparse-delta merge of 10 birds

## Worker endpoints

| handle | branch | R714 ctrl_bpc |
|--------|--------|--------------:|
| hy4TS | fork-SeniorCareMarket-mmllm-claude-train-sym24-c46ded15-hy4TS | 3.5379 |
| exx30 | fork-davidwuchn-mmllm-claude-train-sym24-eb203c7d-exx30 | 3.5406 |
| j7gWw | fork-slaa-us-mmllm-claude-train-sym24-cac427ae-j7gWw | 3.5427 |
| mNtt7 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-36146b70-mNtt7 | 3.5438 |
| o2DfX | fork-joly-os-mmllm-claude-train-sym24-46a80619-o2DfX | 3.5771 |
| A8uD3 | origin/claude/train-sym24-9e30e2b1-A8uD3 | 3.5778 |
| 3lpD3 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-e780095c-3lpD3 | 3.5831 |
| 5fPe6 | origin/claude/train-sym24-b19dde46-5fPe6 | 3.5862 |
| sf5og | fork-slaa-us-mmllm-claude-train-sym24-6b10472c-sf5og | 3.5932 |
| c4PMP | fork-joly-os-mmllm-claude-train-sym24-c2ee4aa5-c4PMP | 3.6237 |
| **mean** | | **3.5706** |
| **best** | | **3.5379** |

## Chain progression R713 → R714

Previous harvest: `workers/dispatcher/harvest-10way-r713_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.7013         | 3.5706         | -0.1307 |
| ctrl_bpc best  | 3.5473         | 3.5379         | -0.0094 |

## Per-round trajectory (best bird: hy4TS)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 714 | 4379 | 3.5379 | +1.4075 |

## Cumulative training contribution

- This harvest: **800 steps** from 10 bird(s)
- Across full ancestry (deduped by bird_id): **1600 steps** from 20 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-10way-r713_sym24`
  - `workers/dispatcher/harvest-4way-r713_sym24`

## Output

`workers/dispatcher/harvest-10way-r714_sym24/round-714/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 10 workers)
- `dense.pt` (averaged across 10 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

