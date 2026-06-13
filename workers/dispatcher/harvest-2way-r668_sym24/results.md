# harvest-2way-r668 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R668 ctrl_bpc |
|--------|--------|--------------:|
| tut30 | fork-joly-os-mmllm-claude-train-sym24-032cdc46-tut30 | 4.2313 |
| wS5SF | fork-davidwuchn-mmllm-claude-train-sym24-fe6fe8b5-wS5SF | 4.2493 |
| **mean** | | **4.2403** |
| **best** | | **4.2313** |

## Chain progression R667 → R668

Previous harvest: `workers/dispatcher/harvest-13way-r667_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.9936         | 4.2403         | +0.2467 |
| ctrl_bpc best  | 3.8934         | 4.2313         | +0.3379 |

## Per-round trajectory (best bird: tut30)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 668 | 6518 | 4.2313 | +0.2737 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r667_sym24`

## Output

`workers/dispatcher/harvest-2way-r668_sym24/round-668/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

