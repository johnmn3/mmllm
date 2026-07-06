# harvest-9way-r857 — sparse-delta merge of 9 birds

## Worker endpoints

| handle | branch | R857 ctrl_bpc |
|--------|--------|--------------:|
| vGQNP | fork-slaa-us-mmllm-claude-train-sym24-6839a8c3-vGQNP | 2.9002 |
| yX2H9 | origin/claude/train-sym24-eff2cc8b-yX2H9 | 2.9031 |
| 7reUT | fork-joly-os-mmllm-claude-train-sym24-aec1f72b-7reUT | 2.9116 |
| QJJT5 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-5b9aa131-QJJT5 | 2.9137 |
| z3J1J | fork-SeniorCareMarket-mmllm-claude-train-sym24-ae3e7a3a-z3J1J | 2.9283 |
| XZ12d | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-b9dfbe55-XZ12d | 3.0575 |
| lRgAa | origin/claude/train-sym24-f11ecce7-lRgAa | 3.0585 |
| gJmVh | fork-slaa-us-mmllm-claude-train-sym24-99d67307-gJmVh | 3.0639 |
| bjXEt | fork-joly-os-mmllm-claude-train-sym24-7ee44c9b-bjXEt | 3.0797 |
| **mean** | | **2.9796** |
| **best** | | **2.9002** |

## Chain progression R856 → R857

Previous harvest: `workers/dispatcher/harvest-5way-r856_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0197         | 2.9796         | -0.0401 |
| ctrl_bpc best  | 2.9048         | 2.9002         | -0.0046 |

## Per-round trajectory (best bird: vGQNP)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 857 | 6767 | 2.9002 | +0.3677 |

## Cumulative training contribution

- This harvest: **720 steps** from 9 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r856_sym24`
  - `workers/dispatcher/harvest-5way-r856_sym24`

## Output

`workers/dispatcher/harvest-9way-r857_sym24/round-857/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 9 workers)
- `dense.pt` (averaged across 9 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

