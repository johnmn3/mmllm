# harvest-4way-r1182 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1182 ctrl_bpc |
|--------|--------|--------------:|
| A4YpD | origin/claude/train-sym24-91ae0376-A4YpD | 2.3076 |
| l8RSr | fork-slaa-us-mmllm-claude-train-sym24-002af186-l8RSr | 2.4958 |
| b7G9o | fork-joly-os-mmllm-claude-train-sym24-09e4d3cb-b7G9o | 2.5057 |
| CPYgN | fork-joly-os-mmllm-claude-train-sym24-f4d5f7fe-CPYgN | 2.7181 |
| **mean** | | **2.5068** |
| **best** | | **2.3076** |

## Chain progression R1181 → R1182

Previous harvest: `workers/dispatcher/harvest-4way-r1181_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4147         | 2.5068         | +0.0921 |
| ctrl_bpc best  | 2.3155         | 2.3076         | -0.0079 |

## Per-round trajectory (best bird: A4YpD)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1182 | 6436 | 2.3076 | +0.2687 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1181_sym24`

## Output

`workers/dispatcher/harvest-4way-r1182_sym24/round-1182/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

