# harvest-2way-r1308 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1308 ctrl_bpc |
|--------|--------|--------------:|
| 5SXBU | origin/claude/train-sym24-0d3b8658-5SXBU | 3.4175 |
| dddCU | fork-slaa-us-mmllm-claude-train-sym24-243b1a65-dddCU | 3.8610 |
| **mean** | | **3.6393** |
| **best** | | **3.4175** |

## Chain progression R1307 → R1308

Previous harvest: `workers/dispatcher/harvest-5way-r1307_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.6191         | 3.6393         | +0.0202 |
| ctrl_bpc best  | 3.4116         | 3.4175         | +0.0059 |

## Per-round trajectory (best bird: 5SXBU)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1308 | 5330 | 3.4175 | +0.1010 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1307_sym24`

## Output

`workers/dispatcher/harvest-2way-r1308_sym24/round-1308/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

