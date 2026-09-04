# harvest-2way-r1392 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1392 ctrl_bpc |
|--------|--------|--------------:|
| saGVN | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-4dee4839-saGVN | 3.1357 |
| 8wMsn | fork-SeniorCareMarket-mmllm-claude-train-sym24-e627714f-8wMsn | 3.8087 |
| **mean** | | **3.4722** |
| **best** | | **3.1357** |

## Chain progression R1391 → R1392

Previous harvest: `workers/dispatcher/harvest-2way-r1391_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4047         | 3.4722         | +0.0675 |
| ctrl_bpc best  | 3.1313         | 3.1357         | +0.0044 |

## Per-round trajectory (best bird: saGVN)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1392 | 6666 | 3.1357 | +0.1057 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1391_sym24`

## Output

`workers/dispatcher/harvest-2way-r1392_sym24/round-1392/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

