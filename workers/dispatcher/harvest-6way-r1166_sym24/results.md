# harvest-6way-r1166 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1166 ctrl_bpc |
|--------|--------|--------------:|
| OmhXW | fork-joly-os-mmllm-claude-train-sym24-4ac6db92-OmhXW | 2.3462 |
| xfKIw | fork-joly-os-mmllm-claude-train-sym24-de98d170-xfKIw | 2.3492 |
| 2Pf7t | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-11e26e17-2Pf7t | 2.3537 |
| 1JbFs | fork-SeniorCareMarket-mmllm-claude-train-sym24-ce32df9f-1JbFs | 2.5267 |
| uk9Vz | fork-slaa-us-mmllm-claude-train-sym24-3aa78f27-uk9Vz | 2.7049 |
| or1Vn | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-6828076e-or1Vn | 2.7099 |
| **mean** | | **2.4984** |
| **best** | | **2.3462** |

## Chain progression R1165 → R1166

Previous harvest: `workers/dispatcher/harvest-9way-r1165_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5667         | 2.4984         | -0.0683 |
| ctrl_bpc best  | 2.3195         | 2.3462         | +0.0267 |

## Per-round trajectory (best bird: OmhXW)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1166 | 3658 | 2.3462 | +0.2364 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r1165_sym24`
  - `workers/dispatcher/harvest-9way-r1165_sym24`

## Output

`workers/dispatcher/harvest-6way-r1166_sym24/round-1166/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

