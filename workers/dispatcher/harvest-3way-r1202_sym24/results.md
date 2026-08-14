# harvest-3way-r1202 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1202 ctrl_bpc |
|--------|--------|--------------:|
| iY8Xg | fork-joly-os-mmllm-claude-train-sym24-ea02950c-iY8Xg | 2.2838 |
| ZoNGQ | origin/claude/train-sym24-f3286320-ZoNGQ | 2.3042 |
| 2SKhO | fork-slaa-us-mmllm-claude-train-sym24-1f25f0ad-2SKhO | 2.6662 |
| **mean** | | **2.4181** |
| **best** | | **2.2838** |

## Chain progression R1201 → R1202

Previous harvest: `workers/dispatcher/harvest-5way-r1201_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4151         | 2.4181         | +0.0030 |
| ctrl_bpc best  | 2.2929         | 2.2838         | -0.0091 |

## Per-round trajectory (best bird: iY8Xg)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1202 | 3804 | 2.2838 | +0.2541 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1201_sym24`
  - `workers/dispatcher/harvest-5way-r1201_sym24`

## Output

`workers/dispatcher/harvest-3way-r1202_sym24/round-1202/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

