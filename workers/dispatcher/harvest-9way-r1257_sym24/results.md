# harvest-9way-r1257 — sparse-delta merge of 9 birds

## Worker endpoints

| handle | branch | R1257 ctrl_bpc |
|--------|--------|--------------:|
| T3vJr | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-7671c5a7-T3vJr | 2.2354 |
| dB2TJ | fork-SeniorCareMarket-mmllm-claude-train-sym24-c478090c-dB2TJ | 2.2359 |
| tS5oH | fork-slaa-us-mmllm-claude-train-sym24-503a4674-tS5oH | 2.2499 |
| Aaipx | fork-joly-os-mmllm-claude-train-sym24-3eb3fec1-Aaipx | 2.2529 |
| 4JyTj | origin/claude/train-sym24-e0f3c1c3-4JyTj | 2.2611 |
| P1gBZ | fork-SeniorCareMarket-mmllm-claude-train-sym24-8cbd77e2-P1gBZ | 2.4391 |
| w26ux | fork-joly-os-mmllm-claude-train-sym24-8c9e202c-w26ux | 2.4407 |
| kvp2P | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-2e9cc93b-kvp2P | 2.6399 |
| eIADi | origin/claude/train-sym24-06a7957b-eIADi | 2.6423 |
| **mean** | | **2.3775** |
| **best** | | **2.2354** |

## Chain progression R1256 → R1257

Previous harvest: `workers/dispatcher/harvest-8way-r1256_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3429         | 2.3775         | +0.0346 |
| ctrl_bpc best  | 2.2351         | 2.2354         | +0.0003 |

## Per-round trajectory (best bird: T3vJr)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1257 | 6593 | 2.2354 | +0.2542 |

## Cumulative training contribution

- This harvest: **720 steps** from 9 bird(s)
- Across full ancestry (deduped by bird_id): **1360 steps** from 17 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1256_sym24`
  - `workers/dispatcher/harvest-8way-r1256_sym24`

## Output

`workers/dispatcher/harvest-9way-r1257_sym24/round-1257/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 9 workers)
- `dense.pt` (averaged across 9 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

