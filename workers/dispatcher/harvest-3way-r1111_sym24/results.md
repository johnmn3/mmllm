# harvest-3way-r1111 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1111 ctrl_bpc |
|--------|--------|--------------:|
| BnHgJ | fork-slaa-us-mmllm-claude-train-sym24-9449f6f7-BnHgJ | 2.5802 |
| PgUNT | fork-joly-os-mmllm-claude-train-sym24-23b62890-PgUNT | 2.5847 |
| jjwtv | origin/claude/train-sym24-552c0f8a-jjwtv | 2.7925 |
| **mean** | | **2.6525** |
| **best** | | **2.5802** |

## Chain progression R1110 → R1111

Previous harvest: `workers/dispatcher/harvest-6way-r1110_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4961         | 2.6525         | +0.1564 |
| ctrl_bpc best  | 2.3773         | 2.5802         | +0.2029 |

## Per-round trajectory (best bird: BnHgJ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1111 | 4363 | 2.5802 | +0.2178 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r1110_sym24`

## Output

`workers/dispatcher/harvest-3way-r1111_sym24/round-1111/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

