# harvest-3way-r726 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R726 ctrl_bpc |
|--------|--------|--------------:|
| Y4XKo | fork-davidwuchn-mmllm-claude-train-sym24-e50b3487-Y4XKo | 3.5123 |
| Bz4Yr | fork-slaa-us-mmllm-claude-train-sym24-6bbf728b-Bz4Yr | 3.5215 |
| W00L4 | fork-joly-os-mmllm-claude-train-sym24-10c7cc46-W00L4 | 3.7894 |
| **mean** | | **3.6077** |
| **best** | | **3.5123** |

## Chain progression R725 → R726

Previous harvest: `workers/dispatcher/harvest-17way-r725_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5477         | 3.6077         | +0.0600 |
| ctrl_bpc best  | 3.4758         | 3.5123         | +0.0365 |

## Per-round trajectory (best bird: Y4XKo)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 726 | 6525 | 3.5123 | +0.8648 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r725_sym24`

## Output

`workers/dispatcher/harvest-3way-r726_sym24/round-726/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

