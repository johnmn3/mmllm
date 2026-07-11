# harvest-2way-r891 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R891 ctrl_bpc |
|--------|--------|--------------:|
| SMzrn | origin/claude/train-sym24-d660d321-SMzrn | 2.8384 |
| 0PMD5 | fork-joly-os-mmllm-claude-train-sym24-47ae7e83-0PMD5 | 3.2010 |
| **mean** | | **3.0197** |
| **best** | | **2.8384** |

## Chain progression R890 → R891

Previous harvest: `workers/dispatcher/harvest-4way-r890_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9303         | 3.0197         | +0.0894 |
| ctrl_bpc best  | 2.8163         | 2.8384         | +0.0221 |

## Per-round trajectory (best bird: SMzrn)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 891 | 4422 | 2.8384 | +0.1399 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r890_sym24`

## Output

`workers/dispatcher/harvest-2way-r891_sym24/round-891/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

