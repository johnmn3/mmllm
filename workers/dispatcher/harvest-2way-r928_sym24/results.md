# harvest-2way-r928 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R928 ctrl_bpc |
|--------|--------|--------------:|
| qFpOU | fork-joly-os-mmllm-claude-train-sym24-c11dfb23-qFpOU | 2.7143 |
| yKUTs | fork-SeniorCareMarket-mmllm-claude-train-sym24-ba7dfd2e-yKUTs | 2.7654 |
| **mean** | | **2.7399** |
| **best** | | **2.7143** |

## Chain progression R610 → R928

Previous harvest: `workers/dispatcher/harvest-2way-merge-r610_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.1372         | 2.7399         | +0.6027 |
| ctrl_bpc best  | 2.1268         | 2.7143         | +0.5875 |

## Per-round trajectory (best bird: qFpOU)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 928 | 6520 | 2.7143 | +0.1649 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r927_sym24`
  - `workers/dispatcher/harvest-5way-r927_sym24`

## Output

`workers/dispatcher/harvest-2way-r928_sym24/round-928/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

