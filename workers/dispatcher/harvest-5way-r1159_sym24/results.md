# harvest-5way-r1159 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1159 ctrl_bpc |
|--------|--------|--------------:|
| CDCqC | fork-SeniorCareMarket-mmllm-claude-train-sym24-65815f5b-CDCqC | 2.3548 |
| RU6G6 | origin/claude/train-sym24-251cb4da-RU6G6 | 2.5199 |
| fWymG | origin/claude/train-sym24-067a91b5-fWymG | 2.5238 |
| 8PgVB | fork-slaa-us-mmllm-claude-train-sym24-ea8b9572-8PgVB | 2.5250 |
| Y8RaR | fork-joly-os-mmllm-claude-train-sym24-5476341a-Y8RaR | 2.7123 |
| **mean** | | **2.5272** |
| **best** | | **2.3548** |

## Chain progression R1158 → R1159

Previous harvest: `workers/dispatcher/harvest-9way-r1158_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4916         | 2.5272         | +0.0356 |
| ctrl_bpc best  | 2.3258         | 2.3548         | +0.0290 |

## Per-round trajectory (best bird: CDCqC)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1159 | 4287 | 2.3548 | +0.2417 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1158_sym24`
  - `workers/dispatcher/harvest-9way-r1158_sym24`

## Output

`workers/dispatcher/harvest-5way-r1159_sym24/round-1159/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

