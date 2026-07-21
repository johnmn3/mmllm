# harvest-2way-r982 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R982 ctrl_bpc |
|--------|--------|--------------:|
| IPqTT | fork-joly-os-mmllm-claude-train-sym24-dc05113c-IPqTT | 2.6227 |
| ruXjL | fork-slaa-us-mmllm-claude-train-sym24-79d2d74f-ruXjL | 2.6294 |
| **mean** | | **2.6261** |
| **best** | | **2.6227** |

## Chain progression R981 → R982

Previous harvest: `workers/dispatcher/harvest-1way-r981_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9880         | 2.6261         | -0.3619 |
| ctrl_bpc best  | 2.9880         | 2.6227         | -0.3653 |

## Per-round trajectory (best bird: IPqTT)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 982 | 3735 | 2.6227 | +0.1529 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r981_sym24`

## Output

`workers/dispatcher/harvest-2way-r982_sym24/round-982/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

