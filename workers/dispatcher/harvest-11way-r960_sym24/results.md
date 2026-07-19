# harvest-11way-r960 — sparse-delta merge of 11 birds

## Worker endpoints

| handle | branch | R960 ctrl_bpc |
|--------|--------|--------------:|
| Eba6I | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-3fe610ec-Eba6I | 2.6345 |
| 7riqN | fork-joly-os-mmllm-claude-train-sym24-cf2cfff7-7riqN | 2.8258 |
| 5y4N3 | fork-SeniorCareMarket-mmllm-claude-train-sym24-db908f37-5y4N3 | 2.8321 |
| eQNOQ | fork-slaa-us-mmllm-claude-train-sym24-ae88b5e6-eQNOQ | 2.8421 |
| QK73v | origin/claude/train-sym24-b40ea808-QK73v | 2.8511 |
| AoYXW | fork-slaa-us-mmllm-claude-train-sym24-2a19928e-AoYXW | 2.8530 |
| tJz17 | origin/claude/train-sym24-eb0513dd-tJz17 | 2.8539 |
| gmkbn | fork-slaa-us-mmllm-claude-train-sym24-971e6c8c-gmkbn | 3.0183 |
| NaMPY | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-bebb410f-NaMPY | 3.0244 |
| JvRjJ | fork-joly-os-mmllm-claude-train-sym24-023d609f-JvRjJ | 3.0247 |
| CtzdC | fork-SeniorCareMarket-mmllm-claude-train-sym24-e9f17a32-CtzdC | 3.0484 |
| **mean** | | **2.8917** |
| **best** | | **2.6345** |

## Chain progression R959 → R960

Previous harvest: `workers/dispatcher/harvest-8way-r959_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7187         | 2.8917         | +0.1730 |
| ctrl_bpc best  | 2.6287         | 2.6345         | +0.0058 |

## Per-round trajectory (best bird: Eba6I)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 960 | 6680 | 2.6345 | +0.1592 |

## Cumulative training contribution

- This harvest: **880 steps** from 11 bird(s)
- Across full ancestry (deduped by bird_id): **1520 steps** from 19 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r959_sym24`
  - `workers/dispatcher/harvest-8way-r959_sym24`

## Output

`workers/dispatcher/harvest-11way-r960_sym24/round-960/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 11 workers)
- `dense.pt` (averaged across 11 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

