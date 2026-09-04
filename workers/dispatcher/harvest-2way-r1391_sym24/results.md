# harvest-2way-r1391 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1391 ctrl_bpc |
|--------|--------|--------------:|
| z9iYZ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-83958335-z9iYZ | 3.1313 |
| MAMo7 | fork-SeniorCareMarket-mmllm-claude-train-sym24-afc41e9c-MAMo7 | 3.6782 |
| **mean** | | **3.4047** |
| **best** | | **3.1313** |

## Chain progression R1390 → R1391

Previous harvest: `workers/dispatcher/harvest-4way-r1390_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2941         | 3.4047         | +0.1107 |
| ctrl_bpc best  | 3.0950         | 3.1313         | +0.0363 |

## Per-round trajectory (best bird: z9iYZ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1391 | 5285 | 3.1313 | +0.1334 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1390_sym24`

## Output

`workers/dispatcher/harvest-2way-r1391_sym24/round-1391/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

