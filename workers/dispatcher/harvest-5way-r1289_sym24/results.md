# harvest-5way-r1289 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1289 ctrl_bpc |
|--------|--------|--------------:|
| uyP96 | fork-slaa-us-mmllm-claude-train-sym24-ec61913b-uyP96 | 2.2241 |
| 91rlV | fork-joly-os-mmllm-claude-train-sym24-5897932b-91rlV | 2.2362 |
| Co9Bn | fork-slaa-us-mmllm-claude-train-sym24-5c6280ce-Co9Bn | 2.4219 |
| KPLJY | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-3a413e49-KPLJY | 2.6326 |
| lZex3 | fork-SeniorCareMarket-mmllm-claude-train-sym24-066a5e30-lZex3 | 11.5297 |
| **mean** | | **4.2089** |
| **best** | | **2.2241** |

## Chain progression R1288 → R1289

Previous harvest: `workers/dispatcher/harvest-5way-r1288_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3441         | 4.2089         | +1.8648 |
| ctrl_bpc best  | 2.2089         | 2.2241         | +0.0152 |

## Per-round trajectory (best bird: uyP96)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1289 | 3916 | 2.2241 | +0.2440 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1288_sym24`
  - `workers/dispatcher/harvest-5way-r1288_sym24`

## Output

`workers/dispatcher/harvest-5way-r1289_sym24/round-1289/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

