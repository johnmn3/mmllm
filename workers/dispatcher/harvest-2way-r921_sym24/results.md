# harvest-2way-r921 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R921 ctrl_bpc |
|--------|--------|--------------:|
| ZrM4q | fork-joly-os-mmllm-claude-train-sym24-291804e4-ZrM4q | 2.7224 |
| dGIp6 | fork-SeniorCareMarket-mmllm-claude-train-sym24-bb5f7da6-dGIp6 | 2.8454 |
| **mean** | | **2.7839** |
| **best** | | **2.7224** |

## Chain progression R920 → R921

Previous harvest: `workers/dispatcher/harvest-8way-r920_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9647         | 2.7839         | -0.1808 |
| ctrl_bpc best  | 2.7414         | 2.7224         | -0.0190 |

## Per-round trajectory (best bird: ZrM4q)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 921 | 4444 | 2.7224 | +0.1809 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r920_sym24`

## Output

`workers/dispatcher/harvest-2way-r921_sym24/round-921/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

