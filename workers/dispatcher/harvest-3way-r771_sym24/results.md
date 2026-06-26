# harvest-3way-r771 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R771 ctrl_bpc |
|--------|--------|--------------:|
| Oq6OL | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-7faa7340-Oq6OL | 3.2597 |
| c625s | origin/claude/train-sym24-a7f216d0-c625s | 3.6099 |
| 9VYPP | fork-joly-os-mmllm-claude-train-sym24-49521724-9VYPP | 3.6224 |
| **mean** | | **3.4973** |
| **best** | | **3.2597** |

## Chain progression R770 → R771

Previous harvest: `workers/dispatcher/harvest-3way-r770_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2684         | 3.4973         | +0.2289 |
| ctrl_bpc best  | 3.2650         | 3.2597         | -0.0053 |

## Per-round trajectory (best bird: Oq6OL)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 771 | 6525 | 3.2597 | +0.6133 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r770_sym24`

## Output

`workers/dispatcher/harvest-3way-r771_sym24/round-771/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

