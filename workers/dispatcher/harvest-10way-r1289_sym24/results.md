# harvest-10way-r1289 — sparse-delta merge of 10 birds

## Worker endpoints

| handle | branch | R1289 ctrl_bpc |
|--------|--------|--------------:|
| OVLVR | origin/claude/train-sym24-3aa52a0c-OVLVR | 2.2135 |
| uyP96 | fork-slaa-us-mmllm-claude-train-sym24-ec61913b-uyP96 | 2.2241 |
| 91rlV | fork-joly-os-mmllm-claude-train-sym24-5897932b-91rlV | 2.2362 |
| ONbD1 | fork-joly-os-mmllm-claude-train-sym24-7a6e1c99-ONbD1 | 2.4098 |
| TrNkk | origin/claude/train-sym24-5f4eaf5a-TrNkk | 2.4177 |
| Co9Bn | fork-slaa-us-mmllm-claude-train-sym24-5c6280ce-Co9Bn | 2.4219 |
| StDrq | fork-SeniorCareMarket-mmllm-claude-train-sym24-c6b37f73-StDrq | 2.6226 |
| Z9lMS | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-fbc23ede-Z9lMS | 2.6284 |
| KPLJY | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-3a413e49-KPLJY | 2.6326 |
| lZex3 | fork-SeniorCareMarket-mmllm-claude-train-sym24-066a5e30-lZex3 | 11.5297 |
| **mean** | | **3.3337** |
| **best** | | **2.2135** |

## Chain progression R1288 → R1289

Previous harvest: `workers/dispatcher/harvest-5way-r1288_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3441         | 3.3337         | +0.9895 |
| ctrl_bpc best  | 2.2089         | 2.2135         | +0.0046 |

## Per-round trajectory (best bird: OVLVR)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1289 | 6694 | 2.2135 | +0.2599 |

## Cumulative training contribution

- This harvest: **800 steps** from 10 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1288_sym24`
  - `workers/dispatcher/harvest-5way-r1288_sym24`

## Output

`workers/dispatcher/harvest-10way-r1289_sym24/round-1289/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 10 workers)
- `dense.pt` (averaged across 10 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

