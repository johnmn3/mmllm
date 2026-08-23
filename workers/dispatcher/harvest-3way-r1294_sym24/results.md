# harvest-3way-r1294 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1294 ctrl_bpc |
|--------|--------|--------------:|
| KYXf8 | fork-joly-os-mmllm-claude-train-sym24-1f6b6e82-KYXf8 | 4.1761 |
| JFGQn | origin/claude/train-sym24-16f24b9c-JFGQn | 4.1880 |
| 7LBW4 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-8ae07177-7LBW4 | 4.2925 |
| **mean** | | **4.2189** |
| **best** | | **4.1761** |

## Chain progression R1293 → R1294

Previous harvest: `workers/dispatcher/harvest-5way-r1293_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.4242         | 4.2189         | -0.2053 |
| ctrl_bpc best  | 4.3090         | 4.1761         | -0.1329 |

## Per-round trajectory (best bird: KYXf8)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1294 | 3858 | 4.1761 | +0.0045 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1293_sym24`

## Output

`workers/dispatcher/harvest-3way-r1294_sym24/round-1294/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

