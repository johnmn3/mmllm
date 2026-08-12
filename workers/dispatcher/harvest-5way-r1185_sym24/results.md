# harvest-5way-r1185 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1185 ctrl_bpc |
|--------|--------|--------------:|
| GzDVs | origin/claude/train-sym24-ef831967-GzDVs | 2.3143 |
| LNKvL | origin/claude/train-sym24-4947b6e3-LNKvL | 2.4965 |
| pmcsp | fork-joly-os-mmllm-claude-train-sym24-506cc3ad-pmcsp | 2.5007 |
| D7Iop | fork-SeniorCareMarket-mmllm-claude-train-sym24-8c7c277f-D7Iop | 2.5028 |
| YY0pf | fork-slaa-us-mmllm-claude-train-sym24-35285155-YY0pf | 2.6911 |
| **mean** | | **2.5011** |
| **best** | | **2.3143** |

## Chain progression R1184 → R1185

Previous harvest: `workers/dispatcher/harvest-3way-r1184_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4293         | 2.5011         | +0.0718 |
| ctrl_bpc best  | 2.3010         | 2.3143         | +0.0133 |

## Per-round trajectory (best bird: GzDVs)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1185 | 6485 | 2.3143 | +0.2467 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1184_sym24`

## Output

`workers/dispatcher/harvest-5way-r1185_sym24/round-1185/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

