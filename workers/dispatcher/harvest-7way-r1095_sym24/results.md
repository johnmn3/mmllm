# harvest-7way-r1095 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R1095 ctrl_bpc |
|--------|--------|--------------:|
| La1Rh | fork-slaa-us-mmllm-claude-train-sym24-5d873c18-La1Rh | 2.4129 |
| adoL5 | origin/claude/train-sym24-53d1bdd3-adoL5 | 2.4154 |
| qSJR0 | origin/claude/train-sym24-d5a7a62b-qSJR0 | 2.4315 |
| uJWJd | fork-joly-os-mmllm-claude-train-sym24-0f65a130-uJWJd | 2.6082 |
| 0tJvc | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-b8b4df98-0tJvc | 2.6122 |
| QMb3N | fork-slaa-us-mmllm-claude-train-sym24-d233f6d4-QMb3N | 2.7889 |
| Yu6V0 | fork-SeniorCareMarket-mmllm-claude-train-sym24-f3fdc1ce-Yu6V0 | 2.8121 |
| **mean** | | **2.5830** |
| **best** | | **2.4129** |

## Chain progression R1094 → R1095

Previous harvest: `workers/dispatcher/harvest-8way-r1094_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5071         | 2.5830         | +0.0759 |
| ctrl_bpc best  | 2.3966         | 2.4129         | +0.0163 |

## Per-round trajectory (best bird: La1Rh)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1095 | 6636 | 2.4129 | +0.2299 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1094_sym24`
  - `workers/dispatcher/harvest-4way-r1094_sym24`

## Output

`workers/dispatcher/harvest-7way-r1095_sym24/round-1095/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

