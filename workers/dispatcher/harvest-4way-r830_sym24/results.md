# harvest-4way-r830 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R830 ctrl_bpc |
|--------|--------|--------------:|
| yphaz | fork-joly-os-mmllm-claude-train-sym24-350e2189-yphaz | 2.9814 |
| L1aC2 | fork-SeniorCareMarket-mmllm-claude-train-sym24-1a6fba14-L1aC2 | 2.9905 |
| iiBmU | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-c0b4cb62-iiBmU | 2.9946 |
| j6Ymb | origin/claude/train-sym24-617edf0b-j6Ymb | 3.3648 |
| **mean** | | **3.0828** |
| **best** | | **2.9814** |

## Chain progression R829 → R830

Previous harvest: `workers/dispatcher/harvest-2way-r829_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0694         | 3.0828         | +0.0134 |
| ctrl_bpc best  | 2.9854         | 2.9814         | -0.0040 |

## Per-round trajectory (best bird: yphaz)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 830 | 6609 | 2.9814 | +0.4877 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r829_sym24`

## Output

`workers/dispatcher/harvest-4way-r830_sym24/round-830/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

