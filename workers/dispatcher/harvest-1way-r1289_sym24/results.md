# harvest-1way-r1289 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1289 ctrl_bpc |
|--------|--------|--------------:|
| uyP96 | fork-slaa-us-mmllm-claude-train-sym24-ec61913b-uyP96 | 2.2241 |
| **mean** | | **2.2241** |
| **best** | | **2.2241** |

## Chain progression R1288 → R1289

Previous harvest: `workers/dispatcher/harvest-5way-r1288_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3441         | 2.2241         | -0.1200 |
| ctrl_bpc best  | 2.2089         | 2.2241         | +0.0152 |

## Per-round trajectory (best bird: uyP96)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1289 | 3916 | 2.2241 | +0.2440 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1288_sym24`

## Output

`workers/dispatcher/harvest-1way-r1289_sym24/round-1289/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

