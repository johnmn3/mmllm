# harvest-4way-r1050 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1050 ctrl_bpc |
|--------|--------|--------------:|
| AJqct | fork-SeniorCareMarket-mmllm-claude-train-sym24-36e3cdf5-AJqct | 2.5040 |
| LPT3o | origin/claude/train-sym24-99b16257-LPT3o | 2.5156 |
| vyXuq | origin/claude/train-sym24-2f685f87-vyXuq | 2.8527 |
| 62RBc | fork-joly-os-mmllm-claude-train-sym24-06e31b8c-62RBc | 2.8646 |
| **mean** | | **2.6842** |
| **best** | | **2.5040** |

## Chain progression R1049 → R1050

Previous harvest: `workers/dispatcher/harvest-5way-r1049_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6423         | 2.6842         | +0.0419 |
| ctrl_bpc best  | 2.4705         | 2.5040         | +0.0335 |

## Per-round trajectory (best bird: AJqct)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1050 | 4130 | 2.5040 | +0.2006 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1049_sym24`
  - `workers/dispatcher/harvest-2way-r1049_sym24`

## Output

`workers/dispatcher/harvest-4way-r1050_sym24/round-1050/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

