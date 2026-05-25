# harvest-3way-r124 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R124 ctrl_bpc |
|--------|--------|--------------:|
| Pngcc | origin/claude/train-3b9ccbc0-Pngcc | 1.3377 |
| d1pBC | fork-joly-os-mmllm-claude-train-98bfd8ea-d1pBC | 1.6199 |
| oyG8V | fork-slaa-us-mmllm-claude-train-0b9941e7-oyG8V | 1.6337 |
| **mean** | | **1.5304** |
| **best** | | **1.3377** |

## Chain progression R121 → R124

Previous harvest: `workers/dispatcher/harvest-7way-r121`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 1.0519         | 1.5304         | +0.4785 |
| ctrl_bpc best  | 0.9290         | 1.3377         | +0.4087 |

## Per-round trajectory (best bird: Pngcc)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 120 | 504 | 1.0987 | +0.0073 |
| 121 | 447 | 1.3829 | +0.0192 |
| 122 | 449 | 1.4071 | +0.0062 |
| 123 | 435 | 1.2542 | -0.0051 |
| 124 | 450 | 1.3377 | +0.0025 |

## Cumulative training contribution

- This harvest: **105 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **2788 steps** from 73 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-6way-r119`

## Output

`workers/dispatcher/harvest-3way-r124/round-124/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

