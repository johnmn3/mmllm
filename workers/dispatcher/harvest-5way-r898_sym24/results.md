# harvest-5way-r898 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R898 ctrl_bpc |
|--------|--------|--------------:|
| 1LgEq | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-531475e1-1LgEq | 2.8011 |
| hPLKn | origin/claude/train-sym24-e4a595f0-hPLKn | 2.8122 |
| DFj4q | fork-slaa-us-mmllm-claude-train-sym24-7c1fb090-DFj4q | 2.9670 |
| wqkrs | fork-SeniorCareMarket-mmllm-claude-train-sym24-d7d80e48-wqkrs | 2.9681 |
| Nu77q | fork-joly-os-mmllm-claude-train-sym24-b4a40154-Nu77q | 3.1598 |
| **mean** | | **2.9416** |
| **best** | | **2.8011** |

## Chain progression R897 → R898

Previous harvest: `workers/dispatcher/harvest-14way-r897_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9655         | 2.9416         | -0.0239 |
| ctrl_bpc best  | 2.7877         | 2.8011         | +0.0134 |

## Per-round trajectory (best bird: 1LgEq)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 898 | 6534 | 2.8011 | +0.2416 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r897_sym24`

## Output

`workers/dispatcher/harvest-5way-r898_sym24/round-898/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

