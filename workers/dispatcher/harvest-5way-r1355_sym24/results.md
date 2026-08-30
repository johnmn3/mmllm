# harvest-5way-r1355 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1355 ctrl_bpc |
|--------|--------|--------------:|
| ApU4g | origin/claude/train-sym24-6c781471-ApU4g | 3.2876 |
| bvnn3 | fork-joly-os-mmllm-claude-train-sym24-0649fef9-bvnn3 | 3.2934 |
| wgODK | origin/claude/train-sym24-d2013518-wgODK | 3.2943 |
| CfFyq | origin/claude/train-sym24-6d657300-CfFyq | 3.2966 |
| VldsM | fork-slaa-us-mmllm-claude-train-sym24-0d9038e9-VldsM | 3.6117 |
| **mean** | | **3.3567** |
| **best** | | **3.2876** |

## Chain progression R1354 → R1355

Previous harvest: `workers/dispatcher/harvest-6way-r1354_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3440         | 3.3567         | +0.0127 |
| ctrl_bpc best  | 3.2511         | 3.2876         | +0.0365 |

## Per-round trajectory (best bird: ApU4g)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1355 | 6578 | 3.2876 | +0.0941 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1354_sym24`
  - `workers/dispatcher/harvest-6way-r1354_sym24`

## Output

`workers/dispatcher/harvest-5way-r1355_sym24/round-1355/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

