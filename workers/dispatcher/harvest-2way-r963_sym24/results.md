# harvest-2way-r963 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R963 ctrl_bpc |
|--------|--------|--------------:|
| ckKVh | fork-SeniorCareMarket-mmllm-claude-train-sym24-d92b3c53-ckKVh | 2.8248 |
| Z5m9x | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-153ad27d-Z5m9x | 3.0061 |
| **mean** | | **2.9154** |
| **best** | | **2.8248** |

## Chain progression R962 → R963

Previous harvest: `workers/dispatcher/harvest-4way-r962_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7809         | 2.9154         | +0.1345 |
| ctrl_bpc best  | 2.6221         | 2.8248         | +0.2027 |

## Per-round trajectory (best bird: ckKVh)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 963 | 4433 | 2.8248 | +0.1354 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r962_sym24`

## Output

`workers/dispatcher/harvest-2way-r963_sym24/round-963/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

