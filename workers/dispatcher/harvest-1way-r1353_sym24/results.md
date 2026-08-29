# harvest-1way-r1353 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1353 ctrl_bpc |
|--------|--------|--------------:|
| kxYdF | fork-joly-os-mmllm-claude-train-sym24-33edb9a6-kxYdF | 3.2946 |
| **mean** | | **3.2946** |
| **best** | | **3.2946** |

## Chain progression R1352 → R1353

Previous harvest: `workers/dispatcher/harvest-7way-r1352_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3058         | 3.2946         | -0.0112 |
| ctrl_bpc best  | 3.2234         | 3.2946         | +0.0712 |

## Per-round trajectory (best bird: kxYdF)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1353 | 6622 | 3.2946 | +0.0775 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1352_sym24`

## Output

`workers/dispatcher/harvest-1way-r1353_sym24/round-1353/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

