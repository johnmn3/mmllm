# harvest-3way-r1387 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1387 ctrl_bpc |
|--------|--------|--------------:|
| dhuW7 | fork-joly-os-mmllm-claude-train-sym24-fb90c499-dhuW7 | 3.0837 |
| JFOTM | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-2b755172-JFOTM | 3.4565 |
| uOe1d | origin/claude/train-sym24-d36a34bd-uOe1d | 3.4623 |
| **mean** | | **3.3342** |
| **best** | | **3.0837** |

## Chain progression R1386 → R1387

Previous harvest: `workers/dispatcher/harvest-4way-r1386_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2061         | 3.3342         | +0.1281 |
| ctrl_bpc best  | 3.0663         | 3.0837         | +0.0174 |

## Per-round trajectory (best bird: dhuW7)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1387 | 6553 | 3.0837 | +0.1173 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1386_sym24`

## Output

`workers/dispatcher/harvest-3way-r1387_sym24/round-1387/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

