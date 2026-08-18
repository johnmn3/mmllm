# harvest-4way-r1245 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1245 ctrl_bpc |
|--------|--------|--------------:|
| 02myJ | origin/claude/train-sym24-1e4e1f6b-02myJ | 2.2580 |
| kXP5F | fork-slaa-us-mmllm-claude-train-sym24-e7afe12a-kXP5F | 2.2611 |
| WWXlp | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-82311bf0-WWXlp | 2.2647 |
| bBgdP | fork-SeniorCareMarket-mmllm-claude-train-sym24-55b5d8c3-bBgdP | 2.4527 |
| **mean** | | **2.3091** |
| **best** | | **2.2580** |

## Chain progression R1244 → R1245

Previous harvest: `workers/dispatcher/harvest-11way-r1244_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3427         | 2.3091         | -0.0336 |
| ctrl_bpc best  | 2.2409         | 2.2580         | +0.0171 |

## Per-round trajectory (best bird: 02myJ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1245 | 6284 | 2.2580 | +0.2393 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1244_sym24`

## Output

`workers/dispatcher/harvest-4way-r1245_sym24/round-1245/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

