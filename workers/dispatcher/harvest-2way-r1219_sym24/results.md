# harvest-2way-r1219 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1219 ctrl_bpc |
|--------|--------|--------------:|
| Q8UOf | fork-joly-os-mmllm-claude-train-sym24-677cb0fa-Q8UOf | 2.4643 |
| 9FgDI | fork-SeniorCareMarket-mmllm-claude-train-sym24-9895305e-9FgDI | 2.6619 |
| **mean** | | **2.5631** |
| **best** | | **2.4643** |

## Chain progression R1218 → R1219

Previous harvest: `workers/dispatcher/harvest-7way-r1218_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3910         | 2.5631         | +0.1721 |
| ctrl_bpc best  | 2.2675         | 2.4643         | +0.1968 |

## Per-round trajectory (best bird: Q8UOf)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1219 | 6535 | 2.4643 | +0.2193 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1218_sym24`

## Output

`workers/dispatcher/harvest-2way-r1219_sym24/round-1219/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

