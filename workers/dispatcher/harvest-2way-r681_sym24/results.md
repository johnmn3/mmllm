# harvest-2way-r681 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R681 ctrl_bpc |
|--------|--------|--------------:|
| NysJS | origin/claude/train-sym24-b669f016-NysJS | 3.8301 |
| YoTZg | fork-slaa-us-mmllm-claude-train-sym24-1c8de6b3-YoTZg | 4.1007 |
| **mean** | | **3.9654** |
| **best** | | **3.8301** |

## Chain progression R680 → R681

Previous harvest: `workers/dispatcher/harvest-2way-r680_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.9566         | 3.9654         | +0.0088 |
| ctrl_bpc best  | 3.8210         | 3.8301         | +0.0091 |

## Per-round trajectory (best bird: NysJS)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 681 | 6332 | 3.8301 | +0.5328 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r680_sym24`

## Output

`workers/dispatcher/harvest-2way-r681_sym24/round-681/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

