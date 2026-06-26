# harvest-2way-r773 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R773 ctrl_bpc |
|--------|--------|--------------:|
| KDQHJ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-d923efd4-KDQHJ | 3.2566 |
| 6Vqxm | origin/claude/train-sym24-92fb2797-6Vqxm | 3.5969 |
| **mean** | | **3.4268** |
| **best** | | **3.2566** |

## Chain progression R772 → R773

Previous harvest: `workers/dispatcher/harvest-4way-r772_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2608         | 3.4268         | +0.1660 |
| ctrl_bpc best  | 3.2130         | 3.2566         | +0.0436 |

## Per-round trajectory (best bird: KDQHJ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 773 | 6654 | 3.2566 | +0.5175 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r772_sym24`

## Output

`workers/dispatcher/harvest-2way-r773_sym24/round-773/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

