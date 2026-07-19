# harvest-6way-r960 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R960 ctrl_bpc |
|--------|--------|--------------:|
| 7riqN | fork-joly-os-mmllm-claude-train-sym24-cf2cfff7-7riqN | 2.8258 |
| eQNOQ | fork-slaa-us-mmllm-claude-train-sym24-ae88b5e6-eQNOQ | 2.8421 |
| QK73v | origin/claude/train-sym24-b40ea808-QK73v | 2.8511 |
| NaMPY | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-bebb410f-NaMPY | 3.0244 |
| JvRjJ | fork-joly-os-mmllm-claude-train-sym24-023d609f-JvRjJ | 3.0247 |
| CtzdC | fork-SeniorCareMarket-mmllm-claude-train-sym24-e9f17a32-CtzdC | 3.0484 |
| **mean** | | **2.9361** |
| **best** | | **2.8258** |

## Chain progression R959 → R960

Previous harvest: `workers/dispatcher/harvest-12way-r959_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7338         | 2.9361         | +0.2023 |
| ctrl_bpc best  | 2.6287         | 2.8258         | +0.1971 |

## Per-round trajectory (best bird: 7riqN)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 960 | 6539 | 2.8258 | +0.1557 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r959_sym24`

## Output

`workers/dispatcher/harvest-6way-r960_sym24/round-960/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

