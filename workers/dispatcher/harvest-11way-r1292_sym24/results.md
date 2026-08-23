# harvest-11way-r1292 — sparse-delta merge of 11 birds

## Worker endpoints

| handle | branch | R1292 ctrl_bpc |
|--------|--------|--------------:|
| 0iSuF | fork-joly-os-mmllm-claude-train-sym24-e844572a-0iSuF | 4.5577 |
| WruW4 | fork-slaa-us-mmllm-claude-train-sym24-e3536142-WruW4 | 4.6250 |
| 1e0LJ | fork-slaa-us-mmllm-claude-train-sym24-a7876f9b-1e0LJ | 4.6360 |
| RNwQM | fork-SeniorCareMarket-mmllm-claude-train-sym24-654d8b2a-RNwQM | 4.6579 |
| HR412 | origin/claude/train-sym24-930b4482-HR412 | 4.6835 |
| bR1oW | origin/claude/train-sym24-3e518c08-bR1oW | 4.8880 |
| iZ0yv | fork-joly-os-mmllm-claude-train-sym24-73d6a5e5-iZ0yv | 5.0439 |
| XKWqo | fork-slaa-us-mmllm-claude-train-sym24-2663f184-XKWqo | 5.0513 |
| gIb1M | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-daee5518-gIb1M | 5.1084 |
| qtXb0 | fork-SeniorCareMarket-mmllm-claude-train-sym24-9c7f4032-qtXb0 | 5.1480 |
| qFEZX | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-ebe284a6-qFEZX | 5.1714 |
| **mean** | | **4.8701** |
| **best** | | **4.5577** |

## Chain progression R1291 → R1292

Previous harvest: `workers/dispatcher/harvest-8way-r1291_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.9191         | 4.8701         | -0.0490 |
| ctrl_bpc best  | 4.8221         | 4.5577         | -0.2644 |

## Per-round trajectory (best bird: 0iSuF)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1292 | 6504 | 4.5577 | +0.0154 |

## Cumulative training contribution

- This harvest: **880 steps** from 11 bird(s)
- Across full ancestry (deduped by bird_id): **1520 steps** from 19 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1291_sym24`
  - `workers/dispatcher/harvest-6way-r1291_sym24`
  - `workers/dispatcher/harvest-8way-r1291_sym24`

## Output

`workers/dispatcher/harvest-11way-r1292_sym24/round-1292/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 11 workers)
- `dense.pt` (averaged across 11 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

