# harvest-2way-r937 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R937 ctrl_bpc |
|--------|--------|--------------:|
| YHujZ | fork-slaa-us-mmllm-claude-train-sym24-8c6152b6-YHujZ | 2.6959 |
| qEtnD | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-ff3b316c-qEtnD | 2.7008 |
| **mean** | | **2.6984** |
| **best** | | **2.6959** |

## Chain progression R936 → R937

Previous harvest: `workers/dispatcher/harvest-6way-r936_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8016         | 2.6984         | -0.1033 |
| ctrl_bpc best  | 2.6920         | 2.6959         | +0.0039 |

## Per-round trajectory (best bird: YHujZ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 937 | 6792 | 2.6959 | +0.1787 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r936_sym24`

## Output

`workers/dispatcher/harvest-2way-r937_sym24/round-937/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

