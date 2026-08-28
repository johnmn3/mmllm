# harvest-2way-r1343 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1343 ctrl_bpc |
|--------|--------|--------------:|
| mNBrL | fork-SeniorCareMarket-mmllm-claude-train-sym24-f11ca9b1-mNBrL | 3.2806 |
| FVfHp | origin/claude/train-sym24-66bbee44-FVfHp | 3.7740 |
| **mean** | | **3.5273** |
| **best** | | **3.2806** |

## Chain progression R1342 → R1343

Previous harvest: `workers/dispatcher/harvest-2way-r1342_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3035         | 3.5273         | +0.2238 |
| ctrl_bpc best  | 3.2795         | 3.2806         | +0.0011 |

## Per-round trajectory (best bird: mNBrL)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1343 | 4047 | 3.2806 | +0.0738 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1342_sym24`

## Output

`workers/dispatcher/harvest-2way-r1343_sym24/round-1343/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

