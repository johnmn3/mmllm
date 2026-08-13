# harvest-6way-r1194 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1194 ctrl_bpc |
|--------|--------|--------------:|
| SlAyR | origin/claude/train-sym24-b8c75a50-SlAyR | 2.2894 |
| zOIvK | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-6696e90e-zOIvK | 2.2952 |
| hWU2H | fork-joly-os-mmllm-claude-train-sym24-240fa1be-hWU2H | 2.3040 |
| sa1sQ | origin/claude/train-sym24-c145d391-sa1sQ | 2.3075 |
| rGT0h | fork-slaa-us-mmllm-claude-train-sym24-a17a9ab0-rGT0h | 2.3096 |
| J2WOp | fork-SeniorCareMarket-mmllm-claude-train-sym24-a4fb8fc2-J2WOp | 2.6898 |
| **mean** | | **2.3659** |
| **best** | | **2.2894** |

## Chain progression R1193 → R1194

Previous harvest: `workers/dispatcher/harvest-11way-r1193_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3735         | 2.3659         | -0.0076 |
| ctrl_bpc best  | 2.2911         | 2.2894         | -0.0017 |

## Per-round trajectory (best bird: SlAyR)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1194 | 6655 | 2.2894 | +0.2618 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1193_sym24`

## Output

`workers/dispatcher/harvest-6way-r1194_sym24/round-1194/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

