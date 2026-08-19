# harvest-5way-r1257 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1257 ctrl_bpc |
|--------|--------|--------------:|
| dB2TJ | fork-SeniorCareMarket-mmllm-claude-train-sym24-c478090c-dB2TJ | 2.2359 |
| P1gBZ | fork-SeniorCareMarket-mmllm-claude-train-sym24-8cbd77e2-P1gBZ | 2.4391 |
| w26ux | fork-joly-os-mmllm-claude-train-sym24-8c9e202c-w26ux | 2.4407 |
| kvp2P | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-2e9cc93b-kvp2P | 2.6399 |
| eIADi | origin/claude/train-sym24-06a7957b-eIADi | 2.6423 |
| **mean** | | **2.4796** |
| **best** | | **2.2359** |

## Chain progression R1256 → R1257

Previous harvest: `workers/dispatcher/harvest-11way-r1256_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3347         | 2.4796         | +0.1449 |
| ctrl_bpc best  | 2.2351         | 2.2359         | +0.0008 |

## Per-round trajectory (best bird: dB2TJ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1257 | 6476 | 2.2359 | +0.2549 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1256_sym24`
  - `workers/dispatcher/harvest-8way-r1256_sym24`

## Output

`workers/dispatcher/harvest-5way-r1257_sym24/round-1257/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

