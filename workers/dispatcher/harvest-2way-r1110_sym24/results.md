# harvest-2way-r1110 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1110 ctrl_bpc |
|--------|--------|--------------:|
| c0s8d | fork-joly-os-mmllm-claude-train-sym24-0a1550a1-c0s8d | 2.4138 |
| mrmAn | origin/claude/train-sym24-969927ed-mrmAn | 2.5936 |
| **mean** | | **2.5037** |
| **best** | | **2.4138** |

## Chain progression R1109 → R1110

Previous harvest: `workers/dispatcher/harvest-5way-r1109_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4786         | 2.5037         | +0.0251 |
| ctrl_bpc best  | 2.4030         | 2.4138         | +0.0108 |

## Per-round trajectory (best bird: c0s8d)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1110 | 3682 | 2.4138 | +0.2244 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1109_sym24`
  - `workers/dispatcher/harvest-3way-r1109_sym24`

## Output

`workers/dispatcher/harvest-2way-r1110_sym24/round-1110/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

