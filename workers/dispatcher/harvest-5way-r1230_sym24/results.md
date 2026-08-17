# harvest-5way-r1230 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1230 ctrl_bpc |
|--------|--------|--------------:|
| smGRm | fork-joly-os-mmllm-claude-train-sym24-1f916a25-smGRm | 2.2561 |
| 0uTR6 | origin/claude/train-sym24-2c1982d3-0uTR6 | 2.4561 |
| Mskms | origin/claude/train-sym24-68e8aeab-Mskms | 2.4587 |
| NQmd7 | fork-slaa-us-mmllm-claude-train-sym24-c3d140a1-NQmd7 | 2.4673 |
| sRm64 | fork-slaa-us-mmllm-claude-train-sym24-9a4cf79a-sRm64 | 2.6605 |
| **mean** | | **2.4597** |
| **best** | | **2.2561** |

## Chain progression R1229 → R1230

Previous harvest: `workers/dispatcher/harvest-3way-r1229_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4008         | 2.4597         | +0.0589 |
| ctrl_bpc best  | 2.2552         | 2.2561         | +0.0009 |

## Per-round trajectory (best bird: smGRm)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1230 | 4371 | 2.2561 | +0.2482 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1229_sym24`
  - `workers/dispatcher/harvest-3way-r1229_sym24`

## Output

`workers/dispatcher/harvest-5way-r1230_sym24/round-1230/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

