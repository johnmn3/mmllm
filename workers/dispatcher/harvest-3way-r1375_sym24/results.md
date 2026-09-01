# harvest-3way-r1375 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1375 ctrl_bpc |
|--------|--------|--------------:|
| w0za2 | origin/claude/train-sym24-837b6015-w0za2 | 3.1795 |
| pUuEe | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-19b2cef3-pUuEe | 3.4417 |
| fb16Q | fork-SeniorCareMarket-mmllm-claude-train-sym24-95b4331e-fb16Q | 3.5596 |
| **mean** | | **3.3936** |
| **best** | | **3.1795** |

## Chain progression R1374 → R1375

Previous harvest: `workers/dispatcher/harvest-6way-r1374_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2504         | 3.3936         | +0.1432 |
| ctrl_bpc best  | 3.1043         | 3.1795         | +0.0752 |

## Per-round trajectory (best bird: w0za2)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1375 | 5375 | 3.1795 | +0.1239 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-6way-r1374_sym24`

## Output

`workers/dispatcher/harvest-3way-r1375_sym24/round-1375/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

