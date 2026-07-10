# harvest-4way-r887 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R887 ctrl_bpc |
|--------|--------|--------------:|
| HpJmY | origin/claude/train-sym24-6ef49d22-HpJmY | 2.8444 |
| qqk0V | fork-joly-os-mmllm-claude-train-sym24-9cfe78df-qqk0V | 2.9924 |
| Q26z5 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-0eb9032b-Q26z5 | 3.2073 |
| YZyUj | fork-SeniorCareMarket-mmllm-claude-train-sym24-efe7bcce-YZyUj | 3.2228 |
| **mean** | | **3.0667** |
| **best** | | **2.8444** |

## Chain progression R886 → R887

Previous harvest: `workers/dispatcher/harvest-6way-r886_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9591         | 3.0667         | +0.1076 |
| ctrl_bpc best  | 2.8141         | 2.8444         | +0.0303 |

## Per-round trajectory (best bird: HpJmY)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 887 | 6299 | 2.8444 | +0.2215 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r886_sym24`
  - `workers/dispatcher/harvest-6way-r886_sym24`

## Output

`workers/dispatcher/harvest-4way-r887_sym24/round-887/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

