# harvest-4way-r1123 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1123 ctrl_bpc |
|--------|--------|--------------:|
| Hpqbx | origin/claude/train-sym24-47e32306-Hpqbx | 2.3817 |
| XkeHP | fork-SeniorCareMarket-mmllm-claude-train-sym24-31a11cdb-XkeHP | 2.7586 |
| f3ipU | origin/claude/train-sym24-ace91dcc-f3ipU | 2.7686 |
| edun1 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-9bd7a744-edun1 | 2.7737 |
| **mean** | | **2.6706** |
| **best** | | **2.3817** |

## Chain progression R1122 → R1123

Previous harvest: `workers/dispatcher/harvest-5way-r1122_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4843         | 2.6706         | +0.1863 |
| ctrl_bpc best  | 2.3634         | 2.3817         | +0.0183 |

## Per-round trajectory (best bird: Hpqbx)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1123 | 4067 | 2.3817 | +0.2357 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1122_sym24`

## Output

`workers/dispatcher/harvest-4way-r1123_sym24/round-1123/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

