# harvest-2way-r1169 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1169 ctrl_bpc |
|--------|--------|--------------:|
| Myb3n | fork-joly-os-mmllm-claude-train-sym24-ce0bce0d-Myb3n | 2.5164 |
| 5h09r | origin/claude/train-sym24-b897f80a-5h09r | 2.7094 |
| **mean** | | **2.6129** |
| **best** | | **2.5164** |

## Chain progression R1168 → R1169

Previous harvest: `workers/dispatcher/harvest-9way-r1168_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4355         | 2.6129         | +0.1774 |
| ctrl_bpc best  | 2.3175         | 2.5164         | +0.1989 |

## Per-round trajectory (best bird: Myb3n)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1169 | 6660 | 2.5164 | +0.2210 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1168_sym24`

## Output

`workers/dispatcher/harvest-2way-r1169_sym24/round-1169/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

