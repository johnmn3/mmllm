# harvest-3way-r129 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R129 ctrl_bpc |
|--------|--------|--------------:|
| d8qJq | fork-joly-os-mmllm-claude-train-8268979e-d8qJq | 1.3191 |
| zVYT4 | fork-slaa-us-mmllm-claude-train-405e4336-zVYT4 | 1.5247 |
| FGBGF | origin/claude/train-940abf15-FGBGF | 1.6787 |
| **mean** | | **1.5075** |
| **best** | | **1.3191** |

## Chain progression R126 → R129

Previous harvest: `workers/dispatcher/harvest-4way-r126`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 1.4040         | 1.5075         | +0.1035 |
| ctrl_bpc best  | 1.3243         | 1.3191         | -0.0052 |

## Per-round trajectory (best bird: d8qJq)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 125 | 616 | 1.5825 | -0.0182 |
| 126 | 574 | 1.3234 | +0.0017 |
| 127 | 568 | 1.3235 | +0.0096 |
| 128 | 528 | 1.3937 | +0.0099 |
| 129 | 537 | 1.3191 | +0.0040 |

## Cumulative training contribution

- This harvest: **105 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **2893 steps** from 76 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r124`

## Output

`workers/dispatcher/harvest-3way-r129/round-129/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

