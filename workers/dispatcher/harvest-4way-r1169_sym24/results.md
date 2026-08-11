# harvest-4way-r1169 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1169 ctrl_bpc |
|--------|--------|--------------:|
| KsAwM | origin/claude/train-sym24-0f09a618-KsAwM | 2.3114 |
| Myb3n | fork-joly-os-mmllm-claude-train-sym24-ce0bce0d-Myb3n | 2.5164 |
| 5h09r | origin/claude/train-sym24-b897f80a-5h09r | 2.7094 |
| q1fRm | fork-slaa-us-mmllm-claude-train-sym24-1ba82a70-q1fRm | 2.7226 |
| **mean** | | **2.5649** |
| **best** | | **2.3114** |

## Chain progression R1168 → R1169

Previous harvest: `workers/dispatcher/harvest-9way-r1168_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4355         | 2.5649         | +0.1294 |
| ctrl_bpc best  | 2.3175         | 2.3114         | -0.0061 |

## Per-round trajectory (best bird: KsAwM)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1169 | 6674 | 2.3114 | +0.2602 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1168_sym24`

## Output

`workers/dispatcher/harvest-4way-r1169_sym24/round-1169/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

