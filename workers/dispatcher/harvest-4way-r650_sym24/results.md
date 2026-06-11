# harvest-4way-r650 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R650 ctrl_bpc |
|--------|--------|--------------:|
| lEF14 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-2b14bd44-lEF14 | 4.2784 |
| dB7iy | origin/claude/train-sym24-b1fca47a-dB7iy | 4.2932 |
| v3jDP | fork-slaa-us-mmllm-claude-train-sym24-dd188189-v3jDP | 4.3033 |
| iVmOm | fork-joly-os-mmllm-claude-train-sym24-cf302b4c-iVmOm | 4.3273 |
| **mean** | | **4.3006** |
| **best** | | **4.2784** |

## Chain progression R649 → R650

Previous harvest: `workers/dispatcher/harvest-1way-r649_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.3552         | 4.3006         | -0.0546 |
| ctrl_bpc best  | 4.3552         | 4.2784         | -0.0768 |

## Per-round trajectory (best bird: lEF14)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 650 | 6331 | 4.2784 | +0.0547 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r649_sym24`

## Output

`workers/dispatcher/harvest-4way-r650_sym24/round-650/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

