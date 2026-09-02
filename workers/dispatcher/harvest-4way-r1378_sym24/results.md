# harvest-4way-r1378 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1378 ctrl_bpc |
|--------|--------|--------------:|
| xOmUq | origin/claude/train-sym24-a72b7936-xOmUq | 3.1221 |
| 42aMi | fork-SeniorCareMarket-mmllm-claude-train-sym24-79d14f95-42aMi | 3.2038 |
| qZGz4 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-bb6911a2-qZGz4 | 3.5074 |
| V0PG1 | fork-joly-os-mmllm-claude-train-sym24-c5d527cc-V0PG1 | 3.5074 |
| **mean** | | **3.3352** |
| **best** | | **3.1221** |

## Chain progression R1377 → R1378

Previous harvest: `workers/dispatcher/harvest-4way-r1377_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3258         | 3.3352         | +0.0094 |
| ctrl_bpc best  | 3.0703         | 3.1221         | +0.0518 |

## Per-round trajectory (best bird: xOmUq)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1378 | 6579 | 3.1221 | +0.1110 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1377_sym24`

## Output

`workers/dispatcher/harvest-4way-r1378_sym24/round-1378/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

