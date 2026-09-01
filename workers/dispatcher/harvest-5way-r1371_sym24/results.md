# harvest-5way-r1371 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1371 ctrl_bpc |
|--------|--------|--------------:|
| Ig9Dn | fork-SeniorCareMarket-mmllm-claude-train-sym24-141233ea-Ig9Dn | 3.1489 |
| bKURw | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-1f7de39f-bKURw | 3.1851 |
| BKnxs | origin/claude/train-sym24-8a175792-BKnxs | 3.2121 |
| J9BkA | origin/claude/train-sym24-78e42836-J9BkA | 3.2227 |
| 3NVu8 | fork-joly-os-mmllm-claude-train-sym24-b3041def-3NVu8 | 3.5270 |
| **mean** | | **3.2592** |
| **best** | | **3.1489** |

## Chain progression R1370 → R1371

Previous harvest: `workers/dispatcher/harvest-3way-r1370_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2657         | 3.2592         | -0.0065 |
| ctrl_bpc best  | 3.1133         | 3.1489         | +0.0356 |

## Per-round trajectory (best bird: Ig9Dn)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1371 | 6525 | 3.1489 | +0.1289 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1370_sym24`
  - `workers/dispatcher/harvest-3way-r1370_sym24`

## Output

`workers/dispatcher/harvest-5way-r1371_sym24/round-1371/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

