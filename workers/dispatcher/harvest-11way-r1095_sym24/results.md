# harvest-11way-r1095 — sparse-delta merge of 11 birds

## Worker endpoints

| handle | branch | R1095 ctrl_bpc |
|--------|--------|--------------:|
| 0WI4n | origin/claude/train-sym24-6451475a-0WI4n | 2.3988 |
| RJq5P | fork-SeniorCareMarket-mmllm-claude-train-sym24-167e6a2e-RJq5P | 2.4076 |
| La1Rh | fork-slaa-us-mmllm-claude-train-sym24-5d873c18-La1Rh | 2.4129 |
| adoL5 | origin/claude/train-sym24-53d1bdd3-adoL5 | 2.4154 |
| qSJR0 | origin/claude/train-sym24-d5a7a62b-qSJR0 | 2.4315 |
| hIYdK | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-caa7effa-hIYdK | 2.6018 |
| uJWJd | fork-joly-os-mmllm-claude-train-sym24-0f65a130-uJWJd | 2.6082 |
| 0tJvc | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-b8b4df98-0tJvc | 2.6122 |
| FpH04 | fork-joly-os-mmllm-claude-train-sym24-c6b3debf-FpH04 | 2.6128 |
| QMb3N | fork-slaa-us-mmllm-claude-train-sym24-d233f6d4-QMb3N | 2.7889 |
| Yu6V0 | fork-SeniorCareMarket-mmllm-claude-train-sym24-f3fdc1ce-Yu6V0 | 2.8121 |
| **mean** | | **2.5547** |
| **best** | | **2.3988** |

## Chain progression R1094 → R1095

Previous harvest: `workers/dispatcher/harvest-8way-r1094_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5071         | 2.5547         | +0.0476 |
| ctrl_bpc best  | 2.3966         | 2.3988         | +0.0022 |

## Per-round trajectory (best bird: 0WI4n)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1095 | 6516 | 2.3988 | +0.2404 |

## Cumulative training contribution

- This harvest: **880 steps** from 11 bird(s)
- Across full ancestry (deduped by bird_id): **1520 steps** from 19 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1094_sym24`
  - `workers/dispatcher/harvest-4way-r1094_sym24`
  - `workers/dispatcher/harvest-8way-r1094_sym24`

## Output

`workers/dispatcher/harvest-11way-r1095_sym24/round-1095/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 11 workers)
- `dense.pt` (averaged across 11 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

