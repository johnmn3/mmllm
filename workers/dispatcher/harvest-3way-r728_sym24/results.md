# harvest-3way-r728 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R728 ctrl_bpc |
|--------|--------|--------------:|
| NTSyO | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-a5d724b5-NTSyO | 3.4808 |
| hDNoR | fork-slaa-us-mmllm-claude-train-sym24-4933a9f8-hDNoR | 3.5003 |
| uRLss | origin/claude/train-sym24-c4b10938-uRLss | 3.5054 |
| **mean** | | **3.4955** |
| **best** | | **3.4808** |

## Chain progression R727 → R728

Previous harvest: `workers/dispatcher/harvest-4way-r727_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.6538         | 3.4955         | -0.1583 |
| ctrl_bpc best  | 3.4963         | 3.4808         | -0.0155 |

## Per-round trajectory (best bird: NTSyO)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 728 | 6527 | 3.4808 | +0.8474 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r727_sym24`

## Output

`workers/dispatcher/harvest-3way-r728_sym24/round-728/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

