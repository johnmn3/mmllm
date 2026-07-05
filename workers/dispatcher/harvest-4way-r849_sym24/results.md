# harvest-4way-r849 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R849 ctrl_bpc |
|--------|--------|--------------:|
| pPL0t | fork-slaa-us-mmllm-claude-train-sym24-a0182dbe-pPL0t | 2.9404 |
| x7odQ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-17830c67-x7odQ | 2.9503 |
| Mc4xp | fork-joly-os-mmllm-claude-train-sym24-0563ad12-Mc4xp | 3.0957 |
| tRMDH | fork-SeniorCareMarket-mmllm-claude-train-sym24-cd9b819a-tRMDH | 3.3113 |
| **mean** | | **3.0744** |
| **best** | | **2.9404** |

## Chain progression R848 → R849

Previous harvest: `workers/dispatcher/harvest-5way-r848_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0120         | 3.0744         | +0.0624 |
| ctrl_bpc best  | 2.9339         | 2.9404         | +0.0065 |

## Per-round trajectory (best bird: pPL0t)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 849 | 6609 | 2.9404 | +0.2610 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r848_sym24`

## Output

`workers/dispatcher/harvest-4way-r849_sym24/round-849/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

