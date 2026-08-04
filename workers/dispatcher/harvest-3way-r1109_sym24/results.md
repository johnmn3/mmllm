# harvest-3way-r1109 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1109 ctrl_bpc |
|--------|--------|--------------:|
| a2lFs | fork-joly-os-mmllm-claude-train-sym24-9e2584f9-a2lFs | 2.4030 |
| TpqZp | origin/claude/train-sym24-8f807cb1-TpqZp | 2.4151 |
| 254Q1 | fork-slaa-us-mmllm-claude-train-sym24-90315730-254Q1 | 2.5838 |
| **mean** | | **2.4673** |
| **best** | | **2.4030** |

## Chain progression R1108 → R1109

Previous harvest: `workers/dispatcher/harvest-6way-r1108_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4884         | 2.4673         | -0.0211 |
| ctrl_bpc best  | 2.3848         | 2.4030         | +0.0182 |

## Per-round trajectory (best bird: a2lFs)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1109 | 6300 | 2.4030 | +0.2222 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1108_sym24`

## Output

`workers/dispatcher/harvest-3way-r1109_sym24/round-1109/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

