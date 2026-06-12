# harvest-2way-r656 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R656 ctrl_bpc |
|--------|--------|--------------:|
| 1r4Fc | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-60b3229d-1r4Fc | 4.1258 |
| H4gsy | origin/claude/train-sym24-c86b88cc-H4gsy | 4.1493 |
| **mean** | | **4.1376** |
| **best** | | **4.1258** |

## Chain progression R655 → R656

Previous harvest: `workers/dispatcher/harvest-7way-r655_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.1845         | 4.1376         | -0.0469 |
| ctrl_bpc best  | 4.1119         | 4.1258         | +0.0139 |

## Per-round trajectory (best bird: 1r4Fc)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 656 | 6667 | 4.1258 | +0.0759 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r655_sym24`

## Output

`workers/dispatcher/harvest-2way-r656_sym24/round-656/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

