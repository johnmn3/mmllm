# harvest-2way-r641 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R641 ctrl_bpc |
|--------|--------|--------------:|
| Mav6q | fork-joly-os-mmllm-claude-train-sym24-5ffb368f-Mav6q | 4.7236 |
| 0glKF | origin/claude/train-sym24-882c3a1e-0glKF | 5.2122 |
| **mean** | | **4.9679** |
| **best** | | **4.7236** |

## Chain progression R640 → R641

Previous harvest: `workers/dispatcher/harvest-5way-r640_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 5.2156         | 4.9679         | -0.2477 |
| ctrl_bpc best  | 4.9453         | 4.7236         | -0.2217 |

## Per-round trajectory (best bird: Mav6q)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 641 | 6282 | 4.7236 | +0.0160 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **2800 steps** from 35 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r640_sym24`

## Output

`workers/dispatcher/harvest-2way-r641_sym24/round-641/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

