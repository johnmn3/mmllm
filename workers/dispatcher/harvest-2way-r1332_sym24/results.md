# harvest-2way-r1332 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1332 ctrl_bpc |
|--------|--------|--------------:|
| af4Jr | fork-slaa-us-mmllm-claude-train-sym24-0795915e-af4Jr | 3.3489 |
| RfxvN | origin/claude/train-sym24-fdeea7f3-RfxvN | 3.3611 |
| **mean** | | **3.3550** |
| **best** | | **3.3489** |

## Chain progression R1331 → R1332

Previous harvest: `workers/dispatcher/harvest-1way-r1331_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3124         | 3.3550         | +0.0426 |
| ctrl_bpc best  | 3.3124         | 3.3489         | +0.0365 |

## Per-round trajectory (best bird: af4Jr)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1332 | 3448 | 3.3489 | +0.0807 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1331_sym24`

## Output

`workers/dispatcher/harvest-2way-r1332_sym24/round-1332/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

