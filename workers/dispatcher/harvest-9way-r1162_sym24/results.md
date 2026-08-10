# harvest-9way-r1162 — sparse-delta merge of 9 birds

## Worker endpoints

| handle | branch | R1162 ctrl_bpc |
|--------|--------|--------------:|
| BM0af | fork-slaa-us-mmllm-claude-train-sym24-58ed1ad0-BM0af | 2.3184 |
| LHsbQ | origin/claude/train-sym24-6109681a-LHsbQ | 2.3319 |
| DTz2B | fork-joly-os-mmllm-claude-train-sym24-13b34346-DTz2B | 2.3435 |
| Taas1 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-64464f63-Taas1 | 2.3486 |
| dColN | fork-slaa-us-mmllm-claude-train-sym24-ab2110e3-dColN | 2.5163 |
| cNZxD | origin/claude/train-sym24-1b71ef79-cNZxD | 2.5196 |
| dIAyT | fork-SeniorCareMarket-mmllm-claude-train-sym24-78353c5c-dIAyT | 2.5200 |
| qACKn | fork-joly-os-mmllm-claude-train-sym24-2c311650-qACKn | 2.7094 |
| PrBuq | origin/claude/train-sym24-02b43cc1-PrBuq | 2.7217 |
| **mean** | | **2.4810** |
| **best** | | **2.3184** |

## Chain progression R1161 → R1162

Previous harvest: `workers/dispatcher/harvest-6way-r1161_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6199         | 2.4810         | -0.1389 |
| ctrl_bpc best  | 2.3258         | 2.3184         | -0.0074 |

## Per-round trajectory (best bird: BM0af)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1162 | 5365 | 2.3184 | +0.2655 |

## Cumulative training contribution

- This harvest: **720 steps** from 9 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1161_sym24`
  - `workers/dispatcher/harvest-6way-r1161_sym24`

## Output

`workers/dispatcher/harvest-9way-r1162_sym24/round-1162/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 9 workers)
- `dense.pt` (averaged across 9 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

