# harvest-5way-r1302 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1302 ctrl_bpc |
|--------|--------|--------------:|
| jWedx | origin/claude/train-sym24-be8a94f4-jWedx | 3.5489 |
| 98DmB | fork-slaa-us-mmllm-claude-train-sym24-f774a380-98DmB | 3.5778 |
| rEk9j | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-a1a47c38-rEk9j | 3.5779 |
| 8gOiP | fork-slaa-us-mmllm-claude-train-sym24-50c80707-8gOiP | 3.9726 |
| tGXVv | fork-SeniorCareMarket-mmllm-claude-train-sym24-6ca9437f-tGXVv | 3.9821 |
| **mean** | | **3.7319** |
| **best** | | **3.5489** |

## Chain progression R1301 → R1302

Previous harvest: `workers/dispatcher/harvest-4way-r1301_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.8760         | 3.7319         | -0.1441 |
| ctrl_bpc best  | 3.6795         | 3.5489         | -0.1306 |

## Per-round trajectory (best bird: jWedx)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1302 | 5366 | 3.5489 | +0.0705 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1301_sym24`
  - `workers/dispatcher/harvest-4way-r1301_sym24`

## Output

`workers/dispatcher/harvest-5way-r1302_sym24/round-1302/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

