# harvest-4way-r672 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R672 ctrl_bpc |
|--------|--------|--------------:|
| vSAog | origin/claude/train-sym24-de99c369-vSAog | 3.8554 |
| kotwm | fork-SeniorCareMarket-mmllm-claude-train-sym24-86b8f563-kotwm | 3.9034 |
| PgXJh | fork-slaa-us-mmllm-claude-train-sym24-26acc068-PgXJh | 3.9037 |
| OG2zm | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-68101f7a-OG2zm | 4.2110 |
| **mean** | | **3.9684** |
| **best** | | **3.8554** |

## Chain progression R671 → R672

Previous harvest: `workers/dispatcher/harvest-1way-r671_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.9317         | 3.9684         | +0.0367 |
| ctrl_bpc best  | 3.9317         | 3.8554         | -0.0763 |

## Per-round trajectory (best bird: vSAog)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 672 | 6387 | 3.8554 | +0.4540 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r671_sym24`

## Output

`workers/dispatcher/harvest-4way-r672_sym24/round-672/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

