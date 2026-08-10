# harvest-9way-r1163 — sparse-delta merge of 9 birds

## Worker endpoints

| handle | branch | R1163 ctrl_bpc |
|--------|--------|--------------:|
| 6u7jh | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-a8b32b7a-6u7jh | 2.3178 |
| z8GPY | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-82d1da51-z8GPY | 2.3258 |
| 2dUVZ | origin/claude/train-sym24-32cf3e3b-2dUVZ | 2.3487 |
| FRuH2 | fork-SeniorCareMarket-mmllm-claude-train-sym24-50eb7ae5-FRuH2 | 2.3518 |
| WWTf1 | fork-joly-os-mmllm-claude-train-sym24-f287755e-WWTf1 | 2.5172 |
| FW6rn | fork-SeniorCareMarket-mmllm-claude-train-sym24-e6a15f8f-FW6rn | 2.5228 |
| lhQLW | origin/claude/train-sym24-d82f9e8d-lhQLW | 2.5236 |
| 5iX0A | fork-slaa-us-mmllm-claude-train-sym24-487de4a1-5iX0A | 2.7152 |
| ZYeP5 | origin/claude/train-sym24-4d364cbf-ZYeP5 | 2.7338 |
| **mean** | | **2.4841** |
| **best** | | **2.3178** |

## Chain progression R1162 → R1163

Previous harvest: `workers/dispatcher/harvest-9way-r1162_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4810         | 2.4841         | +0.0031 |
| ctrl_bpc best  | 2.3184         | 2.3178         | -0.0006 |

## Per-round trajectory (best bird: 6u7jh)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1163 | 3676 | 2.3178 | +0.2536 |

## Cumulative training contribution

- This harvest: **720 steps** from 9 bird(s)
- Across full ancestry (deduped by bird_id): **1440 steps** from 18 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1162_sym24`
  - `workers/dispatcher/harvest-5way-r1162_sym24`
  - `workers/dispatcher/harvest-9way-r1162_sym24`

## Output

`workers/dispatcher/harvest-9way-r1163_sym24/round-1163/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 9 workers)
- `dense.pt` (averaged across 9 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

